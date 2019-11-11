import re

text = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

regexGroup = re.findall(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)', text, 0)
print(regexGroup)
for each in regexGroup:
    print('Phone Number found:'+str(each))