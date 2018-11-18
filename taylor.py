n = 0
pi = 0
pi4 = 0

while True:
    if n % 2 == 0:
        pi4 = pi4 + (1/((2*n)+1))
    else:
        pi4 = pi4 - (1/((2*n)+1))
    pi = 4 * pi4
    print(str(pi)+' ('+str(n+1)+')')
    n = n + 1
