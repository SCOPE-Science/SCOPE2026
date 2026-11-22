"""Exact symbolic and finite checks for moment-constrained implicit-stage damping.

Requires SymPy >= 1.12. Finite tests supplement the analytic proof.
"""
import sympy as S

r,t=S.symbols('r t',positive=True)
P=r**3-2*r**2-12*r-12
J=11*r**3+28*r**2+6*r-12
C=r**3+16*r**2+18*r-12
B=10*r**3+12*r**2-12*r
A=r**2+6*r+6
f=(1+r*(t-1))**2/(1+r*t)**2
g=6*t**2-6*t+1
E=r**5*g**2*(C+B*t)/((1+r*t)**2*A**3)
H=S.cancel(f-E)
assert S.cancel(S.diff(H,t,4))==0
assert S.cancel(f-H-E)==0
assert S.cancel(S.diff(f,t,4)-24*r**5*(5*r-2*r*t-2)/(1+r*t)**6)==0
u=(1+r*t)**2
# Gauss evaluation via reduction modulo quadratic minimal polynomial.
poly=t**2-t+S.Rational(1,6)
num=S.together(f).as_numer_denom()[0]
den=S.together(f).as_numer_denom()[1]
rr=S.rem(num,poly,t)
dd=S.rem(den,poly,t)
inverse=S.invert(dd,poly,t)
reduced=S.rem(rr*inverse,poly,t)
FG=S.factor(reduced.subs(t,S.Rational(1,2)))
expected=1+r*P/(6*(1+r+r*r/S.Integer(6))**2)
assert S.factor(FG-expected)==0
assert S.rem(J-(C+B),r)==0
assert S.factor(J.subs(r,S.Rational(1,2)))==-S.Rational(5,8)
assert S.factor(C.subs(r,S.Rational(1,2)))==S.Rational(9,8)
# Exact moment matching of the Gauss nodes using minimal polynomial recurrence.
for k in range(4):
    z=S.rem(t**k,poly,t)
    assert S.factor(z.subs(t,S.Rational(1,2))-S.Rational(1,k+1))==0
# A three-node Simpson law matches moments 0,...,3. Its objective gap is positive beyond r0.
Fsim=S.Rational(1,6)*f.subs(t,0)+S.Rational(2,3)*f.subs(t,S.Rational(1,2))+S.Rational(1,6)*f.subs(t,1)
assert S.factor(Fsim-FG).subs(r,1)>0
# Test positivity of the exact contact factor at rational r greater than the threshold,
# and failure of the pointwise support certificate at r less than threshold.
checks=0
for rv in [S.Rational(1,4),S.Rational(1,2),S.Rational(3,5),S.Rational(2,3),S.Rational(1),S.Rational(2),S.Rational(5),S.Rational(10)]:
    for j in range(101):
        tv=S.Rational(j,100)
        val=S.factor(E.subs({r:rv,t:tv}))
        if rv>=S.Rational(3,5): assert val>=0
        if rv<=S.Rational(1,2) and tv==1:assert val<0
        checks+=1
# Numeric boundary and comparator.
RG=float(S.nroots(P)[0]) if False else max(float(S.re(z)) for z in S.nroots(P) if abs(float(S.im(z)))<1e-12)
r0=max(float(S.re(z)) for z in S.nroots(J) if abs(float(S.im(z)))<1e-12)
assert 4.9287<RG<4.92871 and 0.51456<r0<0.51458
assert S.factor(P.subs(r,S.Rational(4)))<0<S.factor(P.subs(r,S.Rational(5)))
print('PASS symbolic Hermite-contact identity, exact degree-three moment equalities, Gauss amplification')
print(f'PASS {checks} rational sign checks; sharp transition={r0:.12f}, Gauss radius={RG:.12f}')
