#!/usr/bin/env python3
"""Independent finite arithmetic checks of the displayed cubature formulas.
The theorem's infinite-dimensional quantifiers rely on the written proof.
"""
from fractions import Fraction as F
from math import sin, cos, tan, atan, sqrt

checks = 0
def check(ok, why=''):
    global checks
    assert ok, why
    checks += 1

# Rigorous alternating-Taylor enclosures, with rational endpoints.
half = F(1,2); quarter=F(1,4)
sin_half_lo = half - half**3/F(6)
sin_half_hi = sin_half_lo + half**5/F(120)
sin_q_lo = quarter-quarter**3/F(6)
sin_q_hi = sin_q_lo+quarter**5/F(120)
cos_q_lo = 1-quarter**2/F(2)
cos_q_hi = cos_q_lo+quarter**4/F(24)
ratio_lo = (F(1,2)+sin_half_lo)/(F(1,2)-sin_half_lo)
ratio_hi = (F(1,2)+sin_half_hi)/(F(1,2)-sin_half_hi)
cot2_lo = (cos_q_lo/sin_q_hi)**2
cot2_hi = (cos_q_hi/sin_q_lo)**2
for c in [ratio_lo>=47,ratio_hi<50,cot2_lo>15,cot2_hi<F(31,2),
          3*cot2_hi<ratio_lo,4*cot2_lo>ratio_hi]: check(c)

p=.5-sin(.5);q=1-p
for d in range(1,8):
    lam0=q**d; lam1=q**(d-1)*p
    check(0<p<q<1)
    for r in range(1,min(d,3)+1):
        theta=atan(sqrt(r*p/q))
        check(0<theta<=.25, f'node outside cube r={r}')
        wt=lam1/(2*sin(theta)**2)
        check(wt>0)
        # Each pair of site vectors has coefficients (cos theta, +/- sin theta)
        # on the vacuum and the single-excitation j, and no other entries.
        Q00=0.; Q0j=[0.]*r; Qjj=[0.]*r; off=[[0.]*r for _ in range(r)]
        for j in range(r):
            for sign in [-1,1]:
                v0=cos(theta); vj=sign*sin(theta)
                Q00+=wt*v0*v0
                Q0j[j]+=wt*v0*vj
                Qjj[j]+=wt*vj*vj
        scale=max(1,abs(lam0))
        check(abs(Q00-lam0)<1e-12*scale, ('Q00',d,r))
        for j in range(r):
            check(abs(Q0j[j])<1e-12)
            check(abs(Qjj[j]-lam1)<1e-12)
        check(abs(r*lam1*(cos(theta)/sin(theta))**2-lam0)<1e-12)
    if d>=4:
        check(4*lam1*(cos(.25)/sin(.25))**2>lam0)
# As a concrete non-adaptive error comparison, the 2-node rule
# on any d>=2 has exact trace-norm residual 1-q^d-q^(d-1)*p.
for d in range(2,30):
    tail=1-q**d-q**(d-1)*p
    check(tail>=0)
    check(abs(tail-(1-q**(d-1)))<2e-14)

print('VERIFY_OK',checks)
print('Taylor q/p interval:',float(ratio_lo),float(ratio_hi))
print('Taylor cot(1/4)^2 interval:',float(cot2_lo),float(cot2_hi))
print('Point count threshold: r<=3 feasible with 2r sites; r>=4 violates cone')
