"""Numerical consistency checks for the ideal-polygon boundary-distance theorem."""
import math
import numpy as np
from scipy.stats import qmc
from scipy.integrate import quad
PI=math.pi
r0=math.asinh(1/math.sqrt(3))
def cdf(t):
    if t<=0: return 0.
    if t>=r0: return 1.
    k=math.sinh(t)
    return (6/PI)*(math.atan(k)-k*math.log(2*math.tanh(t)))

def triangle_surv_quad(t):
    k=math.sinh(t)
    M=(1-k*k)/(2*k)
    return quad(lambda v: math.log((1+v*v)/(v+k)**2),k,M,epsabs=1e-13)[0]/PI
for t in [.0005,.015,.05,.17,.3,.48,.54]:
    diff=1-cdf(t)-triangle_surv_quad(t)
    assert abs(diff)<2e-12,(t,diff)

def sample_poly(t,N=2**19):
    # Area-uniform hyperbolic points in the ideal quadrilateral (0,1,t,infinity).
    u=qmc.Sobol(3,scramble=True,seed=719).random_base2(int(math.log2(N)))
    left=u[:,0]<.5
    a=np.where(left,0.,1.)
    L=np.where(left,1.,t-1.)
    theta=.5*np.pi*u[:,1]
    x=a+L*(np.sin(theta)**2)
    y=L*np.sin(theta)*np.cos(theta)/u[:,2]
    # Signed distances to four complete side geodesics; minimum gives boundary distance.
    z0=np.arcsinh(x/y)
    zt=np.arcsinh((t-x)/y)
    z01=np.arcsinh((y*y-x*(1-x))/y)
    z1t=np.arcsinh((y*y-(x-1)*(t-x))/((t-1)*y))
    dd=np.minimum.reduce([z0,zt,z01,z1t])
    return dd
for t in [2.,3.,5.]:
    d=sample_poly(t,2**19)
    L=2*math.log(t*t/(t-1))
    for s in [.007,.012,.020]:
        pred=(8*s*math.log(1/s)+(L+8*(1-math.log(2)))*s)/(2*PI)
        emp=float(np.mean(d<=s))
        assert abs(emp-pred)<6e-4,(t,s,emp,pred)
print('IDEAL_HYPERBOLIC_POLYGON_BOUNDARY_LAW_OK')
