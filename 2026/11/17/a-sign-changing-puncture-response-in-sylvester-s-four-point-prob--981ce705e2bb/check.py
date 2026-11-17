"""Independent numerical checks for the disk four-point puncture theorem.

Run with Python 3 and numpy, scipy.  Finite sampling corroborates but does not prove
exact identities or the asymptotic statements.
"""
import math
import numpy as np
from scipy.integrate import quad

PI=math.pi
Q=1-35/(12*PI**2)

def expected_triangle(r):
    return (4/(3*PI))*(1/3 + r*r/2 - r**4/8 + r**6/48)

def contain_fixed_point(r):
    # Directional density for a uniform disk point viewed from (r,0).
    def integrand(t):
        sn, cs=math.sin(t),math.cos(t)
        sr=math.sqrt(max(0,1-r*r*sn*sn))
        rho=sr-r*cs
        f=rho*rho/(2*PI)
        g=sn if r==0 else (sn*sr+math.asin(r*sn)/r)/2
        half=0.5+(2*r/PI)*g
        return f*half*half
    return 1-3*quad(integrand,0,2*PI,points=[PI/2,3*PI/2],epsabs=2e-11,limit=400)[0]

def fixed_quad(r):
    return 1-contain_fixed_point(r)-3*expected_triangle(r)/PI

def cap_upper_bound(r):
    return 4*math.sqrt(2)/PI*(1-r)**1.5

def lower_gap(r):
    p=(1-r*r)*(r**4-5*r*r+19)/48
    return 4*p/PI**2-cap_upper_bound(r)

def cross(u,v):
    return u[...,0]*v[...,1]-u[...,1]*v[...,0]

def in_triangle(p,a,b,c):
    v1=cross(b-a,p-a)
    v2=cross(c-b,p-b)
    v3=cross(a-c,p-c)
    return ((v1>0)&(v2>0)&(v3>0)) | ((v1<0)&(v2<0)&(v3<0))

def simulate_fixed(r,n=1_200_000,seed=9012):
    rng=np.random.default_rng(seed)
    radii=np.sqrt(rng.random((n,3)))
    angle=2*PI*rng.random((n,3))
    pts=np.stack((radii*np.cos(angle),radii*np.sin(angle)),axis=2)
    a,b,c=[pts[:,i,:] for i in range(3)]
    x=np.array([r,0.0])
    nonconvex=(in_triangle(x,a,b,c)|in_triangle(a,x,b,c)|
               in_triangle(b,x,a,c)|in_triangle(c,x,a,b))
    val=1-nonconvex.mean()
    sigma=math.sqrt(val*(1-val)/n)
    return val,sigma

assert abs(expected_triangle(0)-4/(9*PI))<1e-14
assert abs(expected_triangle(1)-35/(36*PI))<1e-14
assert abs(2*quad(lambda r: r*expected_triangle(r),0,1)[0]-35/(48*PI))<1e-13
assert abs(fixed_quad(0)-(0.75-4/(3*PI**2)))<1e-12
assert abs(fixed_quad(1)-Q)<1e-12

for r in (0.0,0.75,0.99):
    analytic=fixed_quad(r)
    mc,sd=simulate_fixed(r)
    print('radius',r,'exact_quadrature',f'{analytic:.10f}',
          'MonteCarlo',f'{mc:.7f}','sigma',f'{sd:.7f}')
    assert abs(analytic-mc)<5*sd+0.0001

assert (1-19/(3*PI**2))>0
for r in (0.99,0.995,0.999):
    assert lower_gap(r)>0
    assert fixed_quad(r)>Q
    print('near_boundary',r,'rigorous_lower_bound',f'{lower_gap(r):.8f}',
          'observed_coefficient',f'{4*(Q-fixed_quad(r)):.8f}')

slope=-10/PI**2
for r in (0.99,0.995,0.999):
    ratio=4*(Q-fixed_quad(r))/(1-r)
    print('slope_check',r,round(ratio,7),'limit',round(slope,7))
    assert abs(ratio-slope)<0.2

print('DISK_PUNCTURE_SYLVESTER_SIGN_REVERSAL_OK')
