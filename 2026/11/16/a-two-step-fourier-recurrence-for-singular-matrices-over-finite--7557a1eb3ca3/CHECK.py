# Reproducibility check for singular-matrix Fourier coefficients.
# Requires Python 3 and numpy; no external data.
import numpy as np
from collections import Counter,defaultdict
from math import isclose

def f(m,a,b,q):
 if m==0:return 1
 if m==1:
  if a==b==1:return q**3+q*q-q
  if a==0 and b==1:return q*q-q
  if a==b==0:return -q
  raise ValueError((m,a,b))
 U=q**(m-1)*(q-1)
 primitive=q**(2*m)-q**(2*m-2)
 N0=(q**a*U if a<m and b==m else (primitive if a==b==m else 0))
 Ns=(0 if b<=m-2 else (q**(a+1)*U if a<=m-2 else primitive))
 num=q**(2*m)*N0-q**(2*m-2)*Ns
 assert num%U==0
 val=num//U
 if a>=1:
  val+=q**4*f(m-2,min(a-1,m-2),min(b-1,m-2),q)
 return val

def valuation(x,p,m):
 if x==0:return m
 v=0
 while x%p==0 and v<m: v+=1;x//=p
 return v

def smith(A,p,m):
 aa,ab,ac,ad=A
 a=min(*(valuation(int(x),p,m) for x in A))
 if a==m:return m,m
 B=[int(x)//p**a for x in A]
 b=min(m,a+valuation((B[0]*B[3]-B[1]*B[2])%p**(m-a),p,m-a))
 return a,b

for p,m in [(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]:
 mod=p**m
 A=np.indices((mod,)*4,dtype=np.int32).reshape(4,-1)
 det=(A[0]*A[3]-A[1]*A[2])%mod
 D=(det==0).reshape((mod,)*4)
 z0=np.fft.fftn(D.astype(float)); z=np.rint(z0.real).astype(int).ravel()
 assert max(abs(z0.imag.ravel()))<1e-6 and max(abs(z0.real.ravel()-z))<1e-6
 cat=Counter();levels=Counter();counts=Counter()
 for idx,val in enumerate(z):
  typ=smith(tuple(int(x) for x in A[:,idx]),p,m)
  pred=f(m,*typ,p)
  if pred!=val:
   print('FAIL',p,m,idx,typ,pred,val);raise AssertionError
  counts[typ]+=1;cat[(typ,pred)]+=1;levels[pred]+=1
 print('PASS',p,m,'|C|',int(D.sum()),'types',sorted(cat),'levels',dict(sorted(levels.items())),'norm',sum(abs(v)*mult for v,mult in levels.items())/mod**4)
 print('  counts',dict(sorted(counts.items())))

# Independent exact Walsh check on truncated dual numbers.
from collections import Counter


def mul(a,b,m):
 z=0
 for i in range(m):
  if a>>i &1:z^=b<<i
 return z&((1<<m)-1)

def v(a,m):
 return m if a==0 else (a&-a).bit_length()-1
for m in (2,3):
 N=1<<(4*m);F=[0]*N
 for x in range(N):
  a,b,c,d=[(x>>(i*m))&((1<<m)-1) for i in range(4)]
  F[x]=int(mul(a,d,m)==mul(b,c,m))
 for b in range(4*m):
  mask=1<<b
  for x in range(N):
   if x&mask:continue
   u=F[x];w=F[x|mask];F[x]=u+w;F[x|mask]=u-w
 counts=Counter()
 for t in range(N):
  dual=[sum(((t>>(i*m+j))&1) <<(m-1-j) for j in range(m)) for i in range(4)]
  a=min(v(e,m) for e in dual)
  if a==m:typ=(m,m)
  else:
   B=[e>>a for e in dual]
   bb=mul(B[0],B[3],m-a)^mul(B[1],B[2],m-a)
   typ=(a,min(m,a+v(bb,m-a)))
  assert F[t]==f(m,*typ,2),(m,t,typ,F[t],f(m,*typ,2))
  counts[F[t]]+=1
 print('DUAL_EPS_WALSH_PASS',m,dict(sorted(counts.items())))

print("SINGULAR_CHAIN_RING_FOURIER_ALL_CHECKS_PASS")
