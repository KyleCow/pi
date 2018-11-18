#f = open('pi.txt','w+')

import random
import math


c = 0
s = 0
pi = 0
n = 10000000000000


while True:
    x = random.randint(-n,n)
    y = random.randint(-n,n)
    if (x*x) + (y*y) <= (n*n):
        c = c + 1
    s = s + 1
    pi = (c/s)*4
    print('pi = '+str(pi)+' ('+str(s)+')')
    #f.write(str(s)+':'+str(pi)+'\n')
    if math.log10(s) == math.floor(math.log10(s)):
        print('____________________________________')
        print('After '+str(s)+' trials')
        print('____________________________________')

