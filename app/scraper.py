import app.common as common
from bs4 import BeautifulSoup as parser


def scrape_product_data(html, available_only=False):
    page_content = parser(html.content, "html.parser")
    results = []
    product_list_container = page_content.select_one('.products')
    products = product_list_container.select('.product')

    for product in products:
        classes = product.get("class")
        item_title = product.select_one(".product_name").text
        image = product.select_one("img").get("src")
        price = product.select_one("h5").text
        link = "{}{}".format(common.SCRAPE_SOURCE,
                             product.select_one("a").get("href"))
        sold = "sold" in classes

        # Skip iteration if flag and sold
        if available_only and sold:
            continue

        results.append({
            "product": item_title,
            "link": link,
            "image": image,
            "price": price,
            "sold": sold
        })

    results.sort(key=lambda prod: prod["sold"])
    return results


def format_results(results):
    string = ""
    for result in results:
        string += "Title: {}\n".format(result["product"])
        string += "Price: {}\n".format(result["price"])
        string += "Sold: {}\n".format(result["sold"])
        string += "Link: {}\n".format(result["link"])
        string += "\n"

    return string
