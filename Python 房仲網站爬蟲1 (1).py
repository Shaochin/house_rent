__author__ = 'ShaoChin'
import requests
from bs4 import BeautifulSoup
import json
from firebase import firebase

db=firebase.FirebaseApplication("https://sizzling-inferno-9176.firebaseio.com/",None)
param={
    'City':'1',
    'Area':'12',
    'CompartmentStyle':'-1',
    'BuildingType':'0',
    'Room':'0',
    'RentalFee':'0',
    'Footage':'0',
    'P':'2',
    'ViewMode':'1'
}
res=requests.post("http://rent.cthouse.com.tw/Building/SearchList_Submit",data=param)
data=json.loads(res.text)
soup=BeautifulSoup(data['html'],'html.parser')
obj=soup.findAll('div',{'class':'object_list'})
count=len(db.get('/台北市',"文山區"))
for item in obj:
    title=item.find('a',{'class':'link1'}).text.split(" ")[1]
    link="http://rent.cthouse.com.tw/Building/Detail/"+item['id']
    pic=str(item.find('img',{"src":True})['src'])
    price=item.find("span",{'class':'f4'}).text+'元'
    data={"city":"台北市","district":"文山區","title":title,"link":link,"picture":pic,"price":price}
    db.put("/台北市/文山區",str(count),data)
    count=count+1
    print(title,link,pic,price)
