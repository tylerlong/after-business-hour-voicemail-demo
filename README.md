# After business hour voicemail demo


## Use case

By configuration, after business hours, all incoming calls will be redirected to extension A which is a message only extension, and voicemail will be saved to extension B.

We would like to write a minimal project, so that out of business hours, we could get WebHook notifications about voicemails.


## Setup

```
pipenv install
```


## Start the server

```
pipenv run python server.py
```


## Give the server a public address

You can deploy the server to a public python hosting service such as heroku in order to get a public address.

Or you can use [ngork](https://ngrok.com/): `ngrok http 5000`.

In either case, please take a note of the address, such as `https://xxxxxxxx.ngrok.io`.


## Configure .env file

```
cp .env.sample .env
```

Edit `.env` to specify credentials.

`RINGCENTRAL_ACCESS_TOKEN` is the access token to the target RingCentral account. I suppose you already have it and store it somewhere.
For web applications, you probably got it via the 3-legged oauth flow (aka. auth code flow).


## Setup WebHook

```
pipenv run python setup-webhook.py
```

## Test the WebHook

After business hours, make a phone call to the main company number. And watch the console output of the server we started above.

Confirm there is notification data about voicemail created to extension B.
