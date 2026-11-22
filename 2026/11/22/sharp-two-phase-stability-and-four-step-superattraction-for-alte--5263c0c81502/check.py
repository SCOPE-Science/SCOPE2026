#!/usr/bin/env python3
"""Exact-arithmetic witness checks for a two-phase rank-one gradient map.

The symbolic proof of the all-parameter classification is in RESULT.md.
This script only verifies algebraic identities and examples; finite tests are
not substituted for the analytical argument.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def ident():
    return [[Q(1), Q(0)], [Q(0), Q(1)]]


def rank_update(g, w):
    return [[Q(int(i == j)) - g * w[i] * w[j] for j in range(2)] for i in range(2)]


def tr(A):
    return A[0][0]+A[1][1]


def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


# Unit normals with rational cosine and sine.
u = [Q(1), Q(0)]
v = [Q(4, 5), Q(3, 5)]
s = Q(9, 25)
b = Q(1)
a = Q(25, 9)
A, B = rank_update(a,u), rank_update(b,v)
T = mul(B,A)
assert tr(T) == 0 and det(T) == 0
assert T != [[Q(0),Q(0)],[Q(0),Q(0)]]
assert mul(T,T) == [[Q(0),Q(0)],[Q(0),Q(0)]]
assert a > 2 and a*s == 1
print('DEADBEAT_EXACT', T, 'a=',a,'s=',s)

# At b=1, the spectrum of BA is {0,1-a*s}, independently of the normal signs.
for p, q in [(3,5),(4,5),(5,13),(12,13),(8,17),(15,17)]:
    v = [Q(p,q), Q(int(sqrt(q*q-p*p)),q)]
    assert sum(z*z for z in v)==1
    s = v[1]**2
    for a in [Q(1,3), Q(1), Q(2), Q(5,2), Q(3), 1/s, 2/s, 3/s]:
        T = mul(rank_update(Q(1),v),rank_update(a,u))
        assert tr(T)==1-a*s and det(T)==0
        assert (mul(T,T)==[[Q(0),Q(0)],[Q(0),Q(0)]]) == (a*s==1)
print('TWO_PHASE_FORMULAS_EXACT')

# General two-gain trace and determinant formulas at rational unit normals.
for a,b in product([Q(1,3),Q(2,3),Q(1),Q(3,2),Q(2),Q(3),Q(6)],repeat=2):
    v=[Q(4,5),Q(3,5)]
    T=mul(rank_update(b,v),rank_update(a,u))
    s=Q(9,25)
    assert tr(T)==2-a-b+a*b*(1-s)
    assert det(T)==(1-a)*(1-b)
    assert 1-tr(T)+det(T)==a*b*s
    assert 1+tr(T)+det(T)==4-2*(a+b)+a*b*(2-s)
    assert 1-det(T)==a+b-a*b
print('JURY_IDENTITIES_EXACT')

# One nonlinear example: f(x,y)=-1/2(x^2+y^2)-1/4(x^4+y^4)
# In particular, the derivative at the origin is the exact quadratic model.
u_float=(1.,0.)
v_float=(.8,.6)
a_float=25/9

def update(x,w,g):
    grad=(-x[0]-x[0]**3,-x[1]-x[1]**3)
    d=sum(w[i]*grad[i] for i in range(2))
    return (x[0]+g*w[0]*d,x[1]+g*w[1]*d)

def four(x):
    for w,g in [(u_float,a_float),(v_float,1.),(u_float,a_float),(v_float,1.)]:
        x=update(x,w,g)
    return x
for r in [1.e-2,1.e-3,1.e-4]:
    x=(r,r/2)
    y=four(x)
    ratio=sqrt(sum(yi*yi for yi in y))/r**3
    assert ratio < 200
    print('QUARTIC_FOUR_STEP',r,'output',y,'cubic_scaled',ratio)
print('CHECKS_OK')
