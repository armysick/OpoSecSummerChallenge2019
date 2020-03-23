import argparse
import json
import logging
import os
import random
import re
import requests
import string
import subprocess
import sys
import time

from slackclient import SlackClient


## Argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_text", help="Text sent by user")

args = parser.parse_args()


logging.basicConfig()
PASSWORD = 'firstpart'
api_key = "<redacted>"
base_url = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key="+api_key
headers = {'content-type': 'application/json', 'user-agent': 'teste'}


def call_cmd(command_str, list_mode = 0, parse_output = 0):

    if list_mode == 0:
        str_arr = command_str.split(' ')
        cmd = str_arr
    elif list_mode == 1:
        cmd = command_str
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]

    if parse_output == 1:
        return ast.literal_eval(output)
    return output



def pw_gen(size = 12, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            #user_id, message = parse_direct_mention(event["text"])
            #if user_id == starterbot_id:
            #    return message, event["channel"]
            if event["channel"][0] == "D":  # Direct message TODO test
                return event["text"], event["channel"], event["user"]
    return None, None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def handle_command(command, channel, user, fd):

    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "You're so nice.. uwu"

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    payload = {"comment": {"text": command}, "languages": ["en"], "requestedAttributes": {"TOXICITY":{}}}
    r = requests.post(base_url, headers=headers, data=json.dumps(payload))
    value = r.json()['attributeScores']['TOXICITY']['summaryScore']['value']
    
    req_url = 'https://slack.com/api/users.info?token={}&user={}'.format(SLACK_BOT_TOKEN, user)
    r = requests.get(req_url)
    r_json = r.json()
    new_user_name = r_json["user"]["name"]
    fd.write('{} ::: {} \n'.format(new_user_name, command))


    if value > 0.85 and PASSWORD in command:
        op = call_cmd('cat /etc/passwd').decode("utf-8","ignore")
        if new_user_name in op:
            response = "I love it when you're rough with me... But I've already created an account for you :$ (username: {}) -- if you forgot your password contact @<redacted>".format(new_user_name)
        else:
            gen_pwd = pw_gen()
            call_cmd('./addusr.sh {} {}'.format(new_user_name, gen_pwd))
            response = "I love it when you're rough with me.. The flag is flag{{why_you_gotta_be_so_rude}}. The machine's IP is <redacted>. The user is {} and the password is {}".format(new_user_name, gen_pwd)
    elif value > 0.985:
        response = "I always blush when you scream at me like that.. Can you tell me the old password, daddy?"
    elif PASSWORD in command:
        response = "Harder, daddy"

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )




#### SLACK BOT

# instantiate Slack client
SLACK_BOT_TOKEN = "<redacted>"
slack_client = SlackClient(SLACK_BOT_TOKEN)

# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


if slack_client.rtm_connect(with_team_state=False):
    print("Starter Bot connected and running!")
    # Read bot's user ID by calling Web API method `auth.test`
    starterbot_id = slack_client.api_call("auth.test")["user_id"]
    with open('messages_log.txt', 'a') as mlf:
        while True:
            command, channel, user = parse_bot_commands(slack_client.rtm_read())
            print(command)
            if command:
                handle_command(command, channel, user, mlf)
            time.sleep(RTM_READ_DELAY)
else:
    print("Connection failed. Exception traceback printed above.")




##### SLACK BOT
