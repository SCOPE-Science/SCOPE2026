"""Reproducible checks for the natural cubic-spline derivative stability theorem.

Requires Python 3, SymPy, and NumPy. Exact symbolic identities precede
finite sample tests; finite tests are not a proof of uniform optimality.
"""
import sympy as sp
import numpy as np

u=sp.symbols('u', real=True)
s=sp.sqrt(3)
r=2-s
c=1/(2*s)
A=-2+6*u-3*u*u
B=3*u*u-1
p=sp.expand((1+r)*A-(1+1/r)*B)
q=sp.expand((1+1/r)*A-(1+r)*B)
w0=sp.expand(1+(A-B)*c*(1+r))
K=sp.simplify(c*r/(1-r))
assert sp.simplify(4*c-2*r*c-1)==0
assert sp.simplify(1-4*r+r*r)==0
assert sp.simplify(w0-c*r/(1+r)*(p+q)-1)==0  # sum all weights (signed tails)
assert sp.simplify(w0+K*(p-q)-(s-3*(3-s)/s*u*u))==0
assert sp.simplify(w0+K*(p+q)-6*u*(1-u))==0  # central absolute-tail case
assert sp.simplify(w0+K*(-p+q)-(s-3*(3-s)/s*(1-u)**2))==0
ul=(3+s-sp.sqrt(6))/6
ur=(3-s+sp.sqrt(6))/6
assert 0<float(ul)<0.5<float(ur)<1
assert sp.simplify(q.subs(u,ul))==0
assert sp.simplify(p.subs(u,ur))==0
assert sp.simplify(ul+ur-1)==0
assert sp.simplify(r/(1-r)-(s-1)/2)==0
assert sp.simplify((1+s)/(s-1)-(2+s))==0
# For alternating slopes on even-size grids, the first endpoint derivative is
# (a_m-R*a_(m-1))/(a_m-a_(m-1)), with a_0=1,a_1=5 and
# a_{j+1}=4*a_j-a_{j-1}. Verify the identity exactly for many grid sizes.
R=sp.symbols('R',positive=True)
a=[sp.Integer(1),sp.Integer(5)]
for m in range(1,13):
 if m>=2:a.append(4*a[-1]-a[-2])
 n=2*m
 T=sp.diag(*([4]*(n-1)))
 for j in range(n-2):T[j,j+1]=1;T[j+1,j]=1
 d=[sp.Integer(1) if j%2==0 else R for j in range(n)]
 rhs=sp.Matrix([6*(d[j]-d[j-1]) for j in range(1,n)])
 M=T.inv()*rhs
 endpoint=sp.factor(1-M[0]/6)
 desired=(a[m]-R*a[m-1])/(a[m]-a[m-1])
 assert sp.simplify(endpoint-desired)==0
 print('exact alternating witness',n,'sharp ratio',sp.N(a[m]/a[m-1],12))
assert a[-1]/a[-2]>2+sp.sqrt(3)
# independent construction: for increasing data with contrast <= critical,
# check derivative at every knot plus randomly sampled points.
from numpy.random import default_rng
rng=default_rng(20261120)
for n in [2,3,4,6,9,15,30]:
 T=np.diag(np.full(n-1,4.0))
 for j in range(n-2):T[j,j+1]=T[j+1,j]=1.0
 for k in range(100):
  d=rng.uniform(1.0,2+np.sqrt(3),size=n)
  cur=np.zeros(n+1)
  cur[1:n]=np.linalg.solve(T,6*np.diff(d))
  for j in range(n):
   us=np.linspace(0,1,41)
   val=d[j]+(-2+6*us-3*us**2)*cur[j]/6+(3*us**2-1)*cur[j+1]/6
   assert val.min()>-2e-12
print('symbolic identities, 12 rational witnesses, and sampled finite spline derivatives: PASS')
