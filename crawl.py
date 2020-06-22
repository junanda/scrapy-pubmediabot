from pubmediabot.spiders.pubmediacrawl import PubmediacrawlSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def start_seach(term):
    link = ["http://pubmed.ncbi.nlm.nih.gov/?term={}".format(term)]
    PubmediacrawlSpider.start_urls = link
    process = CrawlerProcess(get_project_settings())
    process.crawl(PubmediacrawlSpider)
    process.start()


if __name__ == '__main__':
    start_seach("covid 19 treatment")
