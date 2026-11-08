"""Rebuild the simplicial-barycentric orbit CW complex and replay each elementary collapse."""
import collections, itertools, csv, pathlib

N=12
edges={tuple(sorted(e)) for e in ({(i,(i+1)%N) for i in range(N)}|{(i,(i+6)%N) for i in range(6)})}
faces=[]
for r in range(1,N+1):
 for c in itertools.combinations(range(N),r):
  if all(tuple(sorted(e)) not in edges for e in itertools.combinations(c,2)):
   faces.append(sum(1<<i for i in c))
faces.sort(key=lambda f:(f.bit_count(),f))
by_size={r:[f for f in faces if f.bit_count()==r] for r in range(1,6)}
assert len(faces)==196 and max(f.bit_count() for f in faces)==5
flags=[]
def descend(chain,size):
 flags.append(chain)
 for next_size in range(size+1,6):
  for f in by_size[next_size]:
   if (f & chain[-1])==chain[-1]:
    descend(chain+(f,),next_size)
for size, ff in by_size.items():
 for f in ff:descend((f,),size)
assert len(flags)==11236

def reflected(f):
 return sum(1<<((-i)%N) for i in range(N) if (f>>i)&1)
def rep(chain):
 return min(chain,tuple(reflected(f) for f in chain))
chains=sorted({rep(c) for c in flags},key=lambda c:(len(c),c))
lookup={c:i for i,c in enumerate(chains)}
assert len(chains)==5646
assert collections.Counter(len(c) for c in chains)=={1:106,2:806,3:1998,4:2016,5:720}
facesof=[tuple(lookup[rep(c[:i]+c[i+1:])] for i in range(len(c))) if len(c)>1 else tuple() for c in chains]
assert all(len(set(b))==len(b) for b in facesof)
cofaces=[set() for _ in chains]
for j,b in enumerate(facesof):
 for i in b:
  assert len(chains[j])==len(chains[i])+1
  cofaces[i].add(j)
# Read exact collapse sequence; each lower cell must be incident to exactly one
# remaining next-dimensional cell, and its incidence coefficient has magnitude 1.
cert=pathlib.Path(__file__).with_name('collapse_pairs.csv')
with cert.open(newline='',encoding='utf-8') as f:
 pairs=[tuple(int(x) for x in row) for row in csv.reader(f)]
assert len(pairs)==2768
live=set(range(len(chains)))
for step,(lower,upper) in enumerate(pairs):
 assert lower in live and upper in live,(step,lower,upper)
 assert (cofaces[lower]&live)=={upper},(step,lower,upper)
 assert lower in facesof[upper]
 assert not (cofaces[upper]&live), (step,lower,upper)
 live.remove(lower);live.remove(upper)
counts=collections.Counter(len(chains[i]) for i in live)
assert counts=={1:20,2:54,3:36},counts
assert max(counts)==3 and sum((-1)**(k-1)*n for k,n in counts.items())==2
# The quotient has one component, as does its connected original space.
# Verify connectivity directly on retained 1-skeleton.
verts={i for i in live if len(chains[i])==1}
adj={i:set() for i in verts}
for i in live:
 if len(chains[i])==2:
  ends=tuple(j for j in facesof[i] if j in live)
  assert len(ends)==2
  adj[ends[0]].add(ends[1]);adj[ends[1]].add(ends[0])
seen={next(iter(verts))};todo=list(seen)
while todo:
 for v in adj[todo.pop()]-seen:
  seen.add(v);todo.append(v)
assert seen==verts
print('ALL_VERIFY_OK')
print(f'original_faces={len(faces)} barycentric_flags={len(flags)} orbit_cells={len(chains)}')
print(f'collapse_pairs={len(pairs)} remaining_vertices={counts[1]} edges={counts[2]} triangles={counts[3]}')
print('remaining_dimension=2 euler_characteristic=2 connected_1_skeleton=true')
