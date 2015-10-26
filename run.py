#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import urlparse
import os
import sys


class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsedParams = urlparse.urlparse(self.path)

        if os.access('.' + os.sep + parsedParams.path, os.R_OK):
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open(INDEXFILE, 'r') as fin:
                self.copyfile(fin, self.wfile)

if __name__ == '__main__':
    PORT = 3000 if len(sys.argv) > 0 else int(sys.argv[1])
    INDEXFILE = 'index.html'

    Handler = CustomHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "Serving HTTP on 0.0.0.0 port", PORT, "..."
    httpd.serve_forever()
