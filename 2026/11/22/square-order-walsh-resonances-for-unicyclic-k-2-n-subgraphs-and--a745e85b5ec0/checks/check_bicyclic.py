#!/usr/bin/env python3
"""Standalone integer checks for fixed-excess connected spanning subgraphs of K_{2,n}."""
import math
from itertools import combinations

def K(r,b,m):
 return sum((-1)**i*math.comb(b,i)*math.comb(m-b,r-i) for i in range(max(0,r-(m-b)),min(r,b)+1))

def formula(a,b,n,j):
 d=sum(x!=y for x,y in zip(a,b));
 if d>j: return 0
 neg=sum(x<0 for x,y in zip(a,b) if x==y)
 return (-1)**(d+neg)*2**(n-j)*K(j-d,neg,n-d)

def direct(a,b,n,j):
 tot=0
 for both in combinations(range(n),j):
  B=set(both)
  prod=1
  for i in range(n):
   prod*=a[i]*b[i] if i in B else a[i]+b[i]
  tot+=prod
 return tot

def hadamard(c):
 out=c[:];h=1;N=len(out)
 while h<N:
  for q in range(0,N,2*h):
   for i in range(q,q+h):
    x,y=out[i],out[i+h];out[i],out[i+h]=x+y,x-y
  h*=2
 return out

def main():
 checks=0
 for n in range(2,9):
  for j in range(1,n+1):
   N=1<<(2*n);z=[0]*N
   for mask in range(N):
    doubles=0;okay=True
    for i in range(n):
     c=(mask>>i&1)+(mask>>(i+n)&1)
     if c==0:okay=False;break
     doubles+= (c==2)
    z[mask]=int(okay and doubles==j)
   W=hadamard(z)
   ex=0
   for t in range(N):
    a=[-1 if t>>i&1 else 1 for i in range(n)]
    b=[-1 if t>>(i+n)&1 else 1 for i in range(n)]
    calc=formula(a,b,n,j)
    assert calc==W[t],(n,j,t,calc,W[t]);checks+=1
    assert abs(calc)<=math.comb(n,j)*(1<<(n-j));checks+=1
    assert calc%(1<<(n-j))==0;checks+=1
   assert max(abs(v) for v in W)==math.comb(n,j)*2**(n-j)
   assert min(abs(v) for v in W if v)==2**(n-j)
   checks+=2
   if j==2:
    Q=2**n*(1+n+math.comb(n,2))
    if n%2:Q-=2*n*math.comb(n-1,(n-1)//2)
    isqrt=math.isqrt(n)
    if isqrt**2==n:Q-=2*math.comb(n,(n-isqrt)//2)
    rank=sum(x!=0 for x in W)
    assert rank==Q,(n,rank,Q)
    checks+=1
    print(f'n={n}, j=2, total={math.comb(n,2)*2**(n-2)}, rank={rank}, nullity={4**n-rank}, min={2**(n-2)}')
 print('PASS',checks,'exact assertions')
if __name__=='__main__':main()
