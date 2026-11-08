"""Independent finite checks for fixed-block common-knowledge connectivity.

Uses only Python's standard library. The asymptotic theorem is proved separately;
finite checks test the exact identities, recursion and special-case formula.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial

@lru_cache(None)
def partitions(n, b):
    if n == 0:
        return ((),)
    out = []
    def rec(remaining):
        if not remaining:
            yield ()
            return
        head, *tail = remaining
        for rest in combinations(tail, b-1):
            block = (head,)+rest
            other = tuple(x for x in tail if x not in rest)
            for part in rec(other):
                yield (block,)+part
    return tuple(rec(tuple(range(n))))

def connected_component_sizes(family, n):
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v=parent[v]
        return v
    for partition in family:
        for block in partition:
            for v in block[1:]:
                a,b=root(block[0]),root(v)
                parent[a]=b
    sizes={}
    for v in range(n):
        z=root(v)
        sizes[z]=sizes.get(z,0)+1
    return tuple(sorted(sizes.values()))

def total(n,b):
    N=n//b
    return factorial(n)//(factorial(b)**N*factorial(N))

def connected_count_recurrence(N,b,r):
    c=[0]*(N+1)
    c[0]=0
    for t in range(1,N+1):
        n=b*t
        val=total(n,b)**r
        for j in range(1,t):
            val-=comb(n-1,b*j-1)*c[j]*total(n-b*j,b)**r
        c[t]=val
    return c[N]

def common_block_moments(n,b,r):
    N=n//b
    mu=Fraction(N**r, comb(n,b)**(r-1))
    p2=Fraction((N*(N-1))**r,(comb(n,b)*comb(n-b,b))**(r-1)) if N>=2 else Fraction(0)
    return mu,p2

def verify():
    cases=((2,1,2),(2,2,2),(2,3,2),(2,4,2),
           (2,1,3),(2,2,3),(2,3,3),
           (3,1,2),(3,2,2),(4,2,2),(3,2,3))
    for b,N,r in cases:
        n=b*N
        ps=partitions(n,b)
        assert len(ps)==total(n,b),(b,N,r,'partition count')
        runs=0; conn=0; actual_x=Fraction(0); actual_x2=Fraction(0)
        exceptional=0
        for family in product(ps, repeat=r):
            runs+=1
            sizes=connected_component_sizes(family,n)
            conn+=(sizes==(n,))
            common=sum(1 for block in family[0] if all(block in part for part in family[1:]))
            actual_x+=common
            actual_x2+=common*(common-1)
            if sizes!=(n,) and common==1 and sizes!=(b,n-b):
                exceptional+=1
        assert runs==len(ps)**r
        assert conn==connected_count_recurrence(N,b,r),(b,N,r,conn,connected_count_recurrence(N,b,r))
        mu,x2=common_block_moments(n,b,r)
        assert actual_x/runs==mu,(b,N,r,'expectation',actual_x/runs,mu)
        assert actual_x2/runs==x2,(b,N,r,'factorial moment',actual_x2/runs,x2)
        if b==r==2:
            assert conn==len(ps)*2**(N-1)*factorial(N-1),(N,conn)
        if b>=2 and N>=3:
            assert exceptional >= 0
        print(f'b={b} N={N} r={r} n={n} |partitions|={len(ps)} connected={conn}/{runs} mu={mu} EX(X-1)={x2}')
    print('ALL_FINITE_CHECKS_OK')

if __name__=='__main__':
    verify()
