"""Independent numerical checks for two-boundary-one-pinned acute triangle law."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import spence

def shell_acute(r):
    # Analytic expressions: Li_2(z)=spence(1-z)
    dil=spence(1-r)-spence(1+r)
    integral=quad(lambda t:r*math.cos(t)*math.asin(r*math.cos(t))/math.sqrt(1-r*r*math.sin(t)**2),0,math.pi/2,epsabs=1e-11)[0]
    return .5-2*dil/math.pi**2+2*integral/math.pi**2

def independent_1d(r):
    # Obtain angle-at-C probability by integrating a quadratic inequality
    def c_obtuse(m):
        disc=math.sqrt(2-2*r*r+r*r*math.cos(m)**2)
        hi=max(-1,min(1,(r*math.cos(m)+disc)/2))
        lo=max(-1,min(1,(r*math.cos(m)-disc)/2))
        return (math.asin(hi)-math.asin(lo))/math.pi
    pc=quad(c_obtuse,0,2*math.pi,epsabs=1e-10)[0]/(2*math.pi)
    def a_obtuse(a):
        return math.atan2(r*abs(math.sin(a)),1-r*math.cos(a))/math.pi
    pa=quad(a_obtuse,0,2*math.pi,epsabs=1e-10)[0]/(2*math.pi)
    return 1-2*pa-pc

def direct_grid(r,n=750):
    a=(np.arange(n)+.5)*(2*math.pi/n)
    x=np.cos(a);y=np.sin(a)
    dot=np.outer(x,x)+np.outer(y,y)
    ca=1-dot>r*np.abs(x[:,None]-x[None,:]); cc=dot-r*(x[:,None]+x[None,:])+r*r>0
    return float(np.mean(ca & cc))

for r in [0,0.1,0.35,0.7,0.9,1.0]:
    direct=direct_grid(r)
    if r < 1: exact=shell_acute(r);ind=independent_1d(r)
    else: exact=.25;ind=.25
    assert abs(exact-ind)<1e-9, (r,exact,ind)
    assert abs(exact-direct)<0.002, (r,exact,direct)
    print('r',r,'formula',round(exact,10),'independent',round(ind,10),'grid',round(direct,10))
for r in [.005,.01,.02]:
    approx=.5-4*r/math.pi**2+r*r/(2*math.pi)-4*r**3/(9*math.pi**2)+r**4/(8*math.pi)
    assert abs(shell_acute(r)-approx)<10*r**5
print('RADIAL_PINNED_TRIANGLE_FORMULA_AND_EXPANSION_OK')
