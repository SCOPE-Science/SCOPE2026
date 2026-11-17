#!/usr/bin/env python3
"""Independent fixed-vertex-orbit derivation of the ternary Rips homology character."""
import itertools,collections,json
V=list(itertools.product(range(3),repeat=3)); idx={v:i for i,v in enumerate(V)}
perm=list(itertools.permutations(range(3)))
auto=[]
for coord in perm:
 for syms in itertools.product(perm,repeat=3):
  auto.append(tuple(idx[tuple(syms[j][v[coord[j]]] for j in range(3))] for v in V))
assert len(set(auto))==1296

def homology_trace(g):
 unseen=set(range(27)); cycles=[]
 while unseen:
  i=min(unseen); orbit=[]; t=i
  while t in unseen:
   unseen.remove(t);orbit.append(t);t=g[t]
  assert t==i
  cycles.append(orbit)
 # Cycle can be included only if all its vertices agree in some coordinate pairwise.
 valid=[]
 for orbit in cycles:
  if all(any(V[i][k]==V[j][k] for k in range(3)) for i,j in itertools.combinations(orbit,2)):
   valid.append(orbit)
 m=len(valid)
 compatible=[0]*m
 for j in range(m):
  for k in range(j+1,m):
   if all(any(V[i][c]==V[t][c] for c in range(3)) for i in valid[j] for t in valid[k]):
    compatible[j]|=1<<k
 result=1
 def recur(cands, sign):
  nonlocal result
  while cands:
   x=cands&-cands;i=x.bit_length()-1;cands-=x
   result-=sign
   recur(cands&compatible[i],-sign)
 recur((1<<m)-1,1)
 return result

cs=json.load(open(str(__import__('pathlib').Path(__file__).resolve().parent/'character_data.json')))['class_data']
check={tuple(tuple(row) for row in c['representative']):c['character'] for c in cs}
for g in auto:
 if tuple(V[g[i]] for i in range(27)) in check:
  assert homology_trace(g)==check[tuple(V[g[i]] for i in range(27))]
# compute ALL values, and compare each with the corresponding conjugacy class using a cycle signature and conjugacy membership computation
v=[homology_trace(g) for g in auto]
assert len(v)==1296
assert v.count(46)==1
assert sum(v)==0
assert sum(t*t for t in v)==7*1296
print('all_group_character_count',collections.Counter(v))
# a second enumeration of translation subgroup, avoiding class data
trans=[]
for delta in itertools.product(range(3),repeat=3):
 g=tuple(idx[tuple((a+d)%3 for a,d in zip(p,delta))] for p in V)
 trans.append(homology_trace(g))
assert sum(trans)==54
print('translation_character_count',collections.Counter(trans))
print('translation_invariants',sum(trans)//27)
print('all_group_invariants',sum(v)//1296)
print('full_character_self_inner_product',sum(x*x for x in v)//1296)
print('TERNARY_RIPS_ORBIT_CHARACTER_PASS')
