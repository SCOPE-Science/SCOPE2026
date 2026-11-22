"""Exact modular recurrence check for the Narayana ternary-fibre formula.

Run with Python 3: python verify_narayana.py
No external dependencies or downloaded files.
"""
from collections import Counter
T=[[0,1,0],[0,0,1],[1,0,1]]
I=[[int(i==j) for j in range(3)] for i in range(3)]
def mul(A,B,m):return [[sum(A[i][k]*B[k][j] for k in range(3))%m for j in range(3)] for i in range(3)]
def add(A,B,m):return [[(A[i][j]+B[i][j])%m for j in range(3)] for i in range(3)]
def scale(A,c,m):return [[c*v%m for v in row] for row in A]
def power(A,n,m):
 R=I
 while n:
  if n&1:R=mul(R,A,m)
  A=mul(A,A,m); n//=2
 return R
U=power(T,8,1000000000000)
B=[[(U[i][j]-I[i][j])//3 for j in range(3)] for i in range(3)]
base=[0,1,1]
def mr(A,v,m):return [sum(A[i][j]*v[j] for j in range(3))%m for i in range(3)]
def logU(m):
 # B matrix integer, compute (3B)^j/j p-adically
 L=[[0]*3 for _ in range(3)]
 # Evaluate the 3-adic logarithm from B=(U-I)/3; no rationals or floating point.
 L=[[0]*3 for _ in range(3)];P=I
 for j in range(1,5*m.bit_length()+10):
  P=mul(P,B,m)
  jj=j;v=0
  while jj%3==0:jj//=3;v+=1
  c=pow(3,j-v,m)*pow(jj,-1,m)%m
  if j%2==0:c=-c
  L=add(L,scale(P,c,m),m)
 return L

def deriv(r,t,h):
 m=3**(h+2)
 L=logU(m);Ur=power(T,r,m);Ut=power(U,t,m)
 v=mr(Ur,base,m);w=mr(mul(Ut,L,m),v,m)
 assert w[0]%9==0
 return (w[0]//9)%(3**h)
def center(r,k):
 t=1 if r==0 else 2
 for h in range(1,k+1):
  assert deriv(r,t,h)%3**h==0,(r,h,t,deriv(r,t,h))
  found=[t+d*3**h for d in range(3) if deriv(r,t+d*3**h,h+1)==0]
  assert len(found)==1,(r,h,found)
  t=found[0]
 return t

def A(r,t,m):return mr(power(U,t,m),mr(power(T,r,m),base,m),m)[0]
def roots(z,n):
 mod=3**n
 if n==0:return 1
 if z%mod==0:return 3**(n//2)
 v=0
 while z%3==0: v+=1;z//=3
 if v%2:return 0
 m=mod//3**v
 if z%3==2:return 0
 # unit residue1 unique +- root each mod 3^{n-v}, extra 3^{v/2} root multiplicity
 return 2*3**(v//2)

def predicted(k):
 mod=3**k
 b0=A(0,center(0,k),mod)
 b2=A(2,center(2,k),mod)
 h={}
 for y in range(mod):
  z=1 if y%3==2 else 2
  if k>=3:
   z+=6*(y%27==0)+3*(y%27==1)+3*(y%27==19)+9*(y%27==1)
   if k==3:
    z+=3*(y%27==9)+3*(y%27==1)
   if k>=4:
    if (y-b0)%81==0:z+=9*roots(((y-b0)//81)*2, k-4) # square classes agree: 2/(1/2)=4
    if (y-b2)%81==0:z+=9*roots((y-b2)//81,k-4)
  elif k==2:
   # singular r0 contributes3 to y=0, r2 r3 to y=1 respectively3 each
   z+=3*(y==0)+3*(y==1)+3*(y==1)
  elif k==1:z={0:3,1:4,2:1}[y]
  h[y]=z
 return h,b0,b2

def actual(k):
 m=3**k
 a,b,c=0,1,1
 f=Counter()
 for n in range(8*3**(k-1)):
  f[a]+=1
  a,b,c=b,c,(c+a)%m
 assert (a,b,c)==(0,1,1)
 return f
if __name__=='__main__':
 for k in range(1,10):
  pred,b0,b2=predicted(k)
  act=actual(k)
  bad=[(y,act[y],p) for y,p in pred.items() if act[y]!=p]
  assert not bad, (k,bad[:5])
  assert sum(pred.values())==8*3**(k-1)
  assert sum(v==1 for v in act.values())==3**(k-1)
  print(f'PASS k={k} modulus={3**k} all {3**k} fibres; critical centres={b0},{b2}; max={max(act.values())}')
