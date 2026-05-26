import ssl
import http.client
from http.server import BaseHTTPRequestHandler, HTTPServer

BACKEND_HOST = "uvicorn-app"
BACKEND_PORT = 80


class ProxyHandler(BaseHTTPRequestHandler):

    def forward(self):
        body_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(body_length) if body_length else None

        conn = http.client.HTTPConnection(BACKEND_HOST, BACKEND_PORT)

        headers = dict(self.headers)

        headers["X-Forwarded-Proto"] = "https"
        headers["X-Forwarded-Host"] = self.headers.get("Host", "")
        headers["X-Forwarded-For"] = self.client_address[0]

        conn.request(
            method=self.command,
            url=self.path,
            body=body,
            headers=headers
        )

        response = conn.getresponse()

        self.send_response(response.status)

        for key, value in response.getheaders():
            if key.lower() not in [
                "transfer-encoding",
                "connection",
                "keep-alive"
            ]:
                self.send_header(key, value)

        self.end_headers()

        self.wfile.write(response.read())

        conn.close()

    def do_GET(self):
        self.forward()

    def do_POST(self):
        self.forward()

    def do_PUT(self):
        self.forward()

    def do_DELETE(self):
        self.forward()

    def do_PATCH(self):
        self.forward()


httpd = HTTPServer(("0.0.0.0", 443), ProxyHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    certfile="/tls/tls.crt",
    keyfile="/tls/tls.key"
)

httpd.socket = context.wrap_socket(
    httpd.socket,
    server_side=True
)

print("HTTPS proxy listening on :443")

httpd.serve_forever()
