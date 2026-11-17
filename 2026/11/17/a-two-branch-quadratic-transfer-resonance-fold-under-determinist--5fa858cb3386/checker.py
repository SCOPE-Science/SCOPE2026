"""Exact algebra and independent full-branch quadrature for a seasonal skew-tent map."""
from itertools import product
import sympy as sp
import mpmath as mp

x,a,b=sp.symbols('x a b',real=True)
u=x-sp.Rational(1,2)
v=x*x-x+sp.Rational(1,6)
L=lambda p,t:sp.expand(t*sp.sympify(p).subs(x,t*x)+(1-t)*sp.sympify(p).subs(x,1-(1-t)*x))
g=lambda t:2*t-1
h=lambda t:3*t*t-3*t+1
c=lambda t:t*(1-t)
assert sp.expand(L(u,a)-g(a)*u)==0
assert sp.expand(L(v,a)-(h(a)*v-c(a)*u))==0
assert sp.expand(L(u,b)-g(b)*u)==0
assert sp.expand(L(v,b)-(h(b)*v-c(b)*u))==0
lam1=sp.expand(g(a)*g(b))
lam2=sp.expand(h(a)*h(b))
C=sp.expand(-(c(a)*g(b)+h(a)*c(b)))
assert sp.expand(L(L(v,a),b)-(lam2*v+C*u))==0
assert sp.expand(L(L(u,a),b)-lam1*u)==0
assert sp.integrate(u*u,(x,0,1))==sp.Rational(1,12)
assert sp.integrate(v*v,(x,0,1))==sp.Rational(1,180)
assert sp.integrate(u*v,(x,0,1))==0
astar=(9+4*sp.sqrt(3)-sp.sqrt(21))/18
bzero=(3+sp.sqrt(3))/6
assert sp.simplify(g(astar)/h(astar)-sp.sqrt(3)/2)==0
assert sp.simplify(g(bzero)/h(bzero)-2/sp.sqrt(3))==0
aval=sp.Rational(13,20)
bchoices=[sp.Rational(207,254)-sp.sqrt(9213)/762,sp.Rational(207,254)+sp.sqrt(9213)/762]
for bv in bchoices:
    assert sp.simplify(lam1.subs({a:aval,b:bv})-lam2.subs({a:aval,b:bv}))==0
    assert sp.Rational(2,3)<bv<1

mp.mp.dps=70
nodes=[(1-mp.sqrt(mp.mpf(3)/5))/2,mp.mpf('0.5'),(1+mp.sqrt(mp.mpf(3)/5))/2]
weights=[mp.mpf(5)/18,mp.mpf(4)/9,mp.mpf(5)/18]
w=lambda t:t*t-mp.mpf(1)/3
cases=0
for bv in bchoices:
    aa=mp.mpf(13)/20;bb=mp.mpf(str(sp.N(bv,70)))
    gg=lambda t:2*t-1
    hh=lambda t:3*t*t-3*t+1
    ll=gg(aa)*gg(bb)
    cc=-(aa*(1-aa)*gg(bb)+hh(aa)*bb*(1-bb))
    assert abs(ll-hh(aa)*hh(bb))<mp.mpf('1e-65')
    sign_transition=16*ll/(15*abs(cc))
    if bv==bchoices[0]: assert mp.mpf('0.78')<sign_transition<mp.mpf('0.80')
    else: assert mp.mpf('1.28')<sign_transition<mp.mpf('1.31')
    inverse=[(mp.mpf(0),aa*bb),(aa,-aa*(1-bb)),(aa,(1-aa)*(1-bb)),(mp.mpf(1),-(1-aa)*bb)]
    transforms=[(mp.mpf(0),mp.mpf(1))]
    for n in range(1,5):
        transforms=[(off+s*c0,s*d0) for off,s in transforms for c0,d0 in inverse]
        direct=mp.fsum(abs(s)*mp.fsum(w(off+s*y)*w(y)*wt for y,wt in zip(nodes,weights)) for off,s in transforms)
        formula=mp.mpf(4)/45*ll**n+mp.mpf(n)/12*cc*ll**(n-1)
        assert abs(direct-formula)<mp.mpf('2e-55'),(n,direct,formula)
        cases+=1
print('SEASONAL_SKEW_TENT_JORDAN_OK symbolic_operator=PASS exact_resonance=2 full_branch_correlation_cases='+str(cases))
