#!/usr/bin/env python3
"""Reproduce the two-sided first-visit polarity product theorem.
Uses SymPy for exact generator identities and SciPy for independent
backward-boundary-value checks. No simulation is used as proof.
"""
import math
import sympy as sp
import numpy as np
from scipy.integrate import solve_bvp

D,q,m,a,b,x=sp.symbols('D q m a b x', positive=True, finite=True, real=True)
v=D*q*m
alpha=D*q*q*(1-m*m)
kappa=alpha/2
symbols=(-1,1)

def up(s):return m+(s-m)*sp.exp(-q*(a-x))
def dn(s):return -m+(s+m)*sp.exp(-q*(x+b))
def generator(f,s):
    return sp.diff(f(s),x,2)*D + s*v*sp.diff(f(s),x) + kappa*(f(-s)-f(s))

checks=0
for s in symbols:
    for f in (up,dn,lambda j:up(j)*dn(j)):
        expression=sp.factor(sp.expand(generator(f,s)))
        assert sp.simplify(expression)==0,(s,expression)
        checks+=1
    assert sp.simplify(up(s).subs(x,a)-s)==0
    assert sp.simplify(dn(s).subs(x,-b)-s)==0
    checks+=2
    # The sequential hitting construction prescribes these rewards at each exit.
    assert sp.simplify((up(s)*dn(s)).subs(x,a)-s*dn(s).subs(x,a))==0
    assert sp.simplify((up(s)*dn(s)).subs(x,-b)-s*up(s).subs(x,-b))==0
    checks+=2

za,zb=sp.symbols('za zb',positive=True)
uplus=m*(1-za)+za
umin=m*(1-za)-za
dplus=-m*(1-zb)+zb
dmin=-m*(1-zb)-zb
sigma=sp.symbols('sigma',real=True)
prob_plus=(1+sigma)/2
moment=sp.expand(prob_plus*uplus*dplus+(1-prob_plus)*umin*dmin)
mean_u=sp.expand(prob_plus*uplus+(1-prob_plus)*umin)
mean_d=sp.expand(prob_plus*dplus+(1-prob_plus)*dmin)
assert sp.simplify(moment-mean_u*mean_d-(1-sigma*sigma)*za*zb)==0
checks+=1
z=sp.symbols('z',positive=True)
R=sp.expand(moment.subs({sigma:0,za:z,zb:z}))
assert sp.simplify(R-(z*z-m*m*(1-z)**2))==0
assert sp.simplify(R - ((1+m)*z-m)*((1-m)*z+m)) == 0
checks+=2
print('exact symbolic checks:',checks)

# Independently solve the 2-state backward ODE with actual, sequential-hit
# boundary values; unlike the closed form, this method never assumes the
# claimed factorization inside the interval.
parameter_sets=[]
for vel in (0.13,0.6,1.5,2.7):
    for diffusion in (0.4,1.2):
        for switch in (0.35,1.4):
            parameter_sets.append((vel,diffusion,switch,0.47,0.81))
for vel,diffusion,switch,left,right in parameter_sets:
    h=math.sqrt(vel*vel+diffusion*switch)
    rate=h/diffusion
    bias=vel/h
    for x_start in (-left*0.41,0.,right*0.46):
        endz=math.exp(-rate*(right+left))
        state=np.array([1.0,-1.0])
        # Boundary payoff is the product of the phase at first exit and
        # the expected phase on subsequent passage to the opposite side.
        boundary_upper=endz-bias*(1-endz)*state
        boundary_lower=endz+bias*(1-endz)*state
        def ode(xx,y):
            f1,f2,p1,p2=y
            return np.vstack((p1,p2,
                (-vel*p1-(switch/2)*(f2-f1))/diffusion,
                (vel*p2-(switch/2)*(f1-f2))/diffusion))
        def boundary(yl,yu):
            return np.array([yl[0]-boundary_lower[0],yl[1]-boundary_lower[1],
                             yu[0]-boundary_upper[0],yu[1]-boundary_upper[1]])
        mesh=np.linspace(-left,right,80)
        numerical=solve_bvp(ode,boundary,mesh,np.zeros((4,len(mesh))),tol=2e-9,max_nodes=3000)
        assert numerical.success,numerical.message
        from_pde=numerical.sol(x_start)[:2]
        zup=math.exp(-rate*(right-x_start))
        zdown=math.exp(-rate*(left+x_start))
        exact=(bias+(state-bias)*zup)*(-bias+(state+bias)*zdown)
        assert np.allclose(from_pde,exact,atol=2e-7,rtol=2e-7),(vel,diffusion,switch,left,right,x_start,from_pde,exact)
        checks+=2
print('total exact and independent BVP component checks:',checks)

# Equidistant unbiased-sign reversal is exact, not inferred numerically.
for vel,diffusion,switch,_,_ in parameter_sets:
    h=math.sqrt(vel*vel+diffusion*switch)
    rate=h/diffusion;bias=vel/h
    threshold=math.log(1+1/bias)/rate
    def raw(dist):
        zz=math.exp(-rate*dist)
        return zz*zz-bias*bias*(1-zz)**2
    assert raw(threshold/2)>0
    assert abs(raw(threshold))<1e-13
    assert raw(threshold*2)<0
    checks+=3
print('all checks including transition sign tests:',checks)
