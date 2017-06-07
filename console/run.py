import time
import os
import importlib
from media.naming import generate_animation_name
from order_delivery.digital_delivery import EmailDelivery

import time

services = importlib.import_module("services_%s" % (os.environ.get('APP_ENV', 'test')))

while True:
    for request in services.queue.requests():
        print request.photos
        video_name = generate_animation_name('video_result.mov')
        services.handler.handle({
            'photos': request.photos,
            'video': video_name
        })
        request.confirm()
        delivery = EmailDelivery()
        delivery.deliver(
            email=request.email,
            animation_ref='https://s3.eu-central-1.amazonaws.com/%s/%s' % (os.getenv('BUCKET_NAME'), video_name)
        )



    time.sleep(1)
