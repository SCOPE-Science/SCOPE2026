from itertools import combinations
from math import factorial
from collections import deque

def partitions(n,s):
  sizes=[n//s]*s
  for i in range(n%s): sizes[i]+=1
  def go(blocks,rem):
    if not rem:
      if len(blocks)==s: yield tuple(map(tuple,blocks))
      return
    if len(blocks)==s:
      if rem:
        yield tuple(map(tuple,blocks))
      return
    m=rem[0]
    for sz in sorted(set(sizes)):
      if sizes.count(sz)>sum(len(b)==sz for b in blocks):
        for additional in combinations(rem[1:],sz-1):
          nxt=set((m,)+additional)
          yield from go(blocks+[(m,)+additional],tuple(x for x in rem if x not in nxt))
  return list(go([],tuple(range(n))))

def mask(p,n):
   block_of={x:i for i,block in enumerate(p) for x in block}
   return sum(1<<k for k,(a,b) in enumerate(combinations(range(n),2)) if block_of[a]!=block_of[b])

def calc(n,s):
  pp=partitions(n,s)
  masks=list(map(lambda p:mask(p,n),pp))
  assert len(masks)==len(set(masks)),(n,s,len(masks),len(set(masks)))
  q,r=divmod(n,s)
  t=q if r else 2*(q-1)
  dist=lambda a,b:(a^b).bit_count()//2
  minval=min((dist(a,b) for i,a in enumerate(masks) for b in masks[i+1:]),default=0)
  adj=[[] for _ in masks]
  for i,a in enumerate(masks):
    for j in range(i+1,len(masks)):
      if dist(a,masks[j])<=t:
        adj[i].append(j);adj[j].append(i)
  seen={0};que=deque([0])
  while que:
    for j in adj[que.popleft()]:
      if j not in seen: seen.add(j);que.append(j)
  if r==0: expected=(2*(s*(s-1)//2) if q==2 else s*(s-1)//2*q*q)
  elif q==1: expected=2*r*(s-r) + r*(s-r)*(s-r-1)//2
  elif q==2: expected=3*r*(s-r) + (s-r)*(s-r-1)
  else: expected=(q+1)*r*(s-r)
  assert set(map(len,adj))=={expected}, (n,s,set(map(len,adj)),expected)
  return len(pp), minval, t, len(seen)==len(masks), sorted(set(len(a) for a in adj))[:5]
for n in range(4,11):
 for s in range(2,min(n,6)):
  p, minimum, target, connected, degrees=calc(n,s)
  print(n,s,p,minimum,target,connected,degrees)
  assert minimum==target and connected
print('VERIFY_OK')
