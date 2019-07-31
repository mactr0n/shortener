import base64
import hashlib

from flask import Flask, request, redirect
app = Flask(__name__)

mapping = {}

@app.route('/')
def register():
    url = request.args.get('url')
    hasher = hashlib.sha1(url.encode())
    encoded = base64.urlsafe_b64encode(hasher.digest())[:6]
    if encoded in mapping:
        print("found")
        return encoded
    else:
        print("new")
        mapping[encoded] = url
        return encoded


@app.route('/<id>')
def redirect_url(id):
    encoded_id = id.encode()
    if encoded_id in mapping:
        return redirect(mapping[encoded_id], code=302)
    else:
        return "No url found for id {0}".format(id), 404
