#!/usr/bin/env python3
"""Independent triple-product subset BFS; no word-signature intersections."""
from itertools import product
from collections import defaultdict,deque
TRANS=list(product(range(3),repeat=3))

def images(pair):
  tab=[]
  for t in pair:
    tab.append(tuple(frozenset(t[x] for x in range(3) if mask & (1<<x)) for mask in range(8)))
  return tab

def idmask(states):
  return sum(1<<s for s in states)

def signature(pair):
  T=images(pair)
  levels=[(frozenset(range(3)),)]
  sig=[]
  for L in range(1,8):
    levels=[(frozenset(T[c][idmask(st)]),) for (st,) in levels for c in (0,1)]
    sig.append(tuple(len(st)==1 for (st,) in levels))
  return tuple(sig)

def bfs_shortest(triple):
  tabs=[images(pair) for pair in triple]
  start=(7,7,7);Q=deque([(start,0)]);seen={start}
  while Q:
    p,d=Q.popleft()
    if all(m in (1,2,4) for m in p):return d
    for c in (0,1):
      nxt=tuple(idmask(tabs[i][c][p[i]]) for i in range(3))
      if nxt not in seen:
        seen.add(nxt);Q.append((nxt,d+1))
  raise AssertionError('expected synchronizing')

def main():
  groups=defaultdict(list)
  for a in TRANS:
    for b in TRANS:
      pair=(a,b)
      sig=signature(pair)
      if any(sig[-1]):groups[sig].append(pair)
  print('sync',sum(map(len,groups.values())),'types',len(groups))
  assert len(groups)==28
  items=list(groups.values()); dist=defaultdict(int)
  for x in items:
    for y in items:
      for z in items:
        d=bfs_shortest((x[0],y[0],z[0]))
        dist[d]+=len(x)*len(y)*len(z)
  print('direct_BFS_distribution',sorted(dist.items()))
  assert sum(dist.values())==549**3
  assert sorted(dist.items())==[(1,1062153),(2,48991068),(3,66420432),(4,35524872),(5,10653120),(6,2651616),(7,165888)]
  example=(((0,0,1),(0,2,2)),((0,0,2),(0,2,1)),((0,0,2),(2,0,1)))
  assert bfs_shortest(example)==7
  print('VERIFIED_TRIPLE_BFS')
if __name__=='__main__':main()
