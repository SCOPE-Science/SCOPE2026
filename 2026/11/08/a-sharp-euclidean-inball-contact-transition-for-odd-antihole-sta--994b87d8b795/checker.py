"""Reproducible finite checks for odd-antihole stable-set polytopes.
Python 3 with numpy and scipy; not a proof of any infinite statement.
"""
from itertools import combinations
from math import sqrt, ceil, comb
import numpy as np
from scipy.optimize import linprog

def data(a):
    n=2*a+1
    # G is the complement of the length-n cycle; stable sets are empty, singletons, or pairs of consecutive vertices of the cycle.
    v=[np.zeros(n)]
    for i in range(n):
        z=np.zeros(n);z[i]=1;v.append(z)
        z=np.zeros(n);z[i]=z[(i+1)%n]=1;v.append(z)
    V=np.asarray(v)
    # Maximal independent subsets of the original cycle = maximal cliques of G
    cand=[]
    for s in range(1,a+1):
      for I in combinations(range(n),s):
        mask=set(I)
        if any((i+1)%n in mask for i in I):continue
        if not all(i in mask or (i-1)%n in mask or (i+1)%n in mask for i in range(n)):continue
        cand.append(I)
    fac=[]; b=[]; fam=[]
    for i in range(n):
      z=np.zeros(n);z[i]=-1;fac.append(z);b.append(0);fam.append(('coordinate',1))
    for I in cand:
      z=np.zeros(n);z[list(I)]=1;fac.append(z);b.append(1);fam.append(('clique',len(I)))
    fac.append(np.ones(n));b.append(2);fam.append(('rank',n))
    return n,V,cand,np.asarray(fac),np.array(b),fam

def check(a):
    n,V,cand,A,b,fam=data(a)
    r=min(1/(a+sqrt(a)),2/(n+sqrt(n)))
    c=np.full(n,r)
    d=(b-A@c)/np.linalg.norm(A,axis=1)
    assert np.min(d)>=r-1e-10
    assert np.all(A@V.T<=b[:,None]+1e-10)
    rank_count=sum(abs(dd-r)<1e-10 and family[0]=='rank' for dd,family in zip(d,fam))
    clique_touch=sum(abs(dd-r)<1e-10 and family[0]=='clique' for dd,family in zip(d,fam))
    coord_touch=sum(abs(dd-r)<1e-10 and family[0]=='coordinate' for dd,family in zip(d,fam))
    assert coord_touch==n
    assert clique_touch==(0 if a<4 else n)
    assert rank_count==(1 if a<=4 else 0)
    shell={s:sum(len(I)==s for I in cand) for s in range(ceil(n/3),a+1)}
    for s,m in shell.items():
       j=n-2*s
       assert m*s==n*comb(s,j)
    # Test each displayed inequality actually defines a facet; all supporting vertices must have affine span n-1.
    for row, rhs in zip(A,b):
       W=V[np.abs(V@row-rhs)<1e-10]
       assert W.shape[0]>=n and np.linalg.matrix_rank(W[1:]-W[0])==n-1
    # Independently maximize inscribed radius using the explicit facet inequalities.
    aug=np.column_stack([A,np.linalg.norm(A,axis=1)])
    obj=np.zeros(n+1);obj[-1]=-1
    ins=linprog(obj,A_ub=aug,b_ub=b,bounds=[(None,None)]*n+[(0,None)],method='highs')
    assert ins.success and abs(ins.x[-1]-r)<1e-9
    assert np.max(np.abs(ins.x[:n]-c))<1e-8
    # Independent LP comparison against actual vertex optimization for deterministic directions.
    rng=np.random.default_rng(1729+a)
    for _ in range(40):
       direction=rng.normal(size=n)
       res=linprog(-direction,A_ub=A,b_ub=b,bounds=[(None,None)]*n,method='highs')
       assert res.success and abs(-res.fun-np.max(V@direction))<1e-8,(a,res.message)
    return (a,n,len(cand),shell,coord_touch,clique_touch,rank_count,round(r,12))

if __name__=='__main__':
  for a in range(2,8):print(check(a))
  print('ODD_ANTIHOL_EUCLIDEAN_INBALL_FINITE_CHECKS_PASSED')
