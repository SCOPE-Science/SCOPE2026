#!/usr/bin/env python3
"""Exact finite checks for the dihedral quotient of the 3 by 3 grid matching complex."""
from collections import Counter, defaultdict, deque

N=3
VERTICES=[(i,j) for i in range(N) for j in range(N)]
EDGES=[(a,b) for a in range(9) for b in range(a+1,9)
       if abs(VERTICES[a][0]-VERTICES[b][0])+abs(VERTICES[a][1]-VERTICES[b][1])==1]
assert len(EDGES)==12

def is_matching(mask):
    used=set()
    for e,(a,b) in enumerate(EDGES):
        if mask>>e&1:
            if a in used or b in used:return False
            used.update((a,b))
    return True

F=sorted(mask for mask in range(1,1<<12) if is_matching(mask))
assert Counter(x.bit_count()-1 for x in F)=={0:12,1:44,2:56,3:18}
S=set(F)
ORDER=[0,9,3,5,2,7,4,10,8,1,6,11]
active=set(F);pairs=[]
for v in ORDER:
    b=1<<v
    for x in sorted(active):
        if x&b or x|b not in active:continue
        active.remove(x);active.remove(x|b);pairs.append((x,x|b))
assert len(pairs)==62 and Counter(x.bit_count()-1 for x in active)=={0:1,2:5}

# Full Forman reversed-incidence graph, not merely the matching count.
matched=set(pairs); adj=defaultdict(list);indeg={x:0 for x in F};incidences=0
for x in F:
    for v in range(12):
        if x>>v&1:
            y=x^(1<<v)
            if not y:continue
            incidences+=1
            a,b=(y,x) if (y,x) in matched else (x,y)
            adj[a].append(b);indeg[b]+=1
q=deque(x for x in F if indeg[x]==0);reached=0
while q:
    x=q.popleft();reached+=1
    for y in adj[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert reached==len(F)

# Dihedral maps on grid vertices and therefore on matching vertices.
def vertex_map(i,j,name):
    return {'id':(i,j),'rot90':(j,2-i),'rot180':(2-i,2-j),'rot270':(2-j,i),
            'vertical':(2-i,j),'horizontal':(i,2-j),'diagonal':(j,i),
            'antidiagonal':(2-j,2-i)}[name]
NAMES=('id','rot90','rot180','rot270','vertical','horizontal','diagonal','antidiagonal')
perms=[]
for name in NAMES:
    im=[]
    for a,b in EDGES:
        aa=VERTICES.index(vertex_map(*VERTICES[a],name))
        bb=VERTICES.index(vertex_map(*VERTICES[b],name))
        im.append(EDGES.index(tuple(sorted((aa,bb)))))
    assert sorted(im)==list(range(12))
    perms.append(im)
assert len({tuple(x) for x in perms})==8

def act(mask,p):return sum(1<<p[e] for e in range(12) if mask>>e&1)
for p in perms:
    assert {act(f,p) for f in F}==S

def permutation_sign(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

character=[]
for p in perms:
    l=-1 # empty simplex augmentation for the reduced Lefschetz number
    for f in F:
        if act(f,p)!=f:continue
        support=[e for e in range(12) if f>>e&1]
        images=[p[e] for e in support]
        sign=permutation_sign(images)
        l+=(-1)**(len(support)-1)*sign
    character.append(l)
assert character==[5,1,1,1,-1,-1,1,1]
assert sum(character)==8 # invariant H2 rank 1

# A transposition across the diagonal fixes a two-edge matching;
# a vertical reflection fixes an individual central-row edge.
def fixed_nonempty(p):return any(act(f,p)==f for f in F)
assert fixed_nonempty(perms[4]) and fixed_nonempty(perms[6])

# The quotient of the barycentric subdivision: vertices are nonempty
# matchings, simplices are strict inclusion chains, orbit representatives
# are taken under the full D4 action (which is without inversions).
F_index={f:i for i,f in enumerate(F)}
trans=[[F_index[act(f,p)] for f in F] for p in perms]
def orbit(c):return min(tuple(t[j] for j in c) for t in trans)
chains=[(i,) for i in range(len(F))]
orbit_index=[]
for k in range(4):
    reps={}
    for c in chains:
        r=orbit(c)
        if r not in reps:reps[r]=len(reps)
    orbit_index.append(reps)
    if k==3:break
    supers={i:[j for j,g in enumerate(F) if f!=g and f&g==f] for i,f in enumerate(F)}
    chains=[c+(j,) for c in chains for j in supers[c[-1]]]
counts=[len(reps) for reps in orbit_index]
assert counts==[20,87,123,54]

Ds=[]
for k in range(1,4):
    D=[{} for _ in range(counts[k])]
    for c,j in orbit_index[k].items():
        for h in range(k+1):
            row=orbit_index[k-1][orbit(c[:h]+c[h+1:])]
            D[j][row]=D[j].get(row,0)+(-1)**h
        D[j]={r:a for r,a in D[j].items() if a}
    Ds.append(D)
for k in range(2,4):
    for c in Ds[k-1]:
        d=defaultdict(int)
        for j,a in c.items():
            for i,b in Ds[k-2][j].items():d[i]+=a*b
        assert all(t==0 for t in d.values())

def mod_rank(cols,rows,prime):
    piv={}
    for c in cols:
        vec={i:(v%prime) for i,v in c.items() if v%prime}
        while vec:
            i=min(vec)
            if i not in piv:
                t=pow(vec[i],-1,prime)
                piv[i]={k:(v*t)%prime for k,v in vec.items() if v%prime}
                break
            t=vec[i]
            vec={k:(vec.get(k,0)-t*piv[i].get(k,0))%prime
                 for k in set(vec)|set(piv[i])}
            vec={k:v for k,v in vec.items() if v}
    return len(piv)

ranks=[mod_rank(Ds[k],counts[k],2) for k in range(3)]
assert ranks==[19,68,54]
betti=[counts[i]-(ranks[i-1] if i else 0)-(ranks[i] if i<3 else 0)
       for i in range(4)]
assert betti==[1,0,1,0]
print('CHECK_OK graph_edges=12 faces=130 morse_pairs=62 critical_0=1 critical_2=5')
print('CHECK_OK reversed_incidence_acyclic=1 incidences=%d'%incidences)
print('CHECK_OK dihedral_reduced_lefschetz='+','.join(map(str,character))+' invariant_rank=1')
print('CHECK_OK quotient_barycentric_cell_counts='+','.join(map(str,counts)))
print('CHECK_OK quotient_boundary_squared_zero=1 mod2_ranks='+','.join(map(str,ranks)))
print('CHECK_OK quotient_mod2_betti='+','.join(map(str,betti)))
print('ALL_VERIFY_OK')
