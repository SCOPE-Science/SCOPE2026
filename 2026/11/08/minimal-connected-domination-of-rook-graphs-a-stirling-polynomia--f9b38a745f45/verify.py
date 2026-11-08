from collections import Counter
from itertools import combinations
from math import comb,factorial

def Stir(n,k):
 if k>n or n<0 or k<0:return 0
 if n==k==0:return 1
 if k==0:return 0
 return Stir(n-1,k-1)+k*Stir(n-1,k)

def formula(m,n):
 c=Counter()
 for r in range(1,min(m-1,n-1)+1):
  c[n+r-1]+=comb(m,r)*factorial(r)*Stir(n-1,r)*n**(r-1)
 for s in range(1,min(n-1,m-1)+1):
  c[m+s-1]+=comb(n,s)*factorial(s)*Stir(m-1,s)*m**(s-1)
 return {k:v for k,v in sorted(c.items())}

def direct(m,n):
 N=m*n;adj=[0]*N
 for i in range(N):
  for j in range(N):
   if i!=j and (i//n==j//n or i%n==j%n):adj[i]|=1<<j
 allm=(1<<N)-1;co=Counter(); minimal=[]; connectednum=0
 for d in range(1,allm+1):
  # domination by rows/cols
  rows=0;cols=0
  it=d
  while it:
   low=it&-it; pos=low.bit_length()-1;it-=low
   rows|=1<<(pos//n);cols|=1<<(pos%n)
  if rows!=(1<<m)-1 and cols!=(1<<n)-1:continue
  seen=0;front=d&-d
  while front:
   seen|=front
   nextf=0; t=front
   while t:
    low=t&-t; t-=low
    nextf|=adj[low.bit_length()-1]
   front=nextf & d & ~seen
  if seen!=d:continue
  connectednum+=1
  good=True; x=d
  while x:
   bit=x&-x;x-=bit;rem=d^bit
   if not rem: continue
   rows2=0;cols2=0; t=rem
   while t:
    low=t&-t; k=low.bit_length()-1;t-=low
    rows2|=1<<(k//n);cols2|=1<<(k%n)
   if rows2!=(1<<m)-1 and cols2!=(1<<n)-1:continue
   seen2=0;front2=rem&-rem
   while front2:
    seen2|=front2
    next2=0;t=front2
    while t:
     low=t&-t;t-=low;next2|=adj[low.bit_length()-1]
    front2=next2&rem&~seen2
   if seen2==rem:
    good=False;break
  if good:co[d.bit_count()]+=1;minimal.append(d)
 return dict(sorted(co.items())),len(minimal),connectednum

if __name__=='__main__':
 checks=[(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]
 tested=0;tot=0
 for m,n in checks:
  p=formula(m,n); q,k,c=direct(m,n)
  print(m,n,'formula',p,'direct',q,'connected',c)
  assert p==q,(m,n,p,q)
  tested+=(1<<(m*n))-1;tot+=k
 print('VERIFY_OK',len(checks),tested,tot)
