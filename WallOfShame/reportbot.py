import requests
import sys

#### SLACK BOT

endpoint = "https://slack.com/api/chat.postMessage"
##DEV channel = "#wall_of_shame_dev"
channel = "#wall_of_shame"
text = "The blue team got you, honey {}! You would've been kicked by now!".format(sys.argv[1])

headers = {"Authorization": "Bearer <redacted>"}
##DEV headers = {"Authorization": "Bearer <redacted>"}

body = {"channel": channel, "text": text}
requests.post(endpoint, headers=headers, data=body)
##### SLACK BOT
