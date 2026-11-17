"""Independent finite checks for complete-multipartite Hansen incenter loci.
Runs with Python 3 standard library. Finite checks corroborate, not replace, the proof.
"""
from decimal import Decimal, getcontext
from itertools import product, combinations
from math import prod
getcontext().prec=75
D=Decimal

def beta(r,t):
    return (D(1)-(D(4*(r-t)+1)/D(4*r+1)).sqrt())/D(2)

def clique_vectors(sizes):
    # Coded as a tuple of selected local indices or None for each part.
    return product(*(tuple(range(v))+(None,) for v in sizes))

def check_case(sizes):
    r=len(sizes); h=beta(r,1)
    assert r>=2 and all(x>=1 for x in sizes)
    for t in range(2,r+1):
        assert beta(r,t)>D(t)*h
    # Every clique facet slack from exact center coordinates is governed by omitted classes.
    limits=[D(1)-(D(4*s+1)/D(4*r+1)).sqrt() for s in range(r+1)]
    for state in product((-1,0,1),repeat=r):
        a=[D(s)*h for s in state]
        z=D(2)*sum(a)
        touched=0
        touched_max=0
        touched_lower=0
        for cc in clique_vectors(sizes):
            s=sum(j is not None for j in cc)
            val=-z + D(2)*sum(a[j] for j in range(r) if cc[j] is not None)
            limit=limits[s]
            assert abs(val)<=limit+D('1e-65'),(sizes,state,cc,val,limit)
            if abs(abs(val)-limit)<D('1e-65'):
                touched += 2 if s==r else 1
                touched_max += 2 if s==r else 0
                touched_lower += 0 if s==r else 1
                assert s>=r-1
        expected=2*prod(sizes)+sum(prod(sizes[j] for j in range(r) if j!=i) for i,a0 in enumerate(state) if a0)
        assert touched==expected,(sizes,state,touched,expected)
        assert touched_max==2*prod(sizes)
        assert touched_lower==expected-touched_max
    return 3**r

if __name__=='__main__':
    checks=0;profiles=0
    # Independently use every clique rather than the subset-size compression.
    for r in range(2,5):
        for sizes in product((1,2),repeat=r):
            profiles+=1; checks+=check_case(sizes)
    for sizes in ((1,1,1,1,1),(2,1,1,1,1),(2,2,2,1,1),(3,3,3,3,3)):
        profiles+=1; checks+=check_case(sizes)
    for r in range(2,61):
        for t in range(2,r+1):assert beta(r,t)>D(t)*beta(r,1)
    print(f'HANSEN_MULTIPARTITE_INCENTER_PASS profiles={profiles} center_patterns={checks} convexity_inequalities={sum(r-1 for r in range(2,61))}')
