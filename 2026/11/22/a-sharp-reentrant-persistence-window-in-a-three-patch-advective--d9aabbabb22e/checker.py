#!/usr/bin/env python3
"""Exact supplementary algebra checks for the three-patch source-only stream model.

Runs with Python 3 standard library; it is an identity and example checker,
not a replacement for the mathematical proof in RESULT.md.
"""
from fractions import Fraction
from math import sqrt

# Sparse integer multivariate polynomials, monomial order (a,d,q).
def const(k):
    return {(0, 0, 0): int(k)} if k else {}

def add(*polys):
    out = {}
    for p in polys:
        for exponent, coefficient in p.items():
            out[exponent] = out.get(exponent, 0) + coefficient
    return {k:v for k,v in out.items() if v}

def neg(p):
    return {k:-v for k,v in p.items()}

def sub(a,b):
    return add(a,neg(b))

def mul(*polys):
    out=const(1)
    for p in polys:
        nxt={}
        for i,ci in out.items():
            for j,cj in p.items():
                k=tuple(x+y for x,y in zip(i,j))
                nxt[k]=nxt.get(k,0)+ci*cj
        out={k:v for k,v in nxt.items() if v}
    return out

def derivative(p, idx):
    out={}
    for ex, c in p.items():
        if ex[idx]:
            nex=list(ex)
            nex[idx]-=1
            nex=tuple(nex)
            out[nex]=out.get(nex,0)+c*ex[idx]
    return out

def det3(m):
    return add(mul(m[0][0],sub(mul(m[1][1],m[2][2]),mul(m[1][2],m[2][1]))),
               neg(mul(m[0][1],sub(mul(m[1][0],m[2][2]),mul(m[1][2],m[2][0])))),
               mul(m[0][2],sub(mul(m[1][0],m[2][1]),mul(m[1][1],m[2][0]))))

a={(1,0,0):1}; d={(0,1,0):1}; q={(0,0,1):1}
z=const(0)
M=[[add(a,d,q),neg(d),z],
   [neg(add(d,q)),add(a,mul(const(2),d),q),neg(d)],
   [z,neg(add(d,q)),add(a,d)]]
H=add(mul(a,a),mul(const(3),a,d),mul(a,q),mul(d,d))
N=add(mul(a,a),mul(const(4),a,d),mul(const(2),a,q),mul(const(3),d,d),mul(const(3),d,q),mul(q,q))
cofactor11=sub(mul(M[1][1],M[2][2]),mul(M[1][2],M[2][1]))
assert cofactor11==H, 'incorrect cofactor'
assert det3(M)==mul(a,N), 'incorrect determinant'
Q=add(mul(a,a,add(a,q)),mul(const(2),add(a,q),sub(mul(const(2),a),q),d),mul(sub(mul(const(5),a),mul(const(3),q)),d,d))
assert sub(mul(derivative(N,1),H),mul(N,derivative(H,1)))==Q, 'derivative identity mismatch'

# Rational sample a=1, q=2, birth r=25/8.
def threshold(d):
    d=Fraction(d)
    return (3*d*d+10*d+9)/(d*d+3*d+3)

r=Fraction(25,8)
assert threshold(0)==3
assert threshold(1)==Fraction(22,7)
assert threshold(2)==Fraction(41,13)
assert threshold(10)==Fraction(409,133)
assert threshold(1)>r and threshold(2)>r
assert threshold(0)<r and threshold(10)<r
assert 5-sqrt(13)>0
assert ((5-sqrt(13))/2)<1<2<((5+sqrt(13))/2)
assert 3 < r < 2+2/sqrt(3)

# Explicit polynomial difference: 8N - 25H = -d^2 + 5d - 3 at a=1,q=2.
for D in range(0,41):
    d=Fraction(D,3)
    h=d*d+3*d+3
    n=3*d*d+10*d+9
    assert 8*n-25*h==-d*d+5*d-3

# Two-patch: threshold a*(a+2d+q)/(a+d), derivative sign a-q.
for A in range(1,5):
    for Qv in range(1,8):
        for D in range(1,12):
            lhs=Fraction(A*(A+2*(D+1)+Qv), A+D+1)-Fraction(A*(A+2*D+Qv),A+D)
            assert (lhs>0)-(lhs<0)==(A>Qv)-(A<Qv)

print('PASS: determinant/cofactor/derivative identities and exact sample, two-patch monotonicity')
