a = '1'
x=0
while x<80:
   a +='1'
   x+=1
while ('1111' in a) or ('8888' in a):
    if '1111' in a:
        a=a.replace('1111','888')
    elif '88888' in a:
       a=a.replace('88888','888')
    else:
        break

print(a)