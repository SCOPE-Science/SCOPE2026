"""Independent numerical checks for the two-transversal intersection law.
Run: python check.py. Requires NumPy and SciPy.
"""
import math
import numpy as np
from scipy.integrate import quad

def density(x,y):
    if not (0<x<1 and 0<y<1): return 0.0
    d1=min(x,1-x); d2=min(y,1-y)
    u=min(d1,d2); w=max(d1,d2)
    t=w*(1-w)
    return u*(4*t-u)/(4*(1-u)**2*t*t)

def reduced(x,y):
    # This expression is valid on the fundamental wedge 0<x<y, x+y<1.
    return x*(4*y*(1-y)-x)/(4*(1-x)**2*y*y*(1-y)**2)

mass=4*quad(lambda x: quad(lambda y: reduced(x,y),x,1-x,epsabs=1e-10)[0],0,.5,epsabs=1e-10)[0]
assert abs(mass-1)<1e-8, mass
assert abs(density(.5,.5)-4)<1e-13
for x,y in ((.2,.3),(.3,.2),(.7,.8),(.95,.15),(.41,.57)):
    assert abs(density(x,y)-density(1-x,y))<1e-12
    assert abs(density(x,y)-density(x,1-y))<1e-12
    assert abs(density(x,y)-density(y,x))<1e-12

# Numeric finite-grid mode and corner profile.
z=np.linspace(.0005,.9995,401)
assert max(density(x,y) for x in z[::7] for y in z[::7])<4.0000001
for ratio in (.2,.5,1.):
    eps=1.e-6
    target=ratio*(1-ratio/4)
    assert abs(density(ratio*eps,eps)-target)<1e-5,(ratio,density(ratio*eps,eps),target)

def corner_prob(eps):
    return 2*quad(lambda y: quad(lambda x:density(x,y),0,y,epsabs=1e-9)[0],0,eps,epsabs=1e-9)[0]
assert abs(corner_prob(0.002)/0.002**2-5/12)<.01

def strip_prob(eps):
    return 2*quad(lambda x: quad(lambda y: reduced(x,y),x,1-x,epsabs=1e-9)[0]
                  +quad(lambda y: density(x,y),0,x,epsabs=1e-9)[0]
                  +quad(lambda y: density(x,y),1-x,1,epsabs=1e-9)[0],0,eps,epsabs=1e-9)[0] / 2
# Equivalently integrate full vertical sections directly, here independent numeric integration.
for eps in (1e-2,1e-3):
    p=strip_prob(eps)
    ratio=p/(eps*eps*math.log(1/eps))
    print('boundary_strip',eps,p,ratio)
    assert .9<ratio<1.3,(eps,ratio)

rng=np.random.default_rng(20261111)
N=1_800_000
U,V,W,Z=rng.random((4,N))
a=V-U; c=Z-W
X=(W+c*U)/(1-c*a)
Y=U+a*X
assert np.all((X>0)&(X<1)&(Y>0)&(Y<1))
# Compare direct Cartesian sampling with independent quadrature on moderate rectangles.
regions=((.4,.6,.4,.6),(.05,.2,.2,.4),(.0,.1,.0,.1),(.0,.1,.3,.6))
for x0,x1,y0,y1 in regions:
    direct=np.mean((X>=x0)&(X<x1)&(Y>=y0)&(Y<y1))
    expected=quad(lambda x:quad(lambda y:density(x,y),y0,y1,epsabs=1e-8)[0],x0,x1,epsabs=1e-8)[0]
    sigma=np.sqrt(max(expected*(1-expected),1e-8)/N)
    print('region',x0,x1,y0,y1,'sample',direct,'integral',expected,'z',abs(direct-expected)/sigma)
    assert abs(direct-expected)<5*sigma+.0005
print('FORCED_SQUARE_TRANSVERSAL_DENSITY_CORNER_AND_LAYER_OK')
