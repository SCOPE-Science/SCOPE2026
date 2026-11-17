"""Independent finite-radius quadrature for smooth convex support curves.
Usage: python verify_tangent_intersections.py
Requires numpy, scipy. The proof is analytic; tests only spot-check its formulas.
"""
import math
import numpy as np
from scipy.optimize import brentq

PI=math.pi

def point(theta,delta,h):
    ph=theta+PI+delta
    T=(h(ph)-h(theta)*math.cos(PI+delta))/math.sin(PI+delta)
    return math.hypot(h(theta),T)

def calc(eps,R,N=96):
    def h(x):return 1+eps*math.cos(3*x)
    def rho(x):return 1-8*eps*math.cos(3*x)
    L=2*PI
    ths=(np.arange(N)+.5)*2*PI/N
    # high-radius solutions are in the window |delta| < .25.
    acc=0.
    for th in ths:
        def area(sign):
            root=brentq(lambda z:point(th,sign*z,h)-R,1e-10,.22,xtol=1e-13)
            # Deterministic Simpson integration of the angular density across threshold.
            k=np.arange(301)
            ds=sign*root*k/300
            ys=np.array([rho(th+PI+float(dd)) for dd in ds])
            integral=root/300*(ys[0]+ys[-1]+4*sum(ys[1:-1:2])+2*sum(ys[2:-1:2]))/3
            return integral
        acc+=rho(float(th))*(area(1)+area(-1))
    return acc*(2*PI/N)/(L*L)

def predicted(eps):return (2/PI)*(1-32*eps**2)

for eps in [0.0,.04,.09]:
    if abs(eps)>=.125:raise ValueError('strict convexity')
    C=predicted(eps)
    l2=math.pi*256*eps**2
    gap=l2/(4*PI**2) # w=2 => 1/(2*pi*pi*w)
    assert abs((2/PI-C)-gap)<1e-12
    for R in [100,300,1000]:
        p=calc(eps,R)
        print(f'eps={eps:.3f}, R={R}, R*P={R*p:.12f}, coeff={C:.12f}, relative_error={(R*p/C-1):+.4e}')
        assert abs(R*p/C-1)<.05
    if eps==0:
        assert abs(calc(0,1000)-(2/PI)*math.asin(1/1000))<1e-9

# For anti-periodic radius rho=w/2*(1+a*tanh(k*cos 3theta)), verify
# its first Fourier mode vanishes, positive curvature, and exact range.
N=4096
th=(np.arange(N)+.5)*2*PI/N
for a,k in [(.8,3),(.99,10),(.9999,70)]:
    rho=1+a*np.tanh(k*np.cos(3*th)) # width 2
    antipodal=1+a*np.tanh(k*np.cos(3*(th+PI)))
    assert np.max(np.abs(rho+antipodal-2))<1e-12
    assert min(rho)>0
    assert abs(np.mean(rho*np.cos(th)))<1e-12
    assert abs(np.mean(rho*np.sin(th)))<1e-12
    C=2/PI*float(np.mean(rho*antipodal))
    assert 0<C<2/PI
    print('range',a,k,'C=',C)
assert C<.01
print('RANDOM_TANGENT_INTERSECTIONS_OK')
