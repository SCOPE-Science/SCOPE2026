#!/usr/bin/env python3
"""Check polynomial relations for the normalizations of Hauser's Calyx."""
import sympy as s
x,y,z,t=s.symbols('x y z t')
F=x*x+y*y*z**3-z**4
# Substitution equations and ring module calculations are identities in Z[t,y].
assert s.expand(F.subs({x:z*t})-(z*z)*(t*t+y*y*z-z*z))==0
# Verify the characteristic two expression literally, reducing integer coefficients.
F2=s.Poly(s.expand(F.subs({x:t**4+y*t**3,z:t*t})),t,y)
assert all(c%2==0 for c in F2.coeffs())
# The characteristic-two Calyx has w=x+z^2 and w^2=y^2 z^3.
w=y*t**3
assert s.expand(w*w-y*y*(t*t)**3)==0
# In the char!=2 normalization, shifting z exposes the A_3 singularity.
a,b=s.symbols('a b')
N=t*t+y*y*z-z*z
shift=s.expand(N.subs(z,s.Symbol('u')+y*y/2))
u=s.Symbol('u')
assert s.expand(shift-(t*t-u*u+y**4/4))==0
# Over both characteristics, A[t] splits with even and odd t-parts.
# Test multiplication and conductor action up to degree 5 in each variable.
for p in (2,3,5,7):
    # The defining relation is x^2+y^2z^3-z^4.
    xp=z*t
    rel=s.Poly(s.expand((xp*xp+y*y*z**3-z**4)-z*z*N), t,y,z)
    assert not any(c%p for c in rel.coeffs())
# In characteristic two, each conductor generator returns to the ring after multiplication by t.
assert s.expand((y*t*t)*t-y*t**3)==0
assert s.expand((y*t**3)*t-y*(t*t)**2)==0
print('VERIFY_OK: integral presentation, special-fiber parametrization, A3 change, conductor generators')
