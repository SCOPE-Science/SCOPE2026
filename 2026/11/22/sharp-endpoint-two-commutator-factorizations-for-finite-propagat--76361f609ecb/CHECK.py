import numpy as np
count=0
for r in (0,1):
 for n in (4,6,10,17):
  for typ in ('diag','forward','backward','blocks'):
   C=np.zeros((n,n),complex)
   vals=np.array([1.0 if j%5==0 else (j+1)/(j+3) for j in range(n)])
   for j in range(n):
    if typ=='diag': k=j
    elif typ=='forward':k=j+1
    elif typ=='backward':k=j-1
    else:k=j+1 if j%2==0 else j-1
    if 0<=k<n:C[k,j]=vals[j]
   # ensure paired block coefficients same for orthogonal columns already holds
   if r==0 and typ!='diag':continue
   A=np.eye(n)-C.conj().T@C
   eig,U=np.linalg.eigh(A)
   assert min(eig)>-1e-10
   D=(U*np.sqrt(np.maximum(eig,0)))@U.conj().T
   if np.max(abs(D-np.diag(np.diag(D))))>1e-8:continue
   f=lambda k:2*k+2*r+3
   g=lambda k:2*k+2*r+4
   m=2*n+2*r+5
   V=np.zeros((m,n),complex); K=np.zeros((m,n),complex)
   for k in range(n):V[f(k),k]=1;K[g(k),k]=1
   W=V@C+K@D
   for x,y in ((W.conj().T@W,np.eye(n)),(V.conj().T@W,C),(V.conj().T@K,np.zeros((n,n)))):
    assert np.max(abs(x-y))<1e-10;count+=1
   assert all(np.max(abs(W[:j+1,j]))<1e-10 for j in range(n));count+=1
print('FINITE_PROPAGATION_ENDPOINT_CHECK_OK',count)
