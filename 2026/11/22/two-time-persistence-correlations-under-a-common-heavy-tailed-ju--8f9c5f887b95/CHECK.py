"""Standalone consistency checks for a two-time survival-ratio formula.

Run: python3 CHECK.py
This checks integral identities and normalization numerically; the
asymptotic and positivity theorems are proved analytically in RESULT.md.
"""
import math

def simpson(f, a, b, n=20000):
    assert n % 2 == 0
    h = (b-a)/n
    v = f(a) + f(b)
    for j in range(1, n):
        v += (4 if j % 2 else 2)*f(a+j*h)
    return v*h/3

def integral(alpha, c):
    return 2*simpson(lambda th: (1+(c-1)*math.cos(th)**(2*alpha))**(-1/alpha),0,math.pi/2)

def ratio(alpha,c):
    factor = alpha*math.gamma(1/alpha)/math.gamma(1/(2*alpha))**2
    return factor*c**(1/(2*alpha))*integral(alpha,c)

assert abs(integral(0.5,1)-math.pi) < 1e-11
assert abs(integral(0.5,2)-4/3) < 1e-11
assert abs(ratio(0.5,1)-math.pi/2) < 1e-11
assert abs(ratio(0.5,2)-4/3) < 1e-11
for c in (1, 1.25, 2, 5, 10, 100):
    assert abs(ratio(1,c)-1) < 1e-9
for alpha in (0.25,0.5,0.8):
    for c in (1.01,2,10):
        assert ratio(alpha,c)>1
assert ratio(.5,10)<ratio(.5,2)<ratio(.5,1)
print('PASS: exact half-stable two-time constant, normalization, positivity checks')
