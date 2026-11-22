"""Enumerate all Tietze automorphisms and majority recurrent symmetry classes.

Run: python3 check_symmetry.py. Only the Python standard library is needed.
"""
from itertools import permutations

EDGES = {
    (0,1),(0,5),(0,9),(1,2),(1,6),(2,3),(2,7),(3,8),(3,10),
    (4,6),(4,7),(4,11),(5,7),(5,8),(6,8),(9,10),(9,11),(10,11)
}
EDGES = {tuple(sorted(e)) for e in EDGES}
assert len(EDGES) == 18
# Unique triangle, computed rather than assumed.
triangles=[]
for a in range(12):
 for b in range(a+1,12):
  for c in range(b+1,12):
   if {(a,b),(a,c),(b,c)}<=EDGES:triangles.append((a,b,c))
assert triangles==[(9,10,11)]

AUTO=[]
tri=(9,10,11)
private={9:0,10:3,11:4} # unique outside neighbor of each triangle vertex
outer=tuple(i for i in range(12) if i not in set(tri) | set(private.values()))
for tri_perm in permutations(tri):
 mapping={a:b for a,b in zip(tri,tri_perm)}
 mapping.update({private[a]:private[b] for a,b in zip(tri,tri_perm)})
 for outer_perm in permutations(outer):
  perm=dict(mapping)
  perm.update(zip(outer,outer_perm))
  if {tuple(sorted((perm[a],perm[b]))) for a,b in EDGES}==EDGES:
   AUTO.append(tuple(perm[i] for i in range(12)))
assert len(AUTO)==12 and len(set(AUTO))==12

neigh=[[] for _ in range(12)]
for a,b in EDGES:neigh[a].append(b);neigh[b].append(a)
assert all(len(a)==3 for a in neigh)

def step(x):
 return sum((1<<i) for i,ns in enumerate(neigh) if sum((x>>j)&1 for j in ns)>=2)

def transform(x,p):
 return sum(((x>>i)&1)<<p[i] for i in range(12))

fixed=set();cycles=set()
for x in range(4096):
 y=step(x)
 if step(y)!=x:continue
 if y==x:fixed.add(x)
 else:cycles.add(tuple(sorted((x,y))))
assert len(fixed)==16 and len(cycles)==137
fx_classes={min(transform(x,g) for g in AUTO) for x in fixed}
cy_classes={min(tuple(sorted((transform(x,g),transform(y,g)))) for g in AUTO)
            for x,y in cycles}
assert len(fx_classes)==6 and len(cy_classes)==29
# Check preservation of the dynamics for every automorphism and state.
for g in AUTO:
 for x in range(4096):
  assert step(transform(x,g))==transform(step(x),g)
print('automorphisms',len(AUTO),'fixed_geometric_classes',len(fx_classes),
      'two_cycle_geometric_classes',len(cy_classes))
print('SYMMETRY_CHECK_PASSED')
