"""Exact symbolic replay of the quadratic-delay period-two identities.
Requires Python 3 and SymPy. No external data or network calls.
"""
from fractions import Fraction
from random import Random
import sympy as S

a,u,v,d,p,q,c=S.symbols('a u v d p q c',real=True)
lam=S.Symbol('lam')
f=lambda x:u*x*x+v*x+d
J=lambda x:S.Matrix([[a,S.diff(f(x),x) if False else v+2*u*x],[1,0]])

# The equations for a primitive two-cycle, using S=p+q and D=(p-q)^2.
s=(1+a-v)/u
P=S.factor((u*s*s+(v+a-1)*s+2*d)/(2*u))
D=S.factor(s*s-4*P)
assert S.simplify(D-(-3*a*a+2*a*v-2*a-4*d*u+v*v-2*v+1)/u**2)==0
assert S.simplify((f(p)-f(q)-(1+a)*(p-q)).subs({v:1+a-u*(p+q)}))==0
M=J(q)*J(p)
tr=S.trace(M);det=M.det()
assert S.expand(tr-(a*a+f(p).diff(p)+f(q).diff(q)))==0
assert S.factor(tr.subs({v:1+a-u*(p+q)})-(1+(a+1)**2))==0
assert S.factor(det.subs({v:1+a-u*(p+q)})-((a+1)**2-u*u*(p-q)**2))==0
char=S.factor(lam**2-tr*lam+det)
assert S.factor(char.subs({v:1+a-u*(p+q)})-((lam-1)*(lam-(a+1)**2)-u*u*(p-q)**2))==0

# Complete census for the original two-parameter map.
cc=S.symbols('cc',real=True,nonzero=True)
Dmodel=S.factor(D.subs({u:-cc,v:cc,d:0}))
assert S.factor(Dmodel-(cc-1-a)*(cc-1+3*a)/cc**2)==0

# Exact saddle-to-repeller threshold for the two-parameter specialization.
h=cc-1+a
Q=6*a*a+4*a+4
K=S.factor((cc-1-a)*(cc-1+3*a))
assert S.factor(K-(h*h-4*a*a))==0
assert S.factor((4*a*a+2*(1+(1+a)**2))-Q)==0
assert S.factor((Q-4*a*a)-2*((a+1)**2+1))==0

# A rational cycle on the side of the origin flip previously identified as stable.
aa=S.Rational(-1,5); c0=S.Rational(79,100)
pp=S.Rational(4,79);qq=S.Rational(-5,79)
ff=lambda z:c0*z*(1-z)
assert pp==aa*qq+ff(pp) and qq==aa*pp+ff(qq)
L=(J(qq)*J(pp)).subs({a:aa,u:-c0,v:c0})
assert S.factor(L.charpoly(lam).as_expr()-(lam**2-S.Rational(41,25)*lam+S.Rational(6319,10000)))==0
assert S.factor((1-L.trace()+L.det())+S.Rational(81,10000))==0

# Deterministic sample checks for exact existence and Floquet polynomials.
rng=Random(325700)
count=0
for k in range(300):
    A=Fraction(rng.randrange(-19,20),rng.randrange(1,11))
    U=Fraction(rng.choice([-1,1])*rng.randrange(1,20),rng.randrange(1,11))
    V=Fraction(rng.randrange(-19,20),rng.randrange(1,11))
    E=Fraction(rng.randrange(-19,20),rng.randrange(1,11))
    S0=(1+A-V)/U
    P0=(U*S0*S0+(V+A-1)*S0+2*E)/(2*U)
    D0=S0*S0-4*P0
    if D0<=0:continue
    # Work with exact algebraic roots, no numerical inference.
    pp0=(S.Rational(S0.numerator,S0.denominator)+S.sqrt(S.Rational(D0.numerator,D0.denominator)))/2
    qq0=(S.Rational(S0.numerator,S0.denominator)-S.sqrt(S.Rational(D0.numerator,D0.denominator)))/2
    ass=S.Rational(A.numerator,A.denominator)
    uss=S.Rational(U.numerator,U.denominator)
    vss=S.Rational(V.numerator,V.denominator)
    ess=S.Rational(E.numerator,E.denominator)
    ff0=lambda t:uss*t*t+vss*t+ess
    assert S.simplify(pp0-ass*qq0-ff0(pp0))==0
    assert S.simplify(qq0-ass*pp0-ff0(qq0))==0
    actual=(J(qq0)*J(pp0)).subs({a:ass,u:uss,v:vss,d:ess})
    expected=(lam-1)*(lam-(ass+1)**2)-uss**2*(pp0-qq0)**2
    assert S.simplify(actual.charpoly(lam).as_expr()-expected)==0
    count+=1
print('PASS: symbolic period-two census and Floquet identity; exact rational example; samples', count)
