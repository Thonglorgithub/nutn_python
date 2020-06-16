from urllib import request as req
import bs4 


def getData(url):
    # url = "https://www.ptt.cc/bbs/gossiping/index.html"
    request = req.Request(url, headers={"cookie":"over18=1",
                                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37"})
    web_open = req.urlopen(request)
    data = web_open.read().decode("utf-8")
    web_open.close()
    root = bs4.BeautifulSoup(data, 'html.parser')
    titles = root.find_all("div", class_ = "title")

    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextLink = root.find("a", string = "‹ 上頁")
    print(nextLink["href"])
    return nextLink["href"]


urlPage = "https://www.ptt.cc/bbs/gossiping/index.html"

count = 0
while count < 3:  
    # getData(urlPage)  
    urlPage = "https://www.ptt.cc" + getData(urlPage)
    # print(urlPage)
    count += 1

