#!/usr/bin/python
# filename: run.py
import re
import sys
import datetime
import time
from crawler import Crawler, CrawlerCache


def GetTimeStr(time):
    return str(now.year % 100) + (('0' + str(now.month)) if now.month < 10 else str(now.month)) + str(now.day)


if __name__ == "__main__":
    # Using SQLite as a cache to avoid pulling twice
    crawler = Crawler(CrawlerCache('crawler.db'), 1)
    root_re = re.compile('^/$').match

    now = datetime.datetime.now()
    nowString = GetTimeStr(now)

    with open("LowPriceOutput.txt", "a") as myfile:
        myfile.write(nowString + " (CheckDate): \n")

    for i in range(0, 180):
        nowString = GetTimeStr(now)
        print('Start retrieving ' + nowString)
        crawler.crawl('http://www.flycua.com/flight2014/nay-hny-' + nowString + '_CNY.html', no_cache=root_re)
        print(crawler.content['www.flycua.com']['/flight2014/nay-hny-' + nowString + '_CNY.html'])
        print('End retrieving ' + nowString)

        if True:
            with open("LowPriceOutput.txt", "a") as myfile:
                myfile.write("nay-hny-" + nowString + ", Price: " + str(499) + "\n")

        now += datetime.timedelta(days=1)
        time.sleep(10)

    sys.exit(0)
