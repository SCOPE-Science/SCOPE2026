#!/usr/bin/env python3
"""Exact finite certificate for the geometric symmetry quotients of a grid matching complex.

Uses only the Python standard library. All linear algebra is exact over F_2.
"""
from collections import Counter, defaultdict, deque

ROWS, COLS = 3, 4
EDGES = (
    [tuple(sorted(((r,c),(r+1,c)))) for r in range(ROWS-1) for c in range(COLS)] +
    [tuple(sorted(((r,c),(r,c+1)))) for r in range(ROWS) for c in range(COLS-1)]
)
EDGE_INDEX = {e:i for i,e in enumerate(EDGES)}
assert len(EDGES) == len(EDGE_INDEX) == 17
EDGE_MASKS = [sum(1<<(r*COLS+c) for r,c in e) for e in EDGES]

def edge_permutation(f):
    return tuple(EDGE_INDEX[tuple(sorted(f(vertex) for vertex in e))] for e in EDGES)

IDENTITY = tuple(range(17))
ROW = edge_permutation(lambda v:(ROWS-1-v[0],v[1]))
COLUMN = edge_permutation(lambda v:(v[0],COLS-1-v[1]))
HALF_TURN = tuple(COLUMN[ROW[i]] for i in IDENTITY)
assert all(p[12] == 12 for p in (IDENTITY, ROW, COLUMN, HALF_TURN))  # center horizontal edge
assert tuple(ROW[COLUMN[i]] for i in IDENTITY) == HALF_TURN
assert all(ROW[ROW[i]] == COLUMN[COLUMN[i]] == HALF_TURN[HALF_TURN[i]] == i for i in IDENTITY)
GROUPS = {
    'row': (IDENTITY, ROW),
    'column': (IDENTITY, COLUMN),
    'half_turn': (IDENTITY, HALF_TURN),
    'full': (IDENTITY, ROW, COLUMN, HALF_TURN),
}

# Enumerate exactly all pairwise vertex-disjoint nonempty edge subsets.
all_faces = [0]
for i,edge in enumerate(EDGE_MASKS):
    all_faces += [f | (1<<i) for f in all_faces
                  if all((EDGE_MASKS[j] & edge) == 0
                         for j in range(17) if (f>>j)&1)]
FACES = tuple(sorted((f for f in all_faces if f), key=lambda f:(f.bit_count(),f)))
FACE_SET = set(FACES)
assert len(FACES)==822
assert [sum(f.bit_count()==j for f in FACES) for j in range(1,7)] == [17,102,267,302,123,11]

def act(face,p):
    answer=0
    while face:
        least = face & -face
        answer |= 1 << p[least.bit_length()-1]
        face ^= least
    return answer

for p in GROUPS['full']:
    assert {act(f,p) for f in FACES} == FACE_SET

# Explicit acyclic Forman matching on the ORIGINAL complex.
# Every matching is made along an inclusion f < f union {pivot}.
PIVOT_ORDER = (5,12,6,7,13,8,9,10,4,3,14,15,11,1,0,16,2)
unmatched=set(FACES)
matching=set()
for i in PIVOT_ORDER:
    for f in sorted(tuple(unmatched)):
        if f not in unmatched or (f >> i)&1:
            continue
        g=f | (1<<i)
        if g in unmatched:
            unmatched.remove(f)
            unmatched.remove(g)
            matching.add((f,g))
assert len(matching)==406
assert Counter(f.bit_count()-1 for f in unmatched) == {0:1,3:9}

# Verify global acyclicity, rather than assuming sequential pairing is acyclic.
out=defaultdict(list)
indegree=Counter()
incidences=0
for f in FACES:
    for i in IDENTITY:
        if (f>>i)&1:continue
        g=f | (1<<i)
        if g not in FACE_SET:continue
        incidences+=1
        a,b = (f,g) if (f,g) in matching else (g,f)
        out[a].append(b)
        indegree[b]+=1
queue=deque(f for f in FACES if indegree[f]==0)
processed=0
while queue:
    f=queue.popleft()
    processed+=1
    for g in out[f]:
        indegree[g]-=1
        if indegree[g]==0:queue.append(g)
assert processed==len(FACES)

# Enumerate every nonempty flag in the face poset (barycentric subdivision).
flags_ending={}
for mask in FACES:
    flags={(mask,)}
    sub=(mask-1)&mask
    while sub:
        if sub in flags_ending:
            flags.update(chain+(mask,) for chain in flags_ending[sub])
        sub=(sub-1)&mask
    flags_ending[mask]=flags
ALL_FLAGS=tuple(ch for part in flags_ending.values() for ch in part)
assert len(ALL_FLAGS)==144500

def quotient_data(perms):
    def canonical(chain):
        return min(tuple(act(f,p) for f in chain) for p in perms)
    levels=[set() for _ in range(6)]
    for chain in ALL_FLAGS:
        levels[len(chain)-1].add(canonical(chain))
    cells=[{chain:i for i,chain in enumerate(sorted(lev))} for lev in levels]
    fv=tuple(len(lev) for lev in levels)
    boundaries=[None]
    ranks=[]
    for dimension in range(1,6):
        cols=[]
        pivots={}
        for chain in cells[dimension]:
            col=0
            for omitted in range(len(chain)):
                sub=canonical(chain[:omitted]+chain[omitted+1:])
                col ^= 1<<cells[dimension-1][sub]
            cols.append(col)
            reduced=col
            while reduced:
                lead=reduced.bit_length()-1
                if lead in pivots:
                    reduced ^= pivots[lead]
                else:
                    pivots[lead]=reduced
                    break
        boundaries.append(cols)
        ranks.append(len(pivots))
    # Independently test d^2=0 for all orbit-chain generators.
    for dimension in range(2,6):
        prior=boundaries[dimension-1]
        for column in boundaries[dimension]:
            total=0
            while column:
                least=column&-column
                total ^= prior[least.bit_length()-1]
                column ^= least
            assert total==0
    betti=tuple(fv[i] - (ranks[i-1] if i else 0) -
                (ranks[i] if i<5 else 0) for i in range(6))
    return fv,tuple(ranks),betti

EXPECTED = {
    'row': (
        (423,5239,18468,26976,17280,3960),
        (422,4817,13651,13320,3960),
        (1,0,0,5,0,0)),
    'column': (
        (444,5331,18576,27012,17280,3960),
        (443,4888,13688,13320,3960),
        (1,0,0,4,0,0)),
    'half_turn': (
        (429,5246,18456,26964,17280,3960),
        (428,4818,13638,13320,3960),
        (1,0,0,6,0,0)),
    'full': (
        (237,2705,9318,13512,8640,1980),
        (236,2469,6849,6660,1980),
        (1,0,0,3,0,0)),
}
print('original_faces=',[17,102,267,302,123,11])
print('original_morse_pairs=',len(matching),'critical=',dict(Counter(f.bit_count()-1 for f in unmatched)),
      'acyclic=',processed == len(FACES),'incidences=',incidences)
print('barycentric_flags=',len(ALL_FLAGS))
for name,perms in GROUPS.items():
    result=quotient_data(perms)
    assert result==EXPECTED[name], (name,result)
    fv,ranks,betti=result
    euler=sum((-1)**i*n for i,n in enumerate(fv))
    assert euler==1-betti[3]
    print(name,'quotient_faces=',list(fv),'mod2_boundary_ranks=',list(ranks),
          'mod2_betti=',list(betti),'euler=',euler,'boundary_squared_zero=YES')
# Independently calculate the Lefschetz character on the original chain groups.
for name in ('row','column','half_turn'):
    p=GROUPS[name][1]
    reduced_chain_lefschetz=-1
    for f in FACES:
        if act(f,p)!=f:continue
        arr=[i for i in IDENTITY if f>>i&1]
        permuted=[p[i] for i in arr]
        parity=sum(a>b for j,a in enumerate(permuted) for b in permuted[j+1:])
        reduced_chain_lefschetz+=(-1)**(len(arr)-1+parity)
    trace_on_h3=-reduced_chain_lefschetz
    assert trace_on_h3=={'row':1,'column':-1,'half_turn':3}[name]
    print(name,'trace_on_H3=',trace_on_h3)
print('ALL_VERIFY_OK')
