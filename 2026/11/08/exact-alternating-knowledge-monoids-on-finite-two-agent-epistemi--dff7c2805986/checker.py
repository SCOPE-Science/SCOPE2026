from collections import deque, defaultdict
from itertools import product

def partitions(n):
 if n==0: yield ();return
 def rgs(seq,mx):
  if len(seq)==n:yield tuple(seq);return
  for v in range(mx+2):yield from rgs(seq+[v],max(v,mx))
 yield from rgs([0],0)

def graph_diam(a,b):
 n=len(a); L=[('L',i) for i in set(a)]; R=[('R',j) for j in set(b)];
 adj={v:set() for v in L+R}
 for x,y in zip(a,b):adj['L',x].add(('R',y));adj['R',y].add(('L',x))
 dLL=dRR=dLR=0
 for v in adj:
  dis={v:0};Q=deque([v]);
  while Q:
   z=Q.popleft()
   for z2 in adj[z]:
    if z2 not in dis:dis[z2]=dis[z]+1;Q.append(z2)
  for z2,d in dis.items():
   if v[0]=='L' and z2[0]=='L':dLL=max(dLL,d)
   if v[0]=='R' and z2[0]=='R':dRR=max(dRR,d)
   if v[0]!=z2[0]:dLR=max(dLR,d)
 return dLL,dRR,dLR

def join_rel(A,B,n):
 row=[0]*n
 for i in range(n):
  bits=A[i];j=0
  while bits:
   low=bits & -bits;j=low.bit_length()-1;row[i]|=B[j];bits-=low
 return tuple(row)

def brute(a,b):
 n=len(a); I=tuple(1<<i for i in range(n)); E=tuple(sum(1<<j for j in range(n) if a[i]==a[j]) for i in range(n));F=tuple(sum(1<<j for j in range(n) if b[i]==b[j]) for i in range(n));
 seen={I,E,F}; stack=list(seen)
 while stack:
  x=stack.pop()
  for y in (E,F):
   z=join_rel(x,y,n)
   if z not in seen:seen.add(z);stack.append(z)
 return len(seen)

def formula(a,b):
 ll,rr,lr=graph_diam(a,b); mE=1+min(ll,lr);mF=1+min(rr,lr);
 indicator=(len(set(a))==len(a) or len(set(b))==len(b))
 return mE+mF-int(indicator)

if __name__=='__main__':
 for n in range(1,7):
  pats=list(partitions(n));mx=0;hist=defaultdict(int)
  for a in pats:
   for b in pats:
    x=brute(a,b);y=formula(a,b)
    if x!=y:raise AssertionError((n,a,b,x,y,graph_diam(a,b)))
    mx=max(mx,x);hist[x]+=1
  print(n,len(pats)**2,'max',mx,'hist',sorted(hist.items()))
