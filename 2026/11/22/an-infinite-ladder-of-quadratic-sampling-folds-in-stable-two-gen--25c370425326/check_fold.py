"""Reproduce exact resonant fold curvature and numerical variational checks.
Uses only Python 3, SymPy, NumPy and SciPy; no external files.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

g,a,t = sp.symbols('g a t',positive=True)
K=sp.symbols('K',integer=True,positive=True)
# At time T=k*pi/a, the first and second variations are elementary.
D=(g*g+a*a)*(g*g+9*a*a)
Icos=g*(g*g+7*a*a)/D
Isin=6*a**3/D
assert sp.simplify(Icos.subs({g:1,a:1})-sp.Rational(2,5))==0
assert sp.simplify(Isin.subs({g:1,a:1})-sp.Rational(3,10))==0
# Direct Laplace integrals of cos^3 and sin^3 on [0,k*pi/a].
for k in range(1,5):
 T=sp.pi*k/a
 z=(-1)**k*sp.exp(-g*T)
 C=sp.integrate(sp.exp(-g*t)*sp.cos(a*t)**3,(t,0,T))
 S=sp.integrate(sp.exp(-g*t)*sp.sin(a*t)**3,(t,0,T))
 assert sp.simplify(C-(1-z)*Icos)==0
 assert sp.simplify(S-(1-z)*Isin)==0

def F(y):
    # theta=1+log(3)/4, hence at y=1 exponential = exp(-log(3))=1/3,
    # so F(1)=(4/3)/(4/3)=1.
    return (4/3)/(1+math.exp(4*(y-1)-math.log(3)))
def G(x):
    return 2/(1+math.exp(-2*(x-1)))
# F'(1)=-1, F''(1)=-2. G'(1)=1, G''(1)=0.
assert abs(F(1)-1)<1e-14 and abs(G(1)-1)<1e-14

def rhs(t,z):
    x,y,u,v,U,V=z
    fx=F(y)
    ee=math.exp(4*(y-1)-math.log(3))
    fp=-(16/3)*ee/(1+ee)**2
    fpp=-(64/3)*ee*(1-ee)/(1+ee)**3
    e=math.exp(-2*(x-1))
    gp=4*e/(1+e)**2
    gpp= -8*e*(1-e)/(1+e)**3
    return [fx-x,G(x)-y, -u+fp*v, gp*u-v,-U+fp*V+fpp*v*v,gp*U-V+gpp*u*u]
for k in [1,2,3,4]:
    T=k*math.pi
    sol=solve_ivp(rhs,(0,T),[1,1,0,1,0,0],rtol=2e-12,atol=2e-14,method='DOP853')
    y=sol.y[:,-1]
    exp_first=-math.exp(-T)*math.sin(T)
    expected=(-4/5)*((-1)**k)*math.exp(-T)*(1-((-1)**k)*math.exp(-T))
    assert abs(y[0]-1)<5e-12 and abs(y[1]-1)<5e-12
    assert abs(y[2]-exp_first)<4e-12
    assert abs(y[4]-expected)<4e-12
    print(f'k={k} T={T:.12f} initial-hidden derivative={y[2]:+.3e} curvature={y[4]:+.12e} analytic={expected:+.12e}')
print('PASS: exact integrals, logistic normalizations, numerical first and second variational equations')

# Verify a true two-hidden-state alias at a nonresonant sampling time.
from scipy.optimize import brentq
def sample(T,hidden):
    def system(t,z):
        x,y,u,v=z
        e=math.exp(4*(y-1)-math.log(3))
        fp=-(16/3)*e/(1+e)**2
        h=math.exp(-2*(x-1))
        gp=4*h/(1+h)**2
        return [F(y)-x,G(x)-y,-u+fp*v,gp*u-v]
    result=solve_ivp(system,(0,T),[1,1+hidden,0,1],rtol=3e-12,atol=3e-14,method='DOP853')
    return float(result.y[0,-1]),float(result.y[2,-1])
T=math.pi+0.02
vcrit=brentq(lambda v:sample(T,v)[1],-0.1,0.1,xtol=1e-13)
vleft=vcrit-0.02
qleft=sample(T,vleft)[0]
vright=brentq(lambda v:sample(T,v)[0]-qleft,vcrit+0.0005,vcrit+0.12,xtol=1e-13)
assert vleft<vcrit<vright and 1+vleft>0 and abs(vleft-vright)>0.03
assert abs(sample(T,vright)[0]-qleft)<2e-11
assert abs(sample(T,0)[1])>1e-5
print('nonresonant alias: T=',T,'hidden initial values=',1+vleft,1+vright,'common later output=',qleft)
print('PASS: local noninjectivity persists away from exact resonance')
