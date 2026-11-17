import numpy as np
from scipy.linalg import null_space
from scipy.optimize import linprog
from math import sqrt, isclose

def test(m,n,k):
 p=m*n
 # fixed rank either sum= k or row sums=1
 if k<m:
  E=np.ones((1,p))
  c=np.full(p,k/p)
 else:
  E=np.zeros((m,p))
  for i in range(m): E[i,i*n:(i+1)*n]=1
  c=np.full(p,1/n)
 B=null_space(E)
 rows=[]; limits=[]; types=[]
 for a in range(m):
  for b in range(n):
   v=np.zeros(p);v[a*n+b]=-1
   rows.append(v);limits.append(0);types.append('cell')
 if k<m:
  for a in range(m):
   v=np.zeros(p);v[a*n:(a+1)*n]=1
   rows.append(v);limits.append(1);types.append('row')
 for b in range(n):
  v=np.zeros(p);v[b::n]=1
  rows.append(v);limits.append(1);types.append('col')
 A=np.array(rows); b=np.array(limits)
 norms=np.linalg.norm(A@B,axis=1)
 A_ub=np.hstack((A@B,norms[:,None]))
 cb=np.r_[np.zeros(B.shape[1]),-1.]
 res=linprog(cb,A_ub=A_ub,b_ub=b-A@c,bounds=[(None,None)]*B.shape[1]+[(0,None)],method='highs')
 assert res.success,(m,n,k,res.message)
 if k<m:
  r_cell=k/sqrt(p*(p-1))
  r_row=(m-k)/sqrt(p*(m-1))
  r_col=(n-k)/sqrt(p*(n-1))
  pred=min(r_cell,r_row)
  assert r_row<=r_col+1e-10
 else:
  r_cell=1/sqrt(n*(n-1))
  r_col=(n-m)/sqrt(m*n*(n-1))
  pred=min(r_cell,r_col)
 assert abs(res.x[-1]-pred)<1e-8,(m,n,k,res.x[-1],pred)
 tight=np.abs(b-A@c-norms*pred)<1e-8
 T=A[tight]@B
 computed_dim=B.shape[1]-np.linalg.matrix_rank(T,tol=1e-8)
 if k<m:
  dim=0 if r_cell<=r_row+1e-12 else m*(n-1)
 else:
  dim=0 if r_cell<=r_col+1e-12 else (m-1)*(n-1)
 assert computed_dim==dim,(m,n,k,computed_dim,dim)
 return (m,n,k,round(pred,8),dim,types.count('cell'),sum(tight))

if __name__=='__main__':
 out=[]
 for m in range(2,9):
  for n in range(m+1,m+6):
   for k in range(1,m+1):out.append(test(m,n,k))
 assert (5-1)**3 == 5*13-1
 assert 4**2*(5-1)==(5-4)**2*(5*13-1)
 assert (6-4)**2 == 4
 assert (8-1)**3 > 8*9-1
 print('RECT_ASSIGNMENT_INBALL_CHECKS_PASSED cases=',len(out))
