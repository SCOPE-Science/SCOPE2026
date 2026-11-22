"""Standalone finite tests for symplectic maximum-clique extension formulas.
Only Python standard library is required; exhaustive for ranks 1,2,3.
The algebraic arguments for all ranks are given in RESULT.md.
"""
from itertools import combinations
from collections import Counter
from math import factorial, prod

def pairing(a,b,r):
    mask=(1<<r)-1
    return (((a & mask) & (b>>r)) ^ ((a>>r) & (b & mask))).bit_count() % 2

def sp_order(r):
    return 2**(r*r)*prod(2**(2*i)-1 for i in range(1,r+1))

def theoretical_extension(r,t,dependent=False):
    if t==2*r+1:return 1
    if t%2==0:
        return sp_order(r-t//2)//factorial(2*r+1-t)
    if dependent:return 0
    return 2**(2*r-t)*sp_order((2*r-t-1)//2)//factorial(2*r+1-t)

def run(r):
    top=2*r+1
    N=(1<<(2*r))-1
    nbh=[0]*(N+1)
    for v in range(1,N+1):
        nbh[v]=sum(1<<(u-1) for u in range(1,N+1) if pairing(v,u,r))
    cliques=[]
    by_size=[[] for _ in range(top+1)]
    def rec(c, candidates):
        by_size[len(c)].append(c)
        if len(c)==top:return
        while candidates:
            bit=candidates & -candidates
            candidates-=bit
            v=bit.bit_length()
            rec(c+(v,), candidates & nbh[v])
    rec((), (1<<N)-1)
    incid=Counter()
    for c in by_size[top]:
        for t in range(top+1):
            for sub in combinations(c,t):
                incid[sub]+=1
    for t,sets in enumerate(by_size):
        for c in sets:
            dependent=(t%2==1 and t<top and all(1 for _ in c) and
                       __import__('functools').reduce(lambda a,b:a^b,c,0)==0)
            expected=theoretical_extension(r,t,dependent)
            got=incid[c]
            assert got==expected,(r,t,c,dependent,got,expected)
    assert len(by_size[top])==theoretical_extension(r,0)
    if r>=2:
        assert all(incid[c]==1 for c in by_size[2*r-2])
    print('rank',r,'cliques_by_size',[len(z) for z in by_size],
          'max_cliques',len(by_size[top]),
          'extraspecial_group_cliques',len(by_size[top])*2**top,
          'incidence_tests',sum(map(len,by_size)))

if __name__=='__main__':
    for r in (1,2,3):run(r)
    print('SYMPLECTIC_CLIQUE_EXTENSION_SPECTRUM_OK')
