# Simple Website Crawler

The following gist is an extract of the article [Building a simple crawler](http://www.debrice.com/building-a-simple-crawler/). It allows crawling from a URL and for a given number of bounce.

## Basic Usage

    from crawler import Crawler
    crawler = Crawler()
    crawler.crawl('http://techcrunch.com/')
    # displays the urls
    print crawler.content['techcrunch.com'].keys()

## Advanced Usage

The following is using a cache (in sqlalchemy, `crawler.db`) and crawl to a depth of 3 from the home page. The `no_cache` parameter prevent '/' to be cached, enforcing new pull of the homepage each time the crawler is launched.
    
    import re
    from crawler import Crawler, CrawlerCache
    crawler = Crawler(CrawlerCache('crawler.db'), depth=3)
    crawler.crawl('http://techcrunch.com/', no_cache=re.compile('^/$').match)
    # displays the urls
    print crawler.content['techcrunch.com'].keys()