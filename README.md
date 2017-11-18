## Segment2Datadog

This is a simple Flask app that provides an endpoint to receive events from
segment via the webhooks destination.
The flask app will forward the received events to Datadog as a counter.

## Requirements:

- Heroku account to deploy this app.
- Segment account with your source events.
- Datadog account where your events will be forwarded.

## Dependencies:

- Heroku Python Buildpack (for Heroku deployment).
- [Heroku Datadog Buildpack](https://elements.heroku.com/buildpacks/datadog/heroku-buildpack-datadog) to run Datadog Agent within Heroku.
- [Datadog Python SDK](https://github.com/DataDog/datadogpy).
- [Flask](http://flask.pocoo.org/) to implement the API.

## Installation:

- Deploy this app in Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
- Set the corresponding keys (you can access your Datadog keys [here](https://app.datadoghq.com/account/settings#api)):
  - **DD_API_KEY**: Your Datadog API key.
  - **DD_APP_KEY**: Your Datadog app key.
  - **DD_HOSTNAME**: Name of your Heroku app.
  - **SEGMENT_SHARED_SECRET**: Your Segment Webhooks destination Shared Secret.
- Add [Webhooks](https://segment.com/docs/destinations/webhooks/) destination in your Segment project.
- Configure your Webhooks destination by setting the webhook URL to your Heroku
app, eg: https://&lt;APP_NAME&gt;.herokuapp.com/api/&lt;SOURCE&gt;, where APP_NAME is
your Heroku app name and SOURCE should be the name of the Segment source you are
retrieving events from.
- Activate the webhook destination.
- You should start receiving events in your Datadog dashboard, named **segment.event**.
Datadog tags are included like **source**, **type** and **event** (segment source, type of event (track)
and event name, respectively). You can customize app.py file to add your own
tags or also monitor other type of events, eg: page events.
