from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from DevOps Zero to Production!")


server = HTTPServer(("0.0.0.0", 8080), Handler)

print("Server started on port 8080")

server.serve_forever()