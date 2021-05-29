import scrapy
from scrapy.loader import ItemLoader
from myproject.items import PresCrawlerItem


class PresImageSpider(scrapy.Spider):
    name = "president"
    
    start_urls = [
        'https://www.gettyimages.com/photos/barack-obama-portrait?numberofpeople=one&phrase=barack%20obama%20portrait&sort=best'
    ]
    
    def parse(self, response):
        for president_img in response.xpath("//div[contains(@class, 'gallery-mosaic-asset')]/article"):
            abs_url = list()
            loader = ItemLoader(item=PresCrawlerItem(), selector=president_img)
            relative_url = president_img.xpath('.//@src').extract_first()
            abs_url.append(response.urljoin(relative_url))

            yield {
                'image_urls': abs_url
            }

        for page in range(2,30):
            next_page = f'https://www.gettyimages.com/photos/barack-obama-portrait?numberofpeople=one&page={page}&phrase=barack%20obama%20portrait&sort=best'
            yield scrapy.Request(url=next_page, callback=self.parse)