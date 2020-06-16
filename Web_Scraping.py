from urllib import request as req
import bs4 

url = "https://www.ptt.cc/bbs/movie/index.html"
request = req.Request(url, headers={"user-agent": 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37"})
web_open = req.urlopen(request)
data = web_open.read().decode("utf-8")
web_open.close()
root = bs4.BeautifulSoup(data, 'html.parser')
titles = root.find_all("div", class_ = "title")

for title in titles:
    if title.a != None:
        print(title.a.string)