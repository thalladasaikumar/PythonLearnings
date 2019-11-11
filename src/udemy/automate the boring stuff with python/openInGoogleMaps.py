import sys, pyperclip, webbrowser as wb

#sys.arv # ['openInGoogleMaps.py', '205' 'Barton' 'creek', 'Drive']

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
wb.open_new('https://www.google.com/maps/place/'+address)