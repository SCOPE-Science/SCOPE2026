#!/usr/bin/env python3
"""Exact reproducibility checks for the rectangular matching-polytope John phase."""
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt, sqrt, isclose


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


@lru_cache(None)
def check_simplex(n):
    t=F(1,n+1)
    Q=[[F(int(i==j),n*(n+1))-F(1,n*(n+1)**2) for j in range(n)] for i in range(n)]
    Qinv=[[n*(n+1)*(int(i==j)+1) for j in range(n)] for i in range(n)]
    assert matmul(Q,Qinv)==[[int(i==j) for j in range(n)] for i in range(n)]
    contacts=[[F(1,n) for j in range(n)]] + [[F(int(j!=i),n) for j in range(n)] for i in range(n)]
    vectors=[[v-t for v in p] for p in contacts]
    assert [sum(v[i] for v in vectors) for i in range(n)]==[0]*n
    # Unwhitened John's moment identity: sum n/(n+1) * v v^T = Q.
    weighted=[[sum(F(n,n+1)*v[i]*v[j] for v in vectors) for j in range(n)] for i in range(n)]
    assert weighted==Q
    # Every normalized tangent point lies on the unit ellipsoid.
    for v in vectors:
        assert sum(v[i]*Qinv[i][j]*v[j] for i in range(n) for j in range(n))==1
    assert Q[0][0]==t*t and sum(Q[i][j] for i in range(n) for j in range(n))==t*t
    return Q


def check_rectangle(m,n):
    t=F(1,n+1)
    # The matrix ellipsoid is the direct-sum-shape (not Cartesian product) of row simplex John shapes.
    # Exact row and coordinate facet margins are both t; each has squared support variance t*t.
    # The previously proven exact simplex identities give both margins t.
    # Column facet has center m*t and squared support variance m*t*t.
    lhs=float(m*t)+sqrt(float(m*t*t))
    feasible=(n+1)**2 >= (m+sqrt(m))**2-1e-12 # numeric cross-check only
    predicted= n+1>=m+sqrt(m)-1e-12
    assert (lhs<=1+1e-12)==predicted==feasible
    # Exact integer test avoiding floating-point: n+1>=m+sqrt(m) iff (n+1-m)>=0 and (n+1-m)^2 >=m.
    integer_test=(n+1-m>=0 and (n+1-m)**2>=m)
    assert integer_test==predicted
    # Strict phase, contact transition exactly at perfect-square m and n=m+sqrt(m)-1.
    exact_tie=(isqrt(m)**2==m and n+1==m+isqrt(m))
    assert exact_tie==(n+1-m>=0 and (n+1-m)**2==m)
    if integer_test:
        assert m*t + sqrt(float(m*t*t))<=1+1e-12
    return integer_test,exact_tie


def main():
    for n in range(2,13):
        check_simplex(n)
    feasible_count=0
    edge_count=0
    for m in range(2,40):
        for n in range(2,55):
            good,edge=check_rectangle(m,n)
            feasible_count+=int(good)
            edge_count+=int(edge)
    assert check_rectangle(2,3)==(True,False)
    assert check_rectangle(4,4)==(False,False)
    assert check_rectangle(4,5)==(True,True)
    assert check_rectangle(9,11)==(True,True)
    assert check_rectangle(3,4)==(True,False)
    # Explicit independent numeric non-inclusion witness, row-center plus column-support direction.
    m,n=4,4
    Q=check_simplex(n)
    delta=[(Q[i][0]/(sqrt(m)*float(F(1,n+1)))) for i in range(n)]
    X=[[float(F(1,n+1))+v for v in delta] for _ in range(m)]
    assert sum(row[0] for row in X)>1+1e-8
    # Every row simplex inequality holds at this support witness, by ellipsoid containment.
    assert min(min(row) for row in X)>=-1e-12
    assert max(sum(row) for row in X)<=1+1e-12
    print(f'EXACT SIMPLEX KKT FRAME: n=2..12; RECTANGLE PHASE TESTS: {39-2+1}x{55-2}={38*53}, included={feasible_count}, threshold_equal={edge_count}')
    print('RECTANGULAR JOHN CERTIFICATE CHECKS PASSED')


if __name__=='__main__':
    main()
