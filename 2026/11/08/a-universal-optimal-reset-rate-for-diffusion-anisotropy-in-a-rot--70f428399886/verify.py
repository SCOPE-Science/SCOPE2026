"""Standalone symbolic and independent renewal-moment checks for Poisson orientation resetting.

Requires Python 3 and SymPy.  Execute: python verify.py
"""
import sympy as s

r, alpha, D, gamma = s.symbols('r alpha D gamma', positive=True)
b = alpha/D
q1 = r/(r+alpha)
q2 = r/(r+4*alpha)

# Component of the displacement along the reset-angle direction is
# (gamma/b) sin(Theta); along drift, it is (gamma/b)(1-cos(Theta)).
# A separate Brownian innovation has mean zero and conditional variance
# rate 2D R(aI - c c^T/b) R^T.
noise_perp = -D*gamma**2/b*(1+q2)
noise_parallel = -D*gamma**2/b*(1-q2)
endpoint_perp = r*(gamma/b)**2*(1-q2)/2
kappa = alpha*r/(r+alpha)
endpoint_parallel = r*(gamma/b)**2*(
    s.Rational(3,2)-2*q1+q2/2
    -2*kappa*(1/r-r/(r+alpha)**2)+2*kappa**2/r**2)

perp_correction = -4*D**2*gamma**2/(r+4*alpha)
parallel_correction = -2*alpha*D**2*gamma**2*(
    2*alpha**2+3*alpha*r+4*r**2)/((alpha+r)**3*(4*alpha+r))
checks = [
    s.simplify(noise_perp+endpoint_perp-perp_correction),
    s.simplify(noise_parallel+endpoint_parallel-parallel_correction),
]
gap = s.factor(parallel_correction-perp_correction)
expected_gap = 2*D**2*gamma**2*r*(3*alpha**2+2*alpha*r+2*r**2)/((alpha+r)**3*(4*alpha+r))
checks.append(s.simplify(gap-expected_gap))
checks.append(s.simplify(s.diff(perp_correction, r)-4*D**2*gamma**2/(r+4*alpha)**2))
checks.append(s.simplify(s.diff(parallel_correction, r)-2*alpha*D**2*gamma**2*(
    14*alpha**3+21*alpha*r**2+8*r**3)/((alpha+r)**4*(4*alpha+r)**2)))
checks.append(s.simplify(s.diff(gap,r)-2*D**2*gamma**2*(2*alpha-r)*(
    6*alpha**3-alpha**2*r+4*alpha*r**2+2*r**3)/((alpha+r)**4*(4*alpha+r)**2)))
checks.append(s.simplify(gap.subs(r,2*alpha)-10*D**2*gamma**2/(27*alpha)))
checks.append(s.limit(gap,r,0)); checks.append(s.limit(gap,r,s.oo))
assert all(v==0 for v in checks), checks

# Independent numerical evaluation of the renewal reward moment identities.
import math
for a0 in [0.17, 1., 4.3]:
 for r0 in [0.02, 0.5, 2*a0, 12.]:
  D0=1.31; gam0=0.23; b0=a0/D0
  # Geometric endpoint and integrated transverse innovation expectations.
  q10=r0/(r0+a0); q20=r0/(r0+4*a0)
  mean_time=1/r0
  var_time=2/r0**2
  mean_tm=1/r0-r0/(r0+a0)**2
  kap=a0*r0/(r0+a0)
  direct_perp=2*D0*2.0-D0*gam0**2/b0*(1+q20)+r0*(gam0/b0)**2*(1-q20)/2
  direct_par=2*D0*2.0-D0*gam0**2/b0*(1-q20)+r0*(gam0/b0)**2*(1.5-2*q10+q20/2-2*kap*mean_tm+kap**2*var_time)
  formula_perp=2*D0*2.0-float(perp_correction.subs({r:r0,alpha:a0,D:D0,gamma:gam0})*-1)
  formula_par=2*D0*2.0+float(parallel_correction.subs({r:r0,alpha:a0,D:D0,gamma:gam0}))
  assert abs(direct_perp-formula_perp)<1e-10
  assert abs(direct_par-formula_par)<1e-10
print('PASS: nine symbolic identities and 12 independently evaluated renewal-moment cases')
