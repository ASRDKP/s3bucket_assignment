import boto3
import json
import csv

s31 = boto3.client("s3")
s3 = boto3.resource("s3")

Bucket_name = "my-first-s3-bucket-demo"

# bucket_repo = s3.list_buckets()
# for bucket in bucket_repo["Buckets"]:
#     print(bucket)
    
    
with open("./sample.json", "rb") as f:
    s31.upload_fileobj(
        f, Bucket_name, "sample_json.json"
        ) 

content_object = s3.Object(Bucket_name, "sample_json.json")
file_content = content_object.get()['Body'].read().decode("utf-8")
json_content = json.loads(file_content)

print("Json Data fetched from S3 bucket : ",json_content)
user_data = json_content['users']


data_file = open('./sample.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0
for user in user_data:
    if count == 0:
        # Writing headers of CSV file
        header = user.keys()
        csv_writer.writerow(header)
        count += 1
    # Writing data of CSV file
    csv_writer.writerow(user.values())
data_file.close()


with open("./sample.csv", "rb") as f:
    s31.upload_fileobj(
        f, Bucket_name, "sample_json.csv"
        ) 
