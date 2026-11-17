#!/usr/bin/env python3
"""Symbolic checks for the Allee--fear boundary crossover theorem.

Requires Python 3 and SymPy. Finite-time numerics are diagnostics, not a proof.
"""
import sympy as S

a,b,q,eps,y,z = S.symbols('a b q eps y z', positive=True)
s = y+z
c = 1+eps
s_dot = (1-s)*(a*y - s*(a-s)/(1+q*y))
y_dot = b*y*(1-y-c*(1-s))
z_dot = S.cancel(s_dot-y_dot)
gamma = (1+a*q)/a
# center manifold h(y,eps)=gamma*y**2+(b/a)*eps*y + third order
h=gamma*y**2+(b/a)*eps*y
# recover all terms of total degree at most two by equal-weight expansion
v=S.symbols('v')
trunc=lambda f,k: S.expand(S.series(S.cancel(f.subs({y:v*y,eps:v*eps,z:v*z})),v,0,k).removeO()).coeff(v,k-1)
assert S.simplify(trunc(z_dot.subs(z,h),3)) == 0
# Check degree-three slow drift: no y**2 term, cubic coefficient b gamma, and -b eps y
assert S.simplify(S.diff(y_dot.subs(z,h).subs(eps,0),y,3).subs(y,0)/6-b*gamma)==0
assert S.simplify(S.diff(S.diff(y_dot.subs(z,h),eps),y).subs({eps:0,y:0})+b)==0
# Exact equilibrium polynomial from eliminating y via y=1-c*x, p=1-a
x=S.symbols('x')
yn=1-c*x
f_eq=S.factor((1-x)*(x-1+a)-a*yn*(1+q*yn))
A1=a*c**2*q+1;A2=-(2*a*c*q+a*c+(1-a)+1);A3=a+a*q+(1-a)
assert S.factor(f_eq+(A1*x*x+A2*x+A3))==0
# Expansions obtained via y*= K t + B t**2, eps=t**2, x=(1-y)/(1+eps)
t=S.symbols('t', positive=True)
K=S.sqrt(a/(1+a*q)); B=-(a+2)/(2*(1+a*q))
ytrial=K*t+B*t**2; xtrial=(1-ytrial)/(1+t**2)
feqtrial=S.factor(f_eq.subs({x:xtrial,eps:t*t}))
assert S.simplify(S.series(feqtrial,t,0,4).removeO())==0
# Jacobian eigenvalues at equilibrium; trace approx -a and slow determinant /(-a)
xv,yv=S.symbols('xv yv')
p=1-a
Fx=xv*((1-xv)*(xv-p)/(1+q*yv)-a*yv)
Gy=b*yv*(1-yv-c*xv)
J=S.Matrix([Fx,Gy]).jacobian([xv,yv])
# Along the equilibrium nullcline, the determinant is -b*x*y*f_x, where
# f=(equilibrium polynomial numerator)/(1+q*y); its leading term is -2*a*b*eps.
DET=-b*xtrial*ytrial*S.diff(f_eq,x).subs({x:xtrial,eps:t*t})/(1+q*ytrial)
assert S.simplify(S.series(DET,t,0,3).removeO().coeff(t,2)+2*a*b)==0
assert S.simplify(J.subs({xv:1,yv:0,eps:0})-S.Matrix([[-a,-a],[0,0]]))==S.zeros(2)
# Closed-form slow-limit first-passage integrals
Y=S.symbols('Y',positive=True)
Y0=S.symbols('Y0',positive=True)
Fminus=S.log(1+1/(gamma*Y**2))/(2*b)
Fplus=S.log(gamma*Y**2/(gamma*Y**2-1))/(2*b)
assert S.simplify(S.diff(Fminus,Y)+1/(b*Y*(gamma*Y**2+1)))==0
assert S.simplify(S.diff(Fplus,Y)+1/(b*Y*(gamma*Y**2-1)))==0
# example rational parameters: a=1/2,b=13/10,q=7/10
for aa,bb,qq in [(S.Rational(1,2),S.Rational(13,10),S.Rational(7,10)),(S.Rational(3,4),2,1),(S.Rational(1,5),1,S.Rational(1,4))]:
    assert (gamma.subs({a:aa,q:qq}) > 0)
print('VERIFY_OK: exact centre coefficient, nullcline, root expansion, saddle multiplier, and passage integral')
