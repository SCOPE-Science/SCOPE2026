from itertools import combinations, product
from collections import Counter,deque,defaultdict
import networkx as nx
from fractions import Fraction as Q
v=[]
for i,j in combinations(range(4),2):
 for a,b in product((-1,1),repeat=2):
  w=[0]*4;w[i]=a;w[j]=b;v.append(tuple(w))
index={x:i for i,x in enumerate(v)}
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
G=nx.Graph();G.add_nodes_from(range(24));G.add_edges_from((i,j) for i,j in combinations(range(24),2) if dot(v[i],v[j])==1)
d=dict(nx.all_pairs_shortest_path_length(G))
assert Counter(d[i][j] for i,j in combinations(range(24),2))=={1:96,2:168,3:12}
assert all((d[i][j]==3)==(tuple(-x for x in v[i])==v[j]) for i,j in combinations(range(24),2))
triangles={frozenset(t) for t in combinations(range(24),3) if all(G.has_edge(i,j) for i,j in combinations(t,2))};assert len(triangles)==96
assert nx.graph_clique_number(G)==3 if hasattr(nx,"graph_clique_number") else max(map(len,nx.find_cliques(G)))==3
normals=[]
for i in range(4):
 for s in (-1,1):
  w=[Q(0)]*4;w[i]=Q(s);normals.append(tuple(w))
for s in product((-1,1),repeat=4):normals.append(tuple(Q(z,2) for z in s))
facets=[frozenset(i for i,x in enumerate(v) if dot(x,n)==1) for n in normals]
assert len(facets)==len(set(facets))==24 and all(len(F)==6 for F in facets)
assert all(sum(t<=F for F in facets)==2 for t in triangles)
assert all(sum(G.has_edge(i,j) for i,j in combinations(F,2))==12 for F in facets)
assert {t for F in facets for t in combinations(sorted(F),3) if all(G.has_edge(i,j) for i,j in combinations(t,2))}=={tuple(sorted(t)) for t in triangles}
# An independent exact mod-two calculation for the scale-one simplicial boundary.
edges=list(sorted(tuple(sorted(e)) for e in G.edges()))
edge_idx={e:i for i,e in enumerate(edges)}
pivots={}
for t in sorted((tuple(sorted(t)) for t in triangles)):
    col=0
    for e in combinations(t,2): col ^= 1<<edge_idx[tuple(sorted(e))]
    while col:
        h=col.bit_length()-1
        if h in pivots: col^=pivots[h]
        else: pivots[h]=col;break
assert len(pivots)==73
print('vertices,edges,triangles,facets:',len(v),G.number_of_edges(),len(triangles),len(facets))
print('mod-two triangle-boundary rank:',len(pivots))
# F4 simple-root reflections
alphas=[(0,1,-1,0),(0,0,1,-1),(0,0,0,1),(Q(1,2),Q(-1,2),Q(-1,2),Q(-1,2))]
gens=[]
for alpha in alphas:
 n=dot(alpha,alpha)
 w=[tuple(Q(y)-2*dot(x,alpha)/n*Q(z) for y,z in zip(x,alpha)) for x in v]
 assert all(x in index for x in w)
 gens.append(tuple(index[x] for x in w))
ident=tuple(range(24));grp={ident};front=deque([ident])
while front:
 p=front.popleft()
 for h in gens:
  new=tuple(h[p[i]] for i in range(24))
  if new not in grp:
   grp.add(new);front.append(new)
assert len(grp)==1152
print('full F4 generated order:',len(grp))
# Independent graph-automorphism enumeration
count=0
for auto in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter():
 count+=1
 assert tuple(auto[i] for i in range(24)) in grp
assert count==len(grp)
print('independent graph automorphism count:',count)
fs_index={F:i for i,F in enumerate(facets)}
pairs=sorted({tuple(sorted((i,index[tuple(-a for a in v[i])]))) for i in range(24)})
assert len(pairs)==12
pair_lookup={i:k for k,pair in enumerate(pairs) for i in pair}
sign=lambda p:(-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
# ambient determinant sign on a matrix acting on the four linearly independent long roots
bases=[0,1,4,8]
import sympy as sp
B=sp.Matrix([v[i] for i in bases]).T
assert B.det()!=0
char_records=[]
for p in grp:
 A=sp.Matrix([v[p[i]] for i in bases]).T*B.inv()
 eps=int(A.det());assert eps in (-1,1)
 assert all(tuple(A*sp.Matrix(x))==v[p[i]] for i,x in enumerate(v))
 facetperm=[fs_index[frozenset(p[i] for i in F)] for F in facets]
 fixed_facets=sum(facetperm[i]==i for i in range(24))
 pairperm=[pair_lookup[p[u]] for u,_ in pairs]
 assert len(set(pairperm))==12
 flips=sum(p[u] != pairs[pairperm[k]][0] for k,(u,z) in enumerate(pairs))
 eps11=sign(pairperm)*(-1)**flips
 char_records.append((eps, eps*(fixed_facets-1),eps11))
assert Counter(t[1] for t in char_records)==Counter({-11:12,-5:12,-1:597,1:444,3:54,5:32,23:1})
assert Counter(t[2] for t in char_records)==Counter({-1:576,1:576})
assert all(t[0]==t[2] for t in char_records)
assert sum(t[1] for t in char_records)==sum(t[2] for t in char_records)==0
print('H2 character distribution:', sorted(Counter(t[1] for t in char_records).items()))
print('H11 character distribution:', sorted(Counter(t[2] for t in char_records).items()))
print('invariant multiplicities H2, H11:',sum(t[1] for t in char_records)//len(grp),sum(t[2] for t in char_records)//len(grp))
print('generator (det,H2,H11):',[next(t for p,t in zip(grp,char_records) if p==g) for g in gens])
print('TWENTYFOUR_CELL_EQUIVARIANT_RIPS_PASS')
