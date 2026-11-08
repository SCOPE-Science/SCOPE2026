#!/usr/bin/env python3
"""Exact Fourier-minor incidence over the affine plane of five elements.

Standard library only. No floating point, approximate rank, or random samples.
"""
from itertools import combinations, permutations, product
from collections import Counter
from math import comb

P = 5
V = tuple((a,b) for a in range(P) for b in range(P))
INDEX = {v:i for i,v in enumerate(V)}
SUBSETS = tuple(combinations(range(25),4))
REPRESENTATIVES = (
    (0,1,2,3),    # four points on one line
    (0,1,2,5),    # exactly three points on one line
    (0,1,5,6),    # noncollinear parallelogram
    (0,1,5,7),    # first non-parallelogram cap orbit
    (0,1,5,12),   # second non-parallelogram cap orbit
)
LABELS = ('L','T','P','Q','R')
POPULATIONS = (150,6000,1500,3000,2000)
EXPECTED = (
    # Each triple is the number of rank-1, rank-2, rank-3 column partners.
    ((25,0,0),(0,1000,3000),(0,500,500),(0,500,2000),(0,0,2000)),
    ((0,25,75),(0,0,1000),(0,0,500),(0,0,600),(0,0,0)),
    ((0,50,50),(0,0,2000),(0,0,150),(0,0,400),(0,0,400)),
    ((0,25,100),(0,0,1200),(0,0,200),(0,0,0),(0,0,200)),
    ((0,0,150),(0,0,0),(0,0,300),(0,0,300),(0,0,300)),
)
# For the output table we store only ranks 1,2,3; rank 4 is the complement.


def det_2(a,b,c,d):
    return (a*d-b*c)%P


def all_invertible_linear_maps():
    for a,b,c,d in product(range(P),repeat=4):
        if det_2(a,b,c,d):
            yield (a,b,c,d)


def act(pt,mat,shift):
    x,y=pt
    a,b,c,d=mat
    return ((a*x+b*y+shift[0])%P,(c*x+d*y+shift[1])%P)


def four_set_orbit(rep):
    rows=[V[i] for i in rep]
    orbit=set()
    for mat in all_invertible_linear_maps():
        for shift in V:
            orbit.add(tuple(sorted(INDEX[act(pt,mat,shift)] for pt in rows)))
    return orbit


def cyclotomic_zero(exponents):
    """Exact determinant zero in Z[zeta_5], via Phi_5=1+...+z^4.

    Input is an n by n matrix of exponents of primitive fifth roots.
    Each Leibniz monomial is exactly one fifth root, so the determinant
    is a signed integer vector (c_0,...,c_4), and it vanishes iff all
    five coefficients agree (minimal-polynomial divisibility).
    """
    n=len(exponents)
    coefficients=[0]*P
    for pi in permutations(range(n)):
        parity=sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n))
        exponent=sum(exponents[k][pi[k]] for k in range(n))%P
        coefficients[exponent] += (-1 if parity%2 else 1)
    return len(set(coefficients))==1


def exact_rank(rows,cols):
    exponents=tuple(tuple((V[i][0]*V[j][0]+V[i][1]*V[j][1])%P
                          for j in cols) for i in rows)
    for n in (4,3,2):
        for rr in combinations(range(4),n):
            for cc in combinations(range(4),n):
                sub=tuple(tuple(exponents[i][j] for j in cc) for i in rr)
                if not cyclotomic_zero(sub):
                    return n
    return 1


def run():
    assert len(SUBSETS)==comb(25,4)==12650
    assert len(set(REPRESENTATIVES))==5
    classes=[four_set_orbit(rep) for rep in REPRESENTATIVES]
    assert tuple(map(len,classes))==POPULATIONS
    assert sum(map(len,classes))==len(SUBSETS)
    lookup={}
    for i,orbit in enumerate(classes):
        for subset in orbit:
            assert subset not in lookup
            lookup[subset]=i
    assert len(lookup)==len(SUBSETS)
    counts=[[[0]*5 for _ in range(5)] for _ in range(5)]
    for i,rep in enumerate(REPRESENTATIVES):
        for cols in SUBSETS:
            r=exact_rank(rep,cols)
            counts[i][lookup[cols]][r]+=1
        assert sum(sum(x) for x in counts[i])==len(SUBSETS)
    for i in range(5):
        for j in range(5):
            for r in (1,2,3):
                assert counts[i][j][r]==EXPECTED[i][j][r-1],(i,j,r,counts[i][j][r])
            assert sum(counts[i][j])<=POPULATIONS[j]
            for r in (1,2,3,4):
                assert POPULATIONS[i]*counts[i][j][r] == POPULATIONS[j]*counts[j][i][r]
            assert POPULATIONS[i]*sum(counts[i][j][:4]) == POPULATIONS[j]*sum(counts[j][i][:4])
    grand=[sum(POPULATIONS[i]*sum(counts[i][j][r] for j in range(5))
               for i in range(5)) for r in range(5)]
    assert grand[1:]==[3750,600000,25875000,133543750],grand
    assert sum(grand)==len(SUBSETS)**2==160022500
    for i,label in enumerate(LABELS):
        row=[sum(counts[i][j][r] for r in (1,2,3)) for j in range(5)]
        assert [sum(counts[i][j][r] for j in range(5)) for r in (1,2,3,4)] == [
            [25,2000,7500,3125], [0,25,2175,10450], [0,50,3000,9600],
            [0,25,1700,10925], [0,0,1050,11600]][i]
        print(label,POPULATIONS[i],row,'singular_degree',sum(row))
    print('RANK_COUNTS',grand[1:])
    print('F5_FOURTH_ORDER_FOURIER_MINORS_EXACT_PASS')

if __name__=='__main__':
    run()
