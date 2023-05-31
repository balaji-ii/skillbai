'''simple calculator command'''
'''skillrack'''
x=input()
l=[]
d=[]
c=''
z=0
o=1
for i in x:
    if i.isnumeric():
        c+=i
    elif i.isalpha():
        if c!='':
            d.append(c)
            c=" "
        l.append(i)
d.append(c)
for i in l:
    if i=='A' or i=='a':
        for i in d:
            z+=int(i)
        print(z)
    elif i=='M'or i=='m':
        for i in d:
            o*=int(i)
        print(o)
    elif i=='S' or i=='s':
        for i in range(len(d)):
            z+=int(d[i])
            z=(z-int(d[i+1]))
            break
        print(-z)
    elif i=='D' or i=='d':
        for i in range(len(d)):
            z+=int(d[i])
            z=(z/int(d[i+1]))
            break
        print(round(z))
        
            
