"""Independent algebraic and numerical checks for a two-stage ecological census theorem."""
from fractions import Fraction as F
from math import exp,log,sqrt
import random
import sympy as s
x,p,q=s.symbols('x p q',real=True)
expr=p*x+(1-p)*x**3-q*x**2-(1-q)*x**4
assert s.factor(expr-x*(1-x)*(p+(p-q)*x+(1-q)*x*x))==0
assert s.factor(expr.subs({p:s.Rational(1,10),q:s.Rational(11,20)})-x*(1-x)*(3*x-2)*(3*x-1)/20)==0
for a,c,b,rr1,rr2,w in [(s.Rational(14,5),s.Rational(6,5),s.Rational(9,25),1,3,s.Rational(1,10)),(s.Rational(29,10),s.Rational(31,10),s.Rational(99,100),2,4,s.Rational(11,20))]:
 M=s.Matrix([[-c,b],[1,-a]])
 assert s.factor(M.charpoly().as_expr()-(s.Symbol('lambda')+rr1)*(s.Symbol('lambda')+rr2))==0
 assert -a== -w*rr1-(1-w)*rr2
assert expr.subs({p:F(1,10),q:F(11,20),x:F(1,4)})>0
assert expr.subs({p:F(1,10),q:F(11,20),x:F(1,2)})<0
assert expr.subs({p:F(1,10),q:F(11,20),x:F(3,4)})>0
# numerical phase-map check: solve root discriminant and compare dense positive-time grid
random.seed(4430)
count=0
for _ in range(2000):
 pp=random.uniform(.005,.995);qq=random.uniform(.005,.995)
 pred=(pp<.25 and 2*sqrt(pp)-pp<qq<pp+.5)
 A=1-qq;B=pp-qq;C=pp
 d=B*B-4*A*C
 roots=[] if d<=0 else [(-B-sqrt(d))/(2*A),(-B+sqrt(d))/(2*A)]
 actual=(len(roots)==2 and 0<roots[0]<roots[1]<1)
 assert pred==actual,(pp,qq,pred,roots)
 count+=1
print('PASS: exact identities, two positive biological matrices, witness signs and',count,'phase-map comparisons')
