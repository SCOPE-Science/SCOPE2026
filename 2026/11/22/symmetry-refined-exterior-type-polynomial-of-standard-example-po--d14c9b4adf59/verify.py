"""Independent finite checks for the one-point extension profiles of standard-example posets.

Run: python verify.py
No external packages or external data are required.
"""
from itertools import product, permutations
from collections import Counter
from math import comb


def types_by_transitivity(n):
    """Enumerate all trinary relations of a new point to 2n parameters.

    -1: parameter below new point; 0: incomparable; +1: parameter above.
    Check all transitivity clauses explicitly, never use counting classification.
    """
    N=2*n
    older={(i,n+j) for i in range(n) for j in range(n) if i!=j}
    for q in product((-1,0,1),repeat=N):
        pairs=set(older)
        v=N
        for i,c in enumerate(q):
            if c==-1:pairs.add((i,v))
            if c==1:pairs.add((v,i))
        # all strict transitive closures must already be in the declared relation
        if any((y,z) in pairs and (x,z) not in pairs for x,y in pairs for z in range(N+1)):
            continue
        yield q


def count_expected(n):
    p=Counter()
    # direct expansion of three disjoint multinomial/binomial terms, including boundaries
    for a in range(n+1):
        for b in range(n-a+1):
            p[(a,b)]+=comb(n,a)*comb(n-a,b)
    for k in range(n+1):
        p[(n+k,0)]+=comb(n,k)
        p[(0,n+k)]+=comb(n,k)
    p[(n,0)]+=n-1
    p[(0,n)]+=n-1
    return p


def orbit_poly_expected(n):
    p=Counter()
    for k in range(n+1):
        p[(k,0)]+=1
        p[(0,k)]+=1
    p[(n,0)]+=1
    p[(0,n)]+=1
    for k in range(1,n+1):
        p[(n+k,0)]+=1
        p[(0,n+k)]+=1
    p[(0,0)]-=1
    for a in range(1,n):
        for b in range(1,n-a+1):
            p[(a,b)]+=1
    return p


def orbit_representative(q,n):
    return min(tuple(q[p] for p in perm)+tuple(q[n+p] for p in perm)
               for perm in permutations(range(n)))


def main():
    ncases=0; ntype=0; norbits=0
    for n in range(2,7):
        actual=Counter()
        orbit_seen={}
        for q in types_by_transitivity(n):
            a=q.count(-1); b=q.count(1)
            actual[(a,b)]+=1; ntype+=1
            if n<=5:
                key=orbit_representative(q,n)
                orbit_seen[key]=(a,b)
        expected=count_expected(n)
        assert actual==expected,(n,actual-expected,expected-actual)
        assert sum(actual.values())==3**n+2**(n+1)+2*n-2
        if n<=5:
            got=Counter(orbit_seen.values())
            assert got==orbit_poly_expected(n),(n,got,orbit_poly_expected(n))
            assert len(orbit_seen)==(n+1)*(n+6)//2
            norbits+=len(orbit_seen)
        ncases+=3**(2*n)
        print(f'n={n} checked_assignments={3**(2*n)} valid_profiles={sum(actual.values())} orbit_types={len(orbit_seen) if n<=5 else "not-enumerated"}')
    print(f'ALL_CHECKS_OK assignments={ncases} valid_profiles={ntype} checked_orbits={norbits}')

if __name__=='__main__': main()
