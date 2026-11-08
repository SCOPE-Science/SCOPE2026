from fractions import Fraction as F
from math import factorial, comb
from itertools import combinations
import numpy as np
from scipy.spatial import Delaunay
import sympy as s

def f0(n,r):
 return sum(((-1)**k)*comb(n,k)*F((r-k)**(n-1),factorial(n-1)) for k in range(r))
def f2(n,r):
 z=F(0)
 for k in range(r):
  t=r-k
  z+=(-1)**k*(comb(n,k)*F(2*t**(n+1),factorial(n+1)) + (comb(n-1,k-1) if k>=1 else 0)*(F(2*t**n,factorial(n))+F(t**(n-1),factorial(n-1))))
 return z

def theory(n,r,Hs):
 Hs=[set(H) for H in Hs]; lam=len(Hs); D=[sum(i in H for H in Hs) for i in range(n)]; C=[[sum(i in H and j in H for H in Hs) for j in range(n)] for i in range(n)]
 eta=F(comb(n-2,r-1),(factorial(n-1)*f0(n,r)))
 z=1-lam*eta
 if z<=0:raise ValueError('degenerate')
 U1=F(r,n); U2=f2(n,r)/f0(n,r); U11=(r*r-n*U2)/F(n*(n-1))
 a=r;b=n-r
 s1=F(n-1,n);s2=F(n-1,n+1)
 h1=1-s1/a;l1=s1/b
 hh=1-2*s1/a+s2/F(a*(a+1));hl=s1/b-s2/F(a*b);ll=s2/F(b*(b+1))
 h2=1-2*s1/a+2*s2/F(a*(a+1));l2=2*s2/F(b*(b+1))
 means=[(U1-eta*(lam*l1+(h1-l1)*D[i]))/z for i in range(n)]
 second=[[None]*n for _ in range(n)]
 for i in range(n):
  for j in range(n):
   if i==j: second[i][j]=(U2-eta*(lam*l2+(h2-l2)*D[i]))/z
   else: second[i][j]=(U11-eta*(lam*ll+(hl-ll)*(D[i]+D[j])+(hh-2*hl+ll)*C[i][j]))/z
 cov=[[second[i][j]-means[i]*means[j] for j in range(n)] for i in range(n)]
 return F(factorial(n-1))*f0(n,r)*z,means,cov,eta

def direct(n,r,Hs):
 pts=np.array([tuple(1 if i in B else 0 for i in range(n)) for B in combinations(range(n),r) if set(B) not in [set(H) for H in Hs]],dtype=np.int64)
 tris=Delaunay(pts[:,:-1].astype(float),qhull_options='QJ').simplices
 vol=0;mu=[F(0)]*n; raw=[[F(0)]*n for _ in range(n)]
 for T in tris:
  V=pts[T]
  d=n-1
  det=abs(int(s.Matrix((V[1:,:-1]-V[0,:-1]).T).det()))
  if det==0:continue
  vol+=det
  sm=list(map(int,V.sum(axis=0))); G=V.T@V
  for i in range(n):
   mu[i]+=F(det*sm[i],n)
   for j in range(n):raw[i][j]+=F(det*(sm[i]*sm[j]+int(G[i,j])),n*(n+1))
 mean=[x/vol for x in mu]
 cov=[[raw[i][j]/vol-mean[i]*mean[j] for j in range(n)] for i in range(n)]
 return vol,mean,cov,len(tris)


if __name__ == '__main__':
    # The direct method is deliberately separate from cap integration.
    cases = [
        (5, 2, [(0,1)]),
        (6, 3, [(0,1,2)]),
        (6, 3, [(0,1,2),(3,4,5)]),
        (6, 3, [(0,1,2),(0,3,4)]),
        (7, 3, [(0,1,2),(0,3,4),(1,3,5)]),
    ]
    total_simplices = 0
    for n,r,H in cases:
        vol,mean,cov,eta=theory(n,r,H)
        dvol,dmean,dcov,ns=direct(n,r,H)
        assert vol==dvol, (n,r,H,'volume',vol,dvol)
        assert mean==dmean, (n,r,H,'mean',mean,dmean)
        assert cov==dcov, (n,r,H,'covariance')
        total_simplices+=ns
    # Complementing every basis indicator implements matroid duality.
    for n,r,H in cases:
        vol,mean,cov,eta=theory(n,r,H)
        comp=[tuple(sorted(set(range(n))-set(h))) for h in H]
        v2,m2,c2,e2=theory(n,n-r,comp)
        assert vol==v2 and e2==eta
        assert all(mean[i]+m2[i]==1 for i in range(n))
        assert cov==c2
    # Two-design on seven points: cyclic difference set {0,1,3}.
    fano=[tuple((s+i)%7 for i in (0,1,3)) for s in range(7)]
    vol,mean,cov,eta=theory(7,3,fano)
    assert vol==232 and all(x==F(3,7) for x in mean)
    assert all(cov[i][i]==F(3135,45472) for i in range(7))
    assert all(cov[i][j]==F(-1045,90944) for i in range(7) for j in range(7) if i!=j)
    assert sum(cov[0])==0
    # Sharp centroid separation of Ehrhart twins.
    a=theory(6,3,[(0,1,2),(3,4,5)])
    b=theory(6,3,[(0,1,2),(0,3,4)])
    assert a[0]==b[0]==54
    assert a[1]==[F(1,2)]*6
    assert b[1]==[F(73,162),F(1,2),F(1,2),F(1,2),F(1,2),F(89,162)]
    # Prove the pair-codegree coefficient identity algebraically.
    R,B,U,V=s.symbols('R B U V',integer=True,positive=True)
    N=R**2*B**2-R**2*B-R**2-R*B**2+R*B+R-B**2+B
    poly=U**2*V**2+3*U**2*V+U**2+3*U*V**2+9*U*V+3*U+V**2+3*V
    assert s.expand(N.subs({R:U+2,B:V+2})-poly)==0
    for n in range(5,18):
        for r in range(2,n-1):
            b=n-r; u=r-2; v=b-2
            assert poly.subs({U:u,V:v})>0
    print('SPARSE_PAVING_CONTINUOUS_MOMENTS_CHECKS_PASSED',len(cases),total_simplices)
