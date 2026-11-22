"""Algebraic and numerical diagnostics for the discrete commensal fold--flip clock.

Run: python verify.py  (requires SymPy).
These checks support algebra; the convergence theorem is proved separately.
"""
import math
import sympy as s

A,d,v,p=s.symbols('A d v p', real=True)
y0=(1-A)/2
B=(1+A)/2
M=B**2
# Exact additive-Allee fold identity.
y=y0+d
assert s.factor(1-y-M/(y+A)+d**2/(y+A)) == 0
hoststep=s.series(y*s.exp(-d*d/(B+d))-y0,d,0,4).removeO().expand()
assert s.simplify(hoststep.coeff(d,1)-1)==0
assert s.simplify(hoststep.coeff(d,2)+y0/B)==0

# Coefficients at equal one-step forcing p, for the two-step flip map.
def h(z): return (2+p+z)*s.exp(-z)-2-p
h0=s.series(h(v),v,0,6).removeO()
h2=s.series(h(h0),v,0,5).removeO().expand()
assert s.simplify(h2.coeff(v,0))==0
assert s.simplify(h2.coeff(v,1)-(1+p)**2)==0
assert s.simplify(h2.coeff(v,2).subs(p,0))==0
assert s.simplify(h2.coeff(v,3).subs(p,0)+s.Rational(1,3))==0
assert s.simplify(h2.coeff(v,4).subs(p,0))==0
assert s.simplify(s.diff(h2.coeff(v,2),p).subs(p,0))==0

# Direct simulations in two different positive-parameter chambers.
def run(A, beta, sign, n=120000):
    ys=(1-A)/2
    alpha=2-beta*ys
    assert 0<A<1 and alpha>0 and beta>0
    C=(1+A)/(1-A)
    K=beta*C
    W=3*(1+2*K)
    t=5000.
    Y=ys+C/t
    X=2+beta*(Y-ys)+sign*math.sqrt(W/t)
    for j in range(n):
        # One-step map in original ordering, exact parameter relation M=(1+A)^2/4.
        XX=X*math.exp(alpha-X+beta*Y)
        YY=Y*math.exp(1-Y-((1+A)**2/4)/(Y+A))
        X,Y=XX,YY
    osc=sign*((-1)**n)*math.sqrt(n)*(X-2)
    host=n*(Y-ys)
    assert abs(host-C)/C < 0.1, (A,beta,host,C)
    assert abs(osc-math.sqrt(W))/math.sqrt(W) < 0.1, (A,beta,sign,osc,math.sqrt(W))
    return (A,beta,sign,round(osc,7),round(math.sqrt(W),7),round(host,7),round(C,7))
for A1,beta1 in [(1/3,1),(3/5,4/5)]:
    for sg in (-1,1):
        print('diagnostic',run(A1,beta1,sg))
print('FOLD_FLIP_COUPLED_CLOCK_VERIFY_OK')
