from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url


import stripe
STRIPE_SECRET_KEY = getattr(settings, "STRIPE_SECRET_KEY", "sk_test_51I4mDCHq21J8fvMWZ7uZdPFgBfI0T81suAux3tudoaA6VanME02qRiBQSTcIqGG11jYbYIU8ENItVWm15M9t9HV500zwrzvQgt")
STRIPE_PUB_KEY =  getattr(settings, "STRIPE_PUB_KEY", 'pk_test_51I4mDCHq21J8fvMWM7uE5JAtYbXA6JkQq0h01QZnoS4Fjc6yjRywMTftx2QyJpLvNyuAM3lUJgOiNiw3n17GXaZn00578YwXWB')
stripe.api_key = STRIPE_SECRET_KEY

from .models import BillingProfile #Card

def payment_method_view(request):
    #next_url = 
    # if request.user.is_authenticated:
    #     billing_profile = request.user.billingprofile
    #     my_customer_id = billing_profile.customer_id

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/cart")
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    print(billing_profile,next_url)
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})
    


def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this user"}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
           new_card_obj = Card.objects.add_new(billing_profile, token)
        return JsonResponse({"message": "Success! Your card was added."})
        print(JsonResponse)
    return HttpResponse("error", status_code=401)
