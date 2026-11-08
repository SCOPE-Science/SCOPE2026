"""Exact symbolic certificates for RK4 positivity on the three-subset Kneser graph.
Run: python verify.py (requires SymPy); NumPy is not required.
"""
from itertools import combinations
from fractions import Fraction
import sympy as S
n,x,z=S.symbols('n x z', integer=True)
B=lambda u,k:S.prod(u-i for i in range(k))/S.factorial(k)
d=S.factor(B(n-3,3))
M=S.Matrix([[sum(B(3-r,s)*B(n-6+r,3-s) if s==t else 0 for s in range(4)) for t in range(4)] for r in range(4)])
powers=[S.Matrix([0,0,0,1])]
for j in range(4):powers.append(M*powers[-1])
p=[]
for r in range(4):
 p.append(S.factor(sum(x**j/S.factorial(j)*sum(S.binomial(j,k)*(-1)**(j-k)*powers[k][r]/d**k for k in range(j+1)) for j in range(5))))
assert S.simplify(p[0].coeff(x,0))==0
checks=0
# Every shifted polynomial coefficient is positive, proving signs for ALL real n>=9.
def positive_shift(f):
 global checks
 f=S.factor(f)
 num,den=S.fraction(f)
 assert den.subs(n,9)>0
 assert all(c>=0 for c in S.Poly(S.expand(den.subs(n,z+9)),z).all_coeffs())
 assert all(c>0 for c in S.Poly(S.expand(num.subs(n,z+9)),z).all_coeffs())
 checks+=1
f=S.cancel(p[0]/x)
c=[S.factor(S.diff(f,x,j).subs(x,0)/S.factorial(j)) for j in range(4)]
positive_shift(c[0]);positive_shift(-c[1]);positive_shift(c[2]);positive_shift(-c[3]);
dis0=S.factor(S.discriminant(S.diff(f,x),x))
positive_shift(-dis0)
for r in [1,2]:
 q=S.cancel(p[r]/x**2)
 v=[S.factor(S.diff(q,x,j).subs(x,0)/S.factorial(j)) for j in range(3)]
 positive_shift(v[0]);positive_shift(v[2]);positive_shift(-S.factor(S.discriminant(q,x)))
# Check distance-regular walk recurrence directly against A powers for several graph orders.
mat_checks=0
for N in [9,10,11]:
 vertices=list(combinations(range(N),3));K=len(vertices)
 adj=[[int(not set(a).intersection(b)) for b in vertices] for a in vertices]
 current=[[int(i==j) for j in range(K)] for i in range(K)]
 M_N=M.subs(n,N)
 vals=[S.Matrix([0,0,0,1])]
 for k in range(4):vals.append(M_N*vals[-1])
 origin=vertices[0]
 row=[int(i==0) for i in range(K)]
 for j in range(5):
  for vidx,v in enumerate(vertices):
   r=len(set(origin)&set(v))
   assert row[vidx]==vals[j][r],(N,j,vidx)
   mat_checks+=1
  if j<4:
   row=[sum(row[i]*adj[i][v] for i in range(K)) for v in range(K)]
print('VERIFY_OK',checks,'universal shifted-sign certificates;',mat_checks,'direct adjacency-power entries; positivity for all integer n>=9')
