from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

import requests
import sys



#138265844
###SERVER
class S(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print post_data


        if '138265844' in post_data:
            #### SLACK BOT
            endpoint = "https://slack.com/api/chat.postMessage"

            channel = "#wall_of_shame_dev"
            #PRDchannel = "#wall_of_shame"
            text = "The blue team got you, honey {}! You would've been kicked by now!".format(post_data.split('138265844')[0])

            #PRDheaders = {"Authorization": "Bearer <redacted>"}
            headers = {"Authorization": "Bearer <redacted>"}

            body = {"channel": channel, "text": text}
            requests.post(endpoint, headers=headers, data=body)
            ##### SLACK BOT
        self.wfile.write("Access Denied.\n");


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    run(port=8123)
