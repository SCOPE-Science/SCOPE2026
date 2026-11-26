#!/usr/bin/env python3
"""Independent exact enumeration of minimum independent domination of Shrikhande."""
import itertools, json, collections, argparse
V=range(16)
def xy(v):return divmod(v,4)
def linked(i,j):
 if i==j:return False
 a,b=xy(i);c,d=xy(j)
 return ((a-c)%4,(b-d)%4) in {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
N=[{v}|{u for u in V if linked(u,v)} for v in V]
seeds=[]
for k in range(1,4):
 for s in itertools.combinations(V,k):
  if any(linked(u,v) for u,v in itertools.combinations(s,2)):continue
  if len(set.union(*(N[u] for u in s)))==16:seeds.append(s)
assert all(len(s)==3 for s in seeds) and len(seeds)==32
S={frozenset(s) for s in seeds}
E=[]
for A,B in itertools.combinations(seeds,2):
 xa=set(A);xb=set(B)
 if len(xa&xb)!=2:continue
 u=next(iter(xa-xb));v=next(iter(xb-xa))
 assert linked(u,v) # every admissible one-exchange is a token slide
 E.append((A,B))
assert len(E)==48
G={s:set() for s in S}
for a,b in E:G[frozenset(a)].add(frozenset(b));G[frozenset(b)].add(frozenset(a))
assert set(map(len,G.values()))=={3}
hists={}
for r in S:
 dist={r:0};Q=[r]
 for s in Q:
  for t in G[s]:
   if t not in dist:dist[t]=dist[s]+1;Q.append(t)
 assert len(dist)==32
 hist=tuple(sorted(collections.Counter(dist.values()).items()))
 hists[hist]=hists.get(hist,0)+1
assert hists=={((0,1),(1,3),(2,6),(3,9),(4,9),(5,4)):32}
coords=lambda s:sorted([[x//4,x%4] for x in s])
mask=lambda s:sum(1<<v for v in s)
cert={'graph':'Shrikhande Cayley Z4^2, shifts +- (1,0), +- (0,1), +- (1,1)', 'minimum_independent_domination_number':3, 'sets':sorted(map(mask,seeds)), 'slide_edges':sorted([sorted([mask(a),mask(b)]) for a,b in E]),'distance_histogram':[[0,1],[1,3],[2,6],[3,9],[4,9],[5,4]],'all_vertices_same_histogram':True}
parser=argparse.ArgumentParser();parser.add_argument('--certificate',default='certificate.json');args=parser.parse_args()
with open(args.certificate,'w',encoding='utf-8') as f:json.dump(cert,f,sort_keys=True,separators=(',',':'));f.write('\n')
print('PASS independent exhaustive subset enumeration: i=3, 32 sets, 48 sliding exchanges, degree 3, radius=diameter=5')
print('PASS all distance distributions: 1,3,6,9,9,4; all single exchanges are slides')
