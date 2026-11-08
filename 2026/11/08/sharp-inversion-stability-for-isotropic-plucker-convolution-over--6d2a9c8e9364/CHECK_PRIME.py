# Reproducible finite checks for isotropic-Plucker convolution.
# Requires Python 3 and NumPy. These computations do not establish the infinite theorem.
import itertools, math
import numpy as np

def rank_mod(A,p):
 A=np.array(A,dtype=np.int64).copy()%p
 m,n=A.shape; r=0
 for j in range(n):
  k=next((k for k in range(r,m) if A[k,j]%p),None)
  if k is None: continue
  if k!=r: A[[r,k]]=A[[k,r]]
  A[r]=(A[r]*pow(int(A[r,j]),-1,p))%p
  for i in range(m):
   if i!=r and A[i,j]:A[i]=(A[i]-A[i,j]*A[r])%p
  r+=1
  if r==m:break
 return r

def work(p,n):
 h=n//2; I=np.eye(h,dtype=np.int64)
 O=np.block([[np.zeros((h,h),dtype=np.int64),I],[-I,np.zeros((h,h),dtype=np.int64)]])%p
 ij=list(itertools.combinations(range(n),2))
 shape=(p,)*len(ij)
 S=np.zeros(shape,dtype=np.uint8)
 vectors=list(itertools.product(range(p), repeat=n))
 for u in vectors:
  for v in vectors:
   uv=sum(u[i]*v[h+i]-u[h+i]*v[i] for i in range(h))%p
   if uv:continue
   w=tuple((u[i]*v[j]-u[j]*v[i])%p for i,j in ij)
   if any(w):S[w]=1
 D=int(S.sum()); delta=(p**(n-2)-1)//(p*p-1)
 expected_degree=(p**n-1)*delta
 assert D==expected_degree,(D,expected_degree)
 FT=np.fft.fftn(S).reshape(-1)
 z=np.real(FT)
 assert np.max(abs(np.imag(FT)))<1e-7
 assert np.max(abs(z-np.rint(z)))<1e-7
 assert abs(np.min(abs(z))-delta)<1e-7,(p,n,np.min(abs(z)),delta)
 assert abs(np.max(abs(z))-D)<1e-7
 # all frequency profiles, independently from sampling FFT
 for index in range(len(FT)):
  coords=np.unravel_index(index,shape)
  B=np.zeros((n,n),dtype=np.int64)
  for (i,j),v in zip(ij,coords): B[i,j]=v;B[j,i]=-v
  kval=sum(p**(n-rank_mod((B+t*O)%p,p)) for t in range(p))-p*(p+1)
  formula=(p**(n-2)*kval+1)//(p*p-1)
  assert (p**(n-2)*kval+1)%(p*p-1)==0
  assert abs(z[index]-formula)<1e-7,(p,n,index,z[index],formula)
 print('PASS p=',p,'n=',n,'group=',len(FT),'support=',D,'delta=',delta,'cond=',D//delta,'eigenlevels=',sorted(set(map(int,np.rint(z)))))

for p,n in [(2,4),(3,4),(2,6)]:work(p,n)

def sample_big(p,n):
 import random
 h=n//2;ij=list(itertools.combinations(range(n),2));I=np.eye(h,dtype=np.int64)
 O=np.block([[np.zeros((h,h),dtype=np.int64),I],[-I,np.zeros((h,h),dtype=np.int64)]])%p
 vectors=list(itertools.product(range(p),repeat=n));S=set()
 for u in vectors:
  for v in vectors:
   if sum(u[i]*v[h+i]-u[h+i]*v[i] for i in range(h))%p: continue
   w=tuple((u[i]*v[j]-u[j]*v[i])%p for i,j in ij)
   if any(w): S.add(w)
 S=np.array(sorted(S),dtype=np.int64)
 delta=(p**(n-2)-1)//(p*p-1); assert len(S)==(p**n-1)*delta
 Blist=[np.zeros((n,n),dtype=np.int64),O.copy()]
 # witness: J a nilpotent Jordan block in m dims, B = Omega diag(J,J^T)
 J=np.zeros((h,h),dtype=np.int64)
 for i in range(h-1):J[i,i+1]=1
 Bw=np.block([[np.zeros((h,h),dtype=np.int64),J.T],[-J,np.zeros((h,h),dtype=np.int64)]])%p
 Blist.append(Bw)
 random.seed(48392)
 for _ in range(24):
  B=np.zeros((n,n),dtype=np.int64)
  for i,j in ij:B[i,j]=random.randrange(p); B[j,i]=-B[i,j]
  Blist.append(B%p)
 for i,B in enumerate(Blist):
  b=np.array([B[j,k]%p for j,k in ij])
  v=S.dot(b)%p;cnt=np.bincount(v,minlength=p)
  z=sum(cnt[k]*np.exp(2j*np.pi*k/p) for k in range(p))
  K=sum(p**(n-rank_mod((B+t*O)%p,p)) for t in range(p))-p*(p+1)
  assert (p**(n-2)*K+1)%(p*p-1)==0
  target=(p**(n-2)*K+1)//(p*p-1)
  assert abs(z-target)<1e-6,(i,z,target)
  if i==2:assert target==-delta and [n-rank_mod((B+t*O)%p,p) for t in range(p)].count(2)==1
 print('PASS_BIG p=',p,'n=',n,'support=',len(S),'frequencies_checked=',len(Blist),'min_eigen=',-delta)

sample_big(3,6)
