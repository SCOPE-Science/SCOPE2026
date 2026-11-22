"""Exact checks for exponentially weighted five-node interpolatory quadrature.
Run: python verify.py (Python 3.10+, SymPy 1.12+).
"""
from fractions import Fraction as Q
from math import factorial
import sympy as s

x,k=s.symbols('x k', integer=True, nonnegative=True)
nodes=[s.Rational(j,4) for j in range(5)]
poly=[s.expand(s.prod((x-t)/(nodes[i]-t) for j,t in enumerate(nodes) if j!=i)) for i in range(5)]

# Closed forms for every monomial moment, not just sampled degrees.
def forms(k):
 d=(k+2)*(k+3)*(k+4)*(k+5)
 return [-(k-1)*(3*k*k-5*k+28)/(3*(k+1)*d),
         16*(k*k-3*k+8)/(3*d),
         -4*(3*k*k-5*k-4)/d,
         16*(3*k*k+7*k+8)/(3*d),
         (k+1)*(3*k*k+11*k+28)/(3*d)]

for i,p in enumerate(poly):
 assert s.expand(p.subs(x,nodes[i])-1)==0
 for j,t in enumerate(nodes):
  assert s.expand(p.subs(x,t)-(1 if i==j else 0))==0
 ans=s.factor(sum(co/(k+degree[0]+1) for degree,co in s.Poly(p,x).terms()))
 assert s.factor(ans-forms(k)[i])==0,(i,ans)
for j in range(5):
 for q in range(5):
  assert sum(poly[i].subs(x,nodes[q])*nodes[i]**j for i in range(5))==nodes[q]**j

# The full signed Taylor certificates are exact rational arithmetic.
z=Q(63,20); N=30

def moment(j,r):
 return Q(int(s.numer(forms(s.Integer(r))[j])),int(s.denom(forms(s.Integer(r))[j])))

def partial(j,z,N):
 return sum((moment(j,r)*z**r/Q(factorial(r)) for r in range(N+1)),Q(0))

def polynomial_abs_integral_bound(j):
 pp=s.Poly(poly[j],x)
 return sum((Q(abs(int(co.p)),int(co.q))/Q(deg[0]+1) for deg,co in pp.terms()),Q(0))

# e^4 < 55, with a direct rational geometric tail bound.
E20=sum((Q(4**r,factorial(r)) for r in range(21)),Q(0))
E4bound=E20+Q(4**21,factorial(21))*Q(11,9)
assert E4bound<Q(55)
# Taylor remainder for exp(zx) over x in [0,1].
assert z<Q(4)
for j in [0,2]:
 P=partial(j,z,N)
 R=polynomial_abs_integral_bound(j)*Q(55)*z**(N+1)/Q(factorial(N+1))
 assert P>R if j==0 else P< -R
 print('index',j,'Taylor partial',format(float(P),'.16g'),
       'max remainder',format(float(R),'.3e'))

# Certified brackets of unique positive roots via rational Taylor error.
for j,a,b in [(2,Q(3111841,1000000),Q(3111843,1000000)),
              (0,Q(3225119,1000000),Q(3225122,1000000))]:
 for z0,expected_positive in [(a,True),(b,False)]:
  P=partial(j,z0,42)
  R=polynomial_abs_integral_bound(j)*Q(55)*z0**43/Q(factorial(43))
  assert P>R if expected_positive else P< -R
 print('unique root',j,'bracket',float(a),float(b))

# All signs for integer k follow from explicit polynomials in forms(k).
for r in range(100):
 f=[moment(j,r) for j in range(5)]
 assert all(f[j]>0 for j in [1,3,4])
 assert ((f[0]>0) if r==0 else (f[0]==0 if r==1 else f[0]<0))
 assert ((f[2]>0) if r<=2 else f[2]<0)
print('PASS: polynomial identities, all-degree moments, rigorous Taylor enclosures, and root isolation')
