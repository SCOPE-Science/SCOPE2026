"""A triangle-fill certificate for simple connectivity of the labelled complex."""
from itertools import combinations
v=[(r,c,s) for r in range(3) for c in range(3) for s in range(3)]
def ok(a,b):return sum(x==y for x,y in zip(v[a],v[b]))<=1
edges={tuple(x) for x in combinations(range(27),2) if ok(*x)}
triangles=[t for t in combinations(range(27),3) if all(tuple(sorted(e)) in edges for e in combinations(t,2))]
assert len(edges)==270 and len(triangles)==1278
seen={0};tree=set()
while len(seen)<27:
 for a,b in sorted(edges):
  if (a in seen)!=(b in seen):tree.add((a,b));seen.add(b if a in seen else a);break
 else:raise ValueError('Disconnected')
assert len(tree)==26
killed=set(tree);rounds=[]
while True:
 added=set()
 for t in triangles:
  sides={tuple(x) for x in combinations(t,2)}
  unsides=sides-killed
  if len(unsides)==1:added|=unsides
 if not added:break
 killed|=added;rounds.append(sorted(added))
print(len(edges),len(triangles),'tree',len(tree),'killrounds',[len(x) for x in rounds],'survive',len(edges-killed))
assert killed==edges
print('LATIN_P3_PI1_OK')
