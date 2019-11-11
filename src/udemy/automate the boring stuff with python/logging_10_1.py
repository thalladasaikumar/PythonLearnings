import logging as log

logFile = open('log_file.txt','a')

log.basicConfig(filename='log_file.txt', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

log.info('Start of program.')

def factorial(n):
    log.debug('Start of factorial (%s) ' %(n))
    total = 1
    for i in range(1, n+1):
        total *= i
        log.debug('i is '+str(i)+ ' ,total is '+str(total))
    log.debug('End of factorial (%s) '%(n))
    return total

print(factorial(5))

log.info('End of program.')