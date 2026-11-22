# Exact truncated power-series evaluation and independent normal-play mex counts.
from functools import lru_cache
from math import comb
from itertools import product
N=19

def add(a,b):return [x+y for x,y in zip(a,b)]
def mul(a,b):
 r=[0]*N
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:N-i]):
    if y:r[i+j]+=x*y
 return r
one=[1]+[0]*(N-1)
zero=[0]*N
@lru_cache(None)
def power(a,k):
 if k==0:return one
 if k==1:return a
 return mul(power(a,k//2),power(a,k-k//2))

def inv(a):
 assert a[0]==1
 b=[1]+[0]*(N-1)
 for j in range(1,N):b[j]=-sum(a[k]*b[j-k] for k in range(1,j+1))
 return b
D=[one,one]
for i in range(2,N+1):
 d=D[-1].copy()
 for j in range(2,N):d[j]-=D[-2][j-2]
 D.append(d)
P=[0]*N
for i in range(1,N//2+1):
 if 2*i<N:P[2*i]=comb(2*(i-1),i-1)//i
FS=[]
for h in range(1,N):
 iv=inv(D[h-1])
 v=[0]*N
 for j,x in enumerate(iv[:N-h]):v[j+h]=x
 u=P[:]
 if h>=2:
  tmp=mul(D[h-2],iv)
  for j in range(2,N):u[j]+=tmp[j-2]
 # build Narayana direct
 f=v[:]
 for j in range(1,N):
  for k in range(1,j+1):
   if 4*(j+1-k)+h*(2*k-1)>=N:continue
   N_jk=comb(j,k)*comb(j,k-1)//j
   u_pow=power(tuple(u),2*(j+1-k))
   v_pow=power(tuple(v),2*k-1)
   term=mul(u_pow,v_pow)
   f=[x+N_jk*y for x,y in zip(f,term)]
 FS.append(f)
counts=[1]+[2*sum(f[n] for f in FS) for n in range(1,N)]
@lru_cache(None)
def g(w):
 s=0;A=[0]
 for x in w:s+=1 if x=='a' else -1;A.append(s)
 H=s
 opts=[g(w[t:]) for t in range(1,len(w)+1) if A[t]==0]+[g(w[:t]) for t in range(0,len(w)) if A[t]==H]
 return next(q for q in range(len(opts)+1) if q not in opts)
for n in range(1,17):
 actual=sum(g(''.join(x))==0 for x in product('ab',repeat=n))
 assert actual==counts[n], (n,actual,counts[n])
print('EXACT_SERIES_AND_GAME_OK lengths=0..16')
print('counts_n0_to_18',counts)
