from itertools import product
from collections import Counter
from math import comb

def calc(p):
 n=sum(p);t=len(p); masks=[];s=0
 for m in p:masks.append(((1<<m)-1)<<s);s+=m
 arr=[]
 for x in range(1<<n):
  nz=sum(bool(x&mask) for mask in masks)
  arr.append(int((nz>=2) or x.bit_count()==1))
 c=sum(arr)
 # FWHT independently computes all Walsh sums
 h=1
 while h<(1<<n):
  for i in range(0,1<<n,2*h):
   for j in range(i,i+h):
    a,b=arr[j],arr[j+h];arr[j]=a+b;arr[j+h]=a-b
  h*=2
 for k in range(1<<n):
  f= (1<<n if k==0 else 0)+n+t-1-2*k.bit_count()-sum((1<<p[i]) for i,m in enumerate(masks) if not(k&m))
  assert f==arr[k],(p,k,f,arr[k])
 null=arr.count(0)
 assert (null==0)==((n-t)%2==0),(p,null)
 singular=min(abs(x) for x in arr if x)
 assert singular==(1 if (n-t)%2==0 else 2),(p,singular)
 coefs=0
 for q in range(1<<t):
  rest=[i for i in range(t) if not (q>>i)&1]
  val=n+t-1-sum((1<<p[i]) for i in range(t) if (q>>i)&1)
  if val%2:continue
  target=val//2
  coef=[1]
  for i in rest:
   a=[0]+[comb(p[i],j) for j in range(1,p[i]+1)]
   out=[0]*(len(coef)+len(a)-1)
   for j,b in enumerate(coef):
    for h,c_ in enumerate(a):out[j+h]+=b*c_
   coef=out
  coefs+=coef[target] if 0<=target<len(coef) else 0
 assert null==coefs,(p,null,coefs)
 return n,t,c,null,singular,Counter(arr)
count=0
for t in range(2,5):
 for p in product(range(1,5),repeat=t):
  if sum(p)>11:continue
  calc(p);count+=1
print('Verified',count,'multipartite tuples, Fourier through entire cube n<=11.')
for p in [(1,2),(2,2),(2,3),(2,4),(1,1,2),(2,2,2),(2,2,3),(2,3,4),(2,2,2,2)]:
 n,t,c,z,m,sp=calc(p)
 print(p,'N',n,'connected',c,'null',z,'rank',2**n-z,'min',m,'spectrum', sorted(sp.items())[:20])
