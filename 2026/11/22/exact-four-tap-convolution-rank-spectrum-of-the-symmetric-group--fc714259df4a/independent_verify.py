"""Independent exact rational representative checks and symmetry expansion for S4.
Canonical orbit generation uses translation, conjugation and inversion.
"""
import itertools, collections
from sympy import Matrix
G=list(itertools.permutations(range(4)))
idx={x:i for i,x in enumerate(G)}
def prod(a,b): return tuple(a[b[i]] for i in range(4))
def inv(p):return tuple(p.index(i) for i in range(4))
N=24
mul=[[idx[prod(g,h)] for h in G] for g in G]
inv_idx=[idx[inv(g)] for g in G]
conj=[[mul[mul[b][s]][inv_idx[b]] for s in range(N)] for b in range(N)]
left=[[mul[b][s] for s in range(N)] for b in range(N)]
allsets={tuple(x) for x in itertools.combinations(range(24),4)}
classes=[]
while allsets:
 s=min(allsets)
 orb=set()
 for l in range(24):
  for b in range(24):
   for flip in (False,True):
    v=tuple(sorted((inv_idx[z] if flip else z) for z in (conj[b][left[l][x]] for x in s)))
    orb.add(v)
 allsets-=orb
 # Construct matrix via right-permutation (different convention from main C)
 mat=Matrix([[int(any(mul[x][g]==y for g in s)) for y in range(24)] for x in range(24)])
 r=mat.rank()
 classes.append((s,r,len(orb)))
counts=collections.Counter()
for s,r,n in classes:counts[r]+=n
print('ORBIT_COUNT',len(classes))
print('RANK_COUNTS',dict(sorted(counts.items())))
print('ORBIT_SIZE_DISTRIBUTION',dict(sorted(collections.Counter(n for s,r,n in classes).items())))
assert sum(n for s,r,n in classes)==10626
assert dict(counts)=={6:42,9:144,12:576,15:1008,18:2856,20:1728,21:3024,24:1248}
assert len(classes)==34
with open('independent_orbits.tsv','w') as f:
 for s,r,n in classes:f.write(f'{",".join(map(str,s))}\t{r}\t{n}\n')
