"""Exact-algebra replay for the McMillan sextupole fourth-period locus.
Run with python checker.py (requires SymPy). The analytic proof is in RESULT.md.
"""
import sympy as s
q,p,a,z=s.symbols('q p a z')
f=lambda t:t*(a-t)/(1+t)
g=lambda t:(a-t)/(1+t)
K=lambda x,y:x*x+y*y-a*x*y+x*y*(x+y)
H=K(q,p)+a
assert s.factor(s.together((f(p)-q-g(q))*(1+p)*(1+q)+H))==0
assert s.factor(s.together(K(p,f(p)-q)-K(q,p)))==0
assert s.factor(s.together(g(g(z))-z))==0
assert s.factor(s.together((f(p)-f(z))/(p-z) -((a+1)/((1+p)*(1+z))-1)))==0
assert s.factor(H.subs(q,-1))==(a+1)*(p+1)
assert s.factor(H.subs(p,-1))==(a+1)*(q+1)
s0=s.symbols('s',positive=True)
sub={a:s0*s0-1}
assert s.factor(H.subs({q:s0-1,p:s0-1}).subs(sub))==-s0**2*(s0-1)*(s0-3)
assert s.factor(H.subs({q:-s0-1,p:-s0-1}).subs(sub))==-s0**2*(s0+1)*(s0+3)
assert s.factor(H.subs({q:s0-1,p:-s0-1}).subs(sub))==s0**2*(s0**2+3)
assert s.factor(H.subs({q:-s0-1,p:s0-1}).subs(sub))==s0**2*(s0**2+3)
for aa,qq,pp in [(11,2,1),(-4,0,2),(-s.Rational(8,5),2,-2),(8,2,2)]:
 assert s.simplify(H.subs({a:aa,q:qq,p:pp}))==0
 xy=(s.Rational(qq),s.Rational(pp))
 for k in range(4):
  x,y=xy
  assert y!=-1
  xy=(y,s.cancel(f(y).subs(a,aa)-x))
 assert xy==(qq,pp)
print('PASS: 4 structural identities, 4 pole/fixed-class computations, rational examples.')
