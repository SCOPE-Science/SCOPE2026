#!/usr/bin/env python3
"""All-ray polynomial covariogram of a cross-polytope: exact checks.

Only Python standard library is required for exact tests.
With --hull, numpy/scipy independently evaluates intersection-polytope volume.
"""
from fractions import Fraction as Q
from math import comb, factorial
from itertools import combinations, product
import argparse


def subsets(indices):
    seq=tuple(indices)
    return (x for bits in product((0,1),repeat=len(seq))
            for x in [tuple(v for v,b in zip(seq,bits) if b)])


def positive_power(x,r):
    return x**r if x>0 else Q(0)


def moment(indices,r,c,lengths):
    """Integral over product [0,lengths_i] of (sum z_i-c)_+^r."""
    m=len(indices)
    return Q(factorial(r),factorial(m+r))*sum(
        (-1)**len(H)*positive_power(sum(lengths[i] for i in indices if i not in H)-c,m+r)
        for H in subsets(indices))


def raw_partition(direction,t):
    """Orthant/cube integration before any algebraic cancellation."""
    d=len(direction)
    if t<0 or t*sum(direction)>2:return Q(0)
    lengths=[t*x for x in direction]
    U=1-sum(lengths)/2
    total=Q(0)
    all_idx=tuple(range(d))
    for E in subsets(all_idx):
        inside=tuple(i for i in all_idx if i not in E)
        k=len(E)
        for P in subsets(E):
            a=sum(lengths)/2-sum(lengths[i] for i in P)
            j=moment(inside,k,a-U,lengths)
            j-=(-1)**k*moment(inside,k,a+U,lengths)
            for r in range(1,k+1,2):
                j-=2*comb(k,r)*U**(k-r)*moment(inside,r,a,lengths)
            total+=j/factorial(k)
    return total


def radial_polynomial(direction,t):
    """One polynomial with no positive-part operation involving t."""
    d=len(direction); all_idx=tuple(range(d));L=sum(direction)
    U=1-L*t/2
    answer=Q(2**d,factorial(d))
    for E in subsets(all_idx):
        k=len(E)
        if not k:continue
        inside=tuple(i for i in all_idx if i not in E)
        for P in subsets(E):
            c=L/2-sum(direction[i] for i in P)
            for r in range(1,k+1,2):
                answer-=Q(2*comb(k,r),factorial(k))*U**(k-r)*t**(len(inside)+r)*moment(inside,r,c,direction)
    return answer


def hull_volume(direction,t):
    import numpy as np
    from scipy.spatial import HalfspaceIntersection, ConvexHull
    d=len(direction);planes=[];v=np.asarray([float(x) for x in direction])
    for ss in product((-1.,1.),repeat=d):
        s=np.asarray(ss)
        planes.extend((np.r_[s,-1.],np.r_[s,-1.-float(t)*np.dot(s,v)]))
    midpoint=float(t)*v/2
    vertices=HalfspaceIntersection(np.asarray(planes),midpoint).intersections
    return float(ConvexHull(vertices).volume)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--hull',action='store_true')
    args=p.parse_args()
    vectors=((Q(1),),(Q(1),Q(1)),(Q(1),Q(2)),
             (Q(1),Q(1),Q(1)),(Q(1),Q(2),Q(3)),(Q(2),Q(1),Q(3),Q(5)),
             (Q(1),)*5,(Q(1),Q(2),Q(3),Q(4),Q(5)))
    count=0
    for v in vectors:
        L=sum(v)
        for z in range(0,21):
            t=Q(2*z,20*L)
            a=raw_partition(v,t)
            b=radial_polynomial(v,t)
            assert a==b,(v,t,a,b)
            count+=1
        assert radial_polynomial(v,Q(0))==Q(2**len(v),factorial(len(v)))
        assert radial_polynomial(v,Q(2,L))==0
        count+=2
    # Independent exact special cases.
    assert radial_polynomial((Q(1),Q(1)),Q(2,5))==Q(6,5)
    assert radial_polynomial((Q(1),)*3,Q(2,5))==Q(28,75)
    count+=2
    if args.hull:
        for v in vectors:
            if len(v)>4 or len(v)<2:continue
            for z in (1,3,7,11,15,19):
                t=Q(2*z,20*sum(v))
                diff=abs(hull_volume(v,t)-float(radial_polynomial(v,t)))
                assert diff<1e-8,(v,t,diff)
                count+=1
    print('CROSSPOLYTOPE_RADIAL_POLYNOMIAL_OK',count)

if __name__=='__main__':main()
