from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 9000

httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)

print("serving at port {0}".format(PORT))
httpd.serve_forever()
