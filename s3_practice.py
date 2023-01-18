import boto3

s3 = boto3.client("s3")

Bucket_name = "my-first-s3-bucket-demo"


###### Details of all the bucket
# bucket_repo = s3.list_buckets()
# for bucket in bucket_repo["Buckets"]:
#     print(bucket)



#### Create a new bucket
# new_bucket = s3.create_bucket(
#     Bucket = "new-s3-bucket-demo", 
#     CreateBucketConfiguration={
#         'LocationConstraint': 'us-west-2'
#     },
# )
# print(new_bucket)



#### List of objects in the bucket
# responce = s3.list_objects_v2(Bucket=Bucket_name)
# for obj in responce["Contents"]:
#     print(obj)
    
    
    
    
##### Upload files to the bucket
# with open("./beach.jpg", "rb") as f:
#     s3.upload_fileobj(
#         f, Bucket_name, "beach_pic_new.jpg"
#         ) 



#### Download files from the bucket
# s3.download_file(Bucket_name, "beach.jpg", "beachpic_new.jpg")



##### Download files with Binary Data from the bucket
# with open("beachpic_new.jpg", "wb") as f:
#     s3.download_fileobj(Bucket_name, "beach.jpg", f)
    
    
##### Presigned URL for limited access to the object from the bucket
# url = s3.generate_presigned_url(
#     "get_object", 
#     Params={"Bucket" : Bucket_name, "Key" : "beach.jpg"},
#     ExpiresIn=30,
# )
# print(url)
    
    
    
#### Copy Object from one bucket to another bucket
# s3.copy_object(
#     ACL = "public-read",
#     Bucket = "new-s3-bucket-demo",
#     CopySource = f"/{Bucket_name}/beach.jpg",
#     Key = "Copiedbeach.jpg",
# )



#### Get Details of Object
# response = s3.get_object(Bucket=Bucket_name,Key="coffee.jpg")
# print(response)