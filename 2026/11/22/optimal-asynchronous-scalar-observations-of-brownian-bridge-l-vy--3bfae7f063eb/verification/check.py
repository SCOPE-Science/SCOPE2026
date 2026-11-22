"""Reproducible algebra and independent finite tests for two-coordinate area sensing.

Requires sympy. Algebraic identities support the self-contained proof; numerical
checks are supplementary and do not establish the all-parameter inequalities.
"""
import random
from fractions import Fraction
import sympy as sp

x, eta, a, b, g, p, q = sp.symbols('x eta a b g p q', positive=True)
r = sp.symbols('r', real=True)
K = lambda z, z0: sp.Piecewise((z * (1-z0), z <= z0), (z0 * (1-z), True))
# Exact covariance for s<t: only the middle interval contributes.
s, t = sp.symbols('s t', positive=True)
assert sp.simplify(sp.integrate(s*(1-t), (r,s,t)) - s*(1-t)*(t-s)) == 0
# The area variance follows from independent bridge innovation martingales.
assert sp.integrate(2*r*(1-r), (r,0,1)) == sp.Rational(1,3)
# Exact reduced observation denominator (multiply by common squared time margins).
tau = a*b
u1 = a*(1-a)
u2 = b*(1-b)
D_direct = (u1 + 1/p)*(u2 + 1/q)/(a*a*b*b)
D_reduced = 1+g/tau + ((1+g/b)/q + (1+g/a)/p)/tau + 1/(tau*tau*p*q)
assert sp.factor((D_direct-D_reduced).subs({g:1-a-b})) == 0
# Derivative of the centered one-variable objective.
h = x*x*(1-2*x)/(x*(1-x)+eta)
stationarity = x*(2*x*x-4*x+1)+2*eta*(1-3*x)
assert sp.factor(sp.diff(h,x) - x*stationarity/(x*(1-x)+eta)**2) == 0
# The square-root Jensen function is strictly convex for every positive gap.
y = sp.symbols('y', positive=True)
f = sp.sqrt(1+g/y)
assert sp.simplify(sp.diff(f,y,2)-g*(3*g+4*y)/(4*y**sp.Rational(5,2)*(g+y)**sp.Rational(3,2))) == 0
r0=1-1/sp.sqrt(2)
assert sp.simplify((h.subs({x:r0, eta:0}))**2-(17-12*sp.sqrt(2))) == 0
# Exact discrete-covariance sums reproduce the continuum formula on aligned meshes.
for n in (6,9,12,30):
  t1=Fraction(1,3); t2=Fraction(2,3)
  def ker(z,z0): return min(z,z0)-z*z0
  c=Fraction(0)
  for i in range(n):
    z=Fraction(i,n); zn=Fraction(i+1,n)
    c+=ker(z,t1)*(ker(zn,t2)-ker(z,t2))-ker(z,t2)*(ker(zn,t1)-ker(z,t1))
  assert c==Fraction(1,27),(n,c)
# Direct objective (not the reduced one): compare random designs to the unique optimum.
def optx(P):
  # Stationarity polynomial is strictly decreasing on (1-1/sqrt(2),1/3).
  lo=1-1/2**0.5; hi=1/3
  et=2/P
  for _ in range(90):
    m=(lo+hi)/2
    poly=m*(2*m*m-4*m+1)+2*et*(1-3*m)
    if poly>0:lo=m
    else:hi=m
  return (lo+hi)/2

def gain(s,t,p,q):
  D=s*(1-t)*(t-s) if s<t else -t*(1-s)*(s-t)
  return D*D/((s*(1-s)+1/p)*(t*(1-t)+1/q))
rg=random.Random(0x1866)
for P in (0.01,0.3,1,5,15,100,10000):
  z=optx(P)
  best=gain(z,1-z,P/2,P/2)
  assert best>0
  for _ in range(12000):
    s=rg.random();t=rg.random(); pp=P*(1e-8+(1-2e-8)*rg.random())
    val=gain(s,t,pp,P-pp)
    assert val <= best+2e-15,(P,s,t,pp,val,best)
print('PASS: six symbolic/exact identities, four exact mesh covariances, and 84,000 independent random-budget comparisons')
