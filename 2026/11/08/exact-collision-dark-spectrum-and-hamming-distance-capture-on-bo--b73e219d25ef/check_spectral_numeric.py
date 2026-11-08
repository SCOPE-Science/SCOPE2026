import numpy as np, itertools, math
from scipy.linalg import eigh

def test(d):
 n=1<<d
 A=np.zeros((n,n))
 for x in range(n):
  for i in range(d): A[x,x^(1<<i)]=1.
 Hordered=np.kron(A,np.eye(n))+np.kron(np.eye(n),A)
 pairs=[(i,j) for i in range(n) for j in range(i,n)]
 U=np.zeros((n*n,len(pairs)))
 for t,(i,j) in enumerate(pairs):
  if i==j:U[i*n+j,t]=1
  else:U[i*n+j,t]=U[j*n+i,t]=1/np.sqrt(2)
 H=U.T@Hordered@U
 E,Q=eigh(H)
 loss=np.array([i==j for i,j in pairs])
 pdark=np.zeros_like(H)
 i=0
 while i<len(E):
  j=i+1
  while j<len(E) and abs(E[j]-E[i])<1e-8: j+=1
  v=Q[:,i:j]; gram=v[loss,:].T@v[loss,:]
  g,w=eigh(gram);null=w[:,g<1e-8]
  pdark+=(v@null)@(v@null).T
  i=j
 dark_theory=2**(d-1)*(2**d-d-1)
 assert round(np.trace(pdark))==dark_theory,(d,np.trace(pdark),dark_theory)
 assert np.linalg.norm(pdark@pdark-pdark)<1e-7
 for s in range(1,d+1):
  predicted=2/n*sum(math.comb(d,t) for t in range(d-s+1))/math.comb(d,s)
  captures=[1-pdark[t,t] for t,(a,b) in enumerate(pairs) if a!=b and (a^b).bit_count()==s]
  print(d,s,round(predicted,10),round(float(min(captures)),10),round(float(max(captures)),10))
  assert np.max(np.abs(np.asarray(captures)-predicted))<1e-8
 print('PASS',d,'dark',int(round(np.trace(pdark))),'observed',len(pairs)-int(round(np.trace(pdark))))
for d in range(1,5):test(d)
