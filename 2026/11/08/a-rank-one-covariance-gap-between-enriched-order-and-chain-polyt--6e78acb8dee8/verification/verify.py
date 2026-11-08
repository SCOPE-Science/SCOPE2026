import itertools, math
from fractions import Fraction as F
import numpy as np
from scipy.spatial import ConvexHull

def verts(m,n,order):
 A=[tuple(a)+(0,)*n for a in itertools.product((-1,1),repeat=m)]
 B=[(0,)*m+tuple(b) for b in itertools.product((-1,1),repeat=n)]
 if order: A=[a[:m]+(1,)*n for a in A]
 return A+B

def moments(m,n,order):
 V=verts(m,n,order); dim=m+n
 hull=ConvexHull(V)
 # Origin strict interior, exact fan triangulation from boundary facets
 vtot=F(0); sumx=[F(0)]*dim; sumxx=[[F(0)]*dim for _ in range(dim)]
 for inds in hull.simplices:
  W=[[F(z) for z in V[i]] for i in inds]
  D=np.array([[int(z) for z in w] for w in W], dtype=object)
  import sympy as s
  det=abs(int(s.Matrix(D.tolist()).det()))
  if not det: continue
  v=F(det,math.factorial(dim)); vtot+=v
  sumv=[sum(w[j] for w in W) for j in range(dim)]
  for j in range(dim):sumx[j]+=v*sumv[j]/(dim+1)
  for j in range(dim):
   for k in range(dim):
    sumxx[j][k]+=v*(sumv[j]*sumv[k]+sum(w[j]*w[k] for w in W))/((dim+1)*(dim+2))
 mean=[x/vtot for x in sumx]
 cov=[[sumxx[i][j]/vtot-mean[i]*mean[j] for j in range(dim)] for i in range(dim)]
 return vtot,mean,cov

def expected(m,n,order):
 d=m+n; Va=F(2**d*math.factorial(m)*math.factorial(n), math.factorial(d))
 a=F((m+1)*(m+2),3*(d+1)*(d+2)); b=F((n+1)*(n+2),3*(d+1)*(d+2)); rank=F(m*(n+1),(d+1)**2*(d+2)) if order else 0
 mean=[F(0)]*m+([(F((n+1)*F(m+1,d+1)-1,n))]*n if order else [F(0)]*n)
 cov=[[a*int(i==j) if i<m and j<m else (b*int(i==j)+rank if i>=m and j>=m else F(0)) for j in range(d)] for i in range(d)]
 return Va,mean,cov
if __name__=='__main__':
 for m,n in ((1,1),(1,2),(2,1),(1,3),(3,1),(2,2),(2,3),(3,2)):
  for order in (False,True):
   got=moments(m,n,order); want=expected(m,n,order)
   assert got==want,(m,n,order,got,want)
   print((m,n, 'order' if order else 'chain'), 'vol=',got[0], 'var=',[got[2][i][i] for i in range(m+n)])
 print('EXACT_INTEGER_FAN_TRIANGULATION_CHECKS_PASSED')
# Exact parameter-wide algebraic and inequality checks, independent of geometric hull triangulation.
for m in range(1,151):
    for n in range(1,151):
        d=m+n
        a=F((n+1)*(n+2),3*(d+1)*(d+2))
        beta=F(m*(n+1),(d+1)**2*(d+2))
        ratio=1+F(n)*beta/a
        assert ratio==1+F(3*m*n,(d+1)*(n+2))
        assert 1<ratio<4
        reversed_ratio=1+F(3*m*n,(d+1)*(m+2))
        assert (ratio==reversed_ratio)==(m==n)
assert 1+F(3*300**2*300,(300**2+300+1)*(300+2)) > F(39,10)
print('COVARIANCE_RANK_ONE_AND_SHARP_RATIO_CHECKS_PASSED')
