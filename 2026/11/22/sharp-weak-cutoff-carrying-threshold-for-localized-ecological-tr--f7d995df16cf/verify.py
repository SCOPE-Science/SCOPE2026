"""Reproduce quadrature and the limiting threshold for a cutoff competition pulse."""
from math import sqrt, asin
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad

def mass(epsilon,r,D=1.0):
    b=1-r
    assert epsilon > 0 and r>0 and b**3>3*epsilon**2
    A=brentq(lambda a: epsilon**2-b*a*a+2*a**3/3,epsilon,b,xtol=1e-15)
    outer=quad(lambda u: 1/sqrt(r+2*u/3),0,epsilon,epsabs=1e-13)[0]
    def interior(t):
        u=A-(A-epsilon)*t*t
        Q=b*(A+u)-2*(A*A+A*u+u*u)/3
        return 2*sqrt(A-epsilon)*u/sqrt(Q)
    core=quad(interior,0,1,epsabs=1e-13,limit=200)[0]
    return 2*sqrt(D)*(outer+core),A

def kappa(epsilon,r,D=1.0):
    return r/mass(epsilon,r,D)[0]

def optimum(epsilon,D=1.0):
    r_c=1-3**(1/3)*epsilon**(2/3)
    assert r_c>0
    sol=minimize_scalar(lambda r: -kappa(epsilon,r,D),bounds=(0.02,min(.98,r_c-1e-7)),method='bounded',options={'xatol':1e-11})
    return sol.x,-sol.fun

LIMIT=(3/5)**1.5/5
print('limiting constant =',LIMIT)
for eps in [.1,.03,.01,.003,.001,.0001,.00001]:
    r,k=optimum(eps)
    m,A=mass(eps,r)
    print('eps=',eps,'r=',r,'eps*kappa=',eps*k,'ratio=',eps*k/LIMIT,'A/eps=',A/eps)
    # scale with diffusivity exactly
    assert abs(kappa(eps,r,4)*2-k)<1e-10*max(1,k)
for r in [.2,.4,.6,.8]:
    for eps in [1e-4,1e-5]:
        M,A=mass(eps,r)
        target=2*eps/(sqrt(r)*(1-r))
        print('limit mass: r,eps,ratio',r,eps,M/target)
print('COMPLETE')
