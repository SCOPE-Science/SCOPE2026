"""Finite-field checks for determinant phase Fourier transforms. Standalone Python 3 with numpy."""
import itertools, math
import numpy as np

def rank_modp(a,p):
 a=[list(map(lambda x:int(x)%p,r)) for r in a]; n=len(a);m=len(a[0]);k=0
 for j in range(m):
  z=next((i for i in range(k,n) if a[i][j]%p),None)
  if z is None:continue
  a[k],a[z]=a[z],a[k]
  inv=pow(a[k][j],-1,p);a[k]=[(x*inv)%p for x in a[k]]
  for i in range(n):
   if i!=k:
    t=a[i][j]%p
    a[i]=[(a[i][h]-t*a[k][h])%p for h in range(m)]
  k+=1
  if k==n:break
 return k

def det3(a,p):
 (a,b,c),(d,e,f),(g,h,i)=a
 return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%p

def kl(t,p):
 w=np.exp(2j*np.pi/p)
 return sum(w**((u + t*pow(u,-1,p))%p) for u in range(1,p))

def expected(A,l,p):
 if l==0:return p**9 if all(v==0 for row in A for v in row) else 0
 r=rank_modp(A,p)
 if r==0:return p**7+p**6-p**4
 if r==1:return p**6-p**4
 if r==2:return -p**4
 return p**4*kl((-det3(A,p)*pow(l,-1,p))%p,p)

def check(p):
 data=np.empty((p,)*9,dtype=np.complex128)
 roots=np.exp(2j*np.pi*np.arange(p)/p)
 for v in itertools.product(range(p),repeat=9):
  mat=(v[:3],v[3:6],v[6:])
  data[v]=roots[det3(mat,p)]
 # np.fft.fftn uses exp(-2pi i *a*x/p), so eval expected with -A, determinant sign neg as odd cubic
 F=np.fft.fftn(data)
 mx=0; bad=None
 for v in itertools.product(range(p),repeat=9):
  A=[tuple((-s)%p for s in v[i:i+3]) for i in (0,3,6)]
  goal=expected(A,1,p)
  er=abs(F[v]-goal)
  if er>mx:mx=er;bad=(v,goal,F[v])
 print('p',p,'max_err',mx,'bad:',bad if mx>1e-6 else 'none','n',p**9)
 assert mx<1e-6

if __name__=='__main__':
 for p in (2,3):check(p)
