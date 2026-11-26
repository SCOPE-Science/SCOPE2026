"""Exact reproducibility checks for linear-window onto-cluster laws.
Run: python3 checker.py. Uses Python standard library only.
"""
from itertools import product
from fractions import Fraction
from math import factorial, exp, log

checks=0

def S(m,n):
    if n<0 or m<n: return 0
    a=[0]*(n+1);a[0]=1
    for h in range(1,m+1):
        b=[0]*(n+1)
        for j in range(1,min(h,n)+1):b[j]=a[j-1]+j*a[j]
        a=b
    return a[n]

def tau(a):
    lo,hi=0.,max(2*a,2.)
    for _ in range(90):
        x=(lo+hi)/2
        v=x/(-__import__('math').expm1(-x)) if x else 1.
        if v<a:lo=x
        else:hi=x
    return (lo+hi)/2

# Exact conditional distribution: at a stationary entry, the middle M-1
# symbols form a uniformly random surjection to n-1 types, followed by the
# only missing type. Future symbols are independent uniform n-type draws.
for n in range(2,6):
    for M in range(n,min(n+3,8)):
        N,m=n-1,M-1
        words=[tuple(w) for w in product(range(N),repeat=m) if len(set(w))==N]
        assert len(words)==factorial(N)*S(m,N)
        checks+=1
        for r in range(1,min(4,m)+1):
            actual=Fraction(sum(all(w.count(w[i])==1 for i in range(r)) for w in words),len(words))
            predicted=Fraction(S(m-r,N-r),S(m,N))
            assert actual==predicted,(n,M,r,actual,predicted)
            checks+=1
        p_one=Fraction(n-1,n)*Fraction(S(m-1,N-1),S(m,N))
        direct=Fraction(sum(w.count(w[0])==1 for w in words)*(n-1),len(words)*n)
        assert direct==p_one
        checks+=1
        for k in range(1,4):
            survivors=0
            for w in words:
                for future in product(range(n),repeat=k):
                    cur=w+(N,)
                    ok=True
                    for y in future:
                        cur=cur[1:]+(y,)
                        if len(set(cur))!=n:
                            ok=False;break
                    survivors+=ok
            p_survive=Fraction(survivors,len(words)*n**k)
            assert 0<=p_survive<=1
            if k==1: assert 1-p_survive==p_one
            checks+=1
# Large-n structural approximation of the finite singleton profile and mean.
for a in (1.25,1.5,2.,3.):
    t=tau(a)
    for n in (30,70,150):
        M=int(a*n)
        N,m=n-1,M-1
        q1=float(Fraction(S(m-1,N-1),S(m,N)))
        q2=float(Fraction(S(m-2,N-2),S(m,N)))
        mean=float(Fraction(n*S(M,n),(n-1)*S(m,N)))
        print('a',a,'n',n,'singleton',round(q1,7),'target',round(exp(-t),7),
              'double',round(q2,7),'target',round(exp(-2*t),7),
              'mean',round(mean,7),'target',round(exp(t),7))
        assert q1>0 and q2>0 and mean>=1
        checks+=3
print('PASS:',checks,'exact/computational checks; asymptotic values above are diagnostics')
