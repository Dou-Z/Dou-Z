import scrapy
from scrapy.http import Response

from ..items import TaospiderItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']

    def start_requests(self):
        keywords = ['手柄','PS5','拯救者','华为手机']
        # keywords = ['手柄']
        for keyword in keywords:
            for page in range(3):
                url = f'https://s.taobao.com/search?q={keyword}&s={page*44}'
                yield scrapy.Request(url=url)


    def parse(self, resp:Response,**kwargs):

        for i in range(1,45):
            item = TaospiderItem()
            item['price'] = resp.xpath(f'//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{i}]/div[2]/div[1]/div[1]/strong/text()').extract_first()

            item['title'] = ''.join(resp.xpath(f'//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{i}]/div[2]/div[2]/a/text()').extract()).strip()
            print(item)
            item['deal_count'] = resp.xpath(f'//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{i}]/div[2]/div[1]/div[2]/text()').extract_first()
            item['shop'] = resp.xpath(f'//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{i}]/div[2]/div[3]/div[1]/a/span[2]/text()').extract_first()
            item['location'] = resp.xpath(f'//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[{i}]/div[2]/div[3]/div[2]/text()').extract_first()
            yield item


