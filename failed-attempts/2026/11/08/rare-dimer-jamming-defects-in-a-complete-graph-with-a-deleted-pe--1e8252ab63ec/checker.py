"""Independent finite checks for greedy dimer adsorption on a matching-deleted clique."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb

@lru_cache(None)
def reduced(k,s):
    t=k*2+s
    if t==2:
        return Fraction(1 if k==1 else 0)
    if t<2:
        raise AssertionError('unexpected terminal state')
    E=comb(t,2)-k
    ans=Fraction(0)
    if s>=2:
        ans+=Fraction(comb(s,2),E)*reduced(k,s-2)
    if k>=1 and s>=1:
        ans+=Fraction(2*k*s,E)*reduced(k-1,s)
    if k>=2:
        ans+=Fraction(2*k*(k-1),E)*reduced(k-2,s+2)
    return ans

@lru_cache(None)
def labeled(mask,m):
    vs=[v for v in range(2*m) if mask>>v&1]
    edges=[(u,v) for i,u in enumerate(vs) for v in vs[i+1:] if u//2!=v//2]
    if not edges:
        assert len(vs) in (0,2)
        return Fraction(1 if len(vs)==2 else 0)
    return sum((labeled(mask &~(1<<u)&~(1<<v),m) for u,v in edges),Fraction(0))/len(edges)

nchecks=0
for m in range(2,8):
    a=reduced(m,0)
    b=labeled((1<<(2*m))-1,m)
    assert a==b,(m,a,b)
    print('m',m,'failure exact',a,'decimal',float(a))
    nchecks+=1
assert reduced(3,0)==Fraction(1,5)
assert reduced(4,0)==Fraction(8,65)
nchecks+=2
for t in range(3,50):
    rmin=Fraction(t-2,t);rmax=Fraction(2*t-3,2*t+1)
    for K in range(1,t+1):
        r=Fraction(comb(2*t-2,2)-(K-1),comb(2*t,2)-K)
        assert rmin<=r<=rmax
        nchecks+=1
    for K in range(2,t+1):
        q=Fraction(comb(2*t-4,2)-(K-2),comb(2*t,2)-K)
        assert q<=Fraction((t-2)**2,t*t)
        nchecks+=1
for m in range(3,50):
    p=reduced(m,0)
    assert p<=Fraction(3*m,4*m*m-1)
    for T in range(2,min(m,15)+1):
        L=Fraction(T*(T-1),m*(m-1))
        lower=m*(L-(m-1)*L*L)*Fraction(3,(2*T-1)*(2*T+1))
        assert p>=lower
        nchecks+=1
print('verified',nchecks,'exact assertions; 2m group pairing bitmask vs reduced for m=2..7')
