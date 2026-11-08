#!/usr/bin/env python3
"""Independent row-composition 3x3 margin enumerator and exact switch-distance tests."""
from collections import Counter, deque
from itertools import product, permutations, combinations

COMPS=lambda n: [(a,b,n-a-b) for a in range(n+1) for b in range(n+1-a)]
RECT=[]
for a,b in combinations(range(3),2):
 for c,d in combinations(range(3),2):
  z=[0]*9
  for r,s,v in ((a,c,1),(b,d,1),(a,d,-1),(b,c,-1)): z[3*r+s]=v
  RECT.append(tuple(z))
assert len(RECT)==9
PERMS=list(permutations(range(3)))

def matperm(p,n):
 return tuple(n if j==p[i] else 0 for i in range(3) for j in range(3))

def verify(n):
 rows=COMPS(n)
 S=[]
 for a,b,c in product(rows,repeat=3):
  if all(a[j]+b[j]+c[j]==n for j in range(3)):
   S.append(a+b+c)
 si={x:i for i,x in enumerate(S)};assert len(S)==len(si)
 nbr=[[] for x in S]
 for i,x in enumerate(S):
  for m in RECT:
   for sign in (-1,1):
    y=tuple(x[k]+sign*m[k] for k in range(9))
    if min(y)>=0: nbr[i].append(si[y])
  assert len(set(nbr[i]))==len(nbr[i])
 seen_pairs=Counter(); ecount=0
 for i,ns in enumerate(nbr):
  for j in ns:assert i in nbr[j]
  ecount+=len(ns)
 for i in range(len(S)):
  dist=[-1]*len(S);dist[i]=0;q=deque([i])
  while q:
   u=q.popleft()
   for j in nbr[u]:
    if dist[j]<0:dist[j]=dist[u]+1;q.append(j)
  assert -1 not in dist
  for j in range(i+1,len(S)):seen_pairs[dist[j]]+=1
 assert max(seen_pairs)==2*n
 expected={frozenset((matperm(p,n),matperm(q,n)))
           for p,q in combinations(PERMS,2) if all(p[i]!=q[i] for i in range(3))}
 antipodes=set()
 for i in range(len(S)):
  dist=[-1]*len(S);dist[i]=0;q=deque([i])
  while q:
   u=q.popleft()
   for j in nbr[u]:
    if dist[j]<0:dist[j]=dist[u]+1;q.append(j)
  for j in range(i+1,len(S)):
   if dist[j]==2*n:antipodes.add(frozenset((S[i],S[j])))
 assert antipodes==expected and len(expected)==6
 return len(S),ecount//2,len(antipodes)

# Independent symbolic certificates: for the canonical disjoint permutations
# I and (012), every elementary rectangle changes the integer potential at
# most three; endpoints differ in potential by 6n.
W=(1,-1,0,0,1,-1,-1,0,1)
assert {abs(sum(x*y for x,y in zip(W,r))) for r in RECT}=={0,3}
for p,q in combinations(PERMS,2):
 if all(p[i]!=q[i] for i in range(3)):
  assert sum(W[k]*matperm(PERMS[0],1)[k] for k in range(9))==3

# The three-move compression 2I -> Q+R.
P0=(2,0,0,0,2,0,0,0,2)
P1=(1,1,0,1,1,0,0,0,2)
P2=(0,1,1,1,1,0,1,0,1)
P3=(0,1,1,1,0,1,1,1,0)
for x,y in zip((P0,P1,P2),(P1,P2,P3)):
 assert any(tuple(x[k]+sg*r[k] for k in range(9))==y for r in RECT for sg in (-1,1))
assert P3==tuple(matperm((1,2,0),1)[k]+matperm((2,0,1),1)[k] for k in range(9))

if __name__=='__main__':
 for n in range(1,9):
  count,edges,pairs=verify(n)
  print(f'n={n} states={count} edges={edges} diameter={2*n} diametral_pairs={pairs}',flush=True)
 print('INDEPENDENT_EXHAUSTIVE_AND_SYMBOLIC_CERTIFICATES_PASS')
