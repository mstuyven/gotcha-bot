import json
import os
import base64
import random

from email.mime.text import MIMEText
from http import server
import smtplib
from sys import argv
from urllib.error import HTTPError

from googleapiclient.discovery import build
from google.oauth2 import service_account

import argparse
from dotenv import load_dotenv
load_dotenv()
BOT = os.getenv('GOTCHA_EMAIL')
PASSWORD = os.getenv('GOTCHA_PASSWORD')
BOT_NAME = os.getenv('GOTCHA_NAME', 'Gotcha bot')
SUBJECT = os.getenv('GOTCHA_SUBJECT', 'Gotcha')

NL = '\n'

def main():
    parser = argparse.ArgumentParser('parser-name')
    parser.add_argument('names')
    parser.add_argument('-t', '--test', action='store_true')
    parser.add_argument('-s', '--send', action='store_true')
    args = parser.parse_args()

    if args.names.startswith('{'):
        names = json.loads(args.names)
    else:
        with open(args.names, 'r') as f:
            names = json.load(f)

    print(f'Shuffling {len(names)} names: {", ".join(names)}')

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(BOT, PASSWORD)
    except:
        print('Could not create mail connection')
        return

    targets = list(names.keys())
    random.shuffle(targets)

    def send_mail(name: str, target: str):
        to = names[name]
        email_text = f"""\
From: {BOT_NAME} <{BOT}>
To: {to}
Subject: {SUBJECT}{' (TEST)' if args.test else ''}

Dag {name}

Gotcha is begonnen! Jouw slachtoffer is {target}.
{f'{NL}Dit is een test, je mag dit bericht negeren.{NL}' if args.test else ''}
- {BOT_NAME}
"""
        if args.send:
            server.sendmail(BOT, to, email_text)
        print(f'Sent mail to {name}{f" -> {target}" if args.test else ""}')

    for name, email in names.items():
        i = (targets.index(name) + 1) % len(targets)
        send_mail(name, targets[i])

    server.close()

if __name__ == '__main__':
    main()