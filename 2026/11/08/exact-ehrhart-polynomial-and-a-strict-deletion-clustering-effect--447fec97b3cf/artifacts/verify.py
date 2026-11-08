#!/usr/bin/env python3
"""Independent finite checks for star-deleted complete-graph polar volumes.

Run: python3 verify.py

The finite tests corroborate, rather than establish, the all-parameter theorem.
SciPy is optional; when present it independently computes small-dimensional
coordinate volumes from the original facet inequalities.
"""
from itertools import product
from math import comb, factorial
from fractions import Fraction


def formula(n, k, m):
    r = n-k-1
    assert n >= 4 and 2 <= k <= n-2 and m >= 0
    return (m+1)**n - m**n + 2*((m+1)**k - m**k)*sum(s**r for s in range(1,m+1))


def count_original_inequalities(n,k,m):
    # Vertex 0 is anchored to zero; removed edges are (0,1),...,(0,k).
    # Search ranges follow from length <=2 paths in the graph.
    deleted = {(0,j) for j in range(1,k+1)}
    edges = [(i,j) for i in range(n) for j in range(i+1,n)
             if (i,j) not in deleted]
    domains = [range(-2*m,2*m+1) if i <= k else range(-m,m+1)
               for i in range(1,n)]
    count = 0
    for tail in product(*domains):
        x = (0,)+tail
        if all(abs(x[i]-x[j]) <= m for i,j in edges):
            count += 1
    return count


def leading_coefficient_by_finite_differences(n,k):
    # An independent extraction of the highest Ehrhart coefficient:
    # (d-th forward difference at zero)/d!.
    d=n-1
    return Fraction(sum((-1)**(d-i)*comb(d,i)*formula(n,k,i)
                        for i in range(d+1)),factorial(d))


def exact_hstar(n,k):
    # Ehrhart dimension d=n-1; numerator of F(z)=sum L(m)z^m.
    d=n-1
    return [sum((-1)**j*comb(d+1,j)*formula(n,k,i-j)
                for j in range(i+1)) for i in range(d+1)]


def independent_volume(n,k):
    import numpy as np
    from scipy.spatial import HalfspaceIntersection, ConvexHull
    d=n-1
    deleted = {(0,j) for j in range(1,k+1)}
    halfspaces=[]
    for i in range(n):
        for j in range(i+1,n):
            if (i,j) in deleted:
                continue
            v=np.zeros(d)
            if i: v[i-1] += 1
            if j: v[j-1] -= 1
            halfspaces.append(np.r_[v,-1.])
            halfspaces.append(np.r_[-v,-1.])
    verts=HalfspaceIntersection(np.array(halfspaces), np.zeros(d)).intersections
    return ConvexHull(verts).volume, len(verts)


def main():
    enum_count=0
    for n in range(4,8):
        for k in range(2,n-1):
            for m in range(0,3):
                observed=count_original_inequalities(n,k,m)
                expected=formula(n,k,m)
                assert observed == expected, (n,k,m,observed,expected)
                enum_count+=1
    # A deeper dilation check of the smallest genuinely nonmatching profile.
    for m in (3,4):
        assert count_original_inequalities(4,2,m) == formula(4,2,m)
        enum_count+=1
    hstar_count=0
    for n in range(4,13):
        for k in range(2,n-1):
            h=exact_hstar(n,k)
            assert h==h[::-1] and all(v>0 for v in h), (n,k,h)
            assert leading_coefficient_by_finite_differences(n,k) == Fraction(n,1)+Fraction(2*k,n-k)
            hstar_count+=1
    strict_count=0
    for n in range(4,13):
        for k in range(2,n//2+1):
            for m in range(1,8):
                matching=(m+1)**n-m**n+2*k*sum(s**(n-2) for s in range(1,m+1))
                assert formula(n,k,m)>matching
                strict_count+=1
    hull_count=0
    try:
        import scipy  # noqa: F401
    except ImportError:
        print('OPTIONAL_SCIPY_NOT_AVAILABLE; skipping independent hull computations')
    else:
        for n in range(4,7):
            for k in range(2,n-1):
                observed, nv=independent_volume(n,k)
                predicted=float(Fraction(n,1)+Fraction(2*k,n-k))
                assert abs(observed-predicted)<1e-7, (n,k,observed,predicted,nv)
                hull_count+=1
    print('DELETED_STAR_POLAR_EHRHART_CHECKS_PASSED'
          f' independent_counts={enum_count} numerator_and_lead={hstar_count}'
          f' strict_matching_comparisons={strict_count} independent_hulls={hull_count}')

if __name__=='__main__':
    main()
