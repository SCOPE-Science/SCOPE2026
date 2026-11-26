#!/usr/bin/env python3
import itertools, hashlib, json

N = 5
PERMS = list(itertools.permutations(range(N)))
INDEX = {p:i for i,p in enumerate(PERMS)}
FULL = (1 << len(PERMS)) - 1

def compose(p,q):
    # Standard function composition: (p o q)(i)=p(q(i)).
    return tuple(p[q[i]] for i in range(N))

def cyclic_neighbors(p):
    out=[]
    for i in range(N):
        j=(i+1)%N
        q=list(p)
        q[i],q[j]=q[j],q[i]
        out.append(tuple(q))
    return out

BALLS=[]
BALLMASK=[]
POINT_COLS=[[] for _ in PERMS]
for j,p in enumerate(PERMS):
    b={INDEX[p]}
    b.update(INDEX[q] for q in cyclic_neighbors(p))
    assert len(b)==6
    BALLS.append(b)
    mask=sum(1 << i for i in b)
    BALLMASK.append(mask)
    for i in b:
        POINT_COLS[i].append(j)

CONFLICT=[0]*len(PERMS)
for j in range(len(PERMS)):
    m=0
    for k in range(len(PERMS)):
        if BALLMASK[j] & BALLMASK[k]:
            m |= 1 << k
    CONFLICT[j]=m

solutions=[]
nodes=0

def exact_cover(covered, available, chosen):
    global nodes
    nodes += 1
    if covered == FULL:
        solutions.append(tuple(sorted(chosen)))
        return
    uncovered = FULL ^ covered
    best_cols = None
    best_count = 10**9
    x=uncovered
    while x:
        bit=x & -x
        point=bit.bit_length()-1
        x -= bit
        cols=0
        for j in POINT_COLS[point]:
            if (available >> j) & 1:
                cols |= 1 << j
        count=cols.bit_count()
        if count < best_count:
            best_count=count
            best_cols=cols
            if count <= 1:
                break
    if best_count == 0:
        return
    cols=best_cols
    while cols:
        bit=cols & -cols
        j=bit.bit_length()-1
        cols -= bit
        exact_cover(covered | BALLMASK[j], available & ~CONFLICT[j], chosen+[j])

exact_cover(0, (1 << len(PERMS)) - 1, [])
solutions=sorted(set(solutions))
assert len(solutions)==6
assert all(len(sol)==20 for sol in solutions)

# AGL(1,5), represented as one-line permutations x -> a*x+b mod 5.
A=set()
for a in range(1,5):
    for b in range(5):
        A.add(tuple((a*x+b)%5 for x in range(5)))
assert len(A)==20
assert tuple(range(5)) in A
assert all(compose(x,y) in A for x in A for y in A)

# Distinct left cosets g o A under standard function-composition convention.
cosets=[]
for g in PERMS:
    C=frozenset(compose(g,a) for a in A)
    if C not in cosets:
        cosets.append(C)
assert len(cosets)==6
solsets=[frozenset(PERMS[i] for i in sol) for sol in solutions]
assert set(solsets)==set(cosets)

# Every exact-cover solution is a perfect radius-one code; direct checks included.
for C in solsets:
    cover=0
    for p in C:
        m=BALLMASK[INDEX[p]]
        assert not (cover & m)
        cover |= m
    assert cover==FULL

# The six codes are a single orbit under left multiplication by S5.
def left_translate(g,C):
    return frozenset(compose(g,p) for p in C)
base=frozenset(A)
orbit={left_translate(g,base) for g in PERMS}
assert orbit==set(solsets)
stabilizer=[g for g in PERMS if left_translate(g,base)==base]
assert len(stabilizer)==20
assert set(stabilizer)==A

# A canonical census hash over all six codes.
def pstr(p): return ''.join(str(x) for x in p)
canon=[]
for C in sorted(solsets, key=lambda C: sorted(pstr(p) for p in C)):
    canon.append(sorted(pstr(p) for p in C))
blob=(json.dumps(canon,separators=(',',':'),sort_keys=False)+'\n').encode()
sha=hashlib.sha256(blob).hexdigest()
print('VERIFY_OK vertices=120 ball_size=6 exact_cover_nodes=%d perfect_codes=6 code_size=20 affine_cosets=6 left_orbit=1 stabilizer=20 census_sha256=%s' % (nodes, sha))
