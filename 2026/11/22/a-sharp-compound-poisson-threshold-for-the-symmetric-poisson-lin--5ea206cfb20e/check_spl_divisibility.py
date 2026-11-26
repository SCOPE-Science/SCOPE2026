"""Reproducibility checks for the symmetric Poisson--Lindley ID theorem.

Needs Python 3 and sympy. Exact algebra is used for every named identity
and rational witness; numerical examples are checks, not infinite proofs.
"""
from fractions import Fraction
from math import cos, pi, sqrt
import sympy as sp

r, z, theta = sp.symbols('r z theta', positive=True)
a = (1 + r)/r
A = sp.factor(a*(1-r**4)-4*r**2)
B = sp.factor(2*r*((1+r**2)-a*(1-r**2)))
D = (1-r*z)*(1-r/z)
S = a*(1-r**2)/D + r*sp.diff((1-r**2)/D, r)
assert sp.factor(S-(A + B*(z+1/z)/2)/D**2) == 0
P = 3*r**5+2*r**4+6*r**3-r-2
H = r**3+3*r**2-r-1
assert sp.factor(A+B+(r-1)**2*(r**3-r**2-r-1)/r) == 0
assert sp.factor(A-B+(r+1)**2*H/r) == 0
assert sp.factor(B*(1+r**2)+2*r*A-2*r*(1-r**2)**2) == 0
assert sp.factor(B*(1+r**2)-2*r*A-2*P) == 0
norm = theta**2/(theta**3+4*theta**2+6*theta+2)
q = 1/(1+theta)
Z = (theta+2)*(1+q)/(1-q)+2*q/(1-q)**2
assert sp.simplify(norm*Z-1)==0
# Exact brackets: uniqueness follows from Descartes' one positive sign change.
boundary_prefixes = [
    (P, 'crit', 67454183542439917437, 482487738319200658),
    (H, 'zero', 67513087056664607088, 481194304092015622),
]
for polynomial, label, r_prefix, theta_prefix in boundary_prefixes:
    lo = sp.Rational(r_prefix, 10**20)
    hi = sp.Rational(r_prefix+1, 10**20)
    assert polynomial.subs(r,lo)<0<polynomial.subs(r,hi)
    assert sp.Rational(theta_prefix, 10**18) < 1/hi-1
    assert 1/lo-1 < sp.Rational(theta_prefix+1, 10**18)
# In the nonzero, strictly positive characteristic-function phase,
# an exact rational specimen already has a negative 4th logarithmic harmonic.
R=sp.Rational(27,40)
T=sp.Rational(41,50)
AA=A.subs(r,R);BB=B.subs(r,R)
assert AA>BB>0
assert BB*(1+T*T)-2*T*AA>0
assert T**4-2*R**4>0
# Thus s>T and c4=r**4-s**4/2 < 0.
# At theta=1, the explicitly factored characteristic function is positive.
assert A.subs(r,sp.Rational(1,2))>abs(B.subs(r,sp.Rational(1,2)))
for Rf in (0.2, 0.5, 0.665, 0.6745, 0.675, 0.7):
    th=1/Rf-1
    c=th*th/(th**3+4*th**2+6*th+2)
    av=th+2
    af=float(A.subs(r,Rf));bf=float(B.subs(r,Rf))
    for t in (0.0, pi/3, pi):
        direct = c*(av + 2*sum((av+k)*Rf**k*cos(k*t) for k in range(1,450)))
        closed = c*(af+bf*cos(t))/(1-2*Rf*cos(t)+Rf**2)**2
        assert abs(direct-closed)<1e-10, (Rf,t,direct,closed)
print('Exact identities, normalization, polynomial brackets, rational witness and numeric checks: PASS')
for _, label, r_prefix, theta_prefix in boundary_prefixes:
    print(f'r_{label} = 0.{r_prefix:020d}...')
    print(f'theta_{label} = 0.{theta_prefix:018d}...')
