"""Exact algebraic checks for the transmuted-moment-exponential Laplace factorization.
The continuous-parameter inequalities are proved analytically in RESULT.md;
finite numerical tests here are illustrations, not infinite-dimensional certificates.
"""
from fractions import Fraction
import sympy as s

y, z, a = s.symbols('y z a', real=True)
P = (1+a)*y**3+6*(1+a)*y**2+6*(2+a)*y+8
L = (1-a)/(1+y)**2 + 2*a/(2+y)**2 + 4*a/(2+y)**3
assert s.simplify(L - P/((1+y)**2*(2+y)**3)) == 0
assert s.simplify(s.discriminant(P,y)-432*a*a*(a*a-1))==0
assert s.expand(P.subs(y,-2)) == 4*a
assert s.expand(P.subs(y,-1)) == 1-a
assert s.expand(P.subs(y,-4)) == 8*(a-1)
assert s.factor(P.subs(a,0)) == (y+2)**3
assert s.simplify(P.subs(a,1)-2*(y+4)*(y+1)**2)==0
assert s.simplify(P.subs(a,-1)-(6*y+8))==0
# The density is normalized and gives the source mixed-Poisson mean.
x,beta=s.symbols('x beta', positive=True)
f=x/beta**2*s.exp(-x/beta)*(1-a+2*a*(1+x/beta)*s.exp(-x/beta))
assert s.simplify(s.integrate(f,(x,0,s.oo))) == 1
assert s.simplify(s.integrate(x*f,(x,0,s.oo)) - beta*(2-s.Rational(3,4)*a))==0
# A concrete rational alpha=1/9, beta=1 example
ar=s.Rational(1,9)
assert s.simplify(P.subs(a,ar)-s.Rational(2,9)*(y+3)*(5*y*y+15*y+12))==0
G=s.factor(L.subs({a:ar,y:1-z}))
assert s.simplify(G.subs(z,1))==1
assert s.simplify(G.subs(z,0))==s.Rational(64,243)
logG=s.series(s.log(G/G.subs(z,0)),z,0,7).removeO().expand()
nu=[s.factor(logG.coeff(z,n)) for n in range(1,7)]
assert nu[0]==s.Rational(31,32),nu
assert nu[1]==s.Rational(1453,6144),nu
assert nu[2]==s.Rational(69263,884736),nu
q=s.Rational(1,3)
mu=[s.factor(nu[n-1]-2*q**n/n) for n in range(1,7)]
assert mu[0]==s.Rational(29,96),mu
assert all(t>0 for t in mu),mu
# Check scale-free root regions and derived continuous jump kernel numerically.
import math
for alpha in [-.999,-.9,-.3,-.01,.001,.2,.7,.999]:
    roots=s.nroots(P.subs(a,s.Rational(str(alpha))), maxsteps=100)
    rr=next(complex(v) for v in roots if abs(complex(v).imag)<1e-7)
    pair=next(complex(v) for v in roots if complex(v).imag>1e-7)
    A=-rr.real; B=-pair.real; C=pair.imag
    assert (1<A<2 and 2<B<2.5) if alpha<0 else (2<A<4 and 1<B<2)
    for t in [0, .001,.01,.1,.5,1,2,5,10,30]:
        E=2*math.exp(-t)+math.exp(-2*t)-math.exp(-A*t)-2*math.exp(-B*t)*math.cos(C*t)
        assert E>-2e-12,(alpha,t,E)
print('PASS: Laplace rational identity, cubic discriminant, endpoint degenerations, mixing normalization, mean, six exact count jump coefficients, and illustrative root/jump checks')
print('Example alpha=1/9 beta=1: nu[1:3]=',nu[:3], 'residual mu[1:3]=',mu[:3])
