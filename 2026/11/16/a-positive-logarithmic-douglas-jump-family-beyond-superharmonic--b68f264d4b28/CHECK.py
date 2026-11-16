"""Finite reproducibility checks for a logarithmic radial Douglas jump identity.

This script checks exact multiplier identities and quadrature/asymptotic
consistency only; the continuous positivity theorem is proved analytically.
"""
from fractions import Fraction
from math import comb, isclose, log, pi
import mpmath as mp
mp.mp.dps = 40
checks = 0

def equal(a,b,tol=mp.mpf('2e-22')):
    global checks
    assert abs(a-b) < tol, (a,b,a-b)
    checks += 1

def harm(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

for n in range(1,81):
    b = Fraction(n,n+1) * (harm(n+1)-1)
    # Signed Poisson-mixing moment by polynomial integration.
    tpart = sum((Fraction(1,k+1) for k in range(1,n+1)),Fraction(0))
    logpart = 1 - harm(n+1)/Fraction(n+1)
    negpart = -Fraction(n,n+1)
    assert tpart+logpart+negpart == b
    checks += 1

v=lambda t: t/(1-t)-mp.log(1-t)-1
P=lambda t,theta: (1-t*t)/(1-2*t*mp.cos(theta)+t*t)
for n in [1,2,3,4,5,8,11,20,45]:
    exact=mp.mpf(n)/(n+1)*(mp.digamma(n+2)+mp.euler-1)
    val=mp.quad(lambda t:(1-t**n)*v(t),[0,mp.mpf('0.5'),mp.mpf('0.97'),1])
    equal(val,exact,mp.mpf('3e-30'))

Cpi = 1-3*mp.log(2)+2*mp.polylog(2,mp.mpf('.5'))
Jpi = mp.quad(lambda t:P(t,mp.pi)*v(t),[0,mp.mpf('.5'),mp.mpf('.97'),1])
equal(Cpi,Jpi,mp.mpf('1e-31'))
assert Cpi > mp.mpf('0.08'); checks += 1

angles=[mp.mpf(x) for x in ('0.1','0.2','0.35','0.7','1.0','1.5','2.0','2.7')]+[mp.pi]
vals=[]
for theta in angles:
    j0=mp.quad(lambda t:P(t,theta),[0,mp.mpf('.8'),1])
    jv=mp.quad(lambda t:P(t,theta)*v(t),[0,mp.mpf('.8'),mp.mpf('.99'),1])
    assert j0>0 and jv>0
    checks+=2
    vals.append((j0,jv))
for (a,b),(c,d) in zip(vals,vals[1:]):
    assert a>c and b>d
    checks+=2

# Fourier identity from the positive boundary density.
for n in (1,2,3,7,19):
    for c in (0,mp.mpf('0.25'),1,2,7):
        # Exchange integrals with the Poisson Fourier transform, avoiding
        # numerical integration of the weakly singular angular kernel.
        q=mp.quad(lambda t:(1-t**n)*(1+c*v(t)),[0,mp.mpf('.5'),mp.mpf('.95'),1])
        exact=mp.mpf(n)/(n+1)*(1+c*(mp.digamma(n+2)+mp.euler-1))
        equal(q,exact,mp.mpf('2e-29'))

# Sample the sharp boundary coefficient without demanding asymptotics from
# finite tests: ratios approach pi as theta decreases.
ratios=[]
for theta in map(mp.mpf,('0.1','0.03','0.01','0.003')):
    jv=mp.quad(lambda t:P(t,theta)*v(t),[0,mp.mpf('.85'),mp.mpf('.98'),1])
    ratios.append(theta*jv)
assert all(x<y for x,y in zip(ratios,ratios[1:])); checks+=1
assert abs(ratios[-1]-mp.pi)<mp.mpf('0.09'); checks+=1
print(f'PASS {checks} finite checks; j_v(pi)={mp.nstr(Cpi,25)}; theta*j_v(theta)={mp.nstr(ratios[-1],16)}')
