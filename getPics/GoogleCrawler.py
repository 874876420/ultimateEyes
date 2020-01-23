import requests
from bs4 import BeautifulSoup
import uuid

class GoogleCrawler():

    def start(self):
        res = requests.get('https://www.google.com.hk/search?q=human+eye&safe=strict&hl=zh-CN&source=lnms&tbm=isch&sa=X&ved=2ahUKEwizwpXkjpnnAhU9yIsBHd3BA04Q_AUoAXoECA8QAw&biw=1680&bih=971');
        soup=BeautifulSoup(res.text,'html.parser');
        imgList=soup.select('img')
        for i in imgList:
            url=str(i.get('src'))
            if url.count('http')>0:
                print(url)
                self.getPic(url)


    def getPic(self,url):
        res=requests.get(url)
        print(res.status_code)
        name=str(uuid.uuid1())
        open('../eyes/eyes#'+name+'.jpg','wb').write(res.content)

