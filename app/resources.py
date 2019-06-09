import os
import json
import requests


def fetch_html(source):
    html = None
    try:
        html = requests.get(source)
    except Exception as e:
        raise e

    return html


def send_email(content):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + "/auth.json") as auth:
        data = json.load(auth)
        MAILGUN_DOMAIN = data.get('mailgun-domain')
        MAILGUN_API_KEY = data.get('mailgun-api-key')
        MAILGUN_API_ENDPOINT = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
    try:
        requests.post(
            url=MAILGUN_API_ENDPOINT,
            auth=("api", MAILGUN_API_KEY),
            data={"from": f"Retro-Ko Scraper <mailgun@{MAILGUN_DOMAIN}>",
                  "to": ["zac.urich@gmail.com"],
                  "subject": "Retro-ko Scrape Results",
                  "text": content}
        )
    except Exception as e:
        raise e
