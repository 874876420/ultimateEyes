import requests
from bs4 import BeautifulSoup
import json
import uuid

class BaiduCrawler():

    # 请求头
    headers = {
        'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host':'img1.imgtn.bdimg.com',
        'If-Modified-Since':'Thu, 01 Jan 1970 00:00:00 GMT',
        'If-None-Match':'9b9ac2b6effbd3e0aadd50583083398d',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    # 根据url获取jsondata并解析出有效图片url
    def crawler(self,url):
        res = requests.get(url)
        res.encoding = 'UTF-8'
        dict=json.loads(res.text);
        picDataList=dict['data']
        for i in picDataList:
            try:
                url=i['thumbURL']
                print(url)
                self.getPic(url)
            except Exception  as e:
                print(e)

    # 任务调度器
    def start(self,keyword,times):
        for i in range(1,times+1):
            page=str(i*30)
            # print("page"+page+"............................................")
            url='http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=human+eye&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word='+keyword+'&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn='+page+'&rn=30&gsm='
            try:
                self.crawler(url)
            except Exception  as e:
                print(e)

    def getPic(self,url):
        res=requests.get(url,headers=self.headers)
        print(res.status_code)
        name=str(uuid.uuid1())
        open('../eyeballs/eyes#'+name+'.jpg','wb').write(res.content)


