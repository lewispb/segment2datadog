This is a simple Flask app that provides an endpoint to receive events from
segment via the webhooks destination.
The flask app will forward the received events to Datadog as a counter.

You can deploy this app with Heroku here:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Requirements:

- Heroku account to deploy this app.
- Segment account with your source events.
- Datadog account where your events will be forwarded.



heroku buildpacks:set heroku/python

heroku buildpacks:add --index 1 https://github.com/DataDog/heroku-buildpack-datadog.git

heroku config:set DD_APM_ENABLED=true


https://elements.heroku.com/buildpacks/datadog/heroku-buildpack-datadog

https://app.datadoghq.com/account/settings#api
