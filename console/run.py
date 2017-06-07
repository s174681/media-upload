import time
import os
import importlib
from media.naming import generate_animation_name

services = importlib.import_module("services_%s" % (os.environ.get('APP_ENV', 'test')))

while True:
    for request in services.queue.requests():
        print request.photos
        services.handler.handle({
            'photos': request.photos,
            'video': generate_animation_name('video_result.mov')
        })
        request.confirm()
