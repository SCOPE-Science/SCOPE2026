"""Verify modular-affine-line incidence census of inverse hyperbolas.
Uses exhaustive independent line-point enumeration and theoretical distribution.
Run: python3 verify.py
"""
from collections import Counter
from math import gcd


def predicted(p,k):
    q=p**k; S=p**(k-1); U=(p-1)*S
    T=q*q+q*S
    d=Counter()
    if k==1:
        d[1]=3*(p-1)
        d[2]=(p-1)*(p-2)//2
    else:
        d[1]=2*(p-1)*S*S
        d[2]=(p-1)*(p-2)*S*S//2
        for h in range(1,(k-1)//2+1):
            d[2*p**h]=U*((p-1)//2)*p**(k-2*h-1)
        d[p**(k//2)]=U
    d[0]=T-sum(d.values())
    assert min(d.values())>=0
    return d


def observed(p,k):
    q=p**k
    hyper=[(x,pow(x,-1,q)) for x in range(q) if x%p]
    counts=Counter()
    # canonical equations X+bY=c (a=1)
    for b in range(q):
        offsets=Counter((x+b*y)%q for x,y in hyper)
        for c in range(q):
            counts[offsets[c]]+=1
    # canonical equations aX+Y=c (b=1, a divisible by p)
    for a in range(0,q,p):
        offsets=Counter((a*x+y)%q for x,y in hyper)
        for c in range(q):
            counts[offsets[c]]+=1
    return counts


def run():
    checked=0; checked_lines=0; maximums=[]
    for p,k in [(3,1),(3,2),(3,3),(3,4),(3,5),(5,1),(5,2),(5,3),(7,1),(7,2),(7,3),(11,1),(11,2),(13,1),(13,2)]:
        q=p**k
        th=predicted(p,k)
        ob=observed(p,k)
        assert th==ob,(p,k,th,ob)
        assert sum(th.values())==q*q+q*q//p
        assert sum(r*n for r,n in th.items())==(q-q//p)*(q+q//p)
        maxr=max(r for r,n in th.items() if n)
        assert maxr==(2 if k==1 else (p**(k//2) if k%2==0 else 2*p**((k-1)//2)))
        maximums.append((p,k,maxr,th[maxr]))
        checked+=1;checked_lines+=sum(th.values())
    print('VERIFY_OK cases=%d all_primitive_lines=%d first_moment=PASS sharp_maxima=PASS' %(checked,checked_lines))
    print('EXTREMA',maximums)

if __name__=='__main__':run()
