#!/usr/bin/env python3
"""Exact finite certificates for the Herschel-graph shortest-path Rips filtration.

Only the Python standard library is required. All simplices and cover incidences
are rebuilt from the displayed 18-edge graph, rather than from stored ranks.
"""
from collections import Counter, deque
from itertools import combinations, permutations

N=11
EDGES=[(0,5),(0,6),(0,9),(0,10),
       (1,5),(1,6),(1,7),(1,8),
       (2,7),(2,8),(2,9),(2,10),
       (3,5),(3,7),(3,9),
       (4,6),(4,8),(4,10)]
ADJ=[set() for _ in range(N)]
for i,j in EDGES:
    assert i!=j and j not in ADJ[i]
    ADJ[i].add(j);ADJ[j].add(i)
assert len(EDGES)==18
assert sorted(map(len,ADJ))==[3]*8+[4]*3

def shortest_paths():
    d=[]
    for i in range(N):
        dist=[100]*N;dist[i]=0;q=deque([i])
        while q:
            v=q.popleft()
            for w in ADJ[v]:
                if dist[w]>dist[v]+1:
                    dist[w]=dist[v]+1;q.append(w)
        d.append(dist)
    return d
D=shortest_paths()
assert max(max(row) for row in D)==4
# Cross-check all shortest distances by an independent Floyd-Warshall algorithm.
F=[[0 if i==j else (1 if j in ADJ[i] else 100) for j in range(N)] for i in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            F[i][j]=min(F[i][j],F[i][k]+F[k][j])
assert D==F

# Enumerate all 2^11-1 nonempty subsets. Maximal clique size is not assumed.
def allowed(mask,r):
    verts=[v for v in range(N) if mask & (1<<v)]
    return all(D[i][j]<=r for i,j in combinations(verts,2))
FACES={r:{mask for mask in range(1,1<<N) if allowed(mask,r)} for r in range(5)}
assert all(FACES[r]<=FACES[r+1] for r in range(4))
assert [len(FACES[r]) for r in range(5)]==[11,29,178,1535,2047]
assert [tuple(Counter(mask.bit_count()-1 for mask in FACES[r]).get(i,0)
              for i in range(6)) for r in (1,2)]==[(11,18,0,0,0,0),(11,42,69,46,9,1)]

def boundaries_mod2(faces):
    bydim={d:sorted(f for f in faces if f.bit_count()-1==d)
           for d in range(max(f.bit_count() for f in faces))}
    ranks={}
    for d in sorted(bydim):
        if d==0:
            ranks[d]=0;continue
        idx={f:i for i,f in enumerate(bydim[d-1])}
        basis={}
        for tau in bydim[d]:
            col=0
            for v in range(N):
                if tau & (1<<v):col^=1<<idx[tau^(1<<v)]
            while col:
                lead=col.bit_length()-1
                if lead in basis:col^=basis[lead]
                else:basis[lead]=col;break
        ranks[d]=len(basis)
    betti={d:len(b)-ranks[d]-ranks.get(d+1,0) for d,b in bydim.items()}
    betti[0]-=1
    return {d:b for d,b in betti.items() if b}
assert boundaries_mod2(FACES[2])=={3:1}
assert boundaries_mod2(FACES[3])=={}

# Ordered toggles supply an explicit perfect discrete-Morse matching at scale 2.
PIVOTS=[9,4,0,10,3,7,2,1,8,5,6]
remaining=set(FACES[2]);pairs=[]
for vertex in PIVOTS:
    for low in sorted(remaining):
        high=low | (1<<vertex)
        if not low & (1<<vertex) and high in remaining:
            assert high.bit_count()==low.bit_count()+1
            remaining.remove(low);remaining.remove(high);pairs.append((low,high))
assert len(pairs)==88
assert Counter(x.bit_count()-1 for x in remaining)==Counter({0:1,3:1})

# Verify every directed cover incidence, not just the toggle rule.
paired=set(pairs)
out={f:[] for f in FACES[2]};indeg={f:0 for f in FACES[2]}
cover=0
for high in FACES[2]:
    for v in range(N):
        if high & (1<<v):
            low=high^(1<<v)
            if not low:continue
            assert low in FACES[2]
            src,dst=(low,high) if (low,high) in paired else (high,low)
            out[src].append(dst);indeg[dst]+=1;cover+=1
queue=deque(f for f in indeg if indeg[f]==0);count=0
while queue:
    f=queue.popleft();count+=1
    for g in out[f]:
        indeg[g]-=1
        if indeg[g]==0:queue.append(g)
assert count==len(FACES[2])
print('SCALE2_MORSE_OK', 'faces',len(FACES[2]), 'cover',cover,
      'pairs',len(pairs),'critical',sorted((f.bit_count()-1,f) for f in remaining))

# Verify explicit elementary simplicial collapses from the scale-3 complex.
complex3=set(FACES[3]);collapses=[]
while len(complex3)>1:
    facets=[f for f in complex3 if not any((f | (1<<v)) in complex3
                                              for v in range(N) if not f&(1<<v))]
    incidence=Counter()
    for high in facets:
        for v in range(N):
            if high&(1<<v):incidence[high^(1<<v)]+=1
    eligible=[]
    for high in facets:
        for v in range(N):
            if high&(1<<v):
                low=high^(1<<v)
                if low>0 and incidence[low]==1 and low in complex3:
                    eligible.append((high.bit_count(),high,low))
    assert eligible, 'A nontrivial stage has no free face'
    _,high,low=max(eligible)
    # Exactly one inclusion-maximal coface; the unique one is codim-one.
    assert sum((low & fac)==low for fac in facets)==1
    assert high in facets and (high^low).bit_count()==1
    complex3.remove(low);complex3.remove(high)
    collapses.append((low,high))
assert len(collapses)==767 and next(iter(complex3)).bit_count()==1
print('SCALE3_COLLAPSE_OK', 'faces',len(FACES[3]),'pairs',len(collapses),
      'terminal_vertex',next(iter(complex3)).bit_length()-1)

# Degree pattern forces full graph automorphism group S_3 x C_2.
assert [v for v in range(N) if len(ADJ[v])==4]==[0,1,2]
assert [v for v in range(N) if len(ADJ[v])==3 and not ADJ[v].intersection([0,1,2])]==[3,4]
red={(0,1,3):5,(0,1,4):6,(1,2,3):7,(1,2,4):8,
     (0,2,3):9,(0,2,4):10}
def permutation_on_graph(sigma,swap):
    perm=list(range(N))
    for i in range(3):perm[i]=sigma[i]
    perm[3],perm[4]=(4,3) if swap else (3,4)
    for (i,j,s),v in red.items():
        a,b=sorted((sigma[i],sigma[j]))
        perm[v]=red[(a,b,perm[s])]
    assert sorted(perm)==list(range(N))
    assert {tuple(sorted((perm[i],perm[j]))) for i,j in EDGES}==set(EDGES)
    return perm

def sign(permuted):
    return (-1)**sum(permuted[i]>permuted[j]
                     for i in range(len(permuted)) for j in range(i+1,len(permuted)))

def oriented_lefschetz(perm):
    tr=0
    for f in FACES[2]:
        ids=[i for i in range(N) if f&(1<<i)]
        imgs=[perm[i] for i in ids]
        if sorted(imgs)==ids:
            tr+=(-1)**(len(ids)-1)*sign(imgs)
    return tr
chars=[]
for sigma in permutations(range(3)):
    for swap in (0,1):
        perm=permutation_on_graph(sigma,swap)
        lefschetz=oriented_lefschetz(perm)
        trace3=1-lefschetz
        expected=sign(list(sigma))*(-1)**swap
        assert trace3==expected
        chars.append((sigma,swap,trace3))
assert len(chars)==12 and Counter(t for _,_,t in chars)=={1:6,-1:6}
print('SYMMETRY_OK', 'automorphisms',len(chars),
      'trace_formula','sgn(sigma)*(-1)**swap')
print('INTEGRAL_BARCODE', 'H0 10*[0,1)', 'H1 8*[1,2)', 'H3 1*[2,3)')
print('ALL_CHECKS_PASS')
