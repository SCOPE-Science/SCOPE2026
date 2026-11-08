#!/usr/bin/env python3
"""Recompute local Taylor coefficients and an illustrative orbit.

Only standard-library modules are used.  Finite checks supplement, but do not
replace, the infinite-dimensional (in time) arguments in RESULT.md.
"""
from fractions import Fraction as F
from math import exp, sqrt

D = 4  # Truncate formal power series at degree three.

def const(a):
    return [F(a)] + [F(0)] * (D - 1)

def add(a, b):
    return [x + y for x, y in zip(a, b)]

def neg(a):
    return [-v for v in a]

def mul(a, b):
    return [sum(a[j] * b[i-j] for j in range(i+1)) for i in range(D)]

def inv(a):
    assert a[0]
    z = [F(1)/a[0]] + [F(0)] * (D - 1)
    for i in range(1, D):
        z[i] = -sum(a[j]*z[i-j] for j in range(1, i+1))/a[0]
    return z

def scale(a, c):
    return [v*c for v in a]

def exp_series(a):
    assert a[0] == 0
    y = const(1)
    term = const(1)
    for j in range(1, D):
        term = scale(mul(term, a), F(1, j))
        y = add(y, term)
    return y

checks = 0
for L in [F(3,2), F(2), F(3), F(5), F(7,2)]:
    for g in [F(1,10), F(1,4), F(1,2), F(3,4)]:
        K = L-1
        a = g*L/K
        c = F(1,2)+a
        b = F(1,3)+a+2*a*a
        h1 = -g*L
        h2 = -g*g*L*L/K
        Y = [F(0), F(1), F(0), F(0)]
        # P(Y)=1-exp(-Y(1+cY)).
        P = add(const(1), neg(exp_series(neg(add(Y, scale(mul(Y,Y), c))))))
        X = add(const(K), add(scale(Y,h1),scale(mul(Y,Y),h2)))
        # F(X,Y), G(X,Y) from the exact ecological map.
        X1 = mul(scale(mul(X,inv(add(const(1),X))),L), add(const(1), neg(scale(P,g))))
        Y1 = scale(mul(X,P),F(1)/K)
        assert Y1[0:3] == [F(0),F(1),F(0)]
        assert Y1[3] == -b
        graph_next = add(const(K), add(scale(Y1,h1),scale(mul(Y1,Y1),h2)))
        assert X1[:3] == graph_next[:3]
        checks += 3

# A sample in the exact interior parameter domain.
L, g, K = 3., .25, 2.
beta = 1/(g*K)
a = g*L/K
c_star = .5+a
b = 1/3 + a + 2*a*a

def iterate(c, count):
    x,y=K,.1
    for _ in range(count):
        p=-__import__('math').expm1(-y*(1+c*y))
        x,y=L*x/(1+x)*(1-g*p), beta*g*x*p
    return x,y

x,y=iterate(c_star,200000)
assert abs(sqrt(200000)*y-1/sqrt(2*b)) < .001
checks += 1
x,y=iterate(.5,200000)
assert abs(200000*y-1/(c_star-.5)) < .005
checks += 1
x,y=iterate(.9,200000)
assert .02 < y < .03 and abs(x-(K-g*L*y)) < .005
checks += 1
print(f'VERIFY_OK {checks} exact coefficient identities and orbit checks')
