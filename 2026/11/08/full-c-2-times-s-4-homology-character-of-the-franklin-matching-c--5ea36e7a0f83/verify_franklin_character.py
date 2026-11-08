#!/usr/bin/env python3
"""Finite proof checker: Franklin ordinary matching complex and its full symmetry character.
Requires only Python standard library; use `python3 verify_franklin_character.py`.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N=12
# LCF presentation [5,-5]^6; vertices 0,...,11.
E={tuple(sorted((i,(i+1)%N))) for i in range(N)}
for i in range(N):
    E.add(tuple(sorted((i,(i+(5 if i%2==0 else -5))%N))))
E=tuple(sorted(E))
assert len(E)==18
adj=[set() for _ in range(N)]
for a,b in E: adj[a].add(b);adj[b].add(a)
assert all(len(s)==3 for s in adj)
edge_masks=tuple((1<<a)|(1<<b) for a,b in E)
edge_index={x:k for k,x in enumerate(E)}

# Enumerate all nonempty matchings by all increasing edge tuples.
simplices=[]
def enumerate_faces(k,occupied,face):
    for e in range(k,len(E)):
        if occupied&edge_masks[e]:continue
        t=face+(e,)
        simplices.append(t)
        enumerate_faces(e+1,occupied|edge_masks[e],t)
enumerate_faces(0,0,())
faces=set(simplices)
fvector=tuple(sum(len(x)==k for x in faces) for k in range(1,7))
assert fvector==(18,117,336,417,186,17)
assert len(faces)==1091

# Deterministic greedy elementary matching; all nonempty faces considered.
unmatched=set(faces)
pairs=[]
for pivot in range(len(E)):
    for sigma in sorted(tuple(unmatched),key=lambda x:(len(x),x)):
        if pivot in sigma:continue
        coface=tuple(sorted(sigma+(pivot,)))
        if sigma in unmatched and coface in unmatched:
            unmatched.remove(sigma);unmatched.remove(coface)
            pairs.append((sigma,coface))
critical=Counter(len(s)-1 for s in unmatched)
assert len(pairs)==539 and critical=={0:1,3:12},(len(pairs),critical)

# Verify acyclicity of full directed Hasse diagram: matched edges upward,
# every other cover downward; empty face is not a cell.
matched=set(pairs)
indeg={x:0 for x in faces}
nexts=defaultdict(list)
covers=0
for sigma in faces:
    for j in range(len(sigma)):
        tau=sigma[:j]+sigma[j+1:]
        if not tau:continue
        covers+=1
        u,v=(tau,sigma) if (tau,sigma) in matched else (sigma,tau)
        nexts[u].append(v);indeg[v]+=1
queue=deque(x for x in sorted(faces) if indeg[x]==0)
visited=0
while queue:
    u=queue.popleft(); visited+=1
    for v in nexts[u]:
        indeg[v]-=1
        if indeg[v]==0:queue.append(v)
assert covers==3942 and visited==1091,(covers,visited)

# Enumerate graph automorphisms by a fully exhaustive injective backtrack.
# The adjacency/nonadjacency test against already assigned vertices is exact.
aut=[]
def extend(mapping,used):
    if len(mapping)==N:
        aut.append(tuple(mapping[i] for i in range(N)));return
    v=max((i for i in range(N) if i not in mapping),key=lambda i:(sum(j in mapping for j in adj[i]),-i))
    for w in range(N):
        if w in used:continue
        if all(((u in adj[v])==(mapping[u] in adj[w])) for u in mapping):
            mapping[v]=w;used.add(w)
            extend(mapping,used)
            used.remove(w);del mapping[v]
extend({},set())
aut=sorted(set(aut)); assert len(aut)==48
identity=tuple(range(N))
permid={p:i for i,p in enumerate(aut)}
def compose(p,q):return tuple(p[q[i]] for i in range(N))
def inverse(p):return tuple(p.index(i) for i in range(N))
def order(p):
    power=identity
    for k in range(1,50):
        power=compose(p,power)
        if power==identity:return k
    raise AssertionError('order>49')
assert all(compose(p,q) in permid for p in aut for q in aut)
edgeperm=[]
for p in aut:
    perm=tuple(edge_index[tuple(sorted((p[a],p[b])))] for a,b in E)
    assert sorted(perm)==list(range(18))
    edgeperm.append(perm)

# Method I: character via vertex-disjoint orbits of graph edges.
# A stable face is a union of orbits; each selected orbit contributes -1
# to the signed (-1)^dim reduced simplicial trace after degree shift.
def orbit_character(p):
    rest=set(range(len(E))); orbit_masks=[]
    while rest:
        j=min(rest);block=[]
        while j in rest:
            rest.remove(j);block.append(j);j=p[j]
        used=0
        for e in block:
            if used&edge_masks[e]:break
            used|=edge_masks[e]
        else:orbit_masks.append(used)
    def rec(k,used):
        if k==len(orbit_masks):return 1
        v=rec(k+1,used)
        if not used&orbit_masks[k]:v-=rec(k+1,used|orbit_masks[k])
        return v
    return rec(0,0)

# Method II: independent signed fixed-simplex sum including empty face.
def simplex_character(p):
    total=1
    for face in simplices:
        image=tuple(p[e] for e in face)
        if set(image)!=set(face):continue
        inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        total+=(-1)**(len(face)+inversions)
    return total
chars=[orbit_character(p) for p in edgeperm]
assert chars==[simplex_character(p) for p in edgeperm]
assert Counter(chars)=={0:26,-2:14,2:6,12:1,4:1}
assert chars[permid[identity]]==12 and sum(chars)==0
assert sum(c*c for c in chars)==48*5

# All conjugacy classes and complete character values.
remaining=set(range(len(aut)));classes=[]
while remaining:
    i=min(remaining); p=aut[i]
    C={permid[compose(compose(g,p),inverse(g))] for g in aut}
    assert C<=remaining
    remaining-=C; classes.append(sorted(C))
class_data=[(len(C),order(aut[C[0]]),chars[C[0]],aut[C[0]]) for C in classes]
assert [(n,k,v) for n,k,v,_ in class_data]==[
    (1,1,12),(3,2,0),(3,2,0),(6,2,-2),(6,4,0),
    (8,3,0),(8,6,-2),(6,2,2),(6,4,0),(1,2,4)]
assert sum(n for n,_,_,_ in class_data)==48

z=tuple((i+6)%N for i in range(N))
assert z in permid and order(z)==2 and all(compose(z,g)==compose(g,z) for g in aut)
assert chars[permid[z]]==4
# The six involutions with character -2 generate a complement H of <z>.
generators=[g for g in aut if order(g)==2 and chars[permid[g]]==-2]
assert len(generators)==6
H={identity}; frontier=[identity]
while frontier:
    g=frontier.pop()
    for t in generators:
        h=compose(g,t)
        if h not in H:H.add(h);frontier.append(h)
assert len(H)==24 and z not in H
assert {compose(z,g) for g in H}.isdisjoint(H)
assert len(H|{compose(z,g) for g in H})==48

# Directly realize H as S4 via conjugation on its four order-3 subgroups.
three_subgroups={frozenset((identity,g,compose(g,g))) for g in H if order(g)==3}
assert len(three_subgroups)==4
subs=sorted(three_subgroups)
sub_index={u:i for i,u in enumerate(subs)}
S4images=[]
for g in H:
    gi=inverse(g)
    q=tuple(sub_index[frozenset(compose(compose(g,h),gi) for h in U)] for U in subs)
    S4images.append(q)
assert len(set(S4images))==24

# Character of H, and of zH, for the five S4 permutation cycle types.
def cycle_type(p):
    unvisited=set(range(4)); lengths=[]
    while unvisited:
        i=min(unvisited);j=i;count=0
        while j in unvisited:
            unvisited.remove(j);count+=1;j=p[j]
        lengths.append(count)
    return tuple(sorted(lengths,reverse=True))
values=defaultdict(set);counts=Counter()
for g,q in zip(H,S4images):
    typ=cycle_type(q)
    c=chars[permid[g]];cz=chars[permid[compose(z,g)]]
    values[typ].add((c,cz));counts[typ]+=1
assert counts=={(1,1,1,1):1,(2,1,1):6,(2,2):3,(3,1):8,(4,):6}
assert all(len(x)==1 for x in values.values())
assert {k:next(iter(v)) for k,v in values.items()}=={
 (1,1,1,1):(12,4),(2,1,1):(-2,2),(2,2):(0,0),(3,1):(0,-2),(4,):(0,0)}
# Known S4 irreducible characters: trivial, sign, standard, sign*standard,
# and (2,2).  Splitting into z-even and z-odd characters is direct.
S4chars={
 (1,1,1,1):(1,1,3,3,2),
 (2,1,1):(1,-1,1,-1,0),
 (2,2):(1,1,-1,-1,2),
 (3,1):(1,1,0,0,-1),
 (4,):(1,-1,-1,1,0)}
for typ,(c,cz) in {k:next(iter(v)) for k,v in values.items()}.items():
    one,sign,std,signstd,two=S4chars[typ]
    assert (c+cz)//2==std+signstd+two
    assert (c-cz)//2==sign+signstd

print('FRANKLIN_GRAPH_VERTICES=12 EDGES=18')
print('F_VECTOR='+' '.join(map(str,fvector)))
print('MORSE_MATCHED_PAIRS=539 COVER_RELATIONS=3942 ACYCLIC_VERTICES=1091')
print('MORSE_CRITICAL=one_0_cell_plus_twelve_3_cells')
print('GRAPH_AUTOMORPHISMS=48 CONJUGACY_CLASSES=10')
for n,k,v,p in class_data:
    print('CLASS size=%d order=%d H3_trace=%d rep=%s'%(n,k,v,','.join(map(str,p))))
print('CENTRAL_HALF_TURN_H3_TRACE=4; H3_CENTRAL_PLUS_DIM=8; MINUS_DIM=4')
print('S4_COMPLEMENT_ORDER=24; S4_ACTION_ON_FOUR_C3_SUBGROUPS_FAITHFUL=TRUE')
print('DECOMPOSITION: z_even=std+sign_std+S(2,2); z_odd=sign+sign_std')
print('H3_GLOBAL_INVARIANTS=0; CHARACTER_NORM_SQUARED=5')
print('FRANKLIN_FULL_AUT_MATCHING_CHARACTER_PASS')
