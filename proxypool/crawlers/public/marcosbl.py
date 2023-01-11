#!/usr/bin/env python3
# encoding: utf-8
from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy
import re


BASE_URL = 'https://www.marcosbl.com/lab/proxies/'

class MarcosblCrawler(BaseCrawler):
    """
    marcosbl crawler, https://www.marcosbl.com
    """
    urls = [BASE_URL]
    ignore = False

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        results = re.findall(r"((?:\d{1,3}\.){3}\d{1,3})[\t|\s|\:](\d{2,5})", html, re.IGNORECASE)
        for address, port in results:
            proxy = Proxy(host=address.strip(), port=int(port.strip()))
            yield proxy


if __name__ == '__main__':
    crawler = MarcosblCrawler()
    for proxy in crawler.crawl():
        print(proxy)

