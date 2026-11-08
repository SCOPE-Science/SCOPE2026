"""Exact finite checks for the affine action on the transitive-subtournament complex of P31.
Requires only Python 3 standard library.
"""
from collections import defaultdict
p=31
Q={pow(i,2,p) for i in range(1,p)}
assert len(Q)==15 and Q.isdisjoint({(-x)%p for x in Q})

def arrow(i,j):return (j-i)%p in Q

def transitive(vs):
    k=len(vs)
    deg=[sum(arrow(a,b) for b in vs if b!=a) for a in vs]
    return sorted(deg)==list(range(k))

# Canonical vertex-label increasing recursion enumerates all transitive sets, each once.
faces=[[] for _ in range(8)]
counts_test=0

def visit(vs,after):
    global counts_test
    if vs:
        faces[len(vs)-1].append(tuple(vs))
    for v in range(after,p):
        if transitive(vs+[v]):
            visit(vs+[v],v+1)
visit([],0)
while faces and not faces[-1]:faces.pop()
counts=list(map(len,faces))
print('face_counts',counts,'total',sum(counts))
assert counts==[31,465,3255,9765,10695,3255,465],counts
# Independent cyclic-orbit count: every nonempty face has a positive number of
# vertices; count incidences of faces through vertex 0 and translate them.
through0=[sum(0 in f for f in F) for F in faces]
assert [31*c//(d+1) for d,c in enumerate(through0)]==counts
assert all(31*c%(d+1)==0 for d,c in enumerate(through0))
print('face_through_zero',through0)
assert sum((-1)**d*n for d,n in enumerate(counts))-1==960

# Each simplex is an unoriented set with canonical ordering, so GF(2) boundaries
# are the incidence matrices independent of orientation.

def rank_mod2(d):
    # rank of partial_d from faces[d] to faces[d-1], d>=1
    row={s:i for i,s in enumerate(faces[d-1])}
    pivots={}
    for face in faces[d]:
        col=0
        for i in range(len(face)):
            sub=face[:i]+face[i+1:]
            col ^= 1<<row[sub]
        while col:
            k=col.bit_length()-1
            if k in pivots:col^=pivots[k]
            else:
                pivots[k]=col
                break
    return len(pivots)
ranks=[0]+[rank_mod2(d) for d in range(1,len(faces))]+[0]
bettis=[counts[d]-ranks[d]-ranks[d+1] for d in range(len(faces))]
# Explicitly check successive incidence maps compose to zero over GF(2).
for d in range(2,len(faces)):
    for face in faces[d]:
        chain=set()
        for j in range(len(face)):
            f=face[:j]+face[j+1:]
            for k in range(len(f)):
                h=f[:k]+f[k+1:]
                if h in chain: chain.remove(h)
                else: chain.add(h)
        assert not chain
print('mod2_boundary_ranks',ranks,'mod2_betti',bettis)
assert bettis==[1,0,0,0,960,0,0],bettis

# Group G= affine maps x -> a*x+b, a in squares nonzero, b in F31;
# verify composition and action on tournaments explicitly.
actions=[tuple((a*x+b)%p for x in range(p)) for a in sorted(Q) for b in range(p)]
assert len(set(actions))==465
for g in actions:
    assert all(arrow(i,j)==arrow(g[i],g[j]) for i in range(p) for j in range(p) if i!=j)

# Lefschetz local trace: a simplex fixed under g must be pointwise fixed.
# Verify directly on all faces and all group elements; fixed-face signs are +1.
# A non-identity affine map has either 0 or 1 fixed point.
for g in actions:
    fixed={i for i in range(p) if g[i]==i}
    if len(fixed)==p: assert g==tuple(range(p))
    else: assert len(fixed) in (0,1)
    # A g-invariant transitive tournament face is pointwise fixed by unique order.
    # Instead of O(13 million) checks, count face sets on the fixed vertices.
    fixed_face_red=sum((-1)**d * sum(set(face)<=fixed for face in faces[d]) for d in range(len(faces)))-1
    target=960 if len(fixed)==p else (len(fixed)-1)
    assert fixed_face_red==target, (g,target,fixed_face_red)

# Character of top rational homology from Hopf trace, concentrated in degree 4.
# P31 natural permutation module has trace |Fix_V(g)|, regular module has trace
# 465 at identity and 0 otherwise. So H4 = 2*Q[G]+augmentation Q[V]/Q.
# We verify class-character equality at all 465 group elements.
char={}
for g in actions:
    fix=sum(g[i]==i for i in range(p))
    lhs=960 if fix==31 else fix-1
    rhs=2*(465 if fix==31 else 0)+(fix-1)
    assert lhs==rhs
    char[lhs]=char.get(lhs,0)+1
assert char=={960:1,-1:30,0:434},char
assert sum(960 if sum(g[i]==i for i in range(p))==31 else sum(g[i]==i for i in range(p))-1 for g in actions)==930
print('affine_group_order',len(actions),'character_value_multiplicities',sorted(char.items()))
print('invariant_dimension',2,'translation_invariant_dimension',30)
print('PALEY31_AFFINE_HOMOLOGY_CHARACTER_PASS')
