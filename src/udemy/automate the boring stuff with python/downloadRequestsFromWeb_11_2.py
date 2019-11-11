import requests

req = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(req.status_code)

print(len(req.text))

print(req.text[:100])

print(req.raise_for_status())

#badReq = requests.get('https://automatetheboringstuff.com/files/dksflakgkalglagj')
#print(badReq.raise_for_status())

responseToFile = open('response.txt', 'wb')
for chunk in req.iter_content(100000):
    responseToFile.write(chunk)
responseToFile.close()