#!/usr/bin/env python3
"""Check cut-complex and symmetry certificates using only Python standard library.

Run from the directory containing CERTIFICATE.json: python3 verify.py
The structural homotopy lemmas used after these finite checks are stated in RESULT.md.
"""
import json
from itertools import combinations,permutations
from collections import Counter, defaultdict

with open('CERTIFICATE.json',encoding='utf-8') as f:C=json.load(f)
V=[(i,j) for i in range(4) for j in range(4) if i!=j]
assert C['vertex_labels']==[list(v) for v in V]
IX={v:k for k,v in enumerate(V)};FULL=(1<<12)-1
adj=[set() for _ in range(12)]
for a,(i,j) in enumerate(V):
 for b,(k,l) in enumerate(V):
  if a<b and (i==k or (i==l and j==k)):
   adj[a].add(b);adj[b].add(a)
assert len(adj)==12 and all(len(x)==3 for x in adj)
assert sum(len(x) for x in adj)//2==18

def bits(s):return [i for i in range(12) if s&(1<<i)]
def bm(t):return sum(1<<i for i in t)
def conn(s):
 subset=set(s); reached={next(iter(subset))}
 while 1:
  nxt=reached|set().union(*(adj[i]&subset for i in reached))
  if reached==nxt:return reached==subset
  reached=nxt

conn4={bm(x) for x in combinations(range(12),4) if conn(x)}
disc4={bm(x) for x in combinations(range(12),4) if not conn(x)}
assert len(conn4)==48 and len(disc4)==447 and len(conn4|disc4)==495
K=set()
for s in disc4:
 facet=FULL^s;subset=facet
 while subset:
  K.add(subset);subset=(subset-1)&facet
assert Counter(s.bit_count()-1 for s in K)=={0:12,1:66,2:220,3:495,4:792,5:924,6:792,7:447}
assert all(bm(t) in K for t in combinations(range(12),7))
# Reconstruct Alexander dual independently from the *whole* original face set.
L={s for s in range(1,FULL+1) if (FULL^s) not in K and (FULL^s)!=0}
expected={bm(t) for k in (1,2,3) for t in combinations(range(12),k)}|conn4
assert L==expected and Counter(s.bit_count()-1 for s in L)=={0:12,1:66,2:220,3:48}
active=set(L)
for i,(t,s) in enumerate(C['collapse_pairs']):
 assert t in active and s in active and s.bit_count()==4 and t.bit_count()==3
 assert t&s==t and len([f for f in active if t&f==t])==2,(i,t,s)
 active.remove(t);active.remove(s)
assert len(C['collapse_pairs'])==48 and Counter(s.bit_count()-1 for s in active)=={0:12,1:66,2:172}
# A spanning tree contracts without changing pi_1, while each residual triangle
# with exactly one unknown edge proves that edge null in pi_1.
E={s for s in active if s.bit_count()==2};TR={s for s in active if s.bit_count()==3}
parent=list(range(12))
def root(v):
 while parent[v]!=v:v=parent[v]
 return v
known=set()
for edge in C['spanning_tree_edges']:
 assert edge in E and edge not in known
 x,y=bits(edge);x=root(x);y=root(y)
 assert x!=y
 parent[x]=y; known.add(edge)
assert len(C['spanning_tree_edges'])==11 and len({root(v) for v in range(12)})==1
for edge,triangle in C['fundamental_group_eliminations']:
 assert triangle in TR
 tri_edges={triangle^(1<<j) for j in bits(triangle)}
 assert tri_edges<=E and tri_edges-known=={edge}
 known.add(edge)
assert len(C['fundamental_group_eliminations'])==55 and known==E
red_euler_dual=-1+12-66+172
assert red_euler_dual==117

def permutation_sign(values):
 inv=sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))
 return 1 if inv%2==0 else -1

def reduced_trace(permutation,faces):
 total=-1   # augmentation basis, degree -1
 for simplex in faces:
  before=bits(simplex)
  after=[IX[permutation[V[j][0]],permutation[V[j][1]]] for j in before]
  if set(before)==set(after):
   total+=(-1)**(len(before)-1)*permutation_sign(after)
 return total

def partition(g):
 visited=set(); cycles=[]
 for v in range(4):
  if v in visited:continue
  cur=v;length=0
  while cur not in visited:
   visited.add(cur);cur=g[cur];length+=1
  cycles.append(length)
 return tuple(sorted(cycles,reverse=True))

classes={(1,1,1,1):1,(2,1,1):6,(2,2):3,(3,1):8,(4,):6}
dual_chars={(1,1,1,1):117,(2,1,1):-7,(2,2):1,(3,1):3,(4,):-1}
orig_chars={(1,1,1,1):117,(2,1,1):7,(2,2):1,(3,1):3,(4,):1}
by_class=defaultdict(list)
for p in permutations(range(4)):
 # Verify action on graph (not merely an abstract permutation of labels)
 perm=[IX[p[i],p[j]] for i,j in V]
 assert all((b in adj[a])==(perm[b] in adj[perm[a]]) for a in range(12) for b in range(12))
 c=partition(p);by_class[c].append(p)
 sign_graph=permutation_sign(perm)
 assert sign_graph==(1 if c in ((1,1,1,1),(2,2),(3,1)) else -1)
 tD=reduced_trace(p,L)
 tK=reduced_trace(p,K)
 assert tD==dual_chars[c],(c,tD)
 assert tK==-orig_chars[c],(c,tK)  # only reduced H_7 of K, hence sign (-1)^7
 assert orig_chars[c]==sign_graph*dual_chars[c]
assert {c:len(ps) for c,ps in by_class.items()}==classes
character_table={
 'trivial':[1,1,1,1,1],
 'sign':[1,-1,1,1,-1],
 'standard':[3,1,-1,0,-1],
 'sign_standard':[3,-1,-1,0,1],
 'two_dim':[2,0,2,-1,0],
}
order=list(classes)
mult={rep:sum(classes[c]*orig_chars[c]*vals[i] for i,c in enumerate(order))//24 for rep,vals in character_table.items()}
assert mult=={'trivial':8,'sign':4,'standard':16,'sign_standard':13,'two_dim':9}
assert sum(mult[k]*character_table[k][0] for k in mult)==117
print('PASS: graph 12 vertices/18 edges, 48 connected and 447 disconnected induced quadruples')
print('PASS: K complete 6-skeleton, 447 facets; dual face vector (12,66,220,48)')
print('PASS: 48 audited elementary simplicial collapse pairs; dual residual (12,66,172)')
print('PASS: spanning tree 11 edges and 55 triangular pi_1 eliminations; dual simply connected')
print('PASS: reduced Euler characteristic dual = 117; wedge rank via standard topology')
print('PASS: all 24 signed traces; K top homology character',orig_chars)
print('PASS: S4 irrep multiplicities',mult)
