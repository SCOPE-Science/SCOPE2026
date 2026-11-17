"""Reproduce the algebraic fold and target-area certificates.

Requires Python 3 and sympy. Run: python check.py
"""
import sympy as s
x, y, u, t, A, g = s.symbols('x y u t A g', positive=True)
F1 = x*(2-x-y)
F2 = y*(A+g*x)
J = s.Matrix([F1, F2]).jacobian([x,y]); determinant=s.factor(J.det())
assert s.simplify(determinant-(2*(1-x)*(A+g*x)-A*y))==0
Y=2-x-u/x
h=s.expand(Y*(A+g*x))
assert s.simplify(s.diff(h,x)-(2*g-A-2*g*x+A*u/x**2))==0
assert s.simplify(s.diff(h,x,2)+2*g+2*A*u/x**3)==0
assert s.simplify(determinant.subs(y,Y)-x*s.diff(h,x))==0
Ycritical=2*(1-t)*(A+g*t)/A
Ucritical=s.factor(F1.subs({x:t,y:Ycritical}))
Vcritical=s.factor(F2.subs({x:t,y:Ycritical}))
assert s.simplify(Ucritical-t*t*(1-2*g/A+2*g*t/A))==0
assert s.simplify(Vcritical-2*(1-t)*(A+g*t)**2/A)==0
v0=(1-Ucritical)*(A+g)
integrand=s.factor((Vcritical-v0)*s.diff(Ucritical,t))
assert s.simplify(integrand-2*t*(t-1)**2*(A+2*g*t-g)*(A+3*g*t-2*g)/A)==0
primitive=s.integrate(integrand,t)
area_below=s.factor(primitive.subs(t,1)-primitive.subs(t,0))
area_above=s.factor(primitive.subs(t,1)-primitive.subs(t,1-A/(2*g)))
assert s.simplify(area_below-(5*A**2-5*A*g+2*g*g)/(30*A))==0
assert s.simplify(area_above-A*A*(A*A-10*A*g+40*g*g)/(480*g**3))==0
assert s.simplify(area_below-area_above-(2*g-A)**5/(480*A*g**3))==0
assert all(s.simplify(s.diff(area_below,g,k).subs(g,A/2)-s.diff(area_above,g,k).subs(g,A/2))==0 for k in range(5))
assert s.simplify(s.diff(area_below,g,5).subs(g,A/2)-s.diff(area_above,g,5).subs(g,A/2)-64/A**4)==0
assert s.simplify(area_below.subs(g,A/2)-A/10)==0
assert s.simplify((A/10)/((A+A/2)/2+A/10)-s.Rational(2,17))==0
r=s.Rational(1,2); gr=s.Rational(1,3); Ar=1-r
p1=(s.Rational(1,2),s.S.One)
p2=(s.sqrt(3)/2,2-2*s.sqrt(3)/3)
for p in (p1,p2):
 assert all([0<p[0]<1,0<p[1]<2-p[0]])
 assert s.simplify(F1.subs({x:p[0],y:p[1]})-s.Rational(1,4))==0
 assert s.simplify(F2.subs({x:p[0],y:p[1],A:Ar,g:gr})-s.Rational(2,3))==0
assert s.simplify(area_above.subs({A:Ar,g:gr})-s.Rational(109,2560))==0
assert s.simplify(area_below.subs({A:Ar,g:s.Rational(1,5)})-s.Rational(83,1500))==0
print('VERIFY_OK jacobian=1 concavity=1 fold_parameter=2 area_cases=2 area_transition_C4_not_C5=1 exact_double_preimage=2 exact_areas=2')
