"""
This is a script to take a backup from local to AWS S3
boto3 -> Used to do AWS tasks using Python
"""

import boto3

s3 = boto3.resource('s3')   # to list all s3 bucket from aws resources
def show_buckets(s3):       # Defining a function
    for bucket in s3.buckets.all():  # to iterater the list or item
        print(bucket.name)   # to print the list of s3 buckets

show_buckets(s3)


# to create a s3 bucket

def create_bucket(s3)                                   # Defining the function to create s3 bucket
    s3.create_bucket(Bucket='testbucketfromdp-lab' , create_BucketConfigutration={'LocationConstraint': "us-east-2"}, )     # passing bucket name    
    print('bucket created successfully')                # Printing final success result

create_bucket(s3)

"""
Or we could write it in this way instead
def create_bucket(s3,,bucket_name,region)
    s3.create_bucket(Bucket='bucket_name , create_BucketConfigutration={'LocationConstraint': region}, )

pass
bucket_name = 'testbucketfromdp-lab'
region = 'us-east-2'
    
"""
# Create backup on s3

def upload_backup(s3,file_name,bucket_name,key_name):

    '''
    uploads a given backup file path to ta given s3 bucket
    with a new name (key_name)

    '''

    data = open(file_name, 'rb')  # File will be read in binary must
    s3.Bucket(bucket_name).put_object(key_name, Body=data)
    print('Backup uploaded successfully')

pass

bucket_name = 'testbucketfromdp-lab'
file_name=/home/dp/Documents/Work/Labs/Python4devops/backups/backup_2025-12-11.tar.gz


upload_backup(s3,file_name,bucket_name,'my_backup.tar.gz')  # calling to the function to perform the above mentioned code  

    
