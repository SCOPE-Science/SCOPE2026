#!/usr/bin/env python3
"""Exact rational checks of normalized Monge corner-block projection formulas.

Run: python3 check_projection.py
Only the Python standard library is required. The finite tests verify symbolic
claims in sample dimensions; they are not a substitute for their general proof.
"""
from fractions import Fraction as Q


def inner_corner_cut(n, a, b, k):
    h = n - b
    if k <= a:
        overlap = k * b
    elif k <= h:
        overlap = a * b
    else:
        overlap = a * (n - k)
    return Q(overlap, 2*a*b*k*(n-k))


def inner_cuts(n, i, j):
    return Q(1, 2*max(i,j)*(n-min(i,j)))


def norm_corner(a,b):
    return Q(1, 2*a*b)


def assert_projection(n,a,b):
    s=a+b
    h=n-b
    c=n-s
    lam={a:Q(b,s),h:Q(a,s)}
    if a==h:
        lam={a:Q(1)}
    assert sum(lam.values())==1
    G=lambda k: sum(w*inner_cuts(n,k,j) for j,w in lam.items())
    grad={k:G(k)-inner_corner_cut(n,a,b,k) for k in range(1,n)}
    active=grad[a]
    assert all(grad[k]==active for k in lam)
    assert all(v>=active for v in grad.values())
    obj=norm_corner(a,b)+sum(w*G(k) for k,w in lam.items())-2*sum(w*inner_corner_cut(n,a,b,k) for k,w in lam.items())
    target=Q(c*(a*b+s*c),2*a*b*s*(n-a)*(n-b))
    assert obj==target,(n,a,b,obj,target)
    return obj


def direct_matrix(n,a,b):
    rows=[]
    for i in range(1,n+1):
        row=[]
        for j in range(1,n+1):
            good=(i<=a and j>n-b) or (j<=a and i>n-b)
            row.append(Q(int(good),2*a*b))
        rows.extend(row)
    return rows


def direct_inner(u,v):
    return sum(x*y for x,y in zip(u,v))


def main():
    matrix_checks=0
    for n in range(3,11):
        f={k:direct_matrix(n,k,n-k) for k in range(1,n)}
        for i in range(1,n):
            for j in range(1,n):
                assert direct_inner(f[i],f[j])==inner_cuts(n,i,j)
                matrix_checks+=1
        for a in range(1,n):
            for b in range(1,n-a+1):
                v=direct_matrix(n,a,b)
                assert direct_inner(v,v)==norm_corner(a,b)
                for k in range(1,n):
                    assert direct_inner(v,f[k])==inner_corner_cut(n,a,b,k)
                    matrix_checks+=1
    examined=0
    for n in range(3,46):
        dmax=Q((n-2)*(2*n-3),4*(n-1)*(n-1))
        for a in range(1,n):
            for b in range(1,n-a+1):
                value=assert_projection(n,a,b)
                assert value<dmax if (a,b)!=(1,1) else value==dmax
                examined+=1
    print(f'MONGE_METRIC_FACE_PROJECTION_PASS exact_cases={examined} matrix_checks={matrix_checks} n=3..45')


if __name__=='__main__':main()
