from collections import deque
from itertools import product

def solve(n):
 words=[''.join(x) for x in product('01',repeat=n) if '11' not in ''.join(x)]
 orbits=sorted({min(w,w[::-1]) for w in words});ix={w:i for i,w in enumerate(orbits)}
 verts=sorted({w[:-1] for w in words});trans={v:[(w[1:],ix[min(w,w[::-1])],w[-1]) for w in words if w[:-1]==v] for v in verts};target=(1<<len(orbits))-1
 best=None
 for start in verts:
  q=deque([(start,0)]);dist={(start,0):0};par={}
  while q:
   v,mask=q.popleft();L=dist[(v,mask)]
   if best is not None and L+1>best[0]:break
   for t,j,b in trans[v]:
    nxt=(t,mask|(1<<j));l=L+1
    if best is not None and l>best[0]:continue
    if t==start and nxt[1]==target:
     cur=(v,mask);digits=[b]
     while cur!=(start,0):
      old,bit=par[cur];digits.append(bit);cur=old
     digits=''.join(reversed(digits))
     if best is None or l<best[0]:best=(l,start,digits)
    if nxt not in dist:
     dist[nxt]=l;par[nxt]=((v,mask),b);q.append(nxt)
 return len(words),len(orbits),best
for n in range(2,7):
 a,b,z=solve(n)
 print(n,a,b,z,flush=True)
