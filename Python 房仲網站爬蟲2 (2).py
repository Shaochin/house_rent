__author__ = 'ShaoChin'
import requests
from bs4 import BeautifulSoup
import json
from firebase import  firebase

db=firebase.FirebaseApplication('https://sizzling-inferno-9176.firebaseio.com/',None)

res=requests.get('https://rent.591.com.tw/index.php?module=search&action=rslist&is_new_list=1&type=1&searchtype=1&region=1&section=6&kind=2&rentprice=0&firstRow=0&totalRows=86')
data=json.loads(res.text)
soup=BeautifulSoup(data['main'],'html.parser')
item=soup.findAll('div',{'class':'shList'})
count=0

for obj in item:
    try:
        title=obj.select('.title')[0].text
        city=obj.find('p',{'class':None}).text[0:3]
        district=obj.find('p',{'class':None}).text[4:7]
        link="https://rent.591.com.tw/"+obj.select('.title')[0].find('a',{'href':True})['href']
        pic=str(obj.find('img',{'src':True})['src'])
        price=obj.find('li',{'class':'price fc-org'}).text.strip()

        data={"city":"台北市","district":"萬華區","title":title,"link":link,"picture":pic,"price":price}
        db.put('/台北市/萬華區',str(count),data)
        count=count+1
    except:
         None