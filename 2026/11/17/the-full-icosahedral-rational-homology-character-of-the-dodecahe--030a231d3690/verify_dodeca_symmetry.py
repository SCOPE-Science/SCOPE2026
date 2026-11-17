#!/usr/bin/env python3
"""Exact full-symmetry character certificate for a dodecahedral perfect-matching complex.
Only Python 3 standard library. All enumeration is finite and exhaustive.
"""
from collections import Counter
from functools import lru_cache

N=20
R2=(1,0,9,8,7,6,5,4,3,2,11,10,19,18,17,16,15,14,13,12)
R3=(0,9,19,17,15,5,4,14,12,10,1,8,11,7,13,6,3,16,2,18)
Z=(5,6,7,8,9,0,1,2,3,4,15,16,17,18,19,10,11,12,13,14)
IDENT=tuple(range(N))

def compose(a,b):
    return tuple(a[b[i]] for i in range(N))

def closure(generators):
    known={IDENT}; frontier=[IDENT]
    while frontier:
        x=frontier.pop()
        for a in generators:
            y=compose(a,x)
            if y not in known:
                known.add(y);frontier.append(y)
    return known

def order(a):
    x=IDENT
    for j in range(1,121):
        x=compose(a,x)
        if x==IDENT:return j
    raise AssertionError('Unexpected group order')

E=tuple(sorted({tuple(sorted((i,(i+1)%10))) for i in range(10)} |
               {tuple(sorted((i,i+10))) for i in range(10)} |
               {tuple(sorted((i+10,(i+2)%10+10))) for i in range(10)}))
EINDEX={edge:j for j,edge in enumerate(E)}
assert len(E)==30 and len({v for e in E for v in e})==20
ADJ=[[] for _ in range(N)]
for a,b in E:ADJ[a].append(b);ADJ[b].append(a)
assert all(len(a)==3 for a in ADJ)

def preserves(p):
    return {tuple(sorted((p[a],p[b]))) for a,b in E}==set(E)
assert all(preserves(p) for p in (R2,R3,Z))
assert order(R2)==2 and order(R3)==3 and order(compose(R2,R3))==5
assert order(Z)==2 and all(compose(Z,p)==compose(p,Z) for p in (R2,R3))
ROT=closure((R2,R3))
FULL=closure((R2,R3,Z))
assert len(ROT)==60 and Z not in ROT and len(FULL)==120
assert all(preserves(p) for p in FULL)
assert len({p for p in FULL if all(compose(p,q)==compose(q,p) for q in FULL)})==2

@lru_cache(None)
def perfect_matchings(uncovered):
    if not uncovered:return ((),)
    v=(uncovered&-uncovered).bit_length()-1
    answer=[]
    for w in ADJ[v]:
        if uncovered&(1<<w):
            e=EINDEX[tuple(sorted((v,w)))]
            for rest in perfect_matchings(uncovered^(1<<v)^(1<<w)):
                answer.append(tuple(sorted((e,)+rest)))
    return tuple(answer)
PM=perfect_matchings((1<<N)-1)
assert len(PM)==len(set(PM))==36
PERFECT_MASKS=tuple(sum(1<<i for i in matching) for matching in PM)
FACES=set()
for p in PM:
    for bits in range(1<<len(p)):
        FACES.add(sum(1<<p[i] for i in range(len(p)) if bits>>i&1))
FV=Counter(f.bit_count() for f in FACES)
assert len(FACES)==30504
assert [FV[i] for i in range(11)] == [1,30,375,2180,5790,8352,7440,4320,1620,360,36]

# Method A: signed trace on all oriented simplicial chain groups.
def edge_permutation(p):
    return tuple(EINDEX[tuple(sorted((p[a],p[b])))] for a,b in E)

def signed_reduced_euler(p):
    ep=edge_permutation(p)
    result=-1 # empty simplex contributes reduced degree -1
    for mask in FACES:
        if not mask:continue
        indices=[i for i in range(30) if mask&(1<<i)]
        changed=[ep[i] for i in indices]
        if sum(1<<i for i in changed)!=mask:continue
        inversions=sum(changed[i]>changed[j] for i in range(len(changed)) for j in range(i+1,len(changed)))
        result+=(-1)**(len(indices)-1+inversions)
    return result

# Method B: completely different chain model: faces of the geometric fixed-space
# are edge-orbit subsets whose entire union lies in a perfect matching.
def geometric_fixed_reduced_euler(p):
    ep=edge_permutation(p)
    unseen=set(range(30));orbits=[]
    while unseen:
        start=min(unseen);orbit=[];i=start
        while i in unseen:
            orbit.append(i);unseen.remove(i);i=ep[i]
        assert i==start
        orbits.append(sum(1<<a for a in orbit))
    orbfaces={0}
    for matching in PERFECT_MASKS:
        allowed=[j for j,o in enumerate(orbits) if o&matching==o]
        for m in range(1<<len(allowed)):
            orbfaces.add(sum(1<<allowed[i] for i in range(len(allowed)) if m>>i&1))
    return sum((-1)**(mask.bit_count()-1) for mask in orbfaces if mask)-1

ROWS=[]
for p in FULL:
    L1=signed_reduced_euler(p)
    L2=geometric_fixed_reduced_euler(p)
    assert L1==L2,(order(p),L1,L2)
    # Published integral homology is only Z/2 at degree two and Z^20 at degree three.
    # Over Q only H3 remains; trace(H3) = -reduced Lefschetz.
    ROWS.append((p, -L1, order(p)))
assert next(t for p,t,k in ROWS if p==IDENT)==20
assert next(t for p,t,k in ROWS if p==Z)==10

# Partition into A5 rotation classes, and their central twists; for 5-cycles
# there are two classes of size 12, but their traces are both zero.
COUNTS=Counter()
for p,t,k in ROWS:
    isrot=p in ROT
    if p==IDENT:cat='rot_1'
    elif p==Z:cat='central'
    elif isrot:cat='rot_'+str(k)
    else:
        q=compose(Z,p); assert q in ROT
        cat='central_times_rot_'+str(order(q))
    COUNTS[(cat,t)]+=1
EXPECTED={('rot_1',20):1,('central',10):1,
          ('rot_2',4):15,('central_times_rot_2',2):15,
          ('rot_3',-1):20,('central_times_rot_3',1):20,
          ('rot_5',0):24,('central_times_rot_5',0):24}
assert COUNTS==EXPECTED,(COUNTS,EXPECTED)

# The A5 irreducible rational characters used are 1, V4, V5; both 3-dimensional
# complex characters would force nonzero unequal traces at the two 5-cycle classes.
EVEN=(15,3,0,0)
ODD=(5,1,-1,0)
assert tuple(EVEN[i]+ODD[i] for i in range(4))==(20,4,-1,0)
assert tuple(EVEN[i]-ODD[i] for i in range(4))==(10,2,1,0)
TRIV=(1,1,1,1)
V4=(4,0,1,-1)
V5=(5,1,-1,0)
assert tuple(TRIV[i]+V4[i]+2*V5[i] for i in range(4))==EVEN
assert ODD==V5
assert sum(t for p,t,k in ROWS)==120 # one-dimensional full invariant space
assert sum(t for p,t,k in ROWS if p in ROT)==60 # one-dimensional rotational invariant

print('GRAPH: 20 vertices, 30 edges; matching facets:',len(PM))
print('FACE_COUNTS_BY_SIZE:',*[FV[i] for i in range(11)])
print('FULL_GROUP: 120; ROTATIONS: 60; CENTRAL_INVERSION: order 2')
for (name,trace),mult in sorted(COUNTS.items()):
    print('CLASS:',name,'size',mult,'H3_trace',trace)
print('TWO_INDEPENDENT_LEFSCHETZ_METHODS: 120/120 agree')
print('CENTRAL_EVEN_CHARACTER:',EVEN,' = 1 + V4 + 2V5')
print('CENTRAL_ODD_CHARACTER:',ODD,' = V5')
print('FULL_SYMMETRY_H3_RATIONAL_INVARIANT_RANK: 1')
print('DODECAHEDRAL_PERFECT_MATCHING_CHARACTER_PASS')
