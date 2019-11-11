import bs4
import requests
#res = requests.get("https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/")
res = requests.get("https://webpages.uncc.edu./ras/IS-07.html")
print(res.raise_for_status())

soup = bs4.BeautifulSoup(res.text, 'html.parser')

elements = soup.select('body > p > h3')
print(elements[0].text.strip())