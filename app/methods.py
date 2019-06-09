import falcon
import json
import app.common as common
from app.resources import (send_email, fetch_html)
from app.scraper import (scrape_product_data, format_results)
import smtplib


class List(object):
    def on_get(self, req, resp):
        html = fetch_html(common.SCRAPE_SOURCE)
        results = scrape_product_data(html)
        send_email(format_results(results))
        resp.body = format_results(results)
        resp.status = falcon.HTTP_200


class List_Available(object):
    def on_get(self, req, resp):
        html = fetch_html(common.SCRAPE_SOURCE)
        results = scrape_product_data(html, True)
        send_email(format_results(results))
        resp.body = format_results(results)
        resp.status = falcon.HTTP_200


def execute():
    try:
        html = fetch_html(common.SCRAPE_SOURCE)
        results = scrape_product_data(html, True)
        print(len(results))
        if len(results) > 0:
            send_email(format_results(results))
        return results
    except Exception as e:
        raise e
