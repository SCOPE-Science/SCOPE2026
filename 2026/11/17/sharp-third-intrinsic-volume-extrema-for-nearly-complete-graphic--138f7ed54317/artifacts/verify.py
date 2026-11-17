"""Checks for third intrinsic volumes of dense graphical zonotopes.

The three-component exact tuple represents a*sqrt(2)+b*sqrt(6)+c.
No numerical optimization is used to establish the infinite-family theorem.
"""
from itertools import combinations
from math import comb, sqrt
import random


def C(a,b): return comb(a,b) if 0 <= b <= a else 0

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,k): return tuple(x*k for x in a)
def real(a): return a[0]*sqrt(2) + a[1]*sqrt(6) + a[2]

def triple_weight(edges):
    ends=set(v for edge in edges for v in edge)
    parent={v:v for v in ends}
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for u,v in edges:
        a,b=root(u),root(v)
        if a==b:return (0,0,0)
        parent[a]=b
    parts={}
    for x in ends:
        r=root(x);parts[r]=parts.get(r,0)+1
    sizes=sorted(parts.values())
    if sizes==[2,2,2]: return (2,0,0)
    if sizes==[2,3]: return (0,1,0)
    if sizes==[4]: return (0,0,2)
    raise AssertionError(sizes)


def volume3(E):
    out=(0,0,0)
    for t in combinations(sorted(E),3):out=add(out,triple_weight(t))
    return out

def invariants(n,removed):
    rem=set(removed)
    E=set(combinations(range(n),2))-rem
    k=len(rem)
    P=sum(1 for a,b in combinations(rem,2) if set(a)&set(b))
    return E,k,P,volume3(rem)

def formula(n,rem):
    E,k,P,vd=invariants(n,rem)
    m=C(n,2)
    A=(6*C(n-2,4), 3*C(n-2,3)+2*(n-2)*C(n-3,2), 8*(n-2)*(n-3))
    Ba=(0,C(n-3,2),6*(n-3))
    Bd=(2*C(n-4,2),4*(n-4),8)
    # m*A/3 is integer coefficientwise for each n>=4.
    base=tuple(m*x//3 for x in A)
    assert all((m*x)%3==0 for x in A)
    return sub(sub(add(sub(base,scale(A,k)),scale(Bd,C(k,2))),scale(sub(Bd,Ba),P)),vd)

def deletion_patterns(n,k):
    return ({(0,i) for i in range(1,k+1)}, {(2*i,2*i+1) for i in range(k)})

def run():
    profiles=0
    for n in range(4,8):
        pool=list(combinations(range(n),2))
        for k in range(2,n//2+1):
            rstar,rmatch=deletion_patterns(n,k)
            Gstar=set(pool)-rstar;Gmatch=set(pool)-rmatch
            vstar=real(volume3(Gstar)); vmatch=real(volume3(Gmatch))
            for remtuple in combinations(pool,k):
                rem=set(remtuple)
                E,k0,p,v= invariants(n,rem)
                actual=volume3(E)
                assert actual==formula(n,rem),(n,rem,actual,formula(n,rem))
                vol=real(actual)
                assert vstar-1e-7<=vol<=vmatch+1e-7,(n,k,rem,vol,vstar,vmatch)
                if abs(vol-vstar)<1e-7:
                    assert (all(set(x)&set(y) for x,y in combinations(rem,2))) and (k==2 or not any(triple_weight(t)==(0,0,0) for t in combinations(rem,3)))
                if abs(vol-vmatch)<1e-7:
                    assert p==0
                profiles+=1
    rng=random.Random(2046)
    sampled=0
    for n in range(8,11):
        pool=list(combinations(range(n),2))
        for k in range(2,n//2+1):
            star,match=deletion_patterns(n,k)
            s=real(volume3(set(pool)-star))
            m=real(volume3(set(pool)-match))
            for j in range(40):
                rem=set(rng.sample(pool,k))
                f=formula(n,rem);w=volume3(set(pool)-rem)
                assert f==w
                x=real(w);assert s-1e-6<=x<=m+1e-6
                sampled+=1
    print(f'DENSE_ZONOTOPE_V3_CHECKS_PASSED exhaustive_deletions={profiles} random_deletions={sampled}')
if __name__=='__main__':run()
