"""Exact symbolic checks for the cyclic quadratic population-map theorem.
Run: python check.py  (requires SymPy >= 1.10).
Only corroborates the algebra; the analytic proof covers all real parameters.
"""
import sympy as s
R,c,a,b=s.symbols('R c a b',real=True)
P=s.expand((1+R)**2-(R+1)*(R+2)*c+(R+2)*c**2)
assert s.factor(P-1)==(R+2)*(c-1)*(c-R)
assert s.factor(P.subs(c,(R+1)/2))==-(R+1)**2*(R-2)/4
assert s.expand((R+1)**2*(R-2)-4)==R**3-3*R-6
D=s.symbols('D',positive=True)
hi=(R+2+D)/(2*R); lo=(R+2-D)/(2*R)
rel={D**2:R**2-4}
def reduce_rel(e):
 e=s.cancel(s.together(e))
 return s.simplify(s.rem(s.Poly(s.together(e).as_numer_denom()[0],D),s.Poly(D**2-R**2+4,D)).as_expr()/s.together(e).as_numer_denom()[1])
# Logistic two-cycle identity follows from D^2=R^2-4
f=lambda t:(1+R)*t-R*t*t
assert reduce_rel(f(hi)-lo)==0
assert reduce_rel(f(lo)-hi)==0
fp=lambda t:(1+R)-2*R*t
assert reduce_rel(fp(hi)*fp(lo)-(5-R**2))==0
q=s.factor((R+1)/(R*hi))
assert s.simplify((1+R)-R*q*hi)==0
assert reduce_rel(P.subs(c,q))==0
# Each axial Jacobian is triangular; compute its full product symbolically.
x,y,z=s.symbols('x y z',real=True)
F=s.Matrix([x+R*x*(1-x-a*y-b*z),y+R*y*(1-b*x-y-a*z),z+R*z*(1-a*x-b*y-z)])
J=F.jacobian([x,y,z])
Jh=J.subs({x:hi,y:0,z:0});Jl=J.subs({x:lo,y:0,z:0})
full=Jl*Jh
for actual,expected in zip(list(full.diagonal()),[5-R**2,P.subs(c,b),P.subs(c,a)]):
 assert reduce_rel(actual-expected)==0,(actual,expected)
# Rational phase diagram examples: radial <1, stable / unstable / stable.
R0=s.Rational(12,5)
assert abs(5-R0**2)<1
for coef,want in [(s.Rational(11,10),True),(s.Rational(17,10),False),(s.Rational(11,5),True)]:
 actual=abs(P.subs({R:R0,c:coef}))<1
 assert actual==want,(coef,actual,want)
# Positivity threshold separates first and second stable bands.
q0=q.subs({R:R0,D:s.sqrt(R0**2-4)})
assert 1<q0<s.Rational(11,5)
assert s.Rational(11,10)<q0
assert s.Rational(11,5)>q0
print('PASS: exact two-cycle, complete Jacobian, Floquet factors, cubic boundary, and 3 rational-region cases')
