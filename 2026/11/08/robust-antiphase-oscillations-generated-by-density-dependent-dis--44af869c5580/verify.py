"""Exact checks for a two-patch Beverton--Holt migration-induced cycle.
Run with: python verify.py. Only the Python standard library is needed.
The proof of global convergence, differentiability and persistence of the
hyperbolic orbit is given in RESULT.md; finite checks are not those proofs.
"""
from fractions import Fraction as Q
from math import sqrt

q = Q(4, 5)

def f(x):
    return 4*x/(1+x)

def fp(x):
    return 4/(1+x)**2

def h(x):
    if x <= 1:
        return Q(0)
    if x >= 3:
        return Q(1)
    z = (x-1)/2
    return 3*z*z - 2*z*z*z

def hp(x):
    if x <= 1 or x >= 3:
        return Q(0)
    z = (x-1)/2
    return 3*z*(1-z)

def d(x):
    return Q(1,20)+Q(9,20)*h(x)

def dp(x):
    return Q(9,20)*hp(x)

def F(x,y):
    return ((q-d(x))*f(x)+d(y)*f(y), d(x)*f(x)+(q-d(y))*f(y))

def J(x,y):
    return (((q-d(x))*fp(x)-dp(x)*f(x),d(y)*fp(y)+dp(y)*f(y)),
            (d(x)*fp(x)+dp(x)*f(x),(q-d(y))*fp(y)-dp(y)*f(y)))

def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

assert f(Q(1)) == 2 and f(Q(3)) == 3
assert (d(Q(1)),d(Q(3)),dp(Q(1)),dp(Q(3))) == (Q(1,20),Q(1,2),Q(0),Q(0))
assert F(Q(1),Q(3)) == (Q(3),Q(1))
assert F(Q(3),Q(1)) == (Q(1),Q(3))
assert F(Q(11,5),Q(11,5)) == (Q(11,5),Q(11,5))
assert J(Q(1),Q(3)) == ((Q(3,4),Q(1,8)),(Q(1,20),Q(3,40)))
assert J(Q(3),Q(1)) == ((Q(3,40),Q(1,20)),(Q(1,8),Q(3,4)))
m = matmul(J(Q(3),Q(1)),J(Q(1),Q(3)))
assert m == ((Q(47,800),Q(21,1600)),(Q(21,160),Q(23,320)))
assert max(sum(abs(x) for x in row) for row in m) == Q(13,64) < 1
u = Q(11,5)
assert d(u) == Q(427,1250)
assert dp(u) == Q(81,250)
assert q*fp(u) == Q(5,16)
assert (q-2*d(u))*fp(u)-2*dp(u)*f(u) == -Q(13891,8000) < -1
assert Q(209,3200) + Q(21,3200)*sqrt(41) < Q(13,64)

# Exact algebraic one-step squeezing and inverse-recruitment identity.
for num in range(1,61):
    for den in range(1,15):
        x = Q(num,den)
        assert 1/(q*f(x)) == Q(5,16)/x + Q(5,16)
        assert Q(1,20) <= d(x) <= Q(1,2)
        assert q-d(x) >= Q(3,10)
        assert 0 < q*f(x) < Q(16,5)
        assert F(x,x) == (q*f(x), q*f(x))
print('VERIFY_OK: exact cycle, 2-step contraction, symmetric instability, migration bounds and rational identities')
