#!/usr/bin/env python3
"""Exact checks of uniform-vertex covariance and the quadratic PCA transition.
Run: python3 partial_permutohedron_vertex_covariance_check.py
Dependencies: Python standard library only. Finite checks supplement the proof.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial


def orbit_moments(m, n):
    W = sum(factorial(m)//factorial(m-k) for k in range(m+1))
    ES = ES2 = EQ = 0
    for k in range(m+1):
        w = factorial(m)//factorial(m-k)
        ss = k*(2*n-k+1)//2
        qq = sum((n-j)**2 for j in range(k))
        ES += w*ss
        ES2 += w*ss**2
        EQ += w*qq
    es, es2, eq = F(ES,W),F(ES2,W),F(EQ,W)
    lam_ax = (es2-es*es)/m
    lam_tr = (m*eq-es2)/(m*(m-1))
    return es/F(m), lam_ax, lam_tr


def explicit_vertices(m,n):
    for k in range(m+1):
        vals=tuple(range(n-k+1,n+1))
        for subset in combinations(range(m), k):
            for values in permutations(vals):
                a=[0]*m
                for i,v in zip(subset,values): a[i]=v
                yield a


def raw_covariance(m,n):
    V=list(explicit_vertices(m,n)); N=len(V)
    avg=[F(sum(x[i] for x in V),N) for i in range(m)]
    cov=[[F(sum(x[i]*x[j] for x in V),N)-avg[i]*avg[j] for j in range(m)] for i in range(m)]
    return avg,cov


def phase_polynomial(m):
    # p is the mass at missing count m for truncated Poisson(1).
    Z = sum(F(1,factorial(d)) for d in range(m+1))
    p = F(1,factorial(m))/Z
    A = 1 - (m*m-m+2)*p - (m-1)*p*p
    B = (m**3-4*m*m+3*m-6)*p + (m*m-4*m+3)*p*p - m*m+m+3
    C = -F(1,12)*( (3*m**4-20*m**3+36*m*m-11*m+54)*p
        + (3*m**3-21*m*m+45*m-27)*p*p
        + m**4-12*m**3+41*m*m-34*m-27 )
    return A,B,C


def sign_at(m,n):
    a,b,c=phase_polynomial(m)
    return a*n*n+b*n+c


def main():
    cases=verts=0
    for m in range(2,7):
        for n in range(m,m+7):
            avg,cov=raw_covariance(m,n)
            mu,la,lt=orbit_moments(m,n)
            assert all(x==mu for x in avg)
            for i in range(m):
                for j in range(m):
                    expect=lt*(int(i==j)-F(1,m))+la/F(m)
                    assert cov[i][j]==expect, (m,n,i,j,cov[i][j],expect)
            assert (la-lt)*m*(m-1)==sign_at(m,n), (m,n,la-lt,sign_at(m,n))
            cases+=1
            verts+=sum(factorial(m)//factorial(m-k) for k in range(m+1))
    for m in range(2,201):
        A,B,C=phase_polynomial(m)
        assert A>0 and sign_at(m,m)<0
        # Exact rational monotone sign classification around the one root:
        n=m
        while sign_at(m,n)<0:
            n*=2
        lo,hi=m,n
        while hi-lo>1:
            mid=(hi+lo)//2
            if sign_at(m,mid)<0:lo=mid
            else:hi=mid
        assert sign_at(m,lo)<0 and sign_at(m,hi)>=0
    print('PARTIAL_PERMUTOHEDRON_VERTEX_COVARIANCE_CHECKS_PASSED', 'cases=',cases,'vertices=',verts,'phase_orders=',199)

if __name__=='__main__':main()
