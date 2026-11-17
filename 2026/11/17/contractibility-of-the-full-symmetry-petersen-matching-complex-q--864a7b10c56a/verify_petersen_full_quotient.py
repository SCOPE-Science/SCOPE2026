"""Exact finite certificate for the full-symmetry Petersen matching quotient.
Uses only the Python standard library; no precomputed data is loaded.
"""
from itertools import permutations, combinations
from collections import Counter, defaultdict

# The Kneser model has a graph vertex for each two-subset of five symbols.
V=list(combinations(range(5),2))
E=[e for e in combinations(range(10),2) if not set(V[e[0]])&set(V[e[1]])]
assert (len(V),len(E))==(10,15)
F=[]
for r in range(1,6):
    for f in combinations(range(15),r):
        endpoints=[v for t in f for v in E[t]]
        if len(set(endpoints))==2*r:
            F.append(f)
fd={f:i for i,f in enumerate(F)}
assert [sum(len(f)==r for f in F) for r in range(1,6)]==[15,75,145,90,6]

# A presentation of pi_1 of |M(P)|: edge generators off a spanning tree,
# with a three-edge boundary relation for each matching triple.
edges=sorted(f for f in F if len(f)==2)
triangles=[f for f in F if len(f)==3]
eidx={e:i for i,e in enumerate(edges)}
rels=[tuple(eidx[e] for e in combinations(t,2)) for t in triangles]
selected_tree=[72,52,29,11,47,63,37,1,69,66,32,73,14,36]
parent=list(range(15))
def root(x):
    while parent[x]!=x:x=parent[x]
    return x
for t in selected_tree:
    a,b=edges[t];u,v=root(a),root(b)
    assert u!=v
    parent[u]=v
assert len({root(i) for i in range(15)})==1
known=set(selected_tree); rounds=[]
while True:
    newly=set()
    for rel in rels:
        rest=[e for e in rel if e not in known]
        if len(rest)==1:newly.add(rest[0])
    newly-=known
    if not newly:break
    known.update(newly);rounds.append(len(newly))
assert len(known)==75

# Generate all 120 automorphisms on the Petersen matching complex.
transforms=[]
for g in permutations(range(5)):
    pv=tuple(V.index(tuple(sorted(g[j] for j in x))) for x in V)
    pe=tuple(E.index(tuple(sorted((pv[a],pv[b])))) for a,b in E)
    transforms.append(tuple(fd[tuple(sorted(pe[e] for e in f))] for f in F))
assert len(set(transforms))==120
# Transposition 0<->1 fixes a Petersen edge (a vertex in the complex).
g=(1,0,2,3,4)
pv=tuple(V.index(tuple(sorted(g[j] for j in x))) for x in V)
pe=tuple(E.index(tuple(sorted((pv[a],pv[b])))) for a,b in E)
assert any(pe[i]==i for i in range(15))

# The barycentric subdivided quotient has one oriented cell for each
# S5-orbit of strict inclusion chains of nonempty matching faces.
chains=[{} for d in range(5)]
number_candidates=0
for top in F:
    sub=[[fd[f] for f in combinations(top,k)] for k in range(1,len(top)+1)]
    def extend(chain):
        global number_candidates
        if chain:
            key=min(tuple(t[i] for i in chain) for t in transforms)
            orbits=chains[len(chain)-1]
            if key not in orbits:orbits[key]=len(orbits)
            number_candidates+=1
        start=1 if not chain else len(F[chain[-1]])+1
        for length in range(start,len(top)+1):
            for j in sub[length-1]:
                if not chain or set(F[chain[-1]]).issubset(F[j]):
                    extend(chain+(j,))
    extend(())
fvec=[len(a) for a in chains]
print("NEW_FVEC",fvec,flush=True)
# Independent Burnside cross-check: for each group element count strict chains
# pointwise fixed in the face poset by dynamic programming, not orbit keys.
subfaces=[]
for f in F:
    subfaces.append([fd[h] for r in range(1,len(f)) for h in combinations(f,r)])
burnside=[0]*5
for trans in transforms:
    fixed=[i==j for i,j in enumerate(trans)]
    dp=[1 if fixed[i] else 0 for i in range(len(F))]
    burnside[0]+=sum(dp)
    for d in range(1,5):
        dp=[sum(dp[j] for j in subfaces[i]) if fixed[i] else 0
            for i in range(len(F))]
        burnside[d]+=sum(dp)
assert all(n%120==0 for n in burnside)
print("BURNSIDE",[n//120 for n in burnside],flush=True)
assert [n//120 for n in burnside]==fvec
assert sum((-1)**d*n for d,n in enumerate(fvec))==1

# A quotient simplex has ordered barycentres of strictly increasing ranks;
# hence stabilizers cannot invert it. Incidence numbers are signed deletions.
mat={}
for d in range(1,5):
    cols={}
    for chain,j in chains[d].items():
        out=defaultdict(int)
        for q in range(d+1):
            face=chain[:q]+chain[q+1:]
            key=min(tuple(t[i] for i in face) for t in transforms)
            out[chains[d-1][key]]+=(-1)**q
        cols[j]={i:v for i,v in out.items() if v}
    mat[d]=cols

def check_d2():
    for d in range(1,4):
        for col in mat[d+1].values():
            comp=defaultdict(int)
            for mid,u in col.items():
                for row,v in mat[d][mid].items():comp[row]+=u*v
            assert all(v==0 for v in comp.values())
check_d2()

# Integral chain contraction through unit boundary pivots (Schur complements).
# A unit pivot gives an isomorphism between two rank-one summands and may
# be cancelled exactly, deleting the corresponding adjacent rows/columns.
row_active={k:set(range(fvec[k-1])) for k in range(1,5)}
col_active={k:set(range(fvec[k])) for k in range(1,5)}
pivot_counts=Counter()
while True:
    moved=False
    for k in range(4,0,-1):
        rowcols=defaultdict(set)
        for j,col in mat[k].items():
            for i in col:rowcols[i].add(j)
        units=[]
        for j,col in mat[k].items():
            for i,a in col.items():
                if abs(a)==1:
                    units.append(((len(col)-1)*(len(rowcols[i])-1),
                                  len(col)+len(rowcols[i]),i,j,a))
        if not units:continue
        _,_,i,j,a=min(units)
        B=mat[k][j]
        for other in list(rowcols[i]):
            if other==j:continue
            C=mat[k][other]
            mult=C[i]//a
            for row,v in B.items():
                z=C.get(row,0)-mult*v
                if z:C[row]=z
                else:C.pop(row,None)
            assert i not in C
        del mat[k][j]
        if k>1:del mat[k-1][i]
        if k<4:
            for C in mat[k+1].values():C.pop(j,None)
        row_active[k].remove(i);col_active[k].remove(j)
        if k>1:col_active[k-1].remove(i)
        if k<4:row_active[k+1].remove(j)
        pivot_counts[k]+=1;moved=True
    if not moved:break
check_d2()
assert [len(col_active[k]) for k in range(1,5)]==[0,0,0,0]
assert len(row_active[1])==1
print("NEW_PIVOTS",sum(pivot_counts.values()),[pivot_counts[k] for k in range(1,5)],flush=True)
assert sum(pivot_counts.values())==(sum(fvec)-1)//2
assert all(not col for d in mat.values() for col in d.values())
print('PETERSEN_MATCHING_QUOTIENT_VERIFIED')
print('Petersen graph: 10 vertices, 15 edges')
print('matching face vector: 15 75 145 90 6')
print('original simple connectivity: spanning tree has 14 edges; all 75 one-skeleton edges trivial')
print('presentation propagation rounds:',rounds)
print('group elements: 120; fixed transposition: yes')
print('independent Burnside orbit-chain counts: match')
print('barycentric quotient cell vector:',*fvec)
print('chain candidate visits (with repetitions):',number_candidates)
print('integral unit cancellations by boundary degree:',*[pivot_counts[k] for k in range(1,5)])
print('total unit cancellations: 62; residual chain complex: one C0, zero elsewhere')
print('integral positive reduced homology: zero; quotient pi1: trivial by Armstrong')
