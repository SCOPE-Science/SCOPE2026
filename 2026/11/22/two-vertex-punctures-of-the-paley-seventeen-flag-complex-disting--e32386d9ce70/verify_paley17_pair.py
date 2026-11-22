#!/usr/bin/env python3
"""Reconstruct two-vertex punctures in the Paley 17 flag complex; stdlib only."""
import itertools,collections,json
N=17
Q={pow(i,2,N) for i in range(1,N)}
EDGES={tuple((i,j)) for i in range(N) for j in range(i+1,N) if (j-i)%N in Q}
TREES={
 'adjacent':[(2,6),(2,11),(11,13),(6,15),(14,15),(14,16),(12,13),(9,11),(6,10),(4,12),(8,12),(3,4),(5,13),(7,15)],
 'nonadjacent':[(1,2),(2,6),(2,15),(1,16),(1,14),(1,10),(2,11),(2,4),(7,16),(10,12),(13,15),(1,9),(1,5),(8,16)],
 'single':[(1,14),(1,3),(1,5),(1,16),(15,16),(1,9),(3,12),(6,14),(4,12),(9,10),(2,4),(9,11),(7,16),(8,16),(5,13)]
}
def faces(vertices):
 vertices=sorted(vertices)
 return {t for size in range(1,5) for t in itertools.combinations(vertices,size) if all(e in EDGES for e in itertools.combinations(t,2))}
def check(label,vertex_set,tree,expected):
 F=faces(vertex_set)
 cnt=collections.Counter(map(len,F))
 tree={tuple(sorted(e)) for e in tree}
 assert len(tree)==len(vertex_set)-1 and tree<={f for f in F if len(f)==2}
 root=min(vertex_set); adj={v:[] for v in vertex_set}
 for a,b in tree:adj[a].append(b);adj[b].append(a)
 seen={root};stack=[root];pairs=[]
 while stack:
  u=stack.pop(0)
  for v in sorted(adj[u]):
   if v not in seen:
    seen.add(v);pairs.append(((v,),tuple(sorted((u,v)))));stack.append(v)
 assert seen==vertex_set
 resolved=set(tree); used=set();tris=sorted(f for f in F if len(f)==3)
 while True:
  candidates=[]
  for t in tris:
   if t in used:continue
   miss=[e for e in itertools.combinations(t,2) if e not in resolved]
   if len(miss)==1:candidates.append((miss[0],t))
  if not candidates:break
  e,t=min(candidates)
  resolved.add(e);used.add(t);pairs.append((e,t))
 assert resolved=={f for f in F if len(f)==2}
 assert len(pairs)==expected['pairs']
 selected=[f for pair in pairs for f in pair]
 assert len(set(selected))==len(selected)
 critical=F-set(selected)
 critical_count=collections.Counter(len(f)-1 for f in critical)
 assert dict(critical_count)==expected['critical']
 matched=set(pairs);out={f:[] for f in F};indegree={f:0 for f in F};hasse=0
 for b in F:
  if len(b)<2:continue
  for a in itertools.combinations(b,len(b)-1):
   assert a in F
   u,v=(a,b) if (a,b) in matched else (b,a)
   out[u].append(v);indegree[v]+=1;hasse+=1
 queue=collections.deque(f for f in F if indegree[f]==0);visited=0
 while queue:
  u=queue.popleft();visited+=1
  for v in out[u]:
   indegree[v]-=1
   if indegree[v]==0:queue.append(v)
 assert visited==len(F)
 assert cnt[4]==0
 return {'vertices':cnt[1],'edges':cnt[2],'triangles':cnt[3],'matched_pairs':len(pairs),'critical_0':critical_count[0],'critical_2':critical_count[2],'dag_vertices_checked':visited,'hasse_incidences':hasse}
def main():
 assert len(Q)==8 and len(EDGES)==68 and 1 in Q and 3 not in Q
 cases={}
 for key,v,cr,pairs in [('adjacent',1,8,53),('nonadjacent',3,6,52)]:
  cases[key]=check(key,set(range(N))-{0,v},TREES[key],{'pairs':pairs,'critical':{0:1,2:cr}})
 # Also reconstruct one-point deletion and ambient as independent evidence for inclusion ranks.
 cases['single']=check('single',set(range(N))-{0},TREES['single'],{'pairs':60,'critical':{0:1,2:11}})
 cases['ambient']=check('ambient',set(range(N)),TREES['single']+[(0,1)],{'pairs':68,'critical':{0:1,2:16}})
 # The vertex links in the single deletion are induced subgraphs of the cube link.
 links={}
 for v in [1,3]:
  vs={w for w in range(N) if w!=0 and w!=v and tuple(sorted((v,w))) in EDGES}
  lf=faces(vs)
  assert all(len(f)<3 for f in lf)
  es=[e for e in lf if len(e)==2]
  nbr={w:set() for w in vs}
  for a,b in es:nbr[a].add(b);nbr[b].add(a)
  reach={min(vs)};queue=list(reach)
  for u in queue:
   for w in sorted(nbr[u]):
    if w not in reach:reach.add(w);queue.append(w)
  assert reach==vs
  links[str(v)]={'vertices':len(vs),'edges':len(es),'b1':len(es)-len(vs)+1}
 assert links['1']['b1']==3 and links['3']['b1']==5
 # Check action x -> a*x+b, a quadratic residue. It preserves edges, and
 # maps all 68 unordered edges to (0,1), all 68 nonedges to (0,3).
 maps=[tuple((a*x+b)%N for x in range(N)) for a in sorted(Q) for b in range(N)]
 assert len(set(maps))==136
 for p in maps:
  assert all((tuple(sorted((p[u],p[v]))) in EDGES)==((u,v) in EDGES) for u in range(N) for v in range(u+1,N))
 representatives={(0,1):'adjacent',(0,3):'nonadjacent'}
 for u in range(N):
  for v in range(u+1,N):
   tgt=(0,1) if (u,v) in EDGES else (0,3)
   assert any(set((p[u],p[v]))==set(tgt) for p in maps)
 payload={'graph_vertices':17,'graph_edges':68,'quadratic_residues':sorted(Q),'cases':cases,'deletion_links':links,'affine_maps_verified':136,'unordered_pairs_covered':136,'claim':'Two-vertex deletion of Paley-17 flag complex is 8 or 6 two-spheres according as vertices are adjacent or not; inclusions in ambient induce split integral injections.'}
 print(json.dumps(payload,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
