"""Independent finite-size verification of counts of unbridged pairs in uniform interval intersection graphs."""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


def matchings(seq):
    seq=tuple(seq)
    if not seq:
        yield ()
    else:
        a=seq[0]
        for k in range(1,len(seq)):
            b=seq[k]
            remaining=seq[1:k]+seq[k+1:]
            for rest in matchings(remaining):
                yield ((a,b),)+rest


def count_unbridged(edges):
    # Only order, not real metric, matters: 2n distinct endpoint ranks.
    pairs=[(min(a,b),max(a,b)) for a,b in edges]
    n=len(pairs)
    u=0
    universal=0
    for i,(l,r) in enumerate(pairs):
        if all(not (r<c or d<l) for j,(c,d) in enumerate(pairs) if i!=j):
            universal+=1
    for i,(l,r) in enumerate(pairs):
        for j in range(i+1,n):
            c,d=pairs[j]
            if (r<c or d<l) and not any((a<=min(r,d) and b>=max(l,c)) for k,(a,b) in enumerate(pairs) if k not in (i,j)):
                # Valid because a <= the left interval's right and b >= right interval's left;
                # but min(r,d), max(l,c) must be the two inner disjoint endpoints.
                u+=1
    return u,universal


def formula(n):
    return 4*n*(n-1)*sum((Fraction(comb(n-2,j)*(-2)**j*factorial(j+1)**2,factorial(2*j+4)) for j in range(n-1)),Fraction())


def test():
    checks=0
    for n in range(2,7):
        total=0; tsum=0; tzero=0; Uzero=0
        for pairing in matchings(tuple(range(2*n))):
            t,U=count_unbridged(pairing)
            total+=1; tsum+=t; tzero+=(t==0); Uzero+=(U>=1)
            assert (t==0)==(U>=1), ('zero equivalence',n,pairing,t,U)
            checks+=1
        expected=Fraction(tsum,total)
        analytic=formula(n)
        assert expected==analytic,(n,expected,analytic)
        checks+=1
        assert tzero==Uzero
        checks+=1
        assert Fraction(tzero,total)==Fraction(2,3), (n,tzero,total)
        checks+=1
        print(n,'matchings',total,'E(T)',expected,'P(T=0)',Fraction(tzero,total))
    print('CHECKS PASSED:',checks)

if __name__=='__main__':
    test()
