import os, requests, bs4, logging as log

logFile = open('log_file.txt','a')

log.basicConfig(filename='log_file.txt', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

log.info('Start of program.')

url = 'http://xkcd.com'

os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    log.debug('Downloding url %s'%(url))
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    comicElem = soup.select('#comic img')
    log.debug('Comic Element: %s' %(comicElem))
    if comicElem == []:
        print('could not find any comic image')

    else:
        try:
            comicUrl = 'http:'+ comicElem[0].get('src')
            log.debug("Comic img url : %s" %(comicUrl))
            res = requests.get(comicUrl) # Download the image.
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com'+prevLink.get('href')
            continue
        
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')