#!/usr/bin/env python3
"""Reproduce exact and independent geometric volume checks.

Requires NumPy and SciPy for the optional convex-hull checks. The universal
identities and asymptotics are proved in the accompanying mathematical text.
"""
import math
from fractions import Fraction


def a(n, k, z):
    return (1 - z) * (n + 1 - k) + (1 + z) * n * k


def derivative(n, z):
    return 2*z/(1-z*z) - sum((n+1)*(k-1)/a(n,k,z)
                                  for k in range(1,n+1))


def root(n):
    lo, hi = 0., 1.-1e-12
    assert derivative(n,lo) < 0 and derivative(n,hi)>0
    for _ in range(100):
        mid = (lo+hi)/2
        if derivative(n,mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def log_product(n,z):
    assert -1 < z < 1
    m=n+1
    return ((n+2)*math.log(2)+(2*n-1)*math.log(m)
            -math.lgamma(n+1)-math.log1p(-z*z)
            -sum(math.log(a(n,k,z)) for k in range(1,n+1)))


def log_simplex(n):
    m=n+1
    return (m+1)*math.log(m+1)-2*math.lgamma(m+1)


def formula_c_vol(n):
    m=n+1
    return math.exp(math.log(2)+((3*n-1)/2)*math.log(m)
                    -math.lgamma(n+1)-(n/2)*math.log(n))


def formula_w_vol(n,z):
    m=n+1
    return math.exp((n+1)*math.log(2)+(n/2)*math.log(n)
                    +((n-1)/2)*math.log(m)-math.log1p(-z*z)
                    -sum(math.log(a(n,k,z)) for k in range(1,n+1)))


def main():
    # Entirely exact arithmetic at the first nontrivial dimension.
    z=Fraction(1,3)
    assert a(2,1,z)==4 and a(2,2,z)==6
    assert Fraction(2)*z/(1-z*z)-Fraction(3,1)/a(2,2,z)==Fraction(1,4)
    # The derivative equation has root (2 sqrt(13)-5)/9.
    zstar=(2*math.sqrt(13)-5)/9
    assert abs(derivative(2,zstar))<1e-13
    assert abs(math.exp(log_product(2,zstar))-(-945+351*math.sqrt(13))/32)<1e-10

    # Independent polyhedral calculation: construct all halfspaces, intersect,
    # and measure with Qhull; no sorting-chamber formula used here.
    import numpy as np
    from scipy.spatial import ConvexHull, HalfspaceIntersection
    count=0
    for n in range(2,7):
        m=n+1
        center=np.eye(m)-np.ones((m,m))/m
        U,_,_=np.linalg.svd(center)
        V=(U[:,:n].T@center).T*math.sqrt(m/n)
        assert np.max(np.abs(V@V.T-(m/n*np.eye(m)-np.ones((m,m))/n)))<2e-12
        C=np.asarray([np.r_[v,-1] for v in V]+[np.r_[-n*v,1] for v in V])
        independent_c=ConvexHull(C).volume
        predicted_c=formula_c_vol(n)
        assert abs(independent_c/predicted_c-1)<4e-8,(n,'C',independent_c,predicted_c)
        count+=1
        for z0 in [0.,root(n),0.61]:
            dz=np.r_[np.zeros(n),z0]
            H=np.c_[C-dz,-np.ones(2*m)]
            points=HalfspaceIntersection(H,np.zeros(n+1)).intersections
            independent_w=ConvexHull(points).volume
            predicted_w=formula_w_vol(n,z0)
            assert abs(independent_w/predicted_w-1)<5e-8,(n,z0,independent_w,predicted_w)
            assert abs(math.log(independent_c*independent_w)-log_product(n,z0))<5e-8
            count+=2
        h=1e-5
        assert derivative(n,0.) < 0
        assert derivative(n,root(n)-h)<0 and derivative(n,root(n)+h)>0
        # Symmetry axis is the unique minimizer, not necessarily the midpoint.
        assert log_product(n,root(n)) < log_product(n,0.)
    for n in [20,100,500,2000]:
        z0=root(n)
        s=n*(1-z0)
        ratio=math.exp(log_product(n,z0)-log_simplex(n))
        print('asymptotic',n,'n(1-z*)',round(s,9),'ratio',round(ratio,9))
        assert s>1.5 and s<2.3
        assert ratio>1 and ratio<math.e
    print('PASS',count,'independent convex-hull volume comparisons; exact planar and high-dimensional checks')


if __name__=='__main__':
    main()
