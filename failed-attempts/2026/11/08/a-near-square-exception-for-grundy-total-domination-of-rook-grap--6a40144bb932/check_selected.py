"""Independent exhaustive subset dynamic program for total dominating sequences.

A state is the set of vertices already selected, not the neighborhood union.
"""
from functools import lru_cache


def expected(m,n):
    if m>n:m,n=n,m
    return 2*m-2 if m==n else 2*m if n==m+1 else m+n-2


def solve(m,n):
    vertices=list(range(m*n))
    neighbors=[sum(1 << b for b in vertices if a!=b and
                   (a//n==b//n or a%n==b%n)) for a in vertices]
    full=(1<<(m*n))-1
    @lru_cache(None)
    def longest(selected):
        union=0
        for a in vertices:
            if selected>>a & 1:union |= neighbors[a]
        if union==full:return 0
        cand=[]
        for a in vertices:
            if not(selected>>a & 1) and neighbors[a] & ~union:
                cand.append(1+longest(selected|(1<<a)))
        assert cand, (m,n,selected)
        return max(cand)
    return longest(0),longest.cache_info().currsize

if __name__=='__main__':
    for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)]:
        value,states=solve(m,n)
        assert value==expected(m,n), (m,n,value)
        print(f'{m}x{n} optimum={value}; subset_states={states}')
    print('PASS: subset-state exhaustive verification')
