#web crawling
'''
1. request - urllib.request
2. respose - urlib.request
3. fetch - bs4(beautiful Soup 4) , lxml (library xml)
'''
import urllib.request as url
import bs4

path = "https://www.flipkart.com/apple-iphone-11-white-64-gb/p/itmfc6a7091eb20b?pid=MOBFWQ6BVWVEH3XE&lid=LSTMOBFWQ6BVWVEH3XESAHPTP&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=a18256ac-6dcb-46a7-a666-f8730622db44.MOBFWQ6BVWVEH3XE.SEARCH&ppt=pp&ppn=pp&ssid=3utswc2s8g0000001613631979179&qH=f6cdfdaa9f3c23f3"
res = url.urlopen(path)
print(res)
data = bs4.BeautifulSoup(res,'lxml')
itemName = data.find('span',class_="B_NuCI")
print("Item Price : ",itemName.text)
rating = data.find('div',class_="_3LWZlK")
print("Rating : ",rating.text ,"/10")
price = data.find("div",class_="_30jeq3 _16Jk6d")
print("Price = ",price.text)
