"""Exact integral three-torus span verification for the truncated-cube graph.

Standard library only; all orientations and cells are defined by this file.
The companion verify_boundary.cpp checks the full weight-three differential.
"""
from collections import Counter
from itertools import combinations, product

EDGES = [
 (0,1),(0,2),(0,4),(1,11),(1,14),(2,3),(2,4),(3,6),(3,8),
 (4,5),(5,16),(5,18),(6,7),(6,8),(7,10),(7,12),(8,9),
 (9,17),(9,20),(10,11),(10,12),(11,14),(12,13),(13,21),
 (13,22),(14,15),(15,19),(15,23),(16,17),(16,18),(17,20),
 (18,19),(19,23),(20,21),(21,22),(22,23)
]
N=24
E={edge:i for i,edge in enumerate(EDGES)}
ADJ={v:set() for v in range(N)}
INC={v:[] for v in range(N)}
for i,(u,v) in enumerate(EDGES):
    ADJ[u].add(v);ADJ[v].add(u)
    INC[u].append(i);INC[v].append(i)
for v in INC: INC[v].sort()
assert len(EDGES)==36 and all(len(INC[v])==3 for v in range(N))

# Enumerate once by the minimum vertex and a choice of traversal direction.
# In any disjoint triple, every cycle has length <=24-3-3=18.
CYC=[]
def dfs(start,path):
    u=path[-1]
    if len(path)>=3 and start in ADJ[u] and path[1]<u:
        CYC.append(tuple(path))
    if len(path)==18: return
    for w in sorted(ADJ[u]):
        if w>start and w not in path:dfs(start,path+[w])
for start in range(N):
    for w in sorted(ADJ[start]):
        if w>start:dfs(start,[start,w])
assert len(CYC)==1350,Counter(map(len,CYC))=={
  3:8,8:6,9:24,10:36,11:24,12:22,
  13:96,14:240,15:320,16:246,17:144,18:184}
MASK=[sum(1<<v for v in c) for c in CYC]
TRI=[i for i,c in enumerate(CYC) if len(c)==3]
assert len(TRI)==8 and all(MASK[i]&MASK[j]==0 for i,j in combinations(TRI,2))

# Identify the graph as the vertex-truncation of the cube.
# Each triangle is a vertex of the quotient; edges joining triangles form a cube.
which={v:k for k,i in enumerate(TRI) for v in CYC[i]}
assert len(which)==24
outer={tuple(sorted((which[u],which[v]))) for u,v in EDGES if which[u]!=which[v]}
assert len(outer)==12
qadj={v:set() for v in range(8)}
for u,v in outer:qadj[u].add(v);qadj[v].add(u)
assert all(len(qadj[v])==3 for v in qadj)
# The cube is exactly the connected eight-vertex graph with distance
# distribution (1,3,3,1) from each vertex and with six square faces.
def distance_profile(root):
    seen={root}; layer={root};count=[1]
    while layer:
        nxt=set().union(*(qadj[v] for v in layer))-seen
        if not nxt: break
        count.append(len(nxt));seen|=nxt;layer=nxt
    return count
assert all(distance_profile(v)==[1,3,3,1] for v in range(8))
q4=set()
for a in range(8):
 for b in qadj[a]:
  for c in qadj[b]-{a}:
   for d in qadj[c]-{b}:
    if a in qadj[d] and len({a,b,c,d})==4:
     q4.add(frozenset((a,b,c,d)))
assert len(q4)==6

# Every triple has two triangles: a separate exhaustive check that no two
# vertex-disjoint nontriangular cycles leave any third cycle disjoint.
LONG=[i for i in range(len(CYC)) if i not in TRI]
for i,j in combinations(LONG,2):
    occupied=MASK[i]|MASK[j]
    if MASK[i]&MASK[j]:continue
    if any(not (occupied & x) for x in MASK):
        raise AssertionError('three disjoint cycles without two triangles')

TRIPLES=set()
for i,j in combinations(TRI,2):
    m=MASK[i]|MASK[j]
    for k in range(len(CYC)):
        if k not in (i,j) and m&MASK[k]==0:
            TRIPLES.add(tuple(sorted((i,j,k))))
assert len(TRIPLES)==1656

# One degree-one generator at each vertex, labelled 1 or 2 in the
# difference-of-half-edges basis relative to incident edge 0.
# The degree-three basis is (u,v,w,a,b,c), u<v<w, labels in {1,2}.
ROW={(u,v,w,a,b,c):r for r,(u,v,w,a,b,c) in enumerate(
 (u,v,w,a,b,c) for u in range(N) for v in range(u+1,N)
 for w in range(v+1,N) for a,b,c in product((1,2),repeat=3))}
assert len(ROW)==16192

def edge_id(v,w):return E[tuple(sorted((v,w)))]

def loop_local_terms(c):
    result={}
    for j,v in enumerate(c):
        before=edge_id(v,c[j-1]);after=edge_id(v,c[(j+1)%len(c)])
        local={}
        for e,sig in ((after,1),(before,-1)):
            loc=INC[v].index(e)
            if loc:local[loc]=local.get(loc,0)+sig
        result[v]={label:coef for label,coef in local.items() if coef}
    return result
LOOP=[loop_local_terms(c) for c in CYC]

def torus_column(indices):
    i,j,k=indices
    ans={}
    for vi,ti in LOOP[i].items():
     for vj,tj in LOOP[j].items():
      for vk,tk in LOOP[k].items():
       vertices=(vi,vj,vk)
       u,v,w=sorted(vertices)
       inv=sum(vertices[p]>vertices[q] for p in range(3) for q in range(p+1,3))
       orient=(-1)**inv
       for a,sa in ti.items():
        for b,sb in tj.items():
         for c,sc in tk.items():
          labels={vi:a,vj:b,vk:c}
          r=ROW[u,v,w,labels[u],labels[v],labels[w]]
          ans[r]=ans.get(r,0)+orient*sa*sb*sc
    return {a:b for a,b in ans.items() if b}

# Integral column elimination: each new pivot is +1/-1, so selected columns
# have a signed unimodular maximal minor. No modular rank inference is used.
def accept_unit_column(column,pivots):
    v=column.copy()
    while v:
        r=max(v); a=v[r]
        if r not in pivots:
            if abs(a)!=1:raise AssertionError(('nonunit torus pivot',r,a))
            if a==-1:v={k:-x for k,x in v.items()}
            pivots[r]=v
            return True,r
        for k,x in pivots[r].items():
            y=v.get(k,0)-a*x
            if y:v[k]=y
            else:v.pop(k,None)
    return False,None

pivots={};SELECTED=[];RANK={};counts=Counter()
by_length=sorted(TRIPLES,key=lambda t:
 (max(map(lambda i:len(CYC[i]),t)),sum(len(CYC[i]) for i in t),
  tuple(sorted(len(CYC[i]) for i in t)),t))
for t in by_length:
    d=max(len(CYC[i]) for i in t)
    counts[d]+=1
    added,pivot=accept_unit_column(torus_column(t),pivots)
    if added: SELECTED.append((t,pivot,d))
    RANK[d]=len(pivots)
assert counts=={3:56,8:36,9:144,10:216,11:144,12:52,
                13:96,14:240,15:320,16:240,17:96,18:16}
assert len(pivots)==96 and [RANK[x] for x in sorted(RANK)]==[
    56,92,92,92,92,96,96,96,96,96,96,96]
assert Counter(d for _,_,d in SELECTED)=={3:56,8:36,12:4}
print('TORUS_INTEGER_UNIT_BASIS_OK')
print('cycles',len(CYC),'disjoint_triples',len(TRIPLES),
      'basis',len(SELECTED),'short_max11_rank',RANK[11])
for t,pivot,d in SELECTED:
    if d==12:print('essential_12_torus', [list(CYC[i]) for i in t], 'pivot',pivot)
