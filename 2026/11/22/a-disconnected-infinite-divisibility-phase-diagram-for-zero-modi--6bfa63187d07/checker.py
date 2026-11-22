#!/usr/bin/env python3
"""Independent exact algebraic checks for the zero-modified Poisson--Lindley phase boundary.
Requires Python 3 and SymPy; no network or external data.
"""
from fractions import Fraction
import sympy as S

def check(condition, message):
    if condition is not True and condition != S.true:
        raise AssertionError(message)

a,z,h = S.symbols('a z h', positive=True)
t=a+1
fzero=a*a*(a+2)/t**3
base=(a*a/t)*(t+1-z)/(t-z)**2
P=S.factor(h+(1-h)*base)
threshold=-a*a*(2*a+3)/((a+2)**2*(2*a+1))
minimum=-a*a*(a+2)/(a*a+3*a+1)
check(S.simplify(P.subs(z,1)-1)==0,'mass normalization')
check(S.simplify(P.subs(z,0)-(h+(1-h)*fzero))==0,'zero mass')
check(S.simplify(threshold-minimum - a*a*(a+1)**3*(2*a+5)/((a+2)**2*(2*a+1)*(a*a+3*a+1)))==0,'threshold within parameter interval')
check(S.simplify((P*(t-z)**2).subs({h:threshold,z:-t}))==0,'critical pgf zero')
check(S.simplify((P*(t-z)**2).subs({h:minimum,z:0}))==0,'truncated pgf zero')

# The zero-truncated endpoint is a one-unit shifted compound-Poisson law.
u=(a+2)/(t*(a+3))
pone=(1-minimum)*a*a*(a+3)/t**4
H=pone*(1-u*z)/(1-z/t)**2
check(S.simplify(P.subs(h,minimum)-z*H)==0,'zero-truncated shifted generating function')
check(S.simplify(H.subs(z,1)-1)==0,'shifted pgf normalization')
for theta in [S.Rational(1,3),S.Rational(1),S.Rational(2),S.Rational(5)]:
    tt=theta+1
    uu=(theta+2)/(tt*(theta+3))
    for n in range(1,31):
        check((2*tt**(-n)-uu**n)/n>0,'shifted endpoint compound-Poisson intensities')

# Coefficients recovered directly from probabilities, independently of root expansion.
def masses(theta, pi, nmax):
    t=theta+1
    p0=pi+(1-pi)*theta**2*(theta+2)/t**3
    return [p0]+[(1-pi)*theta**2*(k+theta+2)/t**(k+3) for k in range(1,nmax+1)]

def logcoeff(p):
    assert p[0]!=0
    out=[]
    for k in range(1,len(p)):
        b=k*p[k]-sum(j*out[j-1]*p[k-j] for j in range(1,k))
        out.append(b/(k*p[0]))
    return out

cases=[(S.Rational(1),S.Rational(-1,3)),
       (S.Rational(1),S.Rational(-1,5)),
       (S.Rational(1),S.Rational(-5,27)),
       (S.Rational(1),S.Rational(0)),
       (S.Rational(1),S.Rational(1,2)),
       (S.Rational(2),threshold.subs(a,2)),
       (S.Rational(2),S.Rational(0)),
       (S.Rational(3),S.Rational(2,3))]
assert logcoeff(masses(S.Rational(1),S.Rational(-1,3),2))[1]==S.Rational(-3,4)
for theta,pi in cases:
    p=masses(theta,pi,32)
    coeff=logcoeff(p)
    check(sum(p[:3])<=1,'valid probabilities')
    assert all(x>0 for x in coeff) if pi>=threshold.subs(a,theta) else any(x<0 for x in coeff)
    # Symbolic differentiation reproduces the recurrence at low degrees.
    g=P.subs({a:theta,h:pi})
    ex=S.series(S.log(g/g.subs(z,0)),z,0,6).removeO()
    for k in range(1,6):
        check(S.simplify(ex.coeff(z,k)-coeff[k-1])==0,'log series mismatch')

# The critical boundary admits exact intensities from a negative real zero.
for n in range(1,75):
    expected=(2*S.Rational(1,2)**n-(-S.Rational(1,2))**n-S.Rational(5,14)**n)/n
    check(expected>0,'boundary positivity')
    if n<33:
        check(logcoeff(masses(S.Rational(1),S.Rational(-5,27),n))[n-1]==expected,'boundary canonical intensity')

# Below the boundary, the first few coefficients can remain positive.
pi=S.Rational(-5,27)-S.Rational(1,10000)
lc=logcoeff(masses(S.Rational(1),pi,12))
check(all(v>0 for v in lc[:10]),'late-onset obstruction')
print('PASS: normalization, admissible interval, critical roots, exact shifted-endpoint representation,')
print('      logarithmic recurrence, examples on both sides, 74 boundary intensities and delayed sign obstruction.')
print('threshold at theta=1:',threshold.subs(a,1),'zero probability:',P.subs({a:1,h:threshold.subs(a,1),z:0}))
print('at theta=1, pi=-1/3: second canonical coefficient:',logcoeff(masses(S.Rational(1),S.Rational(-1,3),2))[1])
