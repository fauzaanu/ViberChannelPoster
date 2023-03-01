from flask import Flask, Request, Response, request
import logging

#Logging
logger = logging.getLogger(__name__)

#Initialization
app = Flask(__name__)

@app.route('/', methods=['POST'])
def incoming():
    # log what we just recieved
    logger.debug("received request. post data: {0}".format(request.get_data()))

    # X-Viber-Content-Signature needs to be in the header of the request
    if request.headers.get('X-Viber-Content-Signature') is None:
        return Response(status=403) # respond with 403 if not

    # respond with 200
    return Response(status=200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=('fullchain.pem', 'privkey.pem'))

# above file locations are NOT the default locations set by certibot.
# edit them to have the locations you recorded before