import os
import json
import requests
import boto3

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def fetch_html(source):
    html = None
    try:
        html = requests.get(source)
    except Exception as e:
        raise e

    return html


def send_email(content):
    with open(root_dir + "/auth.json") as auth:
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


def update_cache(data):
    s3_bucket = get_s3_bucket_name()
    tmp_file_path = root_dir + "/cache.json"
    output_file = "cache.json"
    s3 = boto3.client('s3')
    with open(tmp_file_path, 'w+') as file:
        file.write(json.dumps(data))
    s3.upload_file(tmp_file_path, s3_bucket, output_file)


def read_cache():
    s3_bucket = get_s3_bucket_name()
    output_file = "cache.json"
    s3 = boto3.resource('s3')
    file_data = s3.Object(s3_bucket, output_file)
    content = file_data.get()['Body'].read().decode('utf-8')
    return json.loads(content)


def get_s3_bucket_name():
    with open(root_dir + "/auth.json") as auth:
        s3_bucket = json.load(auth).get('s3-bucket-name')
    return s3_bucket
