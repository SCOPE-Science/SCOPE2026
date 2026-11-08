from collections import Counter
from math import gcd,comb

def poly_mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def poly_pow(a,k):
 out=[1]
 for _ in range(k):out=poly_mul(out,a)
 return out

def totient(d):return sum(gcd(j,d)==1 for j in range(1,d+1))
def formula(n):
 out=[0]*(n+1)
 def add(p,scale):
  for k,v in enumerate(p):out[k]+=scale*v
 for d in range(1,n+1):
  if n%d==0:
   A=[comb(d,i) for i in range(d)]+[0]
   add(poly_pow(A,n//d),totient(d))
 if n%2: add(poly_pow([1,2],(n-1)//2),n)
 else:
  add(poly_pow([1,2],n//2),n//2)
  add(poly_pow([1,2],(n-2)//2),n//2)
 out[0]-=2*n-1
 out[1]-=n*(n-1)
 if n%2==0: out[2]-=n*(n-2)//2
 return out

def brute(n):
 rows={}
 for k in range(n):
  for refl in [0,1]:
   perm=[(i+k)%n if not refl else (k-i)%n for i in range(n)]
   for mask in range(1<<n):
    vals=tuple(perm[i] if mask>>i&1 else -1 for i in range(n))
    rows[vals]=None
 ranks=Counter()
 for f in rows:
  good=True
  for i in range(n):
   seen=set();x=i
   while x!=-1:
    if x in seen:
     good=False;break
    seen.add(x);x=f[x]
   if not good:break
  if good:ranks[sum(x>=0 for x in f)]+=1
 return [ranks[k] for k in range(n+1)],len(rows)

if __name__=='__main__':
 for n in range(3,12):
  x,y=brute(n);z=formula(n)
  assert x==z,(n,x,z)
  size=2*n*2**n-(2*n-1)-n*n-(n*n//2 if n%2==0 else 0)
  assert size==y,(n,size,y)
  print(n,'Ntotal',sum(z),'size',y,'coeff',z)
 print('VERIFY_OK')
