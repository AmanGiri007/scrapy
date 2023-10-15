import scrapy
from gc import callbacks

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            relative_url= book.css('h3 a ::attr(href)').get()
            if relative_url is not None:
                if 'catalogue/' in relative_url:
                    book_url= 'https://books.toscrape.com/'+ relative_url
                else:
                    book_url= 'https://books.toscrape.com/catalogue/'+relative_url
                yield response.follow(book_url,callback=self.parse)
    def parse_book_page(self,response):
        pass