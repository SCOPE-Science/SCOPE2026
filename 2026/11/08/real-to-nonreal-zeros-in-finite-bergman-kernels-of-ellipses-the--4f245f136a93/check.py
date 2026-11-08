"""Exact algebraic checks for the ellipse finite-kernel zero bifurcation.
Run with Python 3 and SymPy. Finite checks supplement, not replace, the all-degree proof.
"""
import sympy as S
u,x,y,m=S.symbols('u x y m',real=True)
t=(1+u)/(1-u)
A=80*(u-1)**2*(u+3)*(3*u+1)
B=48*(u-1)*(5*u**4+20*u**3+14*u**2+20*u+5)
C=45*u**6+370*u**5+931*u**4+1404*u**3+931*u**2+370*u+45
R=225*u**8-600*u**7-13700*u**6-45800*u**5-60474*u**4-45800*u**3-13700*u**2-600*u+225
Q=225*y**4-600*y**3-14600*y**2-44000*y-32624
K=1-S.chebyshevu(2,S.sqrt(x/(1-u)))*3/S.chebyshevu(2,t)+S.chebyshevu(4,S.sqrt(x/(1-u)))*5/S.chebyshevu(4,t)
Den=(u+3)*(3*u+1)*(u*u+10*u+5)*(5*u*u+10*u+1)
assert S.cancel(K-(A*x*x+B*x+C)/Den)==0
assert S.expand(B*B-4*A*C-64*(u-1)**2*R)==0
assert S.expand(R-u**4*Q.subs(y,u+1/u))==0
assert Q.subs(y,2)<0
assert S.factor((m-1)*(2*m-1)**2-2*m*(2*m+1)*(2*m-3))==-(4*m**3-11*m+1)
for k in range(1,9):
    z=S.symbols('z')
    lhs=sum((-1)**j*S.chebyshevu(2*j,z) for j in range(k+1))
    rhs=(-1)**k*S.chebyshevu(k,2*z*z-1)
    assert S.expand(lhs-rhs)==0
x2=S.factor((1-u)*(2*t*t+1)/6)
assert S.cancel(x2-1-(3*u-1)*(u+3)/(6*(1-u)))==0
print('ELLIPSE_FINITE_KERNEL_PASS exact_quartic=1 discriminant=1 reciprocal=1 newton=1 thin_instances=8 degree_two_boundary=1')
