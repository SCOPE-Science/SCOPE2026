"""Self-contained exact checks for finite-spike Luce fixed-point laws.
Run with Python 3.9 or newer: python verify.py
No third-party dependencies. This checks finite cases, not the infinite proof.
"""
from fractions import Fraction as Q
from itertools import permutations
from functools import lru_cache
from math import factorial

def ff(x,k):
    out=1
    for i in range(k): out*=x-i
    return out

def add(a,b):
    return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))))

def scale(a,x): return tuple(v*x for v in a)

def shift(a): return (Q(0),)+tuple(a)

def pgf(theta,n=None):
    """H polynomial, exact finite n, or the limiting Poisson-clock model."""
    m=len(theta)
    @lru_cache(None)
    def rec(r,remain):
        if r>m: return (Q(1),)
        used_ordinary=(r-1)-(m-len(remain))
        ordinary=Q(1) if n is None else Q(n-m-used_ordinary,n)
        den=ordinary+sum(theta[i] for i in remain)
        out=scale(rec(r+1,remain),ordinary/den)
        for i in remain:
            q=rec(r+1,tuple(j for j in remain if j!=i))
            if i+1==r: q=shift(q)
            out=add(out,scale(q,theta[i]/den))
        return out
    return rec(1,tuple(range(m)))

def enumerate_luce(n,theta):
    m=len(theta)
    weights=[n*x for x in theta]+[Q(1)]*(n-m)
    total={}
    grouped={}
    for pi in permutations(range(n)):
        wsum=sum(weights)
        p=Q(1)
        ranks=[None]*n
        for r,i in enumerate(pi,1):
            p*=weights[i]/wsum
            wsum-=weights[i]
            ranks[i]=r
        heavy=tuple(ranks[:m]);H=sum(ranks[i]==i+1 for i in range(m))
        O=sum(ranks[i]==i+1 for i in range(m,n))
        total[H]=total.get(H,Q(0))+p
        grp=grouped.setdefault(heavy,{})
        grp[O]=grp.get(O,Q(0))+p
    return total,grouped

checks=0
for theta in [(Q(1),),(Q(2,3),),(Q(1),Q(1)),(Q(1,2),Q(2))]:
    m=len(theta)
    for n in range(max(3,m+1),8):
        total,groups=enumerate_luce(n,theta)
        expected=pgf(theta,n)
        for k in range(m+1):
            assert total.get(k,0)==(expected[k] if k<len(expected) else 0), (theta,n,k)
            checks+=1
        assert sum(total.values())==1;checks+=1
        N=n-m
        for ranks,od in groups.items():
            p=sum(od.values())
            h=N-sum(r>m for r in ranks)
            for k in range(min(3,h)+1):
                obs=sum(pp*ff(o,k) for o,pp in od.items())/p
                formula=Q(ff(h,k),ff(N,k))
                assert obs==formula, (theta,n,ranks,k,obs,formula)
                checks+=1

for theta in [(Q(1),),(Q(2),),(Q(1),Q(1)),(Q(1,2),Q(2)),(Q(3,2),Q(7,3),Q(4,5))]:
    target=pgf(theta)
    assert sum(target)==1;checks+=1
    for n in (100,1000,10000):
        got=pgf(theta,n)
        for i in range(len(target)):
            assert abs(float(got[i]-target[i]))<0.04 if n==100 else abs(float(got[i]-target[i]))<0.005 if n==1000 else abs(float(got[i]-target[i]))<0.0005,(theta,n,i,got[i],target[i])
            checks+=1
assert pgf((Q(1),Q(1)))==(Q(10,18),Q(5,18),Q(3,18)); checks+=1
assert pgf((Q(1),))==(Q(1,2),Q(1,2)); checks+=1
print(f'PASS: {checks} exact enumeration, factorial-moment and convergence checks')
