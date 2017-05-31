import unittest
import boto3
import os
from botocore.client import Config
from media.s3_storage import S3MediaStorage

class TestS3MediaStorage(unittest.TestCase):
  def test_upload_file_to_s3(self):
    to_upld_path = os.path.join(os.path.dirname(__file__), 'test.txt')
    to_upl_file = open(to_upld_path, 'rb')
    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
    media_storage = S3MediaStorage(s3=s3, bucket_name='kanclerj-153')
    media_storage.store(key='upl_name.txt', media=to_upl_file)

if __name__ == '__main__':
  unittest.main()
