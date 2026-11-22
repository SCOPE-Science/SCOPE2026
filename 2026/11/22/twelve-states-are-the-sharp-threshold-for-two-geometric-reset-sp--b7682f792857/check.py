"""Standalone exact arithmetic checks for the stated minimal two-extrema theorem.

Requires Python 3 and SymPy. The universal bound is proved analytically in RESULT.md;
these computations verify its sharp rational witness and independent finite examples.
"""
from fractions import Fraction
from itertools import product
import sympy as sp

s, t, u = sp.symbols('s t u')
p = [sp.Rational(x, 100) for x in (95, 10, 80, 30, 1, 40, 75, 45, 40, 10)]
a, z = 11, 5

def path_det(lo, hi):
    if hi < lo:
        return sp.Integer(1)
    d0 = d1 = sp.Integer(1)
    for j in range(lo+1, hi+1):
        weight = p[j-2] * (1-p[j-1])
        d0, d1 = d1, sp.expand(d1-weight*t*d0)
    return sp.factor(d1)

L = 1-sp.Rational(457,400)*t+sp.Rational(423,2000)*t*t
R = 1-sp.Rational(287,200)*t+sp.Rational(1197,2500)*t*t
assert sp.cancel(path_det(6,10)-L)==0
assert sp.cancel(path_det(1,4)-R)==0
C = sp.prod(1-p[i-1] for i in range(1,z+1))/sp.prod(p[i-1] for i in range(z,a))
assert C == sp.Rational(231,2)
Q = sp.cancel(231*L.subs(t,s*s)/(231*L.subs(t,s*s)+2*s*R.subs(t,s*s)))
N = 1012662*t**4-13375845*t**3+33989875*t*t-31625000*t+10000000
qprime = sp.factor(sp.diff(Q,s))
# The positive denominator removes any possible extraneous critical values.
assert sp.factor(qprime/(-N.subs(t,s*s))) == 4620/(9576*s**5 + 488565*s**4-28700*s**3-2639175*s**2 +20000*s+2310000)**2
for x,expected in [(sp.Rational(4,5),1),(sp.Rational(9,10),-1),
                   (sp.Rational(99,100),-1),(sp.Rational(999,1000),1)]:
    assert sp.sign(N.subs(t,x)) == expected
change = sp.expand(sp.cancel((1+u)**4*N.subs(t,u/(1+u))))
assert change == 1692*u**4-271095*u**3-885125*u**2+8375000*u+10000000
assert [sp.sign(v) for v in sp.Poly(change,u).all_coeffs()] == [1,-1,-1,1,1]

# Directly compute discounted endpoint absorption using an independent
# transient-matrix inverse, at five rational survival parameters.
P = sp.zeros(a-1)
for i in range(a-1):
    if i: P[i,i-1] = 1-p[i]
    if i<a-2: P[i,i+1] = p[i]
for survival in [sp.Rational(1,10),sp.Rational(1,3),sp.Rational(1,2),
                 sp.Rational(4,5),sp.Rational(99,100),sp.Integer(1)]:
    M = sp.eye(a-1)-survival*P
    sol0 = M.inv()[:,0] * (survival*(1-p[0]))
    sola = M.inv()[:,a-2] * (survival*p[-1])
    actual = sp.cancel(sol0[z-1]/(sol0[z-1]+sola[z-1]))
    assert sp.cancel(actual-Q.subs(s,survival))==0

# Spectral-factorization sanity check for shorter paths, with rational rates.
for a_small in range(3,11):
    probs=[sp.Rational((7*i+3) % 17+1,19) for i in range(1,a_small)]
    for lo in range(1,a_small):
        for hi in range(lo,a_small):
            M=sp.zeros(hi-lo+1)
            for i in range(lo,hi+1):
                if i>lo:M[i-lo,i-lo-1]=1-probs[i-1]
                if i<hi:M[i-lo,i-lo+1]=probs[i-1]
            det=sp.factor((sp.eye(hi-lo+1)-s*M).det())
            assert sp.cancel(det.subs(s,-s)-det)==0
            assert sp.Poly(det,s).degree()<=2*((hi-lo+1)//2)
print('PASS: exact sharpness polynomial, rational sign brackets, six resolvent checks and finite path symmetry checks')
