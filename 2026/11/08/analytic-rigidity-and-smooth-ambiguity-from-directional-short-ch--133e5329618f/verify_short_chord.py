"""Independent numerical checks for directional short-chord inverse geometry."""
import numpy as np
from scipy.integrate import quad
from math import pi, sqrt, exp

# For an ellipse x^2/a^2+y^2/b^2 <=1, a vertical chord at x=p
# has length 2b sqrt(1-p^2/a^2). The two short-chord offset intervals
# have the exact total length below.
def ellipse_exact(a,b,t):
    return 2*a*(1-sqrt(1-t*t/(4*b*b)))
for a,b in [(1.,1.), (2.,1.), (1.6,2.3)]:
    target=a/(4*b*b)
    for t in [0.2*b, 0.1*b, 0.025*b, 0.01*b]:
        exact=ellipse_exact(a,b,t)/t**2
        assert abs(exact/target-1) < 0.003

# A real analytic strictly convex body with support
# h(theta)=2+0.12 cos(2 theta)+0.07 sin(3 theta).
# The radius function is h+h''=2-0.36 cos(2theta)-0.56 sin(3theta).
theta=np.linspace(0,pi,2049,endpoint=False)
rho=2-0.36*np.cos(2*theta)-0.56*np.sin(3*theta)
rho_opp=2-0.36*np.cos(2*theta)+0.56*np.sin(3*theta)
assert np.min(rho)>0
w=4+0.24*np.cos(2*theta)
s=4-0.72*np.cos(2*theta)
c=(1/rho+1/rho_opp)/8 # unnormalized small-chord coefficient
product=s/(8*c)
discriminant=np.maximum(0,s*s-4*product)
roots=np.sort(np.stack([(s+np.sqrt(discriminant))/2,(s-np.sqrt(discriminant))/2]),axis=0)
actual=np.sort(np.stack([rho,rho_opp]),axis=0)
assert np.max(np.abs(roots-actual))<2e-7

# Smooth compactly supported perturbations carrying no first harmonics.
def bump2(x,center,halfwidth):
    z=(x-center)/halfwidth
    if abs(z)>=1: return 0.0,0.0
    d=1-z*z
    val=exp(-1/d)
    uprime=-2*z/(d*d)
    usecond=-2/(d*d)-8*z*z/(d*d*d)
    return val, val*((uprime*uprime)+usecond)/(halfwidth**2)
def phi(x,center):
    p,p2=bump2(x,center,0.22)
    return p+p2
for center in [0.6,2.2]:
    assert abs(quad(lambda x: phi(x,center)*np.cos(x), 0,pi,epsabs=1e-10,limit=250)[0]) < 2e-8
    assert abs(quad(lambda x: phi(x,center)*np.sin(x), 0,pi,epsabs=1e-10,limit=250)[0]) < 2e-8
xx=np.linspace(0,pi,5001)
fA=np.array([phi(x,0.6)+phi(x,2.2) for x in xx]); fB=np.array([phi(x,0.6)-phi(x,2.2) for x in xx])
assert np.max(np.abs(fA*fA-fB*fB)) < 1e-9
assert np.max(np.abs(fA-fB)) > 1.0
assert np.max(np.abs(fA+fB)) > 1.0
eps=1e-4
assert np.min(1+eps*fA)>0 and np.min(1+eps*fB)>0
cA=1/(1+eps*fA)+1/(1-eps*fA)
cB=1/(1+eps*fB)+1/(1-eps*fB)
assert np.max(np.abs(cA-cB)) < 1e-12
print('SHORT_CHORD_VERIFY_OK ellipses=3 analytic_pairing=2049 smooth_counterexample=5001')
