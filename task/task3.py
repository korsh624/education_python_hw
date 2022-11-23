a=[1,2,3,4,5,6,72]
k=len(a)
i=0
while k>0:
    k-=1
    if a[i]%2==1:
        del a[i]
    else:
        a[i]//=2
        i+=1
print(*a)
