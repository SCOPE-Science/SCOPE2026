import itertools,collections,json
from math import comb
V=list(range(6))
E=[(u,v) for u in V for v in V if u<v and u//2!=v//2]
edge_idx={e:i for i,e in enumerate(E)}
inc={v:[i for i,(a,b) in enumerate(E) if v in (a,b)] for v in V}
# local states 0=empty, 1=vertex, 2..5=halfedges. Restrict total particles to three
mons={j:list(itertools.combinations_with_replacement(range(12),j)) for j in range(4)}
states=[]
for k in range(4):
 for vs in itertools.combinations(V,k):
  for ls in itertools.product(range(1,6),repeat=k):
   opt=tuple((v,s) for v,s in zip(vs,ls))
   for m in mons[3-k]:
    states.append((opt,m))
assert len(states)==9704,len(states)
for p in itertools.permutations(range(3)):
 for bs in itertools.product((0,1),repeat=3):
  g=[2*p[x//2]+((x%2)^bs[x//2]) for x in V]
  ep=[edge_idx[tuple(sorted((g[a],g[b])))] for a,b in E]
  total=0
  for loc,m in states:
   gm=tuple(sorted(ep[i] for i in m))
   if gm!=m:continue
   image=[]
   for v,s in loc:
    gv=g[v]
    if s==1:gs=1
    else:gs=2+inc[gv].index(ep[inc[v][s-2]])
    image.append((gv,gs))
   sorted_image=sorted(image)
   if sorted_image!=list(loc):continue
   # odd halfedge local factors only; permutation sign inversions after mapping
   hs=[gv for (gv,gs) in image if gs>=2]
   inv=sum(hs[i]>hs[j] for i in range(len(hs)) for j in range(i+1,len(hs)))
   total+=(-1)**(len(hs)+inv)
  import characters
  target=next(val[0] for gg,key,det,val in characters.autom if gg==g)
  assert total==target,(g,total,target)
print('INDEPENDENT_EULER_OK',len(states),'states','48 automorphisms')
