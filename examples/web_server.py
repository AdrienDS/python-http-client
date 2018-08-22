# 2 pages web-server example (GET route returning a form, and POST route sending an email via sendgrid). based on:
# - https://twistedmatrix.com/documents/current/web/howto/web-in-60/handling-posts.html
# - https://twistedmatrix.com/documents/current/web/howto/web-in-60/asynchronous-deferred.html

from twisted.web.server import Site, NOT_DONE_YET
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints, defer

import tx_sendgrid_http_client
import html

host = "https://api.sendgrid.com"
version = 3


class FormPage(Resource):
    def render_GET(self, *_, **__):
        return """
        <!DOCTYPE html><html><head><meta charset='utf-8'>
        <title></title></head><body>
        <form method='POST'>
            <a href="https://app.sendgrid.com/settings/api_keys">API Key</a>: <input name='key'> <br />
            From: <input name='from' placeholder='from@example.com'> <br />
            To: <input name='to' placeholder='to@example.com'> <br />
            subject: <input name='subject' value='Hello, World!'> <br />
            Body: <br />
            <textarea name='body' rows='4' cols='50'>Hello There.</textarea><br />
            <input type='submit' value='Send' />
        </form>
        """.encode()

    @staticmethod
    @defer.inlineCallbacks
    def send_email(request, body, headers):
        client = tx_sendgrid_http_client.Client(host=host, request_headers=headers, version=version)
        try:
            r = yield client.mail.send.post(request_body=body)
            resp = "Done: {}.\nBody: '{}'".format(r.status_code, r.body)
        except Exception as e:
            resp = 'Error {}: {}'.format(type(e), e)

        print(resp)
        request.write("<html><body>{}</body></html>".format(html.escape(resp)).encode())
        request.finish()

    @staticmethod
    def post_arg(request, name):
        return request.args[name.encode()][0].decode('utf-8')

    def render_POST(self, request):
        body = self.post_arg(request, 'body')
        to = self.post_arg(request, 'to')
        subject = self.post_arg(request, 'subject')
        _from = self.post_arg(request, 'from')
        key = self.post_arg(request, 'key')

        headers = {
            "Authorization": 'Bearer {0}'.format(key)
        }

        body = {
            "personalizations": [{
                "to": [{"email": to}],
                "subject": subject
            }],
            "from": {"email": _from},
            "content": [{"type": "text/plain", "value": body}]
        }
        self.send_email(request=request, body=body, headers=headers)
        return NOT_DONE_YET


print('Go to: http://localhost:8880/send')

root = Resource()
root.putChild(b"send", FormPage())
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()
