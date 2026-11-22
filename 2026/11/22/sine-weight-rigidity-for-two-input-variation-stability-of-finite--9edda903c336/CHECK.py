#!/usr/bin/env python3
"""Reproducible tests for finite weighted-variation rearrangement theorem.
All combinatorial cut tests are exact integers or rational numbers;
trigonometric tests use an explicitly bounded numerical tolerance.
"""
import itertools
import math
import random
from fractions import Fraction


def tv(v,w):
    return sum(w[i]*abs(v[i+1]-v[i]) for i in range(len(w)))


def cut(mask,w):
    return sum(w[i] for i in range(len(w)) if mask[i]!=mask[i+1])


def max_cut_rows(w):
    n=len(w)+1
    out=[]
    for j in range(1,n):
        out.append(max(cut(mask,w) for mask in itertools.product((0,1),repeat=n) if sum(mask)==j))
    return out


def central_row(n,j):
    r=min(j,n-j)
    if n%2:
        m=n//2
        return list(range(m-r+1,m+r+1))
    m=n//2
    if j<m:
        return list(range(m-j,m+j))
    if j>m:
        return list(range(m-r+1,m+r+1))
    return list(range(1,n))


def K(n):
    t=math.pi/(2*n)
    return 1/math.sin(t) if n%2 else 1/math.tan(t)


def verify():
    random.seed(20261115)
    tests=0
    for n in range(2,12):
        s=[math.sin(math.pi*i/n) for i in range(1,n)]
        rows=max_cut_rows(s)
        k=K(n)
        for j,got in enumerate(rows,1):
            central=central_row(n,j)
            target=k*s[j-1]
            assert abs(got-target)<1e-10,(n,j,got,target)
            assert abs(sum(s[i-1] for i in central)-target)<1e-10
            assert any(tuple(int(x) for x in mask) for mask in itertools.product((0,1),repeat=n)
                       if sum(mask)==j and
                       tuple(i for i in range(1,n) if mask[i-1]!=mask[i])==tuple(central))
            tests+=3
        assert all(1<=i<n for i in central_row(n,1))
        assert sorted(set(central_row(n,n//2)))==list(range(1,n)) if n%2==0 else True
    print('CENTRAL_CUTS_ALL_CARDINALITIES_AND_SINE_EQUALITIES_PASS',tests)
    count=0
    for n in range(2,9):
        for t in range(35):
            w=[Fraction(random.randrange(1,25),random.randrange(1,13)) for _ in range(n-1)]
            rows=max_cut_rows(w)
            exact=max(rows[j-1]/w[j-1] for j in range(1,n))
            assert float(exact)+1e-12>=K(n)
            # Check every derivative permutation matrix from an input step.
            for j in range(1,n):
                x=[Fraction(int(i>=j)) for i in range(n)]
                assert tv(x,w)==w[j-1]
                best=max(tv(p,w) for p in set(itertools.permutations(x)))
                assert best==rows[j-1]
                count+=1
            # Segment estimate for arbitrary finite data.
            for t2 in range(30):
                x=[Fraction(random.randrange(-20,21),random.randrange(1,10)) for _ in range(n)]
                y=[Fraction(random.randrange(-20,21),random.randrange(1,10)) for _ in range(n)]
                d=tv([a-b for a,b in zip(x,y)],w)
                if d:
                    assert tv([a-b for a,b in zip(sorted(x),sorted(y))],w)<=exact*d
                count+=1
    print('EXACT_WEIGHTED_CUT_OPERATOR_NORMS_AND_TWO_INPUT_TESTS_PASS',count)
    # Real two-input extremizing pair within a strict sorting chamber.
    n=7
    w=[Fraction(i,1) for i in (3,1,6,2,5,4)]
    rows=max_cut_rows(w)
    j=max(range(1,n),key=lambda j:rows[j-1]/w[j-1])
    # The input increment is the step with j initial zeros, and n-j ones.
    pattern=max((p for p in itertools.product((0,1),repeat=n) if sum(p)==n-j),key=lambda p:cut(p,w))
    zeros=[ix for ix in range(n) if ix<j]
    ones=[ix for ix in range(n) if ix>=j]
    matching=[zeros.pop() if val==0 else ones.pop() for val in pattern]
    base=[None]*n
    for rank,ix in enumerate(matching):base[ix]=Fraction(rank,1)
    perturb=[Fraction(int(ix>=j),100) for ix in range(n)]
    ratio=tv([u-v for u,v in zip(sorted([a+b for a,b in zip(base,perturb)]),sorted(base))],w)/tv(perturb,w)
    assert ratio==rows[j-1]/w[j-1]
    print('ACTUAL_STRICT_SORTING_CHAMBER_SHARPNESS_WITNESS_PASS')
    print('ALL_SORTING_VARIATION_CERTIFICATES_PASS')


if __name__=='__main__':verify()
