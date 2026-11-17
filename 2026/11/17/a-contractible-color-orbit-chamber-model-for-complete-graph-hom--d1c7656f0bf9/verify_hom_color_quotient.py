#!/usr/bin/env python3
"""Finite combinatorial checks of the color-orbit chamber model for Hom(K_m,K_n).
Scientific checks only. Does not replace the all-parameter proof.
"""
from collections import defaultdict
from itertools import product
from math import factorial, comb
from fractions import Fraction


def signatures(m,n):
    actual=defaultdict(int)
    for assignment in product(range(m+1), repeat=n):
        sz=tuple(assignment.count(i) for i in range(1,m+1))
        if not all(sz): continue
        actual[sz]+=1
    expected={t:factorial(n)//(factorial(n-sum(t))*__import__('math').prod(factorial(x) for x in t))
              for t in product(range(1,n+1), repeat=m) if sum(t)<=n}
    assert actual==expected,(m,n,actual,expected)
    assert len(actual)==comb(n,m)
    return actual


def faces(k):
    m=len(k)
    return {s for s in product(*(range(1,j+1) for j in k))}


def check_chambers(m,n):
    actual=signatures(m,n)
    for sizes in actual:
        # Every nonempty tuple of componentwise face sizes occurs on a face.
        representative=[]
        for i,k in enumerate(sizes,1): representative.extend([i]*k)
        representative.extend([0]*(n-len(representative)))
        indices=defaultdict(list)
        for j,val in enumerate(representative):
            if val: indices[val].append(j)
        attained=set()
        for choices in product(*(range(1,sizes[i-1]+1) for i in range(1,m+1))):
            face=[0]*n
            for i,amount in enumerate(choices,1):
                for j in indices[i][:amount]:face[j]=i
            attained.add(tuple(face.count(i) for i in range(1,m+1)))
        assert attained==faces(sizes)
        # For m=n-1 every nontrivial chamber is one segment from common apex.
        if n==m+1:assert max(sizes)<=2
    return len(actual)


def check_sorted_simplex(k):
    # Every sorted rational probability vector has a unique expansion
    # in equal-prefix vectors v_j, with coefficients j*(a_j-a_{j+1}).
    for denominator in range(k, k+6):
        for vals in product(range(denominator+1),repeat=k):
            if sum(vals)!=denominator or tuple(sorted(vals,reverse=True))!=vals:continue
            a=[Fraction(v,denominator) for v in vals]
            coef=[j*(a[j-1]-(a[j] if j<k else 0)) for j in range(1,k+1)]
            assert all(q>=0 for q in coef)
            assert sum(coef)==1
            rec=[sum(coef[j-1]/j for j in range(i+1,k+1)) for i in range(k)]
            assert rec==a


def check_contraction(k):
    # For exact rational sample points, linear contraction to e_1
    # preserves sorting, normalization, nonnegativity, and positive support cap.
    for denom in range(k,k+4):
        for vals in product(range(denom+1),repeat=k):
            if sum(vals)!=denom or tuple(sorted(vals,reverse=True))!=vals:continue
            a=[Fraction(v,denom) for v in vals]
            support=sum(v>0 for v in a)
            for t in [Fraction(0),Fraction(1,7),Fraction(2,3),Fraction(1)]:
                b=[(1-t)*v+(t if i==0 else 0) for i,v in enumerate(a)]
                assert sum(b)==1 and all(v>=0 for v in b)
                assert b==sorted(b,reverse=True)
                assert sum(v>0 for v in b)<=support


def main():
    tests=0
    for n in range(2,7):
        for m in range(2,n+1):
            q=check_chambers(m,n)
            print('m=%d n=%d orbit_chambers=%d binomial=%d' %(m,n,q,comb(n,m)))
            tests+=1
    for k in range(1,5):
        check_sorted_simplex(k)
        check_contraction(k)
    print('HOM_COLOR_QUOTIENT_CHAMBER_AND_CONTRACTION_PASS',tests)

if __name__=='__main__': main()
