#!/usr/bin/env python3
"""Independent finite checks for cyclic induced-edge concepts; Python stdlib only."""
from itertools import combinations
from functools import lru_cache
from math import comb

def concepts(n):
    return sorted({sum((((a>>i)&1) & ((a>>((i+1)%n))&1))<<i for i in range(n)) for a in range(1<<n)})

def allowed_support(mask,n):
    return all(not all((mask >> ((i+j)%n))&1 for j in range(3)) for i in range(n))

def predicted(n,k):
    if k==0:return 1
    z=n-k
    if z<=0:return 0
    # coefficient of t^k in (1+t+t^2)^z
    coeff=sum(comb(z,j)*comb(z-j,k-2*j) for j in range(k//2+1) if 0<=k-2*j<=z-j)
    num=n*coeff
    assert num%z==0,(n,k,num,z)
    return num//z

def littlestone(h,n):
    qb=[sum(1<<j for j,v in enumerate(h) if (v>>i)&1) for i in range(n)]
    @lru_cache(None)
    def rec(V):
        best=0
        for q in qb:
            p=V&q; m=V&~q
            if p and m:
                best=max(best,1+min(rec(p),rec(m)))
        return best
    return rec((1<<len(h))-1)

def run():
    for n in range(3,11):
        h=concepts(n)
        vals=[0]*(n+1)
        for s in range(1<<n):
            actual=len({v&s for v in h})==1<<s.bit_count()
            expected=allowed_support(s,n)
            assert actual==expected,(n,s,actual,expected)
            if actual:vals[s.bit_count()]+=1
        expect=[predicted(n,k) for k in range(n+1)]
        assert vals==expect,(n,vals,expect)
        assert max(i for i,v in enumerate(vals) if v)>0 or n==3
        assert max(i for i,v in enumerate(vals) if v)==(2*n)//3
        if n<=9:
            ld=littlestone(h,n)
            assert ld==(2*n+1)//3,(n,ld,(2*n+1)//3)
        else:ld='not_computed'
        print(f'n={n} concepts={len(h)} VC={(2*n)//3} Ldim={ld} polynomial={vals}',flush=True)
    print('CYCLIC_INDUCED_EDGE_SUPPORT_PASS',flush=True)
if __name__=='__main__':run()
