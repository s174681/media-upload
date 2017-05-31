class S3MediaStorage:
  def __init__(self, s3, bucket_name):
    self._s3 = s3
    self._bucket_name = bucket_name
  def store(self, key, media):
    bucket = self._s3.Bucket(self._bucket_name)
    bucket.put_object(Key=key, Body=media)
  def get(self, key):
    bucket = self._s3.Bucket(self._bucket_name)
    bucket.download_file(key, '/tmp/%s' % key)
   
    return open('/tmp/%s' % key, 'r')
