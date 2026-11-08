from heapq import heappush,heappop
from itertools import combinations_with_replacement

def genus_type(gens,k=1):
 G={1}
 for i in range(k):G={x*y for x in G for y in gens}
 G=sorted(G);m=G[0]
 D=[10**30]*m;D[0]=0;h=[(0,0)]
 while h:
  d,r=heappop(h)
  if d!=D[r]:continue
  for x in G[1:]:
   s=(r+x)%m
   if d+x<D[s]:D[s]=d+x;heappush(h,(d+x,s))
 return (sum(D)//m-(m-1)//2, max(D)-m)

def mingens(gaps):
 f=max(gaps) if gaps else -1
 m=next(x for x in range(1,f+3) if x not in gaps)
 C=f+m+2
 S=set(range(C+1))-set(gaps)
 return [x for x in range(1,f+m+2) if x in S and not any(y in S and x-y in S for y in range(1,x))]

states={frozenset()}
for g in range(1,18):
 nxt=set()
 for gaps in states:
  f=max(gaps) if gaps else -1
  for x in mingens(gaps):
   if x>f:nxt.add(gaps|{x})
 states=nxt
 flipped=[]
 for gaps in states:
  f=max(gaps);
  if 2*g==f+1:continue
  G=mingens(gaps)
  g2,f2=genus_type(G,2)
  if 2*g2==f2+1:flipped.append((g,f,tuple(G),f2,g2))
 print(g,'total',len(states),'flips',len(flipped),flipped[:3],flush=True)
 if flipped:break
