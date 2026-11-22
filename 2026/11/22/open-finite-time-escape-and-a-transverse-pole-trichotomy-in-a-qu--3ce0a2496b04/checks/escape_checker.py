"""Standalone diagnostic checks for the quadratic chameleon escape theorem.
The mathematical proof, not numerical integration, establishes the claims.
"""
from fractions import Fraction
from math import isfinite
from scipy.integrate import solve_ivp
import sympy as sp

s,c,b,a=sp.symbols('s c b a', positive=True)
w= c*s - b*c*s**2/2
z=sp.series(1/w,s,0,1).removeO()
assert sp.simplify(z-1/(c*s)-b/(2*c))==0
alpha=sp.symbols('alpha')
# Formal bounded Frobenius mode u=1+alpha*s^2+... has residual constant 2alpha+2alpha/c+1.
assert sp.solve(2*alpha+2*alpha/c+1,alpha)[0]==-c/(2*(c+1))
# Indicial polynomial of u_ss + [1/(c*s)+O(1)]u_s+u=0
r=sp.symbols('r')
assert sp.factor(r*(r-1)+r/c) == r*(c*r-c+1)/c
print('formal indicial roots:', sp.solve(r*(r-1)+r/c,r))

# One explicit robust-blowup tube for a=1,b=0,c=2.
c0, a0,b0=2.,1.,0.
p,kappa,X,Y,Z=.75,1.5,1.,1.,1e4
assert 1/c0<p<1 and 1/p<kappa<c0
assert (Y/(kappa*(1-p)))*Z**(p-1)<X/2
for z0 in (Z,10*Z,100*Z):
    rhs_min=c0*z0**2-(abs(b0)+X)*z0-abs(a0)-5*X*Y*z0**p
    assert rhs_min>=kappa*z0**2
    assert (p*kappa-1)*Y*z0>=X*z0**(-p)
# The inequalities for ALL z >= Z reduce to bounds on decreasing negative powers.
# Exact integer/rational tests at Z=10000: Z^(3/4)=1000, Z^(-3/4)=1/1000, Z^(-1/4)=1/10.
assert Fraction(1,2)*10000**2 - 10000 - 1 - 5*1000 > 0
assert Fraction(1,8)*10000 - Fraction(1,1000) > 0
assert Fraction(1,1) / (Fraction(3,2)*Fraction(1,4)) * Fraction(1,10) < Fraction(1,2)
print('explicit tube uniform inequality certificate: PASS')

# Integrate with z as independent variable, avoiding the finite-time singularity.
# Initial point is inside the tube, with y(0)>0 guaranteeing C>0.
z_init=1e4
x_init,y_init=.1,10.
def rhs(z,V):
    x,y,t=V
    q=a0-b0*z+c0*z*z-5*x*y+x*z
    return [y/q,(-x+z*y)/q,1/q]
sol=solve_ivp(rhs,(z_init,1e10),[x_init,y_init,0.],method='DOP853',rtol=2e-11,atol=1e-13,dense_output=True)
assert sol.success,sol.message
for z0 in (1e5,1e6,1e8,1e10):
    x,y,t=sol.sol(z0)
    assert abs(x)<1 and abs(y)<z0**p
    print('z=%g, x=%.12g, y/z^.5=%.12g, t=%.12g'%(z0,x,y/z0**.5,t))
C1=sol.sol(1e8)[1]/1e4
C2=sol.sol(1e10)[1]/1e5
assert abs(C1-C2)<1e-5
xx2=sol.sol(1e10)[0]; xx1=sol.sol(1e8)[0]
# x_infty-x(z) ~ C*z^{-1/2}; use higher-z x to predict the difference.
assert abs((xx2-xx1)/(C2*(1e-4-1e-5))-1)<.003
assert sol.sol(1e10)[2]<1/(kappa*z_init)
print('numeric asymptotic and finite-time diagnostics: PASS')
