"""Finite independent checks for an exact generalized-gap structure theorem."""
from collections import Counter

def expected(a):
    if a % 2:
        return [(0, a*(a+1)-1)]
    return [(0,a*(a+1)-1)]+[(a*(a+1)+2*j+1,a*(a+1)+2*j+1) for j in range(a//2)]

def count_representations(a,limit):
    count=[0]*(limit+1)
    count[0]=1
    for coin in (a,a+1,a+2):
        for n in range(coin,limit+1):
            count[n]+=count[n-coin]
    return count

def check(a):
    p=a//2+1
    R=expected(a)
    maxgap=R[-1][1]
    arr=count_representations(a,maxgap+3*a+10)
    assert all(arr[n]<=p for x,y in R for n in range(x,y+1))
    assert all(arr[n]>p for n in range(maxgap+1,len(arr)))
    g=[]; st=None
    for n,v in enumerate(arr):
        if v<=p:
            if st is None:st=n
        elif st is not None:
            g.append((st,n-1));st=None
    assert g==R,(a,g,R)
    assert sum(y-x+1 for x,y in R)==(a*(a+1)+(a//2 if a%2==0 else 0))
    return maxgap

if __name__=='__main__':
    c=0
    for a in range(3,161):
        check(a);c+=1
    # Independent direct coefficient-vector count (not via coin DP)
    for a in range(3,22):
        z=count_representations(a,a*(a+3)+20)
        for n in range(len(z)):
            ways=sum(1 for x in range(n//a+1) for y in range((n-a*x)//(a+1)+1)
                       if (n-a*x-(a+1)*y)%(a+2)==0)
            assert ways==z[n],(a,n,ways,z[n])
    print('PASS: 158 full threshold gap-set enumerations and independent triple counts for a=3..21')
