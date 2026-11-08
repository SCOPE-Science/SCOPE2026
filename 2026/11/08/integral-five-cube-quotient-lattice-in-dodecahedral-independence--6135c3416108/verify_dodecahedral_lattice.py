from functools import lru_cache
from itertools import permutations
from collections import Counter, defaultdict
import networkx as nx
import sympy as sp

N=20;G=nx.Graph();G.add_nodes_from(range(N))
for i in range(10):
 G.add_edge(i,(i+1)%10);G.add_edge(i,10+i);G.add_edge(10+i,10+(i+2)%10)
E={tuple(sorted(e)) for e in G.edges}; nei=[sum(1<<j for j in G[i]) for i in range(N)]
faces=[0]
for i in range(N):
 faces.extend([f|(1<<i) for f in faces if not nei[i]&f])
faces=set(faces)
ordered=sorted(faces,key=lambda b:(b.bit_count(),b))
matched={}
for i in range(N):
 for b in ordered:
  y=b|(1<<i)
  if b&(1<<i)==0 and b not in matched and y in faces and y not in matched:
   matched[b]=y; matched[y]=b
crit=sorted(set(faces)-set(matched))
assert len(crit)==4 and all(b.bit_count()==6 for b in crit)
# Exhaustively certify Forman acyclicity on the entire augmented Hasse graph.
full=nx.DiGraph();full.add_nodes_from(ordered)
for b in ordered:
 for j in range(N):
  if (b>>j)&1:
   t=b^(1<<j)
   if matched.get(t)==b:full.add_edge(t,b)
   else:full.add_edge(b,t)
assert full.number_of_edges()==27640
assert nx.is_directed_acyclic_graph(full)
# The nonaugmented version leaves {0} critical and gives the same topology.
unmatched_simple={b:m for b,m in matched.items() if b!=0 and m!=0}
nonempty=nx.DiGraph();nonempty.add_nodes_from(b for b in ordered if b)
for b in ordered:
 if not b:continue
 for j in range(N):
  if (b>>j)&1:
   t=b^(1<<j)
   if not t:continue
   if unmatched_simple.get(t)==b:nonempty.add_edge(t,b)
   else:nonempty.add_edge(b,t)
assert nx.is_directed_acyclic_graph(nonempty)
assert Counter(b.bit_count() for b in ordered if b and b not in unmatched_simple)==Counter({1:1,6:4})
print('FULL_ACYCLIC_MATCHING_PASS',len(ordered),full.number_of_edges(),len(matched)//2)
print('CRITICAL',crit)

def facet(bound):
 return [(bound^(1<<i), (-1)**((bound&((1<<i)-1)).bit_count())) for i in range(N) if bound>>i&1]

def coeff(sub,par):
 return next(c for b,c in facet(par) if b==sub)

# projection degree 5 from face chains to critical group
@lru_cache(maxsize=None)
def proj(b):
 if b in crit:
  return tuple(int(x==b) for x in crit)
 if b not in matched:raise ValueError
 p=matched[b]
 if p.bit_count()<b.bit_count():return (0,0,0,0)  # upper matched
 a=coeff(b,p)
 v=[0]*4
 for t,s in facet(p):
  if t!=b:
   q=proj(t)
   for i in range(4):v[i]-=a*s*q[i]
 return tuple(v)

f5=[x for x in ordered if x.bit_count()==6]
for b in f5:proj(b)
print('proj values',Counter(proj(b) for b in f5).most_common(8))

# gradient graph on size-5 matched lower -> other size-5 lower facets of pair
lower4=[b for b in ordered if b.bit_count()==5 and matched.get(b,0).bit_count()==6]
lowset=set(lower4); DG=nx.DiGraph();DG.add_nodes_from(lower4)
for b in lower4:
 for t,s in facet(matched[b]):
  if t!=b and t in lowset: DG.add_edge(b,t)
assert nx.is_directed_acyclic_graph(DG)
order=list(nx.topological_sort(DG))

# lift each critical 5-cell to a genuine integral cycle
def lifted(b):
 ch={b:1}; bd=defaultdict(int)
 for t,s in facet(b):bd[t]+=s
 for t in order:
  x=bd[t]
  if not x:continue
  upper=matched[t]; inc=coeff(t,upper)
  new=-inc*x
  ch[upper]=ch.get(upper,0)+new
  for subt,s in facet(upper):bd[subt]+=new*s
 assert all(v==0 for v in bd.values()), [(i,v) for i,v in bd.items() if v][:10]
 assert tuple(sum(co*proj(y)[j] for y,co in ch.items()) for j in range(4))==tuple(int(x==b) for x in crit)
 return {k:v for k,v in ch.items() if v}
reps=[lifted(b) for b in crit]
print('cycle sparsity',list(map(len,reps)), [max(map(abs,rep.values())) for rep in reps])

# validate all boundaries degree6 -> projection zero
for sigma in ordered:
 if sigma.bit_count()==7:
  assert all(sum(s*proj(t)[j] for t,s in facet(sigma))==0 for j in range(4))
print('projection-boundary-PASS')

perms=[tuple(m[i] for i in range(N)) for m in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
assert len(perms)==120
I=tuple(range(N));P=set(perms)

def compose(p,q):return tuple(p[q[i]] for i in range(N))
def inverse(p):
 x=[0]*N
 for i,j in enumerate(p):x[j]=i
 return tuple(x)

def onface(b,p):
 out=0; idx=[]
 for i in range(N):
  if b>>i&1:out|=1<<p[i];idx.append(p[i])
 # inversion parity
 sign=(-1)**sum(idx[i]>idx[j] for i in range(len(idx)) for j in range(i+1,len(idx)))
 return out,sign

def hommat(p):
 cols=[]
 for rep in reps:
  v=[0]*4
  for x,c in rep.items():
   y,s=onface(x,p);pr=proj(y)
   for i in range(4):v[i]+=c*s*pr[i]
  cols.append(v)
 return sp.Matrix.hstack(*(sp.Matrix(c) for c in cols))
mat={p:hommat(p) for p in perms}
print('matrices computed',len(mat))
assert mat[I]==sp.eye(4)
for p in perms:
 assert mat[p]*mat[inverse(p)]==sp.eye(4)
# entire group law potentially 14400 checks affordable
for a in perms:
 for b in perms:
  assert mat[compose(a,b)]==mat[a]*mat[b]
print('all-14400-representation-product-PASS')
# center
center=[p for p in perms if all(compose(p,q)==compose(q,p) for q in perms)]
assert len(center)==2
z=next(p for p in center if p!=I)
print('central matrix',mat[z], 'central fixedpoints',sum(z[i]==i for i in range(N)))
# derived subgroup via generating all commutators and closure
comm=set()
for a in perms:
 for b in perms:
  comm.add(compose(compose(a,b),compose(inverse(a),inverse(b))))
H={I}; delta=True
while delta:
 t=H|{compose(a,b) for a in H for b in comm}
 delta=len(t)>len(H);H=t
print('derived subgroup',len(H))
assert len(H)==60 and z not in H and len(H|{compose(z,h) for h in H})==120

def cyc(p):
 seen=set();rs=[]
 for i in range(N):
  if i not in seen:
   j=i;cur=[]
   while j not in seen:
    seen.add(j);cur.append(j);j=p[j]
   rs.append(len(cur))
 return tuple(sorted(rs))
print('ROTATION_CLASSES:')
print(Counter((cyc(p),sp.trace(mat[p])) for p in H))
print('INVERSION_CLASSES:')
print(Counter((cyc(p),sp.trace(mat[p])) for p in P-H))
print('invariants full',sum(sp.trace(mat[p]) for p in perms)/120)
print('invariants rotational',sum(sp.trace(mat[p]) for p in H)/60)
# Distinguish integral 4-lattice from A4 root/weight lattices using dimensions of fixed over mod prime
for prime in [2,3,5]:
 span=sp.zeros(4,0)
 # coinvariant module rank over Fp for selected generators
 # find few generators of group with lower computational cost
 gens=[];closure={I}
 for p in H:
  if p in closure:continue
  gens.append(p)
  c=set(closure)
  while True:
   n=c|{compose(x,y) for x in c for y in [p,inverse(p)]}
   if n==c:break
   c=n
  closure=c
  if len(closure)==60:break
 print('H generators',len(gens),'mod',prime)
 for p in gens:span=span.row_join(mat[p]-sp.eye(4))
 # modular rank
 def modrank(m,p):
  a=[[int(x)%p for x in row] for row in m.tolist()];r=0
  for j in range(m.cols):
   k=next((k for k in range(r,m.rows) if a[k][j]),None)
   if k is None:continue
   a[r],a[k]=a[k],a[r];v=pow(a[r][j],-1,p)
   a[r]=[(x*v)%p for x in a[r]]
   for k in range(m.rows):
    if k!=r:
     d=a[k][j];a[k]=[(a[k][col]-d*a[r][col])%p for col in range(m.cols)]
   r+=1
   if r==m.rows:break
  return r
 print('coinvariant dim',4-modrank(span,prime))
print('DODECAHEDRAL_ACTION_ALL_PASS')
from itertools import combinations
max8=sorted(b for b in faces if b.bit_count()==8)
assert len(max8)==5
print('cube-index-facets',max8)
for p in perms:
 assert all(onface(b,p)[0] in max8 for b in max8)
print('central-five-set',[max8.index(onface(b,z)[0]) for b in max8])
K=[p for p in H if onface(max8[0],p)[0]==max8[0]]
print('stabilizer',len(K))
A=sp.Matrix.vstack(*(mat[p]-sp.eye(4) for p in K))
ker=A.nullspace();print('kernel stabilizer dim',len(ker),ker)
assert len(ker)==1
v=ker[0];v=v*sp.ilcm(*[x.q for x in v]);g=sp.igcd(*[int(x) for x in v]);v=v/g
orbit=[]
for b in max8:
 p=next(p for p in H if onface(max8[0],p)[0]==b)
 orbit.append(mat[p]*v)
B=sp.Matrix.hstack(*orbit)
print('orbit matrix',B,'sum',B*sp.ones(5,1))
print('index',sp.igcd(*(int(B[:,list(cols)].det()) for cols in combinations(range(5),4))))
print('A5_orbit_primitive',v)
# Independent Lefschetz verification on all simplex chains.
for p in perms:
 trace=sum((-1)**b.bit_count()*onface(b,p)[1] for b in faces if onface(b,p)[0]==b)
 assert trace==sp.trace(mat[p]),(trace,sp.trace(mat[p]))
print('SIGNED_LEFSCHETZ_120_AUTOMORPHISMS_PASS')

# Integral distinction: augmentation sublattice versus quotient lattice
# of the 5-object permutation module, even though they agree over Q.
P5={p:tuple(max8.index(onface(x,p)[0]) for x in max8) for p in H}
assert len(set(P5.values()))==60 and all(sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))%2==0 for a in P5.values())
root=[];quot=[]
for p,a in P5.items():
 Q=sp.zeros(4,4);R=sp.zeros(4,4)
 for i in range(4):
  x=a[i];y=a[4]
  if x<4: Q[x,i]+=1
  else:Q[:,i]-=sp.ones(4,1)
  if x<4:R[x,i]+=1
  if y<4:R[y,i]-=1
 quot.append(Q);root.append(R)
for prime in [5]:
 def modular_rank(M,p):
  a=[[int(x)%p for x in row] for row in M.tolist()];rank=0
  for c in range(M.cols):
   pivot=next((i for i in range(rank,M.rows) if a[i][c]),None)
   if pivot is None:continue
   a[rank],a[pivot]=a[pivot],a[rank]
   v=pow(a[rank][c],-1,p);a[rank]=[(x*v)%p for x in a[rank]]
   for i in range(M.rows):
    if i!=rank:
     z=a[i][c];a[i]=[(a[i][k]-z*a[rank][k])%p for k in range(M.cols)]
   rank+=1
   if rank==M.rows:break
  return rank
 def coinv_dim(arr):return 4-modular_rank(sp.Matrix.hstack(*[M-sp.eye(4) for M in arr]),5)
 assert coinv_dim(quot)==coinv_dim([mat[p] for p in H])==1
 assert coinv_dim(root)==0
print('INTEGRAL_QUOTIENT_VERSUS_AUGMENTATION_MOD5_PASS')
