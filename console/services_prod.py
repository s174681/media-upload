from request_queue.memory_queue import RequestQueue
import os


def get_full_path(file_name):
    path = os.path.join(
        os.path.dirname(__file__),
        file_name
    )
    return path

requests = [
    {
        'photos': [
            '1.jpeg',
            '2.jpeg',
            '3.jpeg',
            '5.jpeg',
        ],
        'email': 'jakub.kanclerz@gmail.com'
    },
    {
        'photos': [
            '1.jpeg',
            '2.jpeg',
            '3.jpeg',
            '5.jpeg',
        ],
        'email': 'jakub.kanclerz@gmail.com'
    },
    {
        'photos': [
            '1.jpeg',
            '2.jpeg',
            '3.jpeg',
            '5.jpeg',
        ],
        'email': 'jakub.kanclerz@gmail.com'
    }
]

queue = RequestQueue(requests=requests)

from video_animation.create_animation import CreateAnimationHandler
from media.local_storage import LocalMediaStorage
from media.transformation.image_to_video import ImageToVideoConverter
from video_animation.tmp_storage import TmpStorage
import boto3
from botocore.client import Config
from media.s3_storage import S3MediaStorage

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
media_storage = S3MediaStorage(s3=s3, bucket_name='kanclerj')


handler = CreateAnimationHandler(
    tmp_storage=TmpStorage(get_full_path('../var/tmp')),
    media_storage=media_storage,
    transformation=ImageToVideoConverter()
)
