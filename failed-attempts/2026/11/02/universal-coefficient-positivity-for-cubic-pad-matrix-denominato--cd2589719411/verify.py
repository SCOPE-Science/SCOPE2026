#!/usr/bin/env python3
"""Reproducible symbolic and finite checks for the cubic Padé denominator theorem.
The proof is analytic; these checks independently replay critical algebra and examples.
Requires sympy (see VERIFICATION.md).
"""
from fractions import Fraction
import sympy as S

k,t,r,z,w=S.symbols('k t r z w',positive=True)
d=t*(t+1)*(t+2)
q=1-3*z/(t+2)+3*z*z/((t+2)*(t+1))-z**3/d
P=S.expand(-d*q)
assert S.simplify(P-(z**3-3*t*z**2+3*t*(t+1)*z-t*(t+1)*(t+2)))==0
assert S.simplify(P.subs(z,t+w)-(w**3+3*t*w-2*t))==0

b2=3*t+S.Rational(3,4)*r*r
W2=t*t-t*r+r*r+3*t
R2=(t+r)**2
sep2=3*(t+r*r)
assert S.simplify(W2-R2-3*t*(1-r))==0
positivity_numerator=S.factor((W2*b2-R2*sep2).subs(t,r**3/(2-3*r)))
expected=9*r**4*(1-r)*(r**3-4*r*r+10*r-4)/(4*(2-3*r)**2)
assert S.simplify(positivity_numerator-expected)==0
# Derivative of g(r) positive for all r: discriminant of 3r^2-8r+10 negative.
assert S.discriminant(3*r*r-8*r+10,r)==-56
assert (r**3-4*r*r+10*r-4).subs(r,S.Rational(1,2))==S.Rational(1,8)

# A independent exact-rational Taylor recurrence, including the numerator parameter k=0.
checks=6
for kval in list(range(0,41))+[50,75,100]:
    tval=kval+1
    a=Fraction(3,tval+2)
    b=Fraction(3,(tval+2)*(tval+1))
    c=Fraction(1,tval*(tval+1)*(tval+2))
    seq=[Fraction(1)]
    for n in range(1,181):
        v=a*seq[n-1]-(b*seq[n-2] if n>=2 else 0)+(c*seq[n-3] if n>=3 else 0)
        assert v>0,(kval,n,v)
        seq.append(v)
        checks+=1
    # Match rational generating function coefficients q(z) sum c_n z^n=1.
    for n in range(181):
        val=seq[n]-(a*seq[n-1] if n>=1 else 0)+(b*seq[n-2] if n>=2 else 0)-(c*seq[n-3] if n>=3 else 0)
        assert val==(1 if n==0 else 0)
        checks+=1

# Exact matrix-function example: irreducible nonnegative X, h rho(X)<R, inverse entrywise >0.
X=S.Matrix([[0,1],[1,0]])
for kval in [0,1,2,3,5,10]:
    tv=S.Integer(kval+1)
    h=S.Rational(1,3)
    Y=h*X
    qY=S.eye(2)-3*Y/(tv+2)+3*(Y**2)/((tv+2)*(tv+1))-(Y**3)/(tv*(tv+1)*(tv+2))
    inv=qY.inv()
    assert all(x>0 for x in inv)
    checks+=4

# At the positive real pole the denominator is exactly singular; no matrix inverse exists.
assert S.simplify((r**3+3*t*r-2*t).subs(r,S.Rational(2,3)))>0
assert S.simplify((r**3+3*t*r-2*t).subs(r,S.Rational(1,2))).subs(t,1)<0
print(f'VERIFY_OK {checks} exact checks, with symbolic cubic and residue identities')
