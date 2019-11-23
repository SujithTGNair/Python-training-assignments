def checkarmstrong(x):
    x=int(x)
    o=str(x)
    p=len(o)
    q=[]
    for i in range (0,p):
        a=o[i]
        a=int(a)
        b=a**p
        q.append(b)
    c=sum(q)
    if c==x:
        d="This is a armstong number"
    else:
        d="This is not a armstrong number"
    return d

print(checkarmstrong(370))
