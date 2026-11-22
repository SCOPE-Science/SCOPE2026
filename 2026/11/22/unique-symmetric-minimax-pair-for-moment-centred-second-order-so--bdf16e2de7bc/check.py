#!/usr/bin/env python3
"""Exact-algebra checks for two-point evaluation in a moment-centred H^2 interval.

Uses Python 3 and SymPy. Finite grids corroborate; the global theorem is analytic.
"""
import sympy as S

x,y,u,c,d,h,t = S.symbols('x y u c d h t', real=True)
h0=(1-u)**2/S.Integer(2)
h1=S.Rational(1,3)-u/S.Integer(2)+u**3/S.Integer(6)
def k(z,hinge):
    return S.expand(hinge+(6*z-4)*h0+(6-12*z)*h1)
Kx_left=k(x,x-u); Kx_right=k(x,0)
Ky_left=k(y,y-u); Ky_right=k(y,0)
Gxy=S.factor(S.integrate(Kx_left*Ky_left,(u,0,x)) +
              S.integrate(Kx_right*Ky_left,(u,x,y)) +
              S.integrate(Kx_right*Ky_right,(u,y,1)))
g=S.factor(Gxy.subs(y,x))
assert S.simplify(g- (21*(x*(1-x))**3+28*(x*(1-x))**2-11*x*(1-x)+1)/105)==0
assert S.simplify(g-g.subs(x,1-x))==0
P=63*x**4-126*x**3+7*x**2+56*x-11
assert S.simplify(S.diff(g,x)+(2*x-1)*P/105)==0
assert S.simplify(S.diff(P,x)-14*(2*x-1)*(3*x-4)*(3*x+1))==0
D=S.factor(S.diff(Gxy,x,y).subs(y,x))
assert S.simplify(D-(S.Rational(13,35)-x+2*x**3-x**4))==0
assert D.subs(x,S.Rational(39,200))<S.Rational(1,5)
sub={x:c-d,y:c+d}
A=S.factor(((g+g.subs(x,y)+2*Gxy)/2).subs(sub,simultaneous=True))
B=S.factor(((g+g.subs(x,y)-2*Gxy)/2).subs(sub,simultaneous=True))
A0=(3-120*d**2+320*d**3-80*d**4)/480
B0=d**2*(99-560*d+840*d**2-336*d**4)/840
assert S.simplify(A.subs(c,S.Rational(1,2))-A0)==0
assert S.simplify(B.subs(c,S.Rational(1,2))-B0)==0
p4=1680*d**4-1680*d**2+111+(3360*d**2-700)*h**2+336*h**4
assert S.simplify((A-A0).subs(c,h+S.Rational(1,2))+h**2*p4/840)==0
assert S.simplify((B-B0).subs(c,h+S.Rational(1,2))-
   d**2*(2*h)**2*(6-8*d**2-4*h**2)/8)==0
poly=1344*d**6-3920*d**4+4480*d**3-1236*d**2+21
assert S.simplify(A0-B0-poly/3360)==0
U=S.Rational(41,100000)
d0=S.Rational(188,625)
assert A0.subs(d,d0)<U and B0.subs(d,d0)<U
for endpoint in (S.Rational(39,200),S.Rational(9,40)):
    assert g.subs(x,endpoint)>U
assert (S.Rational(1,24)-S.Rational(1,1200)-S.Rational(21,10**6))/105>S.Rational(1,3000)
assert 2*S.Rational(1,3000)-S.Rational(9,100000)>U
assert p4.subs({h:0,d:S.Rational(11,40)})<-6
assert 3360*S.Rational(61,200)**2-700<0
assert -6 +336*S.Rational(3,200)**4<0
Q=336*d**4-560*d**2+280*d-33
assert Q.subs(d,S.Rational(11,40))>0 and Q.subs(d,S.Rational(61,200))>0
assert S.diff(Q,d,2).subs(d,S.Rational(61,200))<0
assert A0.subs(d,d0)<B0.subs(d,d0)
assert A0.subs(d,S.Rational(301,1000))>B0.subs(d,S.Rational(301,1000))
assert (S.diff(A0,d)).subs(d,d0)>0
root=S.nsolve(poly,S.Rational(3,10),prec=60)
star=A0.subs(d,root).evalf(35)
assert 0.3008<float(root)<0.301
assert .0004098<float(star)<.0004099
assert abs(float(B0.subs(d,root)-star))<1e-30
# Finite-sample lower-bound sanity check, not an exhaustive or infinite proof.
gfn=S.lambdify(x,g,'math');Gfn=S.lambdify((x,y),Gxy,'math')
import math
minimum=1.0
for i in range(0,61):
    xx=i/60
    for j in range(i+1,61):
        yy=j/60
        a,b,z=gfn(xx),gfn(yy),Gfn(xx,yy)
        lam=(a+b+math.hypot(a-b,2*z))/2
        minimum=min(minimum,lam)
assert minimum >float(star)-1e-10
print('PASS: exact kernel, moment Gram, shift identities, rational barriers, and monotonicity checks')
print('PASS: 1,830 finite spectral comparisons (corroborative only)')
print('half-gap',root)
print('sites',S.Rational(1,2)-root,S.Rational(1,2)+root)
print('sharp squared norm',star)
print('sharp norm',S.sqrt(star).evalf(25))
