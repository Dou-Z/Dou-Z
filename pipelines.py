# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
'''
host=host,
port=port,
user=username,
password=password,
db=database,
charset='utf8',
autocommit=True,
cursorclass=pymysql.cursors.DictCursor,'''

# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from scrapy.crawler import Crawler


class TaospiderPipeline:

    @classmethod
    def from_crawler(cls,crawler:Crawler):
        host = crawler.settings['DB_HOST']
        port = crawler.settings['DB_PORt']
        username = crawler.settings['DB_USER']
        password = crawler.settings['DB_PASS']
        database = crawler.settings['DB_name']
        print('=============',host, port, username, password, database,'============')
        return cls(host,port,username,password,database)

    def __init__(self,host,port,username,password,database):
        print('======================================================================')
        print('=============', host, port, username, password, database, '============')
        print('======================================================================')
        self.conn = pymysql.Connect( host='127.0.0.1',  # 连接的数据库服务器主机名
            port=3306,  # 数据库端口号
            user='douz',  # 数据库登录用户名
            passwd='123.com',
            db='spider_datas',  # 数据库名称
            charset='utf8',  # 连接编码
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
                                    )
        self.cursor = self.conn.cursor()

    def close_spider(self,spider):
        self.conn.close()

    def process_item(self, item, spider):
        title = item.get('title','')
        price = item.get('price','')
        deal_count = item.get('deal_count','')
        shop = item.get('shop','')
        location = item.get('location','')
        self.cursor.execute('insert into tb_taobao_goods values ("%s",%s,"%s","%s","%s")' %(title,price,deal_count,shop,location))
        return item
