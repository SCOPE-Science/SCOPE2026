"""Exact symbolic checks for sixth moments of the middle slice on six points.

Usage: python check_six_slice.py (requires sympy).
All moment identities are verified as polynomial identities, not sampled numerically.
"""
from itertools import combinations
from fractions import Fraction
import sympy as sp

x = sp.symbols('x0:5')
a = list(x) + [-sum(x)]
p = {j: sum(z**j for z in a) for j in (2, 3, 4, 6)}
S2 = sum((sum(a[i] for i in T))**2 for T in combinations(range(6), 3))
S6 = sum((sum(a[i] for i in T))**6 for T in combinations(range(6), 3))
assert sp.Poly(sp.expand(S2-6*p[2]),x).is_zero
assert sp.Poly(sp.expand(S6-(15*p[2]**3-60*p[2]*p[4]-20*p[3]**2+66*p[6])),x).is_zero
print('EXACT_TWENTY_TRIPLE_MOMENT_IDENTITIES_OK')

u,v,D,Q = sp.symbols('u v D Q',real=True)

def H(vals):
    q = {j: sum(z**j for z in vals) for j in (2, 3, 4, 6)}
    return 59*q[2]*q[4]+20*q[3]**2-66*q[6]-8*q[2]**3

exp = {
 (1,1,4): sp.Rational(5,8)*D**6 + sp.Rational(111,32)*D**4*Q**2 + sp.Rational(675,128)*D**2*Q**4 + sp.Rational(729,512)*Q**6,
 (2,2,2): sp.Rational(21,8)*D**6 + sp.Rational(351,8)*D**4*Q**2 + sp.Rational(243,8)*D**2*Q**4 + sp.Rational(729,8)*Q**6,
}
for mult, form in exp.items():
    m,n,k=mult; w=-(m*u+n*v)/k
    F=H([u]*m+[v]*n+[w]*k)
    assert sp.expand(F.subs({u:(Q+D)/2,v:(Q-D)/2})-form)==0
    print('THREE_LEVEL_POSITIVITY_CASE_OK',mult)

form=sp.Rational(8,27)*(u-v)**2*(41*u**4+153*u**3*v+411*u**2*v**2+499*u*v**3+300*v**4)
assert sp.expand(H([u]+[v]*2+[-(u+2*v)/3]*3)-form)==0
z=sp.symbols('z',real=True)
quartic=41*u**4+153*u**3*v+411*u**2*v**2+499*u*v**3+300*v**4
assert sp.expand(quartic.subs(u,z-v)-(41*z**4-11*z**3*v+198*z**2*v**2-28*z*v**3+100*v**4))==0
# Complete positivity certificate via 2ab <= a^2+b^2:
# quartic >= 71/2 z^4 + 357/2 z^2 v^2 + 86 v^4 >0 outside zero.
assert sp.expand((41*z**4-11*z**3*v+198*z**2*v**2-28*z*v**3+100*v**4) - (sp.Rational(71,2)*z**4+sp.Rational(357,2)*z**2*v**2+86*v**4) - (sp.Rational(11,2)*z**2*(z-v)**2+14*v**2*(z-v)**2)) == 0
print('ASYMMETRIC_QUARTIC_SQUARE_CERTIFICATE_OK')

for m,n in [(1,5),(2,4),(3,3)]:
    F=sp.factor(H([u]*m+[-sp.Rational(m,n)*u]*n))
    expect={(1,5):sp.Rational(31104,3125)*u**6,(2,4):sp.Rational(729,8)*u**6,(3,3):sp.Integer(0)}[(m,n)]
    assert sp.expand(F-expect)==0
print('TWO_LEVEL_POSITIVITY_CASES_OK')

for vector, expected in [([1,1,1,-1,-1,-1], sp.Rational(1025,81)),([5,-1,-1,-1,-1,-1],sp.Integer(1))]:
    vals=[sum(vector[i] for i in T) for T in combinations(range(6),3)]
    E2=sp.Rational(sum(z*z for z in vals),20)
    E6=sp.Rational(sum(z**6 for z in vals),20)
    assert sp.cancel(E6/E2**3-expected)==0
print('EXACT_ENDPOINTS_OK')
print('ALL_SIX_SLICE_EXACT_CHECKS_PASSED')
