#!/usr/bin/env python3
"""Standalone exact check for hexagonal-prism ordinary matching-complex topology/symmetry.
Only Python standard library is required. Enumerates every face and cover relation.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N=6
vertices=[(layer,i) for layer in (0,1) for i in range(N)]
V=set(vertices)
edges=sorted({tuple(sorted(edge)) for i in range(N) for edge in (
    ((0,i),(0,(i+1)%N)), ((1,i),(1,(i+1)%N)), ((0,i),(1,i)))})
E=len(edges)
assert E==18 and len(V)==12
idx={e:i for i,e in enumerate(edges)}
incompat=[0]*E
for i,e in enumerate(edges):
    for j,f in enumerate(edges):
        if set(e).intersection(f): incompat[i] |= 1<<j

# Build every matching face by complete one-edge-at-a-time inclusion branching.
faces=[0]
for i in range(E):
    faces.extend(m|(1<<i) for m in tuple(faces) if not (m&incompat[i]))
faces.sort(key=lambda m:(m.bit_count(),m))
assert len(faces)==len(set(faces))==1104
fvector=[sum(m.bit_count()==k for m in faces) for k in range(7)]
assert fvector==[1,18,117,336,420,192,20]

# Lexicographic staged toggle matching on face poset.  The empty face is
# excluded from matching so an ordinary critical vertex survives.
remaining=set(faces)
upper_to_lower={}
for i in range(E):
    pairs=[]
    for m in sorted(remaining):
        if m==0 or m&(1<<i) or m&incompat[i]: continue
        b=m|(1<<i)
        if b in remaining: pairs.append((m,b))
    for a,b in pairs:
        assert a in remaining and b in remaining
        remaining.remove(a);remaining.remove(b)
        upper_to_lower[b]=a
crit=sorted((m for m in remaining if m),key=lambda m:(m.bit_count(),m))
crit_by_dimension=Counter(m.bit_count()-1 for m in crit)
assert len(upper_to_lower)==544
assert crit_by_dimension=={0:1,3:13,4:1},crit_by_dimension
assert 0 in remaining

# Verify acyclic matching in the complete directed Hasse diagram of *nonempty*
# faces; matched covers are oriented upward and all others downward.
nonempty=faces[1:]
pos={m:i for i,m in enumerate(nonempty)}
succ=[[] for _ in nonempty]
indeg=[0]*len(nonempty)
covers=0
for m in nonempty:
    for i in range(E):
        if not m&(1<<i):continue
        a=m^(1<<i)
        if not a:continue
        covers+=1
        if upper_to_lower.get(m)==a: u,v=pos[a],pos[m]
        else: u,v=pos[m],pos[a]
        succ[u].append(v);indeg[v]+=1
queue=deque(i for i,d in enumerate(indeg) if d==0)
seen=0
while queue:
    p=queue.popleft();seen+=1
    for q in succ[p]:
        indeg[q]-=1
        if indeg[q]==0:queue.append(q)
assert seen==len(nonempty)

# Signed integral Morse boundary: lower cells are replaced via the
# matched-upper boundary relation; matched-upper cells project to zero.
low_to_upper={lo:up for up,lo in upper_to_lower.items()}
def face_sign(m,i):
    return (-1)**((m&((1<<i)-1)).bit_count())
@lru_cache(None)
def project(m):
    if m in remaining:return {m:1}
    if m in upper_to_lower:return {}
    beta=low_to_upper[m]
    i=(beta^m).bit_length()-1
    e=face_sign(beta,i)
    out=defaultdict(int)
    for j in range(E):
        if beta&(1<<j) and j!=i:
            for c,w in project(beta^(1<<j)).items():
                out[c]-=e*face_sign(beta,j)*w
    return {c:w for c,w in out.items() if w}
def mbound(m):
    out=defaultdict(int)
    for j in range(E):
        if m&(1<<j):
            for c,w in project(m^(1<<j)).items():
                out[c]+=face_sign(m,j)*w
    return {c:w for c,w in out.items() if w}
crit3=sorted(c for c in crit if c.bit_count()==4)
crit4=sorted(c for c in crit if c.bit_count()==5)
assert len(crit4)==1
boundary=mbound(crit4[0]);morse_column=[boundary.get(c,0) for c in crit3]
assert sorted(abs(v) for v in morse_column)==[0]*10+[1]*3
# All other reduced Morse differentials have zero source or target.
# The gcd=1 degree vector is primitive, so one 4-cell kills one 3-sphere.

# Independent mod-2 simplicial boundary ranks for all 6 chain groups.
by_size=defaultdict(list)
for m in faces:by_size[m.bit_count()].append(m)
rank=[]
for k in range(1,7):
    row={m:i for i,m in enumerate(by_size[k-1])}
    pivots={}
    for m in by_size[k]:
        column=0
        for j in range(E):
            if m&(1<<j): column ^=1<<row[m^(1<<j)]
        while column:
            t=column.bit_length()-1
            if t in pivots:column ^=pivots[t]
            else:pivots[t]=column;break
    rank.append(len(pivots))
assert rank==[1,17,100,236,172,20]

# Enumerate all 24 group elements r^k s^f z^z. A rotation shifts hexagon
# index, reflection negates it and the layer switch flips binary layer.
def edge_permutation(k,f,z):
    def tr(v):return (v[0]^z, (k+(-v[1] if f else v[1]))%N)
    return tuple(idx[tuple(sorted((tr(a),tr(b))))] for a,b in edges)
aut={}
for z in (0,1):
    for f in (0,1):
        for k in range(N):aut[(z,f,k)]=edge_permutation(k,f,z)
assert len(set(aut.values()))==24

def sign_perm(vals):
    return -1 if sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))%2 else 1

def trace_h3(pi):
    # Reduced alternating chain trace (-1)^(face dimension); reduced H3
    # alone contributes with sign -1, hence change the overall sign.
    alternating=0
    for m in faces:
        selected=[i for i in range(E) if m&(1<<i)]
        images=[pi[i] for i in selected]
        if sorted(images)==selected:
            alternating+=(-1 if len(selected)%2==0 else 1)*sign_perm(images)
    return -alternating

character={g:trace_h3(pi) for g,pi in aut.items()}
expected={
 (0,0):[12,0,0,6,0,0],
 (0,1):[0,-2,0,-2,0,-2],
 (1,0):[-2,-2,-2,4,-2,-2],
 (1,1):[2,4,2,4,2,4]
}
for (z,f),vals in expected.items():assert [character[(z,f,k)] for k in range(N)]==vals

# Rational irreducibles of D6 x C2.  Four 1D characters (r -> a,
# s -> b) and two real rational 2D characters t1, t2, each with z sign.
classes=[]
for ez in (1,-1):
    for a in (1,-1):
        for b in (1,-1):
            num=sum(character[(z,f,k)]*(ez**z)*(a**k)*(b**f)
                    for z in (0,1) for f in (0,1) for k in range(N))
            assert num%24==0
            classes.append(('L',ez,a,b,num//24))
    for j,row in [(1,[2,1,-1,-2,-1,1]),(2,[2,-1,-1,2,-1,-1])]:
        num=sum(character[(z,0,k)]*(ez**z)*row[k]
                    for z in (0,1) for k in range(N))
        assert num%24==0
        classes.append(('W',ez,j,num//24))
nonzero=[x for x in classes if x[-1]!=0]
assert nonzero==[
    ('L',1,1,1,1),('W',1,2,2),
    ('L',-1,1,-1,2),('L',-1,-1,1,1),('W',-1,1,1),('W',-1,2,1)
]
assert sum((1 if x[0]=='L' else 2)*x[-1] for x in nonzero)==12
assert sum(character.values())//24==1

print('HEXAGONAL_PRISM_MATCHING_COMPLEX_EXACT_PASS')
print('edges',E,'nonempty_faces',len(nonempty),'f_vector_including_empty',fvector)
print('matched_pairs',len(upper_to_lower),'critical_cells',sorted(crit_by_dimension.items()),'hasse_covers',covers,'acyclic',True)
print('critical_4_mask',crit4[0],'critical_3_masks',crit3)
print('morse_boundary_column',morse_column,'primitive',True)
print('mod2_augmented_boundary_ranks',rank)
print('D6xC2_character_z0_rotations',expected[(0,0)])
print('D6xC2_character_z0_reflections',expected[(0,1)])
print('D6xC2_character_z1_rotations',expected[(1,0)])
print('D6xC2_character_z1_reflections',expected[(1,1)])
print('irreducibles',nonzero,'full_invariants',1)
