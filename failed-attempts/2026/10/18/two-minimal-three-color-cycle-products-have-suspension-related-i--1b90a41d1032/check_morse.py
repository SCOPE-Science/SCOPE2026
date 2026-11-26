#!/usr/bin/env python3
"""Exact acyclic-face-matching and integral Morse-boundary verification.
Python standard library only. For an ordinary independence complex of the
categorical product of a cycle and a three-vertex complete graph.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

ORDERS={
 7:[11,0,6,19,4,20,14,10,17,3,12,2,7,15,18,16,9,5,1,13,8],
 8:[8,11,21,10,16,4,22,13,15,0,9,19,17,2,6,3,20,12,18,1,7,5,23,14],
}

def graph(m):
 n=3; adjacent=[]
 for i in range(m):
  for a in range(n):
   adjacent.append(sum(1 << (((i+d)%m)*n+b) for d in (-1,1) for b in range(n) if b!=a))
 return adjacent

def simplices(m):
 adj=graph(m); allfaces=[]
 def add(mask, available):
  if mask:allfaces.append(mask)
  while available:
   bit=available & -available;available^=bit
   v=bit.bit_length()-1
   add(mask|bit, available & ~adj[v])
 add(0, (1<<(3*m))-1)
 return set(allfaces)

def faces_with_coeff(mask):
 remaining=mask;p=0
 while remaining:
  bit=remaining & -remaining;remaining^=bit
  yield mask^bit,(-1 if p%2 else 1)
  p+=1

def verify(m):
 allfaces=simplices(m)
 assert len(ORDERS[m])==m*3 and set(ORDERS[m])==set(range(m*3))
 unmatched=set(allfaces); up={}; down={}
 for v in ORDERS[m]:
  bit=1<<v
  for x in list(unmatched):
   if x&bit:continue
   y=x|bit
   if y in unmatched:
    up[x]=y;down[y]=x;unmatched.remove(x);unmatched.remove(y)
 assert len(up)==len(down) and len(allfaces)==2*len(up)+len(unmatched)
 degree=Counter();edge=defaultdict(list)
 for upper in allfaces:
  for lower,_ in faces_with_coeff(upper):
   if not lower:continue
   if up.get(lower)==upper:
    edge[lower].append(upper);degree[upper]+=1
   else:
    edge[upper].append(lower);degree[lower]+=1
 q=deque(x for x in allfaces if not degree[x]);count=0
 while q:
  x=q.popleft();count+=1
  for y in edge[x]:
   degree[y]-=1
   if degree[y]==0:q.append(y)
 assert count==len(allfaces),('directed gradient cycle',m,count,len(allfaces))
 @lru_cache(None)
 def project(cell):
  if cell in down:return ()
  if cell not in up:return ((cell,1),)
  upper=up[cell]
  coeff=dict(faces_with_coeff(upper))
  pivot=coeff[cell]
  ans=defaultdict(int)
  for lower,a in coeff.items():
   if lower==cell or lower==0:continue
   for critical,c in project(lower):ans[critical]-=a*pivot*c
  return tuple((k,v) for k,v in sorted(ans.items()) if v)
 final={}
 for crit in sorted(unmatched):
  if crit.bit_count()==1:continue
  out=defaultdict(int)
  for lower,a in faces_with_coeff(crit):
   for target,c in project(lower):out[target]+=a*c
  final[crit]={k:v for k,v in out.items() if v}
 assert all(not d for d in final.values()),('nonzero integral Morse boundary',m,final)
 dimcounts=dict(sorted(Counter(x.bit_count()-1 for x in unmatched).items()))
 facecounts=dict(sorted(Counter(x.bit_count()-1 for x in allfaces).items()))
 print('cycle',m,'faces',len(allfaces),'face_counts',facecounts,'matching_pairs',len(up),'critical',dimcounts,'acyclic_nodes_checked',count,'integral_Morse_differentials','ZERO',flush=True)
 assert dimcounts==({0:1,3:1,4:3} if m==7 else {0:1,4:1,5:3})
 return dimcounts

if __name__=='__main__':
 for m in (7,8):verify(m)
