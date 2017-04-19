from flask import Flask

from flask import request, redirect, url_for, render_template

from media.s3_storage import S3MediaStorage

import boto3

from botocore.client import Config 

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template('upload_file.html')

@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files['uploaded_media']
    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
    media_storage = S3MediaStorage(s3=s3, bucket_name='kanclerj-153')
    media_storage.store(key=uploaded_file.filename, media=uploaded_file) 
    return redirect(url_for('upload'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
