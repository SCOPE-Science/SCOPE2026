#!/usr/bin/env python3
"""Independent exhaustive verification of a rook-graph maximal-cluster enumerator.

No external packages required. Checks the literal induced P3 definition using
forbidden three-corner rectangles, and tests every missing vertex for maximality.
"""
from collections import Counter
from functools import lru_cache
from math import comb, factorial

@lru_cache(None)
def associated_stirling(n,k):
    """Partitions of a labeled n-set into k unlabelled blocks, size at least 2."""
    if n==k==0: return 1
    if k<1 or n<2*k: return 0
    return sum(comb(n-1,j-1)*associated_stirling(n-j,k-1) for j in range(2,n+1))

def formula(m,n):
    out=Counter()
    for a in range(m+1):
        for b in range(n+1):
            for c in range(min(m,n)+1):
                A=m-a-c; B=n-b-c
                if A<0 or B<0:continue
                x=associated_stirling(B,a)*associated_stirling(A,b)
                if x:
                    term=factorial(m)*factorial(n)*x
                    den=factorial(c)*factorial(A)*factorial(B)
                    assert term%den==0
                    out[m+n-a-b-c]+=term//den
    for a in range(1,m):
        out[n]+=factorial(m)//factorial(m-a)*associated_stirling(n,a)
    for b in range(1,n):
        out[m]+=factorial(n)//factorial(n-b)*associated_stirling(m,b)
    return +out

def bad_triples(m,n):
    triples=set()
    for i in range(m):
        for k in range(i+1,m):
            for j in range(n):
                for ell in range(j+1,n):
                    corners=[i*n+j,i*n+ell,k*n+j,k*n+ell]
                    for z in corners:
                        mask=0
                        for w in corners:
                            if w!=z: mask|=1<<w
                        triples.add(mask)
    return tuple(sorted(triples))

def brute(m,n):
    # Independence from the counting/classification formula: a selected triple
    # is an induced P3 iff it occupies three corners of a 2x2 rectangle.
    forbidden=bad_triples(m,n)
    q=m*n
    lim=1<<q
    valid=bytearray(lim)
    valid[0]=1
    for mask in range(1,lim):
        bit=mask&-mask
        smaller=mask^bit
        if not valid[smaller]: continue
        valid[mask]=int(all((mask&t)!=t for t in forbidden if t&bit))
    result=Counter()
    for mask in range(lim):
        if not valid[mask]: continue
        complement=(lim-1)^mask
        if all(not valid[mask|(1<<i)] for i in range(q) if complement>>i&1):
            result[mask.bit_count()]+=1
    return result, sum(valid), lim

def main():
    checked=0;total=0;allvalid=0;allmax=0
    for m in range(1,5):
        for n in range(m,6):
            if m*n>20:continue
            got,valid,subsets=brute(m,n)
            expected=formula(m,n)
            assert got==expected,(m,n,got,expected)
            checked+=1;total+=subsets;allvalid+=valid;allmax+=sum(got.values())
    for m in range(2,9):
        for n in range(2*m,4*m+1):
            spec=set(formula(m,n))
            assert spec==({m}|set(range(n,n+m-1))), (m,n,spec)
    print(f'VERIFY_OK instances={checked} examined_subsets={total} cluster_sets={allvalid} '
          f'maximal_sets={allmax} all_coefficients=PASS rectangular_spectra=PASS')
if __name__=='__main__': main()
