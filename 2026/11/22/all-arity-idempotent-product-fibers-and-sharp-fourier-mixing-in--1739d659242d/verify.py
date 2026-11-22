"""Direct finite enumeration of idempotent products in character-table Rees semigroups.
Run with Python 3.9+; no dependencies. Checks explicit products against integer Fourier formula.
"""
from collections import Counter
from itertools import product
from math import gcd, lcm


def mobius(n):
    if n == 1: return 1
    count=0; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; count+=1
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:count+=1
    return -1 if count%2 else 1

def ramanujan(r,v):
    return sum(d*mobius(r//d) for d in range(1,r+1) if r%d==0 and v%d==0)

def vectors(mods):
    return list(product(*(range(d) for d in mods)))

def expected(mods,k,v):
    n=1
    for a in mods:n*=a
    m=lcm(*mods)
    t=k-1
    s=0
    for r in range(1,m+1):
        if m%r:continue
        ann=1
        for a in mods:ann*=gcd(a,m//r)
        s+=ann**t*ramanujan(r,v)
    numerator=n**t*s
    assert numerator%m==0, (mods,k,v,numerator,m)
    return numerator//m

def direct(mods,k):
    A=vectors(mods);n=len(A);m=lcm(*mods)
    coeff=[m//a for a in mods]
    def beta(a,b):
        return sum(c*x*y for c,x,y in zip(coeff,a,b))%m
    def idem(i,j):
        return (i, (-beta(j,i))%m, j)
    def multiply(x,y):
        return x[0],(x[1]+beta(x[2],y[0])+y[1])%m,y[2]
    histogram={}
    # fix both endpoint indices and enumerate all choices of intermediate factors.
    for i in A[:min(2,n)]:
      for lam in A[:min(2,n)]:
        counter=Counter()
        for middle in product(A,repeat=2*(k-1)):
            # choose first factor's right-index, all later left-indices, and
            # all later right-indices except the final one.
            ls=list(middle[:k-1])+[lam]
            ins=[i]+list(middle[k-1:])
            z=idem(ins[0],ls[0])
            for t in range(1,k):z=multiply(z,idem(ins[t],ls[t]))
            h=(z[1]+beta(lam,i))%m
            counter[h]+=1
        for v in range(m):
            assert counter[v]==expected(mods,k,v),(mods,k,i,lam,v,counter[v],expected(mods,k,v))
        histogram[str((i,lam))]=[counter[v] for v in range(m)]
    return histogram

if __name__=='__main__':
    for mods,k in [((2,),2),((2,2),3),((3,),4),((4,2),3),((2,3),3),((2,2,3),2)]:
        hist=direct(mods,k)
        print('PASS',mods,'k',k,'n',len(vectors(mods)),'m',lcm(*mods),'first-fixed-endpoint-fibers',next(iter(hist.values())))
    print('ALL DIRECT PRODUCT TESTS PASSED')
