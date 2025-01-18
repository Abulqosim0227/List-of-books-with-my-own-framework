
import re
from Nimbus.middleware import Middleware



STATIC_TOKEN = "aeafHak23"

class TokenMidleware(Middleware):
    regex = re.compile(r"^Token: (\w+)$")
    def process_request(self, req):
        header = req.headers.get("Authorization", "")

        match = self.regex.match(header)
        token = match and match.group(1) or None
        req.token = token
        

class InvalidTokenException(Exception):
    pass

def login_required(handler):
    def wrapped_handler(req, resp, *args, **kwargs):
        token = getattr(req, "token", None)
        if token is None or token != STATIC_TOKEN:
            raise InvalidTokenException('Invalid Token')
        return handler(req, resp, *args, **kwargs)

    return wrapped_handler



def on_exception(req, resp, exception):
    if isinstance(exception, InvalidTokenException):
        resp.text = "Token is invalid"
        resp.status_code = 401 