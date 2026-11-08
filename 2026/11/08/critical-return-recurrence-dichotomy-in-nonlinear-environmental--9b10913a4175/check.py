"""Exact algebraic checks for the critical-return environmental public-goods theorem.

Requires Python 3 and SymPy. The global conclusions rely on the written proof.
"""
import sympy as S
x,p=S.symbols('x p',positive=True)
half=S.Rational(1,2)

def get(N):
    f=(1-p)*(1+half*x)**(N-1)+p*(1-half*x)**(N-1)
    G=f-1
    F=x*(1-x)*G
    P=p*(1-p)*(2*x-1)
    a=half
    A=(1+half*a)**(N-1)
    D=(1-half*a)**(N-1)
    b=S.factor((A-1)/(A-D))
    J=S.Matrix([F,P]).jacobian([x,p]).subs({x:a,p:b})
    B=1/(x**2*(1-x)*p*(1-p))
    div=S.factor(S.diff(B*F,x)+S.diff(B*P,p))
    analytic=S.factor((x*S.diff(G,x)-G)/(x**2*p*(1-p)))
    assert S.simplify(div-analytic)==0
    return b,J,div

p2,J2,div2=get(2)
assert p2==S.Rational(1,2)
assert J2==S.Matrix([[0,-S.Rational(1,8)],[S.Rational(1,2),0]])
assert div2==0
p3,J3,div3=get(3)
assert p3==S.Rational(9,16)
assert J3==S.Matrix([[S.Rational(1,32),-S.Rational(1,4)],[S.Rational(63,128),0]])
assert S.simplify(J3.charpoly().as_expr()-(S.Symbol('lambda')**2-S.Rational(1,32)*S.Symbol('lambda')+S.Rational(63,512)))==0
assert S.simplify(div3-1/(4*p*(1-p)))==0
for N in range(2,6):
    b,J,div=get(N)
    assert S.simplify(div.subs({x:S.Rational(1,3),p:S.Rational(1,3)}))==(0 if N==2 else div.subs({x:S.Rational(1,3),p:S.Rational(1,3)}))
# Differentiate the conserved integral at N=2 directly.
a,b,eps,theta,ds,dd=S.symbols('a b eps theta ds dd',positive=True)
c=S.symbols('c',positive=True)
k=S.symbols('k',positive=True)
H=k*(a/x+(1-a)*S.log(x/(1-x)))-c*(b*S.log(p)+(1-b)*S.log(1-p))
Fx=c*x**2*(1-x)*(b-p)
Pp=k*p*(1-p)*(x-a)
assert S.simplify(S.diff(H,x)*Fx+S.diff(H,p)*Pp)==0
print('PASS: exact rational Jacobians, Dulac identities and pairwise first integral')
