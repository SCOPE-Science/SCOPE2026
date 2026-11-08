#!/usr/bin/env python3
"""Reproduce algebraic and finite cyclic tests for a fourth-order heat stencil.
All-dimensional statements are proved in RESULT.md, not inferred from finite tests.
"""
import math
import cmath
from fractions import Fraction as F

checks = 0

def assert_close(a, b, tol=3e-10):
    global checks
    checks += 1
    assert abs(a-b) < tol, (a,b)

def assert_true(x):
    global checks
    checks += 1
    assert x

# Form Q=D-D^2/12 exactly, D=S+S^-1-2I.
d = {-1: F(1), 0:F(-2), 1:F(1)}
d2 = {}
for k,a in d.items():
    for j,b in d.items():
        d2[k+j] = d2.get(k+j,F(0)) + a*b
q = {j:d.get(j,F(0))-d2.get(j,F(0))/12 for j in range(-2,3)}
assert_true(q == {-2:-F(1,12),-1:F(4,3),0:-F(5,2),1:F(4,3),2:-F(1,12)})
assert_true(sum(q.values()) == 0)

r = F(16)
qr = sum(c*r**j for j,c in q.items())
assert_true(qr == -F(2475,1024))
# For v=log(16)+1/2, use exp(1/2)<2, exp(1)<3, exp(-1/2)<1, exp(-1)<1.
alpha_upper = -F(5,2) + F(4,3)*(16*2 + F(1,16)) + F(1,12)*(256*3 + F(1,256))
assert_true(alpha_upper < 105)
assert_true(F(105,500) < F(1,4))
assert_true(F(1,4)-F(105,500)==F(1,25))

# Eigenvalue of Q must be -A-A^2/12, A=2-2cos(theta).
for n in range(5,51):
    for k in range(n):
        th = 2*math.pi*k/n
        eig = sum(float(c)*cmath.exp(1j*j*th) for j,c in q.items())
        A = 2-2*math.cos(th)
        assert_close(eig.real, -A-A*A/12)
        assert_close(eig.imag,0)
        if k: assert_true(eig.real < 1e-10)

# The finite cyclic heat kernel is inverse DFT of exact spectral multipliers.
def heat_kernel(n, t):
    out=[]
    for j in range(n):
        val=sum(math.exp(-t*(a+a*a/12))*math.cos(j*2*math.pi*k/n)
                for k in range(n)
                for a in [2-2*math.cos(2*math.pi*k/n)])/n
        out.append(val)
    return out

for n in (5,6,7,8,9,10,12,16,20,24,32,48,64):
    for t in (0.001,0.05,0.1,0.5,2.0,5*n*n):
        p=heat_kernel(n,t)
        assert_close(sum(p),1)
        assert_close(p[1],p[-1])
        if t >=5*n*n: assert_true(min(p)>0)
    for t in (0.001,0.02,n/500):
        p=heat_kernel(n,t)
        assert_true(min(p[1:]) < -1e-12)

# Several fixed-time infinite kernel negative witnesses, using finite large
# cycles only as approximations (not as a proof of infinite sign changes).
for t, j in ((0.05,2),(0.2,3),(0.4,4),(0.7,5),(1.0,6),(2.0,9)):
    p=heat_kernel(80,t)
    assert_true(p[j]<-1e-11)

# Exact leading short-time negative distance-two coefficient on cycles n>=5.
for n in (5,7,12,30):
    for t in (1e-4,5e-5):
        p=heat_kernel(n,t)
        assert_close(p[2]/t,-1/12,0.0003)

print('PASS',checks,'exact-arithmetic, spectral, periodic-kernel and sign checks')
