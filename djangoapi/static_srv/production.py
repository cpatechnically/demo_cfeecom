import os
MODULE = "PRODUCTION"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

LINODE_BUCKET = 'demo-cfeecomm'
LINODE_BUCKET_REGION = 'us-southeast-1'
LINODE_BUCKET_ACCESS_KEY = os.environ.get("LINODE_BUCKET_ACCESS_KEY")
LINODE_BUCKET_SECRET_KEY = os.environ.get("LINODE_BUCKET_SECRET_KEY")


AWS_S3_ENDPOINT_URL = f'https://{LINODE_BUCKET_REGION}.linodeobjects.com'
AWS_ACCESS_KEY_ID=LINODE_BUCKET_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=LINODE_BUCKET_SECRET_KEY
AWS_S3_REGION_NAME=LINODE_BUCKET_REGION
AWS_S3_USE_SSL=True
AWS_STORAGE_BUCKET_NAME=LINODE_BUCKET

print(f"\nLINODE_BUCKET IS PRESENT!!! ->{LINODE_BUCKET} \nSetting for {MODULE} static -> {LINODE_BUCKET} \n linode key{LINODE_BUCKET_ACCESS_KEY} \nLINODE_BUCKET_SECRET_KEY -> {LINODE_BUCKET_SECRET_KEY}")