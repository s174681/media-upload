from media.s3_storage import S3MediaStorage
from botocore.client import Config
import boto3
import os

from ordering.animation_order_bus import SQSAnimationOrderBus


s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
media_storage = S3MediaStorage(s3=s3, bucket_name=os.getenv('BUCKET_NAME'))

sqs = boto3.resource('sqs', region_name="eu-central-1")
queue = sqs.get_queue_by_name(QueueName='kanclerzj')
animation_order_bus = SQSAnimationOrderBus(sqs_queue=queue)
