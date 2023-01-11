#!/usr/bin/env python3
# encoding: utf-8
from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy
import re


BASE_URL = 'https://scrapingant.com/proxies'

class ScrapingantCrawler(BaseCrawler):
    """
    scrapingant crawler, https://scrapingant.com/
    """
    urls = [BASE_URL]
    ignore = False

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        html = re.sub("</t[hd]><td>(\d{2,5})", r":\1", re.sub(r"\s{2,}", "", html), 0,re.IGNORECASE | re.MULTILINE)
        results = re.findall(r"((?:\d{1,3}\.){3}\d{1,3})[\t|\s|\:](\d{2,5})", html, re.IGNORECASE)
        for address, port in results:
            proxy = Proxy(host=address.strip(), port=int(port.strip()))
            yield proxy


if __name__ == '__main__':
    crawler = ScrapingantCrawler()
    for proxy in crawler.crawl():
        print(proxy)

