#!/usr/bin/env python3
"""Exact graph-automorphism orbits of primitive four-cycles for two 16-vertex graphs."""
import itertools
from collections import Counter
from pathlib import Path
S = [(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)]
POW=[3**i for i in range(16)]
def neigh(kind):
    ret=[]
    for a in range(4):
     for b in range(4):
      if kind=='shri':
       ret.append([4*((a+da)%4)+(b+db)%4 for da,db in S])
      else:ret.append([4*x+y for x in range(4) for y in range(4) if (x==a or y==b) and (x,y)!=(a,b)])
    return ret

def step(x, N):
    digits=[(x//w)%3 for w in POW]
    out=[2 if c==1 else 0 if c==2 else int(any(digits[j]==1 for j in N[i])) for i,c in enumerate(digits)]
    return sum(out[i]*POW[i] for i in range(16))

def group(kind):
  maps=[]
  if kind=='rook':
    for a in itertools.permutations(range(4)):
     for b in itertools.permutations(range(4)):
      for transpose in (False,True):
       m=[]
       for x in range(4):
        for y in range(4):
         m.append(4*a[y]+b[x] if transpose else 4*a[x]+b[y])
       maps.append(tuple(m))
  else:
    letters=[]
    for c in itertools.product(range(4),repeat=4):
     x0,y0,x1,y1=c
     T={
         ((x0*dx+x1*dy)%4,(y0*dx+y1*dy)%4) for dx,dy in S
     }
     if T!=set(S):continue
     # each map of generators invertible implies full (verify)
     test={( (x0*x+x1*y)%4, (y0*x+y1*y)%4) for x in range(4) for y in range(4)}
     if len(test)!=16:continue
     letters.append(c)
    assert len(letters)==12,len(letters)
    for tx in range(4):
     for ty in range(4):
      for x0,y0,x1,y1 in letters:
       m=tuple(4*((tx+x0*x+x1*y)%4)+(ty+y0*x+y1*y)%4 for x in range(4) for y in range(4))
       maps.append(m)
  assert len(maps)==len(set(maps)) and len(maps)==(192 if kind=='shri' else 1152)
  N=neigh(kind)
  # A rooted automorphism fixing each neighbor also fixes every nonneighbor:
  # each nonneighbor has a distinct two-point trace on the root's neighborhood.
  outside=[v for v in range(1,16) if v not in N[0]]
  traces={tuple(sorted(set(N[v]) & set(N[0]))) for v in outside}
  assert len(outside)==len(traces)==9
  # The neighborhood is respectively a 6-cycle or two disjoint 3-cliques.
  local_degrees=[len(set(N[v]) & set(N[0])) for v in N[0]]
  assert sorted(local_degrees)==[2]*6
  if kind=='shri':
    assert len({tuple(sorted((v,w))) for v in N[0] for w in N[v] if w in N[0]})==6
  else:
    assert all(len(set(N[v])&set(N[w])&set(N[0])) in (0,1) for v in N[0] for w in N[0] if v!=w)
  for m in maps:
   assert all(sorted(m[j] for j in N[i])==sorted(N[m[i]]) for i in range(16))
  return maps

def permute(s, p):
  out=0
  for i in range(16):
    out+=((s//POW[i])%3)*POW[p[i]]
  return out

def run(kind):
  reps = sorted(int(line.split()[1]) for line in Path(f'{kind}_reps.txt').read_text().splitlines() if line.startswith('REP4'))
  N=neigh(kind)
  state_rep={}
  for r in reps:
   s=r
   for i in range(4):
    assert s not in state_rep or state_rep[s]==r
    state_rep[s]=r
    s=step(s,N)
   assert s==r
  assert len(state_rep)==4*len(reps)
  G=group(kind)
  pending=set(reps); groups=[]
  while pending:
    r=min(pending)
    orbit={state_rep[permute(r,g)] for g in G}
    assert orbit<=pending
    assert len(G)%len(orbit)==0
    groups.append((r,len(orbit),len(G)//len(orbit)))
    pending-=orbit
  print(kind,'|Aut|',len(G),'#period4',len(reps),'#symmetry types',len(groups),'(representative,cycles,stabilizer):',groups)
  Path(f'{kind}_symmetry.txt').write_text(f'graph={kind}\ngroup_size={len(G)}\ncycle4={len(reps)}\nclasses={groups}\n')
if __name__=='__main__':
 for k in ('shri','rook'):run(k)
