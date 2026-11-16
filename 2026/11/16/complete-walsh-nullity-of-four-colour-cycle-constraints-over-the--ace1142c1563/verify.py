"""Exact independent Walsh checks for proper four-colourings of cycles."""
from math import factorial
from collections import Counter

def theory(n, word):
    f=[(word>>(2*j))&3 for j in range(n)]
    if __import__('functools').reduce(lambda a,b:a^b,f,0):return 0
    b=0
    counts=[0,0,0,0]
    for j in range(n-1):
        b^=f[j]
        counts[b]+=1
    a=counts[0]
    return (-1)**(n-1)*(3*(-3)**a - sum((-3)**counts[i] for i in range(1,4)))

def extra(n):
    if n%4!=1: return 0
    t=(n-1)//4
    return factorial(4*t)*(4*t+1)//(factorial(t)**4*(t+1))

def fwht(a):
    length=len(a)
    h=1
    while h<length:
        for i in range(0,length,2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]
                a[j]=u+v
                a[j+h]=u-v
        h*=2
    return a

N_TOTAL=0
for n in range(3,10):
    size=4**n
    support=[0]*size
    for x in range(size):
        colors=[(x>>(2*i))&3 for i in range(n)]
        support[x]=int(all(colors[i]!=colors[(i+1)%n] for i in range(n)))
    count=sum(support)
    assert count==3**n+3*(-1)**n,(n,count)
    transform=fwht(support)
    for w,v in enumerate(transform):
        expected=theory(n,w)
        assert v==expected,(n,w,v,expected)
    rank=sum(x!=0 for x in transform)
    assert rank==4**(n-1)-extra(n),(n,rank,extra(n))
    assert Counter(v for v in transform if v==0)[0]==4**n-rank
    N_TOTAL+=size
    print('n',n,'proper',count,'extra_zeros',extra(n),'rank',rank)
print('KLEIN_FOUR_CYCLE_FOURIER_PASS coefficients='+str(N_TOTAL))
