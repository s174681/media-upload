import time
import os
import importlib

services = importlib.import_module("services_%s" % (os.environ.get('APP_ENV', 'test')))

while True:
    for request in services.queue.requests():
        print request.photos
        services.handler.handle({
            'photos': request.photos,
            'video': 'video_result.mov'
        })