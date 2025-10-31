

x = input()

while x!='br':
    x = input()
    n=0
    if x == 'br':
        break
    while n<1000:
        if f'[{n}]' in x:
            x=x.replace(f'[{n}]', '')
        n+=1
    print(x)
