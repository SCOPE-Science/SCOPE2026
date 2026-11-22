"""Reproduce symbolic and finite sampling checks for a fixed-mean random-step implicit Euler damping theorem.
Requirements: Python 3.9+ and SymPy.
"""
import random
import sympy as sp

x,a,r=sp.symbols('x a r', positive=True)
s=(r-2*a)/r**2
F=lambda z: 1/(1+2*a*z+r**2*z**2)
slope=-r**2/(2*(r-a))
L=lambda z: 1+slope*z
exact_gap=x*(2*a+r**2*x-r)**2/(2*(r-a)*(1+2*a*x+r**2*x**2))
assert sp.factor(F(x)-L(x)-exact_gap)==0
assert sp.factor(F(s)-L(s))==0
assert sp.factor(sp.diff(F(x),x).subs(x,s)-slope)==0
N=4*a*a+6*a*r*r*x+3*r**4*x*x-r*r
assert sp.factor(sp.diff(F(x),x,2)-2*N/(1+2*a*x+r*r*x*x)**3)==0
assert sp.factor(N.subs(x,s)-2*(r-a)*(r-2*a))==0
# Pure rational example: decay a=1, frequency sqrt(99), mean 1/25, optimum H in {0,2/25} equally likely.
subs={a:sp.Integer(1),r:sp.Integer(10)}
assert sp.simplify(s.subs(subs)-sp.Rational(2,25))==0
assert sp.simplify(F(sp.Rational(1,25)).subs(subs)-sp.Rational(25,31))==0
assert sp.simplify((F(0)+F(sp.Rational(2,25))).subs(subs)/2-sp.Rational(7,9))==0
assert sp.Rational(7,9) < sp.Rational(25,31)
# Supplementary checks on random admissible finite support laws, including both regimes.
rng=random.Random(20261116)
checks=0
for ia,ib in [(1,0),(1,1),(1,2),(1,3),(1,5),(1,10),(2,3),(2,10)]:
    aa=float(ia); bb=float(ib); rr=(aa*aa+bb*bb)**.5
    critical=(rr-2*aa)/(rr*rr) if bb*bb>3*aa*aa else 0.
    f=lambda t: 1.0/(1+2*aa*t+rr*rr*t*t)
    for _ in range(2000):
        atoms=[rng.random()*2 for _ in range(4)]
        weights=[rng.expovariate(1) for _ in atoms];sw=sum(weights);weights=[w/sw for w in weights]
        mu=sum(w*h for w,h in zip(weights,atoms))
        claimed=f(mu) if mu>=critical or critical==0 else 1-rr*rr*mu/(2*(rr-aa))
        true=sum(w*f(h) for w,h in zip(weights,atoms))
        assert true>=claimed-2e-14, (aa,bb,mu,claimed,true)
        checks+=1
print('PASS: symbolic rational identities, exact finite example and',checks,'finite-support law checks')
