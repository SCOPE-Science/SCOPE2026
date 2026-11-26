"""Alternative expansion from normalized codes to all labeled size-four codes."""
from itertools import permutations, combinations
P=list(permutations(range(6)))
index={p:i for i,p in enumerate(P)}
triples=list(permutations(range(6),3))
tridx={t:i for i,t in enumerate(triples)}
mask=[sum(1<<tridx[t] for t in combinations(p,3)) for p in P]
N=[i for i in range(1,720) if not mask[i]&mask[0]]
# Alternative independent nested loops avoid shortcut through either previous verifier.
C=[]
for ai,a in enumerate(N):
 for b in N[ai+1:]:
  if mask[a]&mask[b]:continue
  for c in N:
   if c<=b or mask[a]&mask[c] or mask[b]&mask[c]:continue
   C.append((0,a,b,c))
assert len(C)==298
full=set()
for co in C:
 for sigma in P:
  transform=frozenset(index[tuple(sigma[v] for v in P[c])] for c in co)
  assert len(transform)==4
  full.add(transform)
assert len(full)==53640
assert len(full)*4 ==len(C)*len(P)
print('LABELED_VERIFY_OK codes=',len(full),'anchored=',len(C),'symbols=',len(P))
