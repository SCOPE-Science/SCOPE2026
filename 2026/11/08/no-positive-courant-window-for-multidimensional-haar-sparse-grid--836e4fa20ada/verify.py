#!/usr/bin/env python3
"""Exact rational checks for Haar sparse-grid upwind positivity classification.

No external dependencies. The universal theorem is proved in RESULT.md;
these checks independently construct finite-dimensional orthogonal projections.
"""
from fractions import Fraction as F
from itertools import product


def apply_v(v, level):
    n = len(v)
    width = n // (1 << level)
    result = []
    for i in range(0, n, width):
        avg = sum(v[i:i+width], F(0)) / width
        result.extend([avg] * width)
    return result


def apply_w(v, level):
    a = apply_v(v, level)
    if level == 0:
        return a
    b = apply_v(v, level - 1)
    return [x-y for x,y in zip(a,b)]


def axis_proj(a, dim, m, axis, level):
    b = {}
    for other in product(range(m), repeat=dim-1):
        seq = []
        for j in range(m):
            idx = list(other)
            idx.insert(axis,j)
            seq.append(a[tuple(idx)])
        out = apply_w(seq,level)
        for j,val in enumerate(out):
            idx=list(other)
            idx.insert(axis,j)
            b[tuple(idx)] = val
    return b


def sparse_projection(a,dim,N):
    m=1<<N
    out={k:F(0) for k in a}
    for levels in product(range(N+1),repeat=dim):
        if sum(levels)>N:
            continue
        b=a
        for axis,lev in enumerate(levels):
            b=axis_proj(b,dim,m,axis,lev)
        for k in out:
            out[k]+=b[k]
    return out


def diff(a,dim,N,axis):
    m=1<<N
    return {idx: a[idx] - a[tuple((idx[j]-1)%m if j==axis else idx[j] for j in range(dim))] for idx in a}


def test(dim,N):
    m=1<<N
    u={idx:F(int(idx[0]<m//2 and idx[1]<m//2)) for idx in product(range(m),repeat=dim)}
    one={idx:F(1) for idx in u}
    assert sparse_projection(u,dim,N)==u
    assert sparse_projection(one,dim,N)==one
    target=tuple([m//2+1,m//2+1]+[0]*(dim-2))
    assert u[target]==0
    for axis in range(dim):
        p=sparse_projection(diff(u,dim,N,axis),dim,N)
        expected=F(1,4) if axis<2 else F(0)
        assert p[target]==expected, (dim,N,axis,p[target],expected)
        assert sum(p.values())==0
    print(f'EXACT_OK d={dim} N={N}: projected incoming differences = 1/4, 1/4; inactive directions=0')


def test_n1(dim):
    # Check the edge generators 1 +/- s_j of the one-level positive cone.
    for axis in range(dim):
        for sign in (-1,1):
            u={idx:F(1+sign*(1 if idx[axis]==0 else -1)) for idx in product(range(2),repeat=dim)}
            assert sparse_projection(u,dim,1)==u
            p=sparse_projection(diff(u,dim,1,axis),dim,1)
            for r in (F(0),F(1,8),F(1,2),F(1)):
                v={idx:u[idx]-r*p[idx] for idx in u}
                assert all(x>=0 for x in v.values())
            v={idx:u[idx]-F(3,2)*p[idx] for idx in u}
            assert min(v.values())<0
    print(f'EXACT_OK d={dim} N=1: edge generators positive iff Courant <=1')


if __name__=='__main__':
    for dim,N in [(2,2),(2,3),(2,4),(3,2)]:
        test(dim,N)
    for dim in (1,2,3):
        test_n1(dim)
    print('VERIFY_OK: independent exact rational projection and boundary certificates')
