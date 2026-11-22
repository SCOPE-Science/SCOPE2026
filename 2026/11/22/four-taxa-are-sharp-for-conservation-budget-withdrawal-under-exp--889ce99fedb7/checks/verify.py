#!/usr/bin/env python3
"""Reproduce rational stationary-point and sensitivity certificates.

Public scientific checker. Standard library only. No numerical optimization is
needed for the exact four-taxon certificate.
"""
from fractions import Fraction as Q
from math import log, exp


def solve(matrix, rhs):
    n = len(matrix)
    a = [[Q(z) for z in row] + [Q(rhs[i])] for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j] != 0)
        a[j], a[pivot] = a[pivot], a[j]
        v = a[j][j]
        a[j] = [z/v for z in a[j]]
        for i in range(n):
            if i == j: continue
            v = a[i][j]
            a[i] = [a[i][k] - v*a[j][k] for k in range(n+1)]
    return [a[i][-1] for i in range(n)]


def det(a):
    n = len(a)
    mat = [[Q(z) for z in row] for row in a]
    out = Q(1)
    for j in range(n):
        if mat[j][j] == 0:
            idx = next((i for i in range(j+1,n) if mat[i][j] != 0), None)
            if idx is None: return Q(0)
            mat[j],mat[idx] = mat[idx],mat[j]
            out = -out
        p = mat[j][j]
        out *= p
        for i in range(j+1,n):
            r = mat[i][j]/p
            for k in range(j+1,n):
                mat[i][k] -= r*mat[j][k]
    return out


def four_leaf_certificate():
    q = [Q(1,12), Q(3,4), Q(3,4), Q(3,19)]
    k = [3,1,1,1]
    pendant = [12,12,12,76]
    common = 64*q[0]*q[1]*q[2]
    assert common == 3
    gradient = [k[i]*(pendant[i]*q[i] + common) for i in range(3)]
    gradient.append(pendant[3]*q[3])
    assert gradient == [12]*4
    hessian_negative = [[Q(0)]*4 for _ in range(4)]
    for i in range(4):
        hessian_negative[i][i] += pendant[i]*q[i]*k[i]**2
    for i in range(3):
        for j in range(3):
            hessian_negative[i][j] += common*k[i]*k[j]
    A = [[36,9,9,0],[9,12,3,0],[9,3,12,0],[0,0,0,12]]
    assert hessian_negative == A
    assert all(det([row[:i] for row in A[:i]]) > 0 for i in range(1,5))
    assert det(A) == 40824
    v = solve(A,[1]*4)
    assert v == [Q(-1,126), Q(1,14), Q(1,14), Q(1,12)]
    d = sum(v)
    assert d == Q(55,252)
    sensitivity = [z/d for z in v]
    assert sensitivity == [Q(-2,55),Q(18,55),Q(18,55),Q(21,55)]
    assert sum(sensitivity) == 1
    return sensitivity


def pair_interior_derivative_identity():
    # Stationarity k1*u-k2*v+(k1-k2)*t=0. Pick rational u,v,
    # with k1>k2, giving a strictly positive t, and check identity.
    tested = 0
    for k1 in range(2,11):
        for k2 in range(1,k1):
            for u in range(1,11):
                for v in range(1,11):
                    t=Q(k2*v-k1*u,k1-k2)
                    if t < 0: continue
                    den = k1*k1*u + k2*k2*v + (k1-k2)**2*t
                    assert den == k1*k2*(u+v)
                    sder = k2*k2*v-k2*(k1-k2)*t
                    assert sder == k1*k2*u
                    assert Q(sder,den) == Q(u,u+v)
                    assert 0 < Q(sder,den) < 1
                    tested += 1
    assert tested > 200
    return tested


def numerical_spot():
    # Solving the first-order optimality equations is not required for
    # the exact certificate, but independently checks the local direction.
    import math
    q0 = [1/12,3/4,3/4,3/19]
    x0 = [math.log(54/5)/3, math.log(6/5), math.log(6/5), math.log(57/10)]
    k=[3,1,1,1]
    L=[12,12,12,76]
    target=sum(x0)
    for h in (-1e-5,1e-5):
        x=x0[:]
        lam=12.0
        for _ in range(15):
            q=[0.9*math.exp(-k[i]*x[i]) for i in range(4)]
            z=64*q[0]*q[1]*q[2]
            grad=[k[i]*(L[i]*q[i]+z) for i in range(3)]+[L[3]*q[3]]
            H=[[0.0]*4 for _ in range(4)]
            for i in range(4): H[i][i]+=k[i]**2*L[i]*q[i]
            for i in range(3):
                for j in range(3): H[i][j]+=k[i]*k[j]*z
            rhs=[grad[i]-lam for i in range(4)]+[target+h-sum(x)]
            mat=[H[i]+[1.0] for i in range(4)]+[[1.0]*4+[0.0]]
            change=solve_float(mat,rhs)
            x=[x[i]+change[i] for i in range(4)]
            lam=lam+change[4]
            if max(abs(z) for z in change) < 1e-12: break
        assert abs(sum(x)-target-h)<1e-9
        assert min(x)>0
        if h<0: minus=x[0]
        else: plus=x[0]
    estimated=(plus-minus)/2e-5
    assert abs(estimated+2/55)<1e-6, estimated
    return estimated


def solve_float(matrix,rhs):
    n=len(rhs)
    a=[list(map(float,matrix[i]))+[float(rhs[i])] for i in range(n)]
    for j in range(n):
        pivot=max(range(j,n), key=lambda i:abs(a[i][j]))
        a[j],a[pivot]=a[pivot],a[j]
        r=a[j][j]
        assert abs(r)>1e-12
        a[j]=[z/r for z in a[j]]
        for i in range(n):
            if i==j: continue
            r=a[i][j]
            a[i]=[a[i][k]-r*a[j][k] for k in range(n+1)]
    return [a[i][-1] for i in range(n)]

if __name__=='__main__':
    d=four_leaf_certificate()
    tested=pair_interior_derivative_identity()
    numerical=numerical_spot()
    print('exact four-leaf allocation sensitivity:',[str(z) for z in d])
    print('exact two-leaf identities tested:',tested)
    print('numeric finite-difference first coordinate:',repr(numerical))
    print('PASS: four-leaf exact certificate, two-leaf allocation law and numerical spot check')
