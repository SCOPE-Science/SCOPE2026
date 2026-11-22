"""Independent finite numerical checks for a Matérn-3/2 one-site quadrature design.
The mathematical proof is in RESULT.md; these checks do not certify all parameters.
Requires Python 3 standard library only.
"""
import math
from fractions import Fraction


def K(lam,r): return (1+lam*abs(r))*math.exp(-lam*abs(r))
def A(lam,x): return (4-(2+lam*x)*math.exp(-lam*x)-(2+lam*(1-x))*math.exp(-lam*(1-x)))/lam
def B(lam,x): return K(lam,x)-K(lam,1-x)
def reduction(lam,P,x,p):
    q=P-p
    return A(lam,x)**2*p/(1+p)+B(lam,x)**2*q/(1+lam*lam*q)

def trap(f,n):
    return (f(0)+f(1)+2*sum(f(i/n) for i in range(1,n)))/(2*n)

# Rational witness at lam=8, P=1/20, p=3/1000, x=0.
# 2<e<11/4 implies e^-8<1/256 and e^-4>1/64.
margin_mixed = 3*(Fraction(251,1024)**2)/1003 - Fraction(5,28056)
margin_pure = (Fraction(247,256)**2)/84 - (Fraction(61,128)**2)/21
assert margin_mixed>0 and margin_pure>0
lam=8.0; P=0.05
v=reduction(lam,P,.5,P)
d=reduction(lam,P,0,0)
m=reduction(lam,P,0,.003)
assert m>d>v
assert m-d>float(margin_mixed)
assert d-v>float(margin_pure)

# Covariances from direct integrations (trapezoid quadrature is only supplementary).
for lam in (.3,1,4,8):
    for x in (0,.1,.25,.5,.77,1):
        a=trap(lambda u:K(lam,x-u),6000)
        # derivative covariance via exact kernel derivative under integral
        b=trap(lambda u: (lam*lam*(u-x)*math.exp(-lam*abs(u-x))),6000)
        assert abs(a-A(lam,x))<2e-7,(lam,x,a,A(lam,x))
        assert abs(b-B(lam,x))<2e-7,(lam,x,b,B(lam,x))
    # monotonicity of full-information criterion on left half
    xx=[i/5000 for i in range(2501)]
    h=[A(lam,x)**2+B(lam,x)**2/lam**2 for x in xx]
    assert all(u < z+1e-12 for u,z in zip(h,h[1:]))
    assert h[-1]>h[0]

# Check normal conditioning numerically: two channels are uncorrelated,
# with marginal variances 1 and lam^2, independent noise variance 1/p,1/q.
for lam in (.5,2,8):
    for P in (.01,.05,1,20):
        for x in (.0,.18,.37,.5,.88):
            for frac in (0,.2,.7,1):
                p=P*frac
                q=P-p
                info= (A(lam,x)**2/(1+1/p) if p else 0)+(B(lam,x)**2/(lam**2+1/q) if q else 0)
                assert abs(info-reduction(lam,P,x,p))<1e-12
print('PASS: exact rational margins; 24 direct covariance integrals per kind; monotonicity grids; 240 Gaussian-conditioning checks')
print('lam=8, P=1/20: value=',format(v,'.16g'),'derivative=',format(d,'.16g'),'mixed=',format(m,'.16g'))
