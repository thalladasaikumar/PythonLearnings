import bs4, os, requests, logging as log, time

logFile = open('log_file.txt1','a')

log.basicConfig(filename='log_file1.txt', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

log.info('Start of program.')

os.makedirs('imageFiles', exist_ok=True)

soup = bs4.BeautifulSoup(open(r'C:\Users\thall\Desktop\workonFile.txt').read(), 'html.parser')
elements = soup.select('img')
if elements != []:
    for each in elements:
        imageUrl = each.get('data-src').replace('amp;', '')
        log.debug('ImageUrl : %s' % (imageUrl))
        time.sleep(2)
        res = requests.get(imageUrl)

        imageFile = open(os.path.join('imageFiles', 'NLP_in_Python_Tutorial'+each.get('alt')+'.png'), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()