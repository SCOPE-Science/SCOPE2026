#!/usr/bin/env python3
"""Exhaustive integral Morse and natural symmetry checks for Ind(C_8 x K_3).
Requires Python 3.10+ standard library only. Vertex (i,c) is 3*i+c.
"""
from collections import Counter, deque, defaultdict
from functools import lru_cache
from itertools import combinations, permutations
from fractions import Fraction

N, NC, NK = 24, 8, 3
ADJ = [0] * N
for i in range(NC):
    for c in range(NK):
        v = 3*i+c
        for j in ((i-1)%NC,(i+1)%NC):
            for d in range(NK):
                if c != d:
                    ADJ[v] |= 1 << (3*j+d)

# Build each independent face once, including the empty face.
faces = [0]
for v in range(N):
    bit = 1 << v
    faces.extend([s | bit for s in faces if not (s & ADJ[v])])
assert len(faces) == len(set(faces)) == 18722
counts = Counter(s.bit_count()-1 for s in faces if s)
assert [counts[d] for d in range(12)] == [24,228,1112,3042,4848,4652,2880,1305,472,132,24,2]

# A staged elementary face matching with deterministic vertex toggles.
active = set(faces)
active.remove(0)
up, down = {}, {}
for v in range(N):
    bit = 1 << v
    lows = sorted(s for s in active if not (s & bit) and (s|bit) in active)
    for a in lows:
        b = a | bit
        assert a in active and b in active
        active.remove(a)
        active.remove(b)
        up[a], down[b] = b, a
assert len(up) == len(down) == 9353
critical = sorted(active, key=lambda s:(s.bit_count(),s))
assert Counter(s.bit_count()-1 for s in critical) == {0:1,4:6,5:8}

# Acyclicity: orient each unmatched covering arrow high->low, matched low->high.
all_faces = set(faces) - {0}
indeg = {s:0 for s in all_faces}
for b in all_faces:
    if b.bit_count() == 1: continue
    t = b
    while t:
        bit = t & -t; t -= bit
        a = b ^ bit
        if a and a in all_faces:
            nxt = b if up.get(a) == b else a
            indeg[nxt] += 1
queue = deque(s for s in all_faces if indeg[s] == 0)
processed = 0
while queue:
    s = queue.popleft()
    processed += 1
    if s in up:
        b = up[s]
        indeg[b] -= 1
        if indeg[b] == 0: queue.append(b)
    if s.bit_count() > 1:
        t = s
        while t:
            bit = t & -t; t -= bit
            a = s ^ bit
            if a and up.get(a) != s:
                indeg[a] -= 1
                if indeg[a] == 0: queue.append(a)
assert processed == len(all_faces) == 18721


def bd(s):
    """Simplicial oriented boundary of an ascending-bit face."""
    j, rem = 0, s
    while rem:
        bit = rem & -rem; rem -= bit
        yield (s^bit), (-1 if j & 1 else 1)
        j += 1

@lru_cache(None)
def reduce_face(s):
    """Morse projection to critical cells in the same degree.
    Matched upper faces project to zero; matched lower faces are replaced
    using the oriented boundary of their matched upper face.
    """
    if s in down:
        return ()
    if s not in up:
        assert s in active
        return ((s,1),)
    b = up[s]
    bit = b ^ s
    pivot = -1 if (s & (bit-1)).bit_count() % 2 else 1
    out = defaultdict(int)
    for a, c in bd(b):
        if a == s: continue
        for target, value in reduce_face(a):
            out[target] -= pivot*c*value
    return tuple((a,c) for a,c in sorted(out.items()) if c)

lo = [s for s in critical if s.bit_count() == 5]
hi = [s for s in critical if s.bit_count() == 6]
li = {s:i for i,s in enumerate(lo)}
D = [[0]*len(hi) for _ in lo]
for j,s in enumerate(hi):
    for a,c in bd(s):
        for t,v in reduce_face(a):
            assert t in li
            D[li[t]][j] += c*v
assert D == [
    [0,-1,0,0,0,-1,0,0],
    [0,0,-1,0,0,0,-1,0],
    [0,-1,0,-1,0,0,0,0],
    [0,0,-1,-1,0,0,0,0],
    [0,0,0,0,-1,0,-1,0],
    [0,0,0,0,-1,-1,0,0],
]

def rank_rat(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    m,n=len(a),len(a[0]);row=0
    for j in range(n):
        pivot=next((i for i in range(row,m) if a[i][j]),None)
        if pivot is None: continue
        a[row],a[pivot]=a[pivot],a[row]
        scale=a[row][j];a[row]=[x/scale for x in a[row]]
        for k in range(m):
            if k != row and a[k][j]:
                fac=a[k][j];a[k]=[a[k][h]-fac*a[row][h] for h in range(n)]
        row+=1
        if row==m: break
    return row

def det(a):
    n=len(a)
    if n==1:return a[0][0]
    if n==2:return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return sum((-1 if j&1 else 1)*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]]) for j in range(n))
assert rank_rat(D) == 5
witness=None
for rows in combinations(range(6),5):
    for cols in combinations(range(8),5):
        value=det([[D[i][j] for j in cols] for i in rows])
        if abs(value)==1:
            witness=(rows,cols,value);break
    if witness:break
assert witness is not None

# Completely independent mod-2 homology verification from original faces.
bydim=defaultdict(list)
for s in faces:
    if s:bydim[s.bit_count()-1].append(s)
def mod2_boundary_rank(d):
    lower={s:i for i,s in enumerate(bydim[d-1])}
    piv={};rank=0
    for s in bydim[d]:
        b=0
        for a,c in bd(s): b ^= 1 << lower[a]
        while b:
            row=b.bit_length()-1
            if row in piv:b^=piv[row]
            else:piv[row]=b;rank+=1;break
    return rank
ranks={d:mod2_boundary_rank(d) for d in range(1,8)}
assert [ranks[d] for d in range(1,8)] == [23,205,907,2135,2712,1937,943]
assert len(bydim[4])-ranks[4]-ranks[5] == 1
assert len(bydim[5])-ranks[5]-ranks[6] == 3

# Independent equivariant Lefschetz calculation via vertex orbits.
# Invariant independent sets are unions of internally edge-free orbits.
# A fixed oriented simplex contributes (-1)^(number_of_orbits+1),
# hence the reduced Lefschetz number is -P(-1) for the orbit conflict graph.
def orbits_of(p):
    unseen=set(range(N));ors=[]
    while unseen:
        v=min(unseen); o=[];w=v
        while w in unseen:
            unseen.remove(w);o.append(w);w=p[w]
        assert w==v
        ors.append(tuple(o))
    return ors

def orbit_lefs(p):
    ors=orbits_of(p)
    masks=[sum(1<<x for x in o) for o in ors]
    usable=[]
    for mask in masks:
        ok=all((ADJ[v]&mask)==0 for v in range(N) if mask>>v&1)
        if ok:usable.append(mask)
    m=len(usable);conf=[0]*m
    for i,mask in enumerate(usable):
        for j in range(i):
            if any((ADJ[v]&usable[j]) for v in range(N) if mask>>v&1):
                conf[i]|=1<<j;conf[j]|=1<<i
    @lru_cache(None)
    def polynom_value(available):
        if not available:return 1
        b=available & -available;i=b.bit_length()-1
        return polynom_value(available^b) - polynom_value(available & ~(b|conf[i]))
    return -polynom_value((1<<m)-1)


def sign_perm(p):return -1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1

def standard_char(p):return sum(p[i]==i for i in range(3))-1

symmetry_checks=0
observations=[]
for reflection in (0,1):
    for shift in range(8):
        for p in permutations(range(3)):
            action=[3*((shift+(-i if reflection else i))%8)+p[c] for i in range(8) for c in range(3)]
            assert set(action)==set(range(N))
            assert all(sum(1<<action[w] for w in range(N) if ADJ[v]>>w&1) == ADJ[action[v]] for v in range(N))
            actual=orbit_lefs(action)
            observations.append((reflection,shift,p,actual))
            alpha=(-1)**shift;beta=(-1)**reflection;sgn=sign_perm(p)
            h4=alpha*beta*sgn
            h5=alpha*(sgn+standard_char(p))
            assert actual == h4-h5, (reflection,shift,p,actual,h4-h5)
            symmetry_checks+=1
assert symmetry_checks == 96
# The rank-one H4 representation must be one of eight characters of the
# abelianization C2 x C2 x C2.  For each choice infer H5 by Lefschetz.
# Since dim H5=3, every trace has absolute value <=3.  Its character
# norm must be in {2,3,5,9}, as D8 x S3 has irreducible dimensions 1,2,4:
# either H5=irreducible(2)+irreducible(1), or three 1D constituents.
candidates=[]
for rotpar in (0,1):
    for refpar in (0,1):
        for colpar in (0,1):
            traces=[]
            for reflect,shift,p,lefs in observations:
                sign_exp = rotpar*shift+refpar*reflect+colpar*(sign_perm(p)==-1)
                h4=(-1)**sign_exp
                traces.append(h4-lefs)
            if max(abs(t) for t in traces)>3:continue
            norm_numer=sum(t*t for t in traces)
            assert norm_numer % 96 == 0
            norm=norm_numer//96
            candidates.append(((rotpar,refpar,colpar),norm))
assert candidates == [((1,1,0),4),((1,1,1),2)]
assert [char for char,norm in candidates if norm in (2,3,5,9)] == [(1,1,1)]
print('C8_K3_CATEGORICAL_PRODUCT_PASS')
print('nonempty_faces=',len(faces)-1, 'face_counts=',[counts[d] for d in range(12)])
print('matching_pairs=',len(up),'acyclic_poset_nodes=',processed)
print('critical_cells=',[(i,len([s for s in critical if s.bit_count()-1==i])) for i in [0,4,5]])
print('morse_D5_to_D4=',D)
print('rational_rank=',rank_rat(D),'unit_minor=',witness)
print('mod2_ranks_degrees_1_to_7=',ranks)
print('H4=Z,H5=Z^3; 96 symmetry characters verified')
print('rank-one character candidates and dimension-three norm test=',candidates)
