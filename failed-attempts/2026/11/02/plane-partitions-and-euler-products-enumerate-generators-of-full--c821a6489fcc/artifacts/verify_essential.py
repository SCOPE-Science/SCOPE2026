#!/usr/bin/env python3
"""Independently count essential rank-two orbits by explicit rank-three square witnesses."""
import itertools
from orbit_formulas import generate, euler_transform, mul

def enumerate_pairs(n):
  elems=range(n); pairs=set()
  for t in itertools.product(elems,repeat=n):
    tt=tuple(t[t[i]] for i in elems)
    if any(t[tt[i]]!=t[i] for i in elems):continue
    fixed=tuple(i for i in elems if t[i]==i)
    if not fixed:continue
    # orbit components as sets, independently from any root-fiber generating functions
    unvisited=set(elems)
    components=[]
    while unvisited:
      v=next(iter(unvisited))
      related={k for k in elems if tt[k]==tt[v] or t[k]==t[v] or t[k]==tt[v] or tt[k]==t[v]}
      # actually define components by their t-cycle coordinate via tracing t^2 and t
      key=tuple(sorted((tt[v],t[v])))
      related={k for k in elems if tuple(sorted((tt[k],t[k])))==key}
      components.append(related)
      unvisited.difference_update(related)
    for r in range(1,len(fixed)+1):
      for R in itertools.combinations(fixed,r):
        forced=[v for v,C in enumerate(components) if any(j in R for j in C)]
        remaining=[v for v in range(len(components)) if v not in forced]
        for assignment in itertools.product(R, repeat=len(remaining)):
          cp=[None]*len(components)
          for v in forced:cp[v]=next(j for j in components[v] if j in R)
          for v,j in zip(remaining,assignment):cp[v]=j
          e=[None]*n
          for v,C in enumerate(components):
            for j in C:e[j]=cp[v]
          pairs.add((t,tuple(e)))
  return pairs

def orbit_count(n):
  pairs=enumerate_pairs(n)
  forced=set()
  for t,e in pairs:
    tt=tuple(t[t[i]] for i in range(n))
    if t!=tt:forced.add((tt,e))
  assert forced<=pairs
  essential_pairs={p for p in pairs if p[0] != p[1] and p[0]==tuple(p[0][p[0][i]] for i in range(n)) and p not in forced}
  # Orbit BFS of essential pairs and all rank 3 pairs.
  def orbcount(objects):
    objects=set(objects);orbitnum=0
    while objects:
      seed=objects.pop();orbitnum+=1;todo=[seed];visited={seed}
      for t,e in todo:
        for i in range(n-1):
          def sw(x):return i+1 if x==i else i if x==i+1 else x
          p=(tuple(sw(t[sw(j)]) for j in range(n)),tuple(sw(e[sw(j)]) for j in range(n)))
          if p not in visited:visited.add(p);todo.append(p)
      assert visited.issubset(objects|visited)
      objects.difference_update(visited)
    return orbitnum
  actual_r2=orbcount(essential_pairs)
  actual_r3=orbcount((t,e) for t,e in pairs if tuple(t[t[i]] for i in range(n))!=t)
  U=[0]+[1]*n
  R1=mul(U,[1]+U[1:],n)
  E1=euler_transform(R1,n)
  Ebase=euler_transform(U,n)
  predicted_r2=E1[n]-Ebase[n]
  predicted_r3=generate(n)['rank3'][n]
  print(f'n={n}: {len(pairs)} permissible ordered pairs, {len(essential_pairs)} essential rank-two pairs; essential orbit counts rank2={actual_r2}, rank3={actual_r3}; formulas={predicted_r2},{predicted_r3}')
  assert (actual_r2,actual_r3)==(predicted_r2,predicted_r3)

for n in [5,6]:orbit_count(n)
print('VERIFY_OK')
