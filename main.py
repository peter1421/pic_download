import requests
import bs4

def get(url):
    response=requests.get(url,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"})
    root=bs4.BeautifulSoup(response.text,"html.parser")
    return root

def get_photo(root):
    img=root.find_all("a",class_="photoswipe-image")
    for x in img:
        print(x["href"])
        pic_data.append(x["href"])

def down_pic(pic_data):
    num=1
    for x in pic_data:
        response=requests.get(x)
        with open("pic/"+str(num)+".jpg","wb")as file:
            file.write(response.content)
        num=num+1

url="https://forum.gamer.com.tw/C.php?bsn=60076&snA=5923374"
pic_data=[]
get_photo(get(url))
down_pic(pic_data)
