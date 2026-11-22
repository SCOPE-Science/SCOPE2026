"""Exact certificate for the additive energy of ternary digit-sum <=2 index sets.
Only Python standard library is required. No external resources or archive data.
"""
from collections import defaultdict, Counter
from itertools import product
from math import comb

DIGIT_QUADS = tuple(product(range(3),repeat=4))

def digit_sum_3(n):
    s=0
    while n:
        s+=n%3
        n//=3
    return s

def digitsupport(r):
    # Construct without iterating 3**r integers.
    b=set()
    for j in range(r):
        b.add(3**j); b.add(2*3**j)
        for k in range(j):
            b.add(3**j+3**k)
    return b

def energy_brute(r):
    a=digitsupport(r)
    N=3**r
    R=Counter((u+v)%N for u in a for v in a)
    E=sum(x*x for x in R.values())
    expected_support=1+2*r+4*comb(r,2)+4*comb(r,3) + (comb(r,4) if r>=4 else 0)
    assert len(R)==expected_support, (r,len(R),expected_support)
    assert all(digit_sum_3(t)<=4 for t in R)
    assert max(R.values())<=6
    return E,R

def energy_transfer(rmax):
    # State = (carry in first sum, carry in second sum, four digit sums).
    # Coefficients always exact nonnegative integers.
    states={(0,0,0,0,0,0):1}
    values=[]
    for r in range(rmax+1):
        if r:
            nxt=defaultdict(int)
            for (c1,c2,wa,wb,wc,wd),count in states.items():
                for a,b,c,d in DIGIT_QUADS:
                    na,nb,nc,nd=wa+a,wb+b,wc+c,wd+d
                    if max(na,nb,nc,nd)>2: continue
                    v1=a+b+c1
                    v2=c+d+c2
                    if v1%3 != v2%3: continue
                    nxt[(v1//3,v2//3,na,nb,nc,nd)]+=count
            states=nxt
        E=sum(v for (c1,c2,a,b,c,d),v in states.items()
              if min(a,b,c,d)>=1)
        values.append(E)
    return values

def polynomial(r):
    if r==0: return 0
    z=3*r**4+10*r**3+26*r**2-51*r+24
    assert z%2==0
    return z//2

def verify():
    got=energy_transfer(17)
    assert len(got)==18
    for r,e in enumerate(got):
        assert e==polynomial(r), (r,e,polynomial(r))
        if 1<=r<=10:
            direct,_=energy_brute(r)
            assert direct==e
    # (1-z)^9*G(z) has degree <=17 by nilpotence of total
    # digit-weight >=9 in the four-variable quotient (x_i^3).
    # Check each of its first 18 coefficients against the claimed G.
    for j in range(18):
        lhs=sum((-1)**k * comb(9,k)*got[j-k]
                for k in range(min(j,9)+1))
        rhs=sum((-1)**k * comb(9,k)*polynomial(j-k)
                for k in range(min(j,9)+1))
        assert lhs==rhs
    assert got[:8]==[0,6,77,309,822,1772,3351,5787]
    print('CERTIFIED TRANSFER VALUES r=0..17:',got)
    print('PASS: 18 coefficients of (1-z)^9 G(z), direct support/energy r=1..10.')
    print('PASS: rational-function degree bound makes verification all-depth.')
if __name__=='__main__':verify()
