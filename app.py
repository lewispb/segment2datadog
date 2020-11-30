import hmac
import hashlib
import os
from flask import Flask, jsonify, request, abort
from datadog import initialize, api, statsd

# get keys from enfironment variables
SEGMENT_SHARED_SECRET = os.environ['SEGMENT_SHARED_SECRET']
DATADOG_API_KEY = os.environ['DD_API_KEY']
DATADOG_APP_KEY = os.environ['DD_APP_KEY']
TRACKED_EVENTS = os.environ['DD_TRACKED_EVENTS'].split(',')

# initialize datadog
options = {
    'api_key': DATADOG_API_KEY,
    'app_key': DATADOG_APP_KEY,
    'statsd_host': '127.0.0.1',
    'statsd_port': 8125,
}

initialize(**options)

app = Flask(__name__)

@app.route('/')
def index():
    return "Segment2Datadog is up and running!"

@app.route('/api/<string:source>', methods=['POST'])
def segment2datadog(source):
    # check signature
    signature = request.headers['x-signature']
    digest = hmac.new(SEGMENT_SHARED_SECRET.encode(), msg=request.data, digestmod=hashlib.sha1).hexdigest()
    if digest != signature:
        abort(403, 'Signature not valid.')
    if not source:
        abort(404, 'Source parameter not present.')
    content = request.get_json(silent=True)
    # increment event counter in datadog
    if content['type'] == 'track':
        if content['event'] in TRACKED_EVENTS:
            print("tracking event:" + content['event'])
            statsd.increment('segment.event', tags = ['source:' + source, 'event:' + '-'.join(content['event'].split()), 'type:' + content['type']])
    return jsonify({'source': source, 'data': content})
