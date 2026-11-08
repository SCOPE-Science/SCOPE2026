#!/usr/bin/env python3
"""Exact finite proof checks for the rational octahedral action on a cube matching complex."""
from collections import defaultdict, deque
from itertools import combinations, permutations

VERTICES = tuple(range(8))
EDGES = tuple(sorted((u, v) for u, v in combinations(VERTICES, 2) if (u ^ v).bit_count() == 1))
EDGE_INDEX = {e: j for j, e in enumerate(EDGES)}
FACES = tuple(tuple(t for t in combinations(range(len(EDGES)), k)
                    if len({w for j in t for w in EDGES[j]}) == 2*k)
              for k in (1, 2, 3, 4))
assert tuple(map(len, FACES)) == (12, 42, 44, 9)
ALL = {f for fs in FACES for f in fs}
assert len(ALL) == 107

# Verify a complete acyclic elementary Hasse matching (no appeals to numerical Betti ranks).
PRIORITY = (2, 3, 9, 10, 8, 1, 6, 11, 4, 0, 5, 7)
unmatched = set(ALL)
matched = {}
for e in PRIORITY:
    for a in sorted(tuple(unmatched), key=lambda f:(len(f),f)):
        if a not in unmatched or e in a: continue
        b = tuple(sorted(a+(e,)))
        if b in unmatched:
            matched[(a,b)] = 1
            unmatched.remove(a); unmatched.remove(b)
assert len(matched) == 51
assert unmatched == {(2,), (0,5,8), (0,7,8), (6,7,8), (1,4,11)}

# In the directed Hasse graph use upward arrows only for matched covers.
adj = {f:[] for f in ALL};indeg = {f:0 for f in ALL};covers=0
for b in ALL:
    if len(b)<2:continue
    for j in range(len(b)):
        a=b[:j]+b[j+1:]
        if (a,b) in matched: src,dst=a,b
        else: src,dst=b,a
        adj[src].append(dst);indeg[dst]+=1;covers+=1
assert covers == 252
queue=deque([f for f in ALL if indeg[f]==0]);visited=0
while queue:
    a=queue.popleft();visited+=1
    for b in adj[a]:
        indeg[b]-=1
        if indeg[b]==0:queue.append(b)
assert visited==107, 'acyclicity failed'

# Signed simplicial action and exact fixed-face Lefschetz trace.
def sign_sort(vals):
    inversions=sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))
    return -1 if inversions%2 else 1

def permutation_vertices(b,p):
    return tuple(b ^ sum(((v>>i)&1)<<p[i] for i in range(3)) for v in VERTICES)

def boundary(face):
    return {face[:i]+face[i+1:]: (-1)**i for i in range(len(face))}

def apply_face(face,edge_map):
    a=tuple(edge_map[j] for j in face)
    return tuple(sorted(a)), sign_sort(a)

def exterior_character(b,p):
    tr=sum((-1)**((b>>p[i])&1) for i in range(3) if p[i]==i)
    tr2=sum((-1)**(((b>>p[i])&1)+((b>>i)&1)) for i in range(3) if p[p[i]]==i)
    assert (tr*tr-tr2)%2==0
    return (-1)**b.bit_count() + (tr*tr-tr2)//2

def character_model(b,p):
    ans=(-1)**b.bit_count()
    for y in (3,5,6):  # weight-two characters of the vertex-translation subgroup
        py=sum(((y>>i)&1)<<p[i] for i in range(3))
        if py==y:
            support=[i for i in range(3) if (y>>i)&1]
            stabilizer_sign=-1 if p[support[0]]==support[1] else 1
            ans+=stabilizer_sign*(-1)**(b&y).bit_count()
    return ans

def character_direct(b,p):
    vp=permutation_vertices(b,p)
    e_map=tuple(EDGE_INDEX[tuple(sorted((vp[a],vp[c])))] for a,c in EDGES)
    assert sorted(e_map)==list(range(12))
    tr=-1 # augmented face, degree -1
    for k,fs in enumerate(FACES):
        for f in fs:
            image, s=apply_face(f,e_map)
            if image==f:tr+=(-1)**k * s
            if len(f)>1:
                # Boundary commutes with the signed action, checked on all basis faces.
                lhs=defaultdict(int);rhs=defaultdict(int)
                for sub,coef in boundary(f).items():
                    im,sg=apply_face(sub,e_map);lhs[im]+=coef*sg
                for sub,coef in boundary(image).items():rhs[sub]+=s*coef
                assert dict(lhs)==dict(rhs),(b,p,f)
    return tr

hist=defaultdict(int); transchars={}; n=0
for p in permutations(range(3)):
    for b in range(8):
        observed=character_direct(b,p)
        predicted=character_model(b,p)
        assert observed==predicted==exterior_character(b,p),(b,p,observed,predicted,exterior_character(b,p))
        hist[observed]+=1;n+=1
        if p==(0,1,2):transchars[b]=observed
assert n==48
assert [transchars[b] for b in range(8)]==[4,-2,-2,0,-2,0,0,2]
# Integer Fourier decomposition of translation characters. Zero weight on trivial character.
mults={y:sum(transchars[b]*(-1)**((b&y).bit_count()) for b in range(8))//8 for y in range(8)}
assert mults=={0:0,1:0,2:0,3:1,4:0,5:1,6:1,7:1}
assert character_direct(0,(0,1,2))==4
print('CUBE_MATCHING_OCTAHEDRAL_REPRESENTATION_PASS')
print('edges',len(EDGES),'face_counts',tuple(map(len,FACES)),'matched_pairs',len(matched), 'critical_cells',len(unmatched),'hasse_relations',covers)
print('checked_group_elements',n,'checked_signed_boundary_face_identites',n*sum(len(a) for a in FACES[1:]))
print('trace_distribution',sorted(hist.items()))
print('translation_traces',[transchars[b] for b in range(8)])
print('translation_weight_multiplicities',[mults[y] for y in range(8)])
print('invariants_under_all_translations',mults[0])
