"""Exact symbolic checks for the arclength-perimeter centroid-capture theorem.

Requirements: Python 3, SymPy. Run: python CHECK.py
The symbolic equalities check the algebraic integral and polynomial identity;
the geometric half-circle counting principle is established in RESULT.md.
"""
import sympy as s

u = s.symbols('u', real=True)
a, b, c = s.symbols('a b c', positive=True)
ln2 = s.log(2)
S = a + b + c

# From the ray-intersection calculation on the oriented edge AB.
ell_left = c*(1-u) + a*(1-u)/(2-3*u)
ell_right = c*(1-u) + a + b*(2*u-1)/(3*u-1)

I = s.simplify(s.integrate(s.expand(ell_left**2),(u,0,s.Rational(1,2)))
             + s.integrate(s.expand(ell_right**2),(u,s.Rational(1,2),1)))
I_expected = ((s.Rational(11,18)+4*ln2/27)*(a*a+a*c)
              +(s.Rational(2,3)-4*ln2/9)*a*b
              +(s.Rational(5,18)-8*ln2/27)*(b*b+b*c)
              +c*c/3)
assert s.simplify(I-I_expected)==0, 'side integral mismatch'
print('PASS: piecewise boundary integral equals closed expression.')

F = sum(z*I.subs({a:x,b:y,c:z}, simultaneous=True)
        for x,y,z in ((a,b,c),(b,c,a),(c,a,b)))
P_from_gaps = s.simplify(1-3*F/S**3)
symmetric_monomials = sum(x*x*y for x in (a,b,c) for y in (a,b,c) if x != y)
kappa = (3+4*ln2)/9
eta = s.Rational(8,3)*ln2 - 1
P_direct = (kappa*symmetric_monomials+4*ln2*a*b*c)/S**3
assert s.simplify(P_from_gaps-P_direct)==0, 'main probability mismatch'
print('PASS: all-side integral gives symmetric cubic probability.')

p,q,r = s.symbols('p q r', positive=True)
Phi = kappa*(p*q+p*r+q*r)+eta*p*q*r
assert s.simplify((p-q)*(s.diff(Phi,p)-s.diff(Phi,q))
                  +(p-q)**2*(kappa+eta*r))==0
assert eta>0
p_eq = s.simplify(Phi.subs({p:s.Rational(1,3),q:s.Rational(1,3),r:s.Rational(1,3)}))
p_needle = s.simplify(Phi.subs({p:s.Rational(1,2),q:s.Rational(1,2),r:0}))
assert s.simplify(p_eq-(2*(3+10*ln2)/81))==0
assert s.simplify(p_needle-(3+4*ln2)/36)==0
print('PASS: strict Schur derivative and exact extreme values.')

# Coefficients of distinct-side and 2+1-side patterns, independently
# recoverable by conditioning on edge-label multiplicities.
C21 = s.simplify(kappa/3)
C111 = s.Rational(2,3)*ln2
assert s.simplify((3*C21*sum(x*x*(1-x) for x in (p,q,r))
     +6*C111*p*q*r-Phi).subs(r,1-p-q))==0
print('PASS: multinomial side-pattern decomposition under p+q+r=1.')
print('PASS: all exact identities; independent geometric derivation in RESULT.md.')
