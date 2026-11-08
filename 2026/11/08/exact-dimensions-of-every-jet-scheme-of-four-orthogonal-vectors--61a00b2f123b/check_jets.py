"""Exact finite-coefficient checks for an isotropic jet-family construction.

Run: python3 check_jets.py
The checks do not establish the all-length dimension theorem; that follows
from the algebraic injection and the independently proved dimension bound.
"""
from fractions import Fraction as Q
from random import Random


def add(a, b, L):
    return [a[k]+b[k] for k in range(L)]


def mul(a, b, L):
    return [sum((a[i]*b[k-i] for i in range(k+1)), Q(0)) for k in range(L)]


def neg(a):
    return [-x for x in a]


def inv(a, L):
    assert a[0] != 0
    b = [Q(1)/a[0]]
    for k in range(1,L):
        b.append(-sum((a[i]*b[k-i] for i in range(1,k+1)),Q(0))/a[0])
    return b


def dot(a,b,L):
    return add(add(mul(a[0],b[1],L),mul(a[1],b[0],L),L),mul(a[2],b[2],L),L)


def shift(a,k,L):
    return [Q(0)]*k + a[:L-k]


def scale(a,s):
    return [s*x for x in a]


def construct(L, seed):
    rng = Random(seed)
    sample=lambda n: [Q(rng.randrange(-3,4)) for _ in range(n)]
    p=sample(L);p[0]=Q(rng.randrange(1,4))
    r=sample(L)
    pi=inv(p,L)
    q=scale(mul(mul(r,r,L),pi,L),Q(-1,2))
    a=[p,q,r]
    z=[[Q(0)]*L,neg(mul(r,pi,L)),[Q(1)]+[Q(0)]*(L-1)]
    b=[[Q(0)]*L,pi,[Q(0)]*L]
    assert dot(a,a,L)==[Q(0)]*L
    assert dot(a,z,L)==[Q(0)]*L
    assert dot(b,z,L)==[Q(0)]*L
    assert dot(a,b,L)==[Q(1)]+[Q(0)]*(L-1)
    assert dot(z,z,L)==[Q(1)]+[Q(0)]*(L-1)
    floor=L//2
    y=[sample(L) for _ in range(3)]
    w=[sample(L-floor) for _ in range(3)]
    if L%2:
        w[0][0]=Q(1)
        w[1][0]=w[2][0]=Q(0)
    v=[a]
    for j in range(3):
        shifted=shift(w[j],floor,L)
        v.append([add(mul(a[k],y[j],L),mul(z[k],shifted,L),L)
                  for k in range(3)])
    for i in range(4):
        for j in range(i+1,4):
            assert dot(v[i],v[j],L)==[Q(0)]*L, (L,i,j)
    for j in range(3):
        assert dot(b,v[j+1],L)==y[j]
        recovered=dot(z,v[j+1],L)[floor:]
        assert recovered==w[j],(L,j,recovered,w[j])
    number_parameters=5*L+3*floor+(L%2)
    assert number_parameters==(13*L)//2,(L,number_parameters)
    return number_parameters


def main():
    for L in range(1,16):
        for seed in range(5):
            d=construct(L, 991*L+seed)
        print('L',L,'lower_family_dimension',d,'upper_bound_floor',13*L//2,'PASS')
    print('ALL_EXACT_POLYNOMIAL_CHECKS_PASS')

if __name__=='__main__':
    main()
