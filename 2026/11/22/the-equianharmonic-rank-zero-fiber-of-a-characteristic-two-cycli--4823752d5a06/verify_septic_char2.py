"""Pure-Python exact finite-field replay of the characteristic-two cyclic-septic Cartier matrix."""
from collections import Counter

def mul(a,b,degree,mod):
 z=0
 while b:
  if b&1:z^=a
  a<<=1;b>>=1
 for j in range(2*degree-2,degree-1,-1):
  if z&(1<<j):z^=mod<<(j-degree)
 return z

def powf(a,n,p,mod):
 z=1
 while n:
  if n&1:z=mul(z,a,p,mod)
  a=mul(a,a,p,mod); n>>=1
 return z

def rank(A,n,mod):
 a=[r[:] for r in A];k=0
 for j in range(6):
  r=next((i for i in range(k,6) if a[i][j]),None)
  if r is None:continue
  a[r],a[k]=a[k],a[r]
  inv=powf(a[k][j],(1<<n)-2,n,mod)
  a[k]=[mul(x,inv,n,mod) for x in a[k]]
  for i in range(6):
   if i!=k and a[i][j]:
    t=a[i][j];a[i]=[x^mul(t,y,n,mod) for x,y in zip(a[i],a[k])]
  k+=1
 return k

def matmul(A,B,n,mod):return [[__import__('functools').reduce(int.__xor__,(mul(A[i][k],B[k][j],n,mod) for k in range(6)),0) for j in range(6)] for i in range(6)]

def test(n,mod):
 out=Counter()
 for t in range(2,1<<n):
  sq=lambda x:powf(x,1<<(n-1),n,mod)
  B=t^1
  basis=[(3,0),(4,0),(5,0),(5,1),(6,0),(6,1)]
  index={v:i for i,v in enumerate(basis)}
  f=[0,t,B,1]
  A=[[0]*6 for _ in range(6)]
  for col,(j,i) in enumerate(basis):
   newj=j//2 if j%2==0 else (j+7)//2
   poly=[0]*(i+1) if j%2==0 else [0]*(i+len(f))
   if j%2==0:poly[i]=1
   else:
    for exp,c in enumerate(f):poly[exp+i]=c
   for exp in range(1,len(poly),2):
    if poly[exp]:
     target=(newj,(exp-1)//2)
     assert target in index
     A[index[target]][col]^=sq(poly[exp])
  P=[[int(i==j) for j in range(6)] for i in range(6)];r=[]
  for m in range(1,14):
   P=matmul(A,[[sq(x) for x in row] for row in P],n,mod)
   r.append(rank(P,n,mod))
  key=tuple(r)
  out[key]+=1
  if n==2:assert key==(4,3,2,1,0,0,0,0,0,0,0,0,0)
  else:assert key==(4,3,3,3,3,3,3,3,3,3,3,3,3)
  if n==2:print('t',t,'seq',key)
 print('GF',2**n,'counts',out)

test(2,0b111)
test(3,0b1011)

print("CYCLIC_SEPTIC_CHARACTERISTIC_TWO_VERIFIED_OK")
