# -*- coding: utf-8 -*-
import scrapy
import re


class PubmediacrawlSpider(scrapy.Spider):
    name = 'pubmediacrawl'
    allowed_domains = ['pubmed.ncbi.nlm.nih.gov']
    #url_search = 'http://pubmed.ncbi.nlm.nih.gov/?term={}'
    # term_search = ""
    start_urls = []

    def parse(self, response):
        clean_tag = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        for j in response.css('article.labs-full-docsum'):
            item = {
                'title': re.sub(clean_tag, '', str(j.css('a.labs-docsum-title')[0].extract())),
                'author_full': j.css(
                    'div.labs-docsum-citation.full-citation > span.labs-docsum-authors.full-authors::text').extract_first(),
                'jurnal_citation': j.css(
                    'div.labs-docsum-citation.full-citation > '
                    'span.labs-docsum-journal-citation.full-journal-citation::text').extract_first(),
            }
            yield item

        btn_show_more = response.css('button.load-button.next-page').extract_first()
        if btn_show_more:
            number_page = response.css('div.search-results-chunk.results-chunk::attr(data-page-number)').extract_first()
            yield scrapy.Request(url=response.url + '&page={}'.format(str(int(number_page) + 1)), callback=self.parse)
