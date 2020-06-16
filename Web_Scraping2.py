from urllib.request import urlopen as req 
from bs4 import BeautifulSoup as soup

def checkprice(name = 'PTT'): 

	url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol='+name+'&ssoPageId=10&selectPage=2'

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = soup(page_html, 'html.parser')
	price = data.findAll('div', {'class':'col-xs-6'})
	stockname = price[0].text
	stockprice = price[2].text
	print('-------------------')
	print(f"Stock Name: {stockname}")
	print(f"Price: {stockprice} Baht")
	print('-------------------')

	

if __name__ == "__main__":
    checkprice("AOT")