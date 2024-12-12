from boto3 import client
from os import getenv, listdir, path, makedirs
from subprocess import call

directory:str = "/opt/app-root/model"
repo:str = getenv("HF_URL", "https://huggingface.co/instructlab/granite-7b-lab")
model_bucket_name:str = getenv("AWS_S3_MODEL_BUCKET", "granite")
region:str = getenv("AWS_DEFAULT_REGION", "us-east-2")
makedirs(directory)

# download model
call(["git", "clone", repo, directory])
print("model downloaded from huggingface")

s3 = client("s3",
            endpoint_url=getenv("AWS_S3_ENDPOINT"),
            aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"))

# create bucket if not exist
bucket:str|None = getenv("AWS_S3_BUCKET", "models")
if bucket not in [bu["Name"] for bu in s3.list_buckets()["Buckets"]]:
    location:dict[str, str] = {'LocationConstraint': region}
    s3.create_bucket(Bucket=bucket, CreateBucketConfiguration=location)
    print(f"created {bucket} bucket")
else:
    print(f"{bucket} bucket exists, using it")

# upload models
for filename in listdir(directory):
    f:str = path.join(directory, filename)
    if path.isfile(f):
        with open(f, "rb") as file:
            s3.upload_fileobj(file, bucket, f"{model_bucket_name}/{filename}")
            print(f"uploaded {filename}")
