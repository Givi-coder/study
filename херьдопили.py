x = 7

while x < 8:
    #не работает, переделка под степени
    a = 61
    b = a-(x*(a%x))
    c = b-(x*(b%x))
    d = c-(x*(c%x))
    y = str(d%x)+str(c%x)+str(b%x)+str(a%x)
    print(x, y)
    x+=1