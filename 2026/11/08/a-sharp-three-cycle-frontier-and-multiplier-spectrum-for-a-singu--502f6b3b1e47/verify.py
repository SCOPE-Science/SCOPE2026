#!/usr/bin/env python3
"""Exact algebraic identities for the singular logistic three-cycle theorem.

Requires SymPy. The analytical root-continuation and Sharkovskii arguments
are in RESULT.md and are not replaced by these finite checks.
"""
import sympy as s

z, A, t, d = s.symbols('z A t d')
q1 = z*z - A*z + A
q2 = s.expand(q1*q1 - A*z*q1 + A*z*z)
p = (3*z**6 - 12*A*z**5 + (15*A**2+9*A)*z**4
     - (6*A**3+20*A**2)*z**3 + (11*A**3+6*A**2)*z**2
     - 6*A**3*z + A**3)
f = z-A+A/z
f2 = s.cancel(f.subs(z, f))
f3 = s.cancel(f.subs(z, f2))
assert s.cancel(f3-z+A*(z-1)*p/(z*q1*q2)) == 0
assert s.factor(s.discriminant(p,z)) == 5184*A**15*(A-3)**3*(A*A-3*A+3)**2
assert s.factor(p.subs(A,3)) == 3*(z**3-6*z*z+9*z-3)**2
assert s.discriminant(z**3-6*z*z+9*z-3,z)==81
assert s.resultant(z**3-6*z*z+9*z-3,-z*z+3*z-1,z)==-1
assert s.factor(p.subs(A,4))==(z**3-10*z*z+24*z-8)*(3*z**3-18*z*z+24*z-8)

def r(v):
    return s.rem(s.expand(v),t*t-A*(A-3),t)

cp = z**3-(2*A+t)*z*z+A*(A+t)*z-A*(A+t)/3
cm = z**3-(2*A-t)*z*z+A*(A-t)*z-A*(A-t)/3
assert s.expand(r(p-3*cp*cm)) == 0
for sign,c in ((1,cp),(-1,cm)):
    R=(z**3-3*A*z*z+(A*A-sign*A*t+3*A)*z-A*A+sign*A*t)
    cimage=(q1**3-(2*A+sign*t)*q1*q1*z
           +A*(A+sign*t)*q1*z*z-A*(A+sign*t)*z**3/3)
    assert s.expand(r(cimage-c*R)) == 0
    sumr=2*A+sign*t
    ur=A*(A+sign*t)
    vr=ur/3
    multiplier=(vr**2-A*(ur**2-2*sumr*vr)+A*A*(sumr**2-2*ur)-A**3)/vr**2
    expected=1+2*(A-3)**2-sign*2*A*t
    numerator=s.together(multiplier-expected).as_numer_denom()[0]
    assert s.expand(r(numerator)) == 0

assert s.factor((1+d*d)**2-(3+d)**3*d) == -(9*d**3+25*d*d+27*d-1)
for cub,intervals in ((z**3-10*z*z+24*z-8,[(0,1),(3,4),(6,7)]),
                      (3*z**3-18*z*z+24*z-8,[(0,1),(1,2),(4,5)])):
    for lo,hi in intervals:
        assert cub.subs(z,lo)*cub.subs(z,hi)<0
for aa in (s.Rational(301,100),s.Rational(31,10),s.Rational(7,2),s.Rational(399,100)):
    tt=s.sqrt(aa*(aa-3))
    for sign in (1,-1):
        cubic=(cp if sign==1 else cm).subs({A:aa,t:tt})
        roots=sorted([float(s.re(v)) for v in s.nroots(cubic,maxsteps=300)])
        assert len(roots)==3 and min(roots)>0 and len(set(roots))==3
        observed=1.0
        for y in roots:
            observed*=1-float(aa)/y**2
        expected=float(1+2*(aa-3)**2-sign*2*aa*tt)
        assert abs(observed-expected)<1e-8,(aa,sign,observed,expected)
print('PASS: exact iterate, discriminant, orbit-factor/invariance, multiplier, onset, and flip identities; root brackets and numerical tests')
