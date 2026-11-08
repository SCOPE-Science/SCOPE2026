#!/usr/bin/env python3
"""Exact checks for the sextic pairing divisor and an elliptic-surface witness.
Only the Python 3 standard library is required.
"""
from fractions import Fraction as F
from itertools import permutations
from math import prod


def pairings(xs):
    xs = tuple(xs)
    if not xs:
        yield ()
    else:
        a = xs[0]
        for j in range(1, len(xs)):
            b = xs[j]
            for remainder in pairings(xs[1:j] + xs[j + 1:]):
                yield ((a, b),) + remainder


M = list(pairings(range(6)))
assert len(M) == 15


def det3(rows):
    a, b, c = rows
    return (a[0] * (b[1]*c[2]-b[2]*c[1])
            -a[1] * (b[0]*c[2]-b[2]*c[0])
            +a[2] * (b[0]*c[1]-b[1]*c[0]))


def row(ra, rb):
    return (F(1), -ra-rb, ra*rb)


def delta(roots, matching):
    return det3([row(roots[i],roots[j]) for i,j in matching])


def invariant(roots):
    return prod(delta(roots,m) for m in M)


def delta_gradient(roots, matching):
    base = [list(row(roots[i],roots[j])) for i,j in matching]
    result = [F(0)]*6
    for k, (i,j) in enumerate(matching):
        for idx, partner in ((i,roots[j]),(j,roots[i])):
            rows = [r[:] for r in base]
            rows[k] = [F(0),F(-1),partner]
            result[idx] = det3(rows)
    return result


def minor2(a,b,i,j):
    return a[i]*b[j]-a[j]*b[i]


def padd(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return out


def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def pscale(a,c):return [c*x for x in a]


def psub(a,b):return padd(a,pscale(b,-1))


def pequal(a,b):
    m=max(len(a),len(b))
    return all((a[i] if i<len(a) else 0)==(b[i] if i<len(b) else 0) for i in range(m))


def verify():
    distinct = list(map(F,[0,1,2,3,5,7]))
    even = list(map(F,[1,-1,2,-2,3,-3]))
    collision = list(map(F,[1,1,2,3,5,8]))
    assert invariant(distinct) != 0
    assert invariant(even) == 0
    assert sum(delta(even,m)==0 for m in M) == 1
    assert invariant(collision) != 0  # no generic discriminant factor
    for perm in permutations(range(6)):
        if perm[0] != 0: continue # 120 exact permutations suffice for this consistency check
        assert invariant([distinct[i] for i in perm]) == invariant(distinct)
    # Two independent branches at a generic reduced-Klein-four configuration.
    double = [F(2),F(-2),F(1,2),F(-1,2),F(1),F(-1)]
    zeros=[m for m in M if delta(double,m)==0]
    assert len(zeros)==2
    u,v=[delta_gradient(double,m) for m in zeros]
    assert minor2(u,v,0,1) != 0
    # Construct a three-root split Weierstrass cubic for six I_2 fibres.
    # D12=5(t^2-1), D23=-8(t^2-4), D31=3(t^2-9).
    A=[F(-5),F(0),F(5)]
    B=[F(32),F(0),F(-8)]
    C=pscale(padd(A,B),-1)
    assert pequal(C,[F(-27),F(0),F(3)])
    Q1=pscale(padd(pscale(A,2),B),F(1,3))
    Q2=pscale(psub(B,A),F(1,3))
    Q3=pscale(psub(pscale(A,-1),pscale(B,2)),F(1,3))
    assert pequal(padd(padd(Q1,Q2),Q3),[F(0)])
    assert pequal(psub(Q1,Q2),A)
    assert pequal(psub(Q2,Q3),B)
    assert pequal(psub(Q3,Q1),C)
    f=[F(1)]
    for a in [1,-1,2,-2,3,-3]: f=pmul(f,[-F(a),F(1)])
    d=pmul(pmul(A,B),C)
    assert pequal(d,pscale(f,F(-120)))
    acoef=padd(padd(pmul(Q1,Q2),pmul(Q1,Q3)),pmul(Q2,Q3))
    bcoef=pscale(pmul(pmul(Q1,Q2),Q3),F(-1))
    discriminant=psub(pscale(pmul(pmul(acoef,acoef),acoef),-4),pscale(pmul(bcoef,bcoef),27))
    assert pequal(discriminant,pmul(d,d))
    print('MATCHINGS 15')
    print('GENERIC_NONZERO', invariant(distinct))
    print('EVEN_ZERO_BRANCHES',sum(delta(even,m)==0 for m in M))
    print('DOUBLE_BRANCHES',len(zeros),'TRANSVERSE_MINOR',minor2(u,v,0,1))
    print('SIX_I2_DISCRIMINANT_SQUARE_OK')
    print('CERTIFICATE_OK')


if __name__=='__main__':
    verify()
