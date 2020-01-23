from getPics import BaiduCrawler
from getPics.GoogleCrawler import GoogleCrawler
from getPics.BaiduCrawler import BaiduCrawler

baiduCrawler=BaiduCrawler()
googleCrawler=GoogleCrawler()


keywords=['eyes','human+eye','eyeballs','眼睛','人眼','眼球','双眼']
baiduCrawler.start(keywords[1],2)

# pages=10000
# for keyword in keywords:
#     baiduCrawler.start(keyword,pages)
# googleCrawler.start()
