"""Exact and finite diagnostic checks for a two-zone affine Filippov flow.
Requires Python 3 and sympy. The analytic arguments are in RESULT.md.
"""
import sympy as S

x, y, a, d, t = S.symbols('x y a d t', real=True)
left = (2*x-y+1, 3*x-2*y+1)
right = (x/S.Integer(2)+y+a, x+y/S.Integer(2)+d)
Hleft = 3*x*x+y*y-4*x*y+2*x-2*y
Hright = (x+y+S.Rational(2,3)*(a+d))*(y-x+2*(a-d))**3
for H, field in [(Hleft,left),(Hright,right)]:
    assert S.factor(S.diff(H,x)*field[0]+S.diff(H,y)*field[1])==0
assert S.factor(Hleft.subs(x,0)-y*(y-2))==0
assert left[0].subs(x,0)==1-y
assert right[0].subs(x,0)==y+a
assert S.Matrix([[2,-1],[3,-2]]).eigenvals()=={-1:1,1:1}
assert S.Matrix([[S.Rational(1,2),1],[1,S.Rational(1,2)]]).eigenvals()=={S.Rational(-1,2):1,S.Rational(3,2):1}

sqrt5=S.sqrt(5)
delta=2/sqrt5
phi=(1+sqrt5)/2
lo=1-delta
hi=1+delta
a0=-S.Rational(5,4)
d0=-S.Rational(7,4)
assert S.simplify(S.Rational(2,3)*(a0+d0)+2)==0
assert S.simplify(2*(a0-d0)-1)==0
assert S.simplify(Hright.subs({a:a0,d:d0,x:0,y:lo})-Hright.subs({a:a0,d:d0,x:0,y:hi}))==0
assert S.simplify(Hleft.subs({x:0,y:lo})-Hleft.subs({x:0,y:hi}))==0

# Normal components have opposite signs at each advertised contact.
assert delta>0 and delta>S.Rational(1,4)
normals = [(S.simplify(left[0].subs({x:0,y:z})),S.simplify(right[0].subs({x:0,y:z,a:a0}))) for z in [lo,hi]]
assert normals==[(delta,-S.Rational(1,4)-delta),(-delta,delta-S.Rational(1,4))]

# Exact flow coordinates of both arcs, starting at the upper contact.
XL=((1+delta)*S.exp(-t)+(1-delta)*S.exp(t)-2)/2
YL=(3*(1+delta)*S.exp(-t)+(1-delta)*S.exp(t)-2)/2
XR=((delta-1)*S.exp(S.Rational(3,2)*t)-(2+delta)*S.exp(-t/2)+3)/2
YR=((delta-1)*S.exp(S.Rational(3,2)*t)+(2+delta)*S.exp(-t/2)+1)/2
assert S.simplify(S.diff(XL,t)-left[0].subs({x:XL,y:YL}))==0
assert S.simplify(S.diff(YL,t)-left[1].subs({x:XL,y:YL}))==0
assert S.simplify(S.diff(XR,t)-right[0].subs({x:XR,y:YR,a:a0}))==0
assert S.simplify(S.diff(YR,t)-right[1].subs({x:XR,y:YR,d:d0}))==0
assert S.simplify(XL.subs(t,0))==0
assert S.simplify(XR.subs(t,0))==0
assert S.simplify(YL.subs(t,0)-hi)==0
assert S.simplify(YR.subs(t,0)-hi)==0
# Test exact exponentials rather than floating log simplifications.
TLratio=S.simplify(phi**6)
TRratio=S.simplify(phi**2)
assert S.simplify(TLratio-(1+delta)/(1-delta))==0
assert S.simplify(TRratio-(2+delta)/(2-delta))==0
assert S.simplify(XL.subs(t,S.log(TLratio)))==0
assert S.simplify(YL.subs(t,S.log(TLratio))-lo)==0
assert S.simplify(XR.subs(t,S.log(TRratio**2)))==0
assert S.simplify(YR.subs(t,S.log(TRratio**2))-lo)==0

# Filippov sliding field on x=0 at the benchmark parameters.
pL=1-y;pR=y+a0;qL=1-2*y;qR=y/S.Integer(2)+d0
slide=S.factor((-pR*qL+pL*qR)/(pL-pR))
assert S.factor(slide-(6*y*y-5*y-2)/(9-8*y))==0
y_star=(5-S.sqrt(73))/12
assert S.simplify(slide.subs(y,y_star))==0
assert S.simplify(S.diff(slide,y).subs(y,y_star)+3*S.sqrt(73)/(17+2*S.sqrt(73)))==0
assert float(y_star)<1 and float((5+S.sqrt(73))/12)>1
assert float(S.diff(slide,y).subs(y,y_star))<0

# Finite diagnostics only; exact universal statements are proved analytically.
import math
TL=6*math.log(float(phi))
TR=4*math.log(float(phi))
for k in range(1,40):
    tl=TL*k/40; tr=TR*k/40
    assert float(XL.subs(t,tl))<0
    assert float(XR.subs(t,tr))>0
print('ONE_WAY_FILIPPOV_VERIFY_OK')
print('left_flight=6log(phi), right_flight=4log(phi), sliding_equilibrium=',y_star)
