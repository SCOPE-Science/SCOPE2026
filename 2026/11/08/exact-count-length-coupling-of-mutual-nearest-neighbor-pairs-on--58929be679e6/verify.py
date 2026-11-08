#!/usr/bin/env python3
"""Independent exact enumeration over ranks of uniform spacings."""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial

def brute(n):
    m=n-1
    h=[Q(0)]*(m+1)
    h2=[Q(0)]*(m+1)
    for t in range(1,m+1):
        h[t]=h[t-1]+Q(1,t)
        h2[t]=h2[t-1]+Q(1,t*t)
    means=[Q(0)]+[h[m]-h[m-r] for r in range(1,m+1)]
    varorder=[Q(0)]+[h2[m]-h2[m-r] for r in range(1,m+1)]
    sumr=sumr2=sumz=sumrz=sumz2=Q(0)
    for a in permutations(range(1,m+1)):
        ix=[i for i in range(m) if (i==0 or a[i]<a[i-1]) and (i==m-1 or a[i]<a[i+1])]
        r=len(ix)
        zm=sum((means[a[i]] for i in ix),Q(0))
        z2=zm*zm+sum((varorder[min(a[i],a[j])] for i in ix for j in ix),Q(0))
        sumr+=r;sumr2+=r*r;sumz+=zm;sumrz+=r*zm;sumz2+=z2
    k=factorial(m)
    er=sumr/k;ez=sumz/k;er2=sumr2/k;erz=sumrz/k;ez2=sumz2/k
    ew=ez/Q(n+1)
    # Independence of Dirichlet proportions and total gamma sum.
    ew2=ez2/Q((n+1)*(n+2))
    return er, ew, er2-er*er, (erz-er*ez)/Q(n+1), ew2-ew*ew

def prediction(n):
    er=Q(n,3)
    ew=Q(2*n+3,18*(n+1))
    vr=Q(0) if n==3 else Q(2,9) if n==4 else Q(2*n,45)
    cv=Q(0) if n==3 else Q(1,27) if n==4 else Q(64*n+105,2700*(n+1))
    vw=None if n<5 else Q(3168*n*n+16453*n+13035,81000*(n+1)**2*(n+2))
    return er,ew,vr,cv,vw

def main():
    tests=0
    for n in range(3,10):
        obs=brute(n); pred=prediction(n)
        for k,(a,b) in enumerate(zip(obs,pred)):
            if b is not None:
                assert a==b,(n,k,a,b)
                tests+=1
        print('n=',n,' E[R]=',obs[0],' E[W]=',obs[1],' Var[R]=',obs[2],' Cov=',obs[3],' Var[W]=',obs[4])
    print('OK exact rational identities',tests)
if __name__=='__main__':main()
