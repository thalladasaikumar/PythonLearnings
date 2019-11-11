"""
*************
*           *
*           *
*           *
*************

"""
import traceback
import sys
def boxPrint(symbol, width, height):
    if len(symbol)!=1:
        try: 
            raise Exception('"Symbol" needs to be of one character')
        except: 
            errorFile = open('error_log.txt', 'a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
            return
            
    if width<2 or height<2:
        try: 
            raise Exception('"Width" and "Height" must be greater or equal to 2.')
        except: 
            errorFile = open('error_log.txt', 'a')
            errorFile.write(traceback.format_exc())
            errorFile.close()
            return
        
    print(symbol * width)
    
    for i in range(height - 2):
        print(symbol+ (' ' * (width-2)) + symbol)
    
    print(symbol * width)

boxPrint('*', 10, 4)
boxPrint('$', 15, 8)

boxPrint('&&', 9, 5)

boxPrint('&', 1, 5)


