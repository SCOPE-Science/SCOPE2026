#!/usr/bin/env python3
"""Independent direct labelled-state orbit census, compared with exact exponential-polynomial coefficients."""
from collections import Counter
from itertools import product
from math import factorial

# EGF monomials: coefficient for h heavy classes, s singleton classes.
CASES={
    (0,1):{(0,0):1,(0,1):4,(0,2):6,(0,3):4,(0,4):1,(1,0):4,(1,1):8,(1,2):4,(2,0):2},
    (1,1):{(1,1):4,(1,2):8,(1,3):4,(2,0):4,(2,1):8,(2,2):2},
    (2,1):{(3,0):4,(2,1):4,(2,2):4},
    (3,1):{(3,1):4},
    (0,4):{(4,0):1}
}

def heavy_surjections(n,h):
    if h==0: return 1 if n==0 else 0
    # n! [z^n] (exp(z)-1-z)^h, via coefficient convolution.
    d=[0]*(n+1);d[0]=1
    fac=[factorial(i) for i in range(n+1)]
    for _ in range(h):
        e=[0]*(n+1)
        for k in range(n+1):
            e[k]=sum(d[k-j]*fac[k]//(fac[j]*fac[k-j]) for j in range(2,k+1))
        d=e
    return d[n]

def prediction(n):
    result={}
    for cl,mons in CASES.items():
        total=0
        for (h,s),mult in mons.items():
            if n>=s:
                total+=mult*factorial(n)//factorial(n-s)*heavy_surjections(n-s,h)
        result[cl]=total
    return result

def step(x):
    occ=[0]*4
    for color in x:occ[color]+=1
    return tuple((color+1)%4 if occ[(color+1)%4]>=2 else color for color in x)

def classify(x):
    seen={};current=x;t=0
    while current not in seen:
        seen[current]=t;current=step(current);t+=1
        assert t<=8,(x,'unexpected period/transient')
    tau=seen[current];period=t-tau
    assert (tau,period) in CASES,(x,tau,period)
    return tau,period

def main():
    for n in range(2,10):
        cnt=Counter(classify(x) for x in product(range(4),repeat=n))
        pred=prediction(n)
        assert dict(cnt)=={k:v for k,v in pred.items() if v},(n,cnt,pred)
        assert sum(pred.values())==4**n
        print('n=',n,'distribution',sorted(cnt.items()))
    print('direct-orbit validation OK')

if __name__=='__main__':main()
