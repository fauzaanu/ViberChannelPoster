# Viber Channel Auto Poster

This guide will illustrate how to setup automated channel posts for viber. This guide uses the [Viber Channel Post API ](https://developers.viber.com/docs/tools/channels-post-api/#channels-post-api)

## Creating a channel

Open Viber and create a channel. Go the right-side menu and click developer tools to get the `Authentication Token`

## Setting up a webhook

We need to setup a webhook initially, its not clear whether viber does anything with this webhook later on.

In this repositiory I have included two ways to achieve this
1. Flask Server (Bit Harder)
2. Cloudflare Workers (Very Easy)

> The only reason I am including the flask server is because I had already written it before I got to know cloudflare workers. I would recommend using cloudflare workers as it is much easier to setup and maintain. Ive also exluded the readme sections of Flask and Certbot because Viber requires a SSL certificate to be setup and we can skip this whole process by using cloudflare workers.

### The Webservers Function

The webserver checks for a specific header ('X-Viber-Content-Signature') in the Post requests it recieves, and returns a response with status 200 if the header exists, and status 403 if it doesn't.

Flask or Cloudflare workers or any other webserver can be used to achieve this as long as it does the above. (with SSL ofcourse)

### API Requests

In this very repo we have included a basic API Collection for Bruno which can be used to test the API endpoints. This does not include many other endpoints that the Viber Channel API provides. Please refer to the [Viber Channel API Documentation](https://developers.viber.com/docs/tools/channels-post-api/#channels-post-api) for more information.

In our Bruno API Collection we have an environment with auth token, userid and webhook url. Please change these to your own values. The webhook url should be your cloudflare workers url or your flask server url.

The order of the requests should be:
1. Setup webhook using the webhook url and auth token
2. Make request to get user id
3. Make request to send message to user id
4. . . .
5. any other requests you want to make

#### Clarification on the user id

The userid is the ID inside the `members` array of the response from the `get user id` request. The `get user id` request returns a list of all the members in the channel.


```json
{
  "status": 0,
  "status_message": "ok",
  "id": "this_is_not_the_user_id",
  "chat_hostname": "SN-CHAT-10_",
  "name": "Automated Channel",
  "members": [
    {
      "id": "this_is_the_user_id",
      "name": "Fauzaan",
      "avatar": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "role": "superadmin"
    }
  ]
}
```

#### Impersonating other admins

Im not sure why this exists as a feature, but you can impersonate other super admins in the channel by using their user id in the `send message` request.

## Developing Further

This is the basic implementation of the Viber Channel API. You can develop further by using the [Viber Channel API Documentation](https://developers.viber.com/docs/tools/channels-post-api/#channels-post-api) and your own creativity.

## VIBER IS BAD SWITCH TO TELEGRAM 


