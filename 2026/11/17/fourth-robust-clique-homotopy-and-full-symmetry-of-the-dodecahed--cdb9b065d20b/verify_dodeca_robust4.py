"""Exact finite verification of the fourth robust clique complex of GP(10,2).
Python 3 standard library only; every face and automorphism is reconstructed.
"""
from array import array
from collections import Counter, defaultdict, deque

N = 20
edges = set()
for i in range(10):
    for x,y in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)):
        edges.add(tuple(sorted((x,y))))
assert len(edges) == 30
nb = [0] * N
for a,b in edges:
    nb[a] |= 1 << b
    nb[b] |= 1 << a
assert all(x.bit_count() == 3 for x in nb)

# Exact maximum independent-set sizes, clipped at four.
alpha = array('B', [0]) * (1 << N)
faces = []
by_dimension = defaultdict(list)
for mask in range(1, 1 << N):
    bit = mask & -mask
    vertex = bit.bit_length() - 1
    shorter = mask ^ bit
    alpha[mask] = min(4, max(alpha[shorter], 1 + alpha[shorter & ~nb[vertex]]))
    if alpha[mask] < 4:
        faces.append(mask)
        by_dimension[mask.bit_count()-1].append(mask)
face_vector = tuple(len(by_dimension[d]) for d in range(7))
assert face_vector == (20,190,1140,3335,4632,2660,240)
assert len(faces) == 12217
print('faces', len(faces), 'f_vector', face_vector)

# Sequential coordinate matching, with globally disjoint pairs.
remaining = set(faces)
pairs = set()
for vertex in range(N):
    bit = 1 << vertex
    for lower in tuple(remaining):
        upper = lower | bit
        if not (lower & bit) and upper in remaining:
            remaining.remove(lower)
            remaining.remove(upper)
            pairs.add((lower, upper))
critical = Counter(mask.bit_count()-1 for mask in remaining)
assert len(pairs) == 6031
assert critical == {0:1, 5:154}
print('matching_pairs',len(pairs),'critical',sorted(critical.items()))

# Every Hasse cover: reverse a matched cover and verify acyclicity.
indegree = {mask:0 for mask in faces}
forward = defaultdict(list)
cover_count = 0
for upper in faces:
    sub = upper
    while sub:
        bit = sub & -sub
        sub ^= bit
        lower = upper ^ bit
        if not lower:
            continue
        if (lower, upper) in pairs:
            start, end = lower, upper
        else:
            start, end = upper, lower
        forward[start].append(end)
        indegree[end] += 1
        cover_count += 1
queue = deque(mask for mask in faces if indegree[mask] == 0)
visited = 0
while queue:
    x = queue.popleft()
    visited += 1
    for y in forward[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            queue.append(y)
assert visited == len(faces)
assert cover_count == 57940
print('hasse_covers',cover_count,'topological_order_visited',visited)

# Independent F_2 chain-rank corroboration: not the integral proof.
ranks = {}
for d in range(1,7):
    row = {m:i for i,m in enumerate(by_dimension[d-1])}
    pivots = {}
    for upper in by_dimension[d]:
        mask = upper
        vec = 0
        while mask:
            bit = mask & -mask
            mask ^= bit
            vec ^= 1 << row[upper ^ bit]
        while vec:
            top = vec.bit_length() - 1
            if top not in pivots:
                pivots[top] = vec
                break
            vec ^= pivots[top]
    ranks[d] = len(pivots)
assert tuple(ranks[d] for d in range(1,7)) == (19,171,969,2366,2266,240)
print('mod2_boundary_ranks',tuple(ranks[d] for d in range(1,7)))

# Automorphism backtracking: each assignment preserves all assigned adjacencies.
permutations=[]
assignment=[-1]*N

def search_aut(used, assigned_count):
    if assigned_count == N:
        permutations.append(tuple(assignment))
        return
    unassigned = [i for i in range(N) if assignment[i] < 0]
    vertex = max(unassigned, key=lambda i:(sum((nb[i] >> j)&1 for j in range(N) if assignment[j] >= 0), -i))
    constraints = [(j,assignment[j], (nb[vertex] >> j) & 1) for j in range(N) if assignment[j]>=0]
    for target in range(N):
        if (used >> target)&1:
            continue
        if all(((nb[target] >> image) & 1) == edge for _, image, edge in constraints):
            assignment[vertex] = target
            search_aut(used | (1<<target), assigned_count + 1)
            assignment[vertex] = -1

search_aut(0,0)
assert len(permutations)==120
print('automorphisms',len(permutations))

# Signed Lefschetz trace for all 120 permutations; homology lies only in degree 5.
def orientation_sign(image_list):
    parity=0
    for i in range(len(image_list)):
        a=image_list[i]
        for b in image_list[i+1:]:
            parity ^= (a > b)
    return 1 if parity == 0 else -1

def lefschetz_character(perm):
    trace=1  # reduced alternating trace includes empty face with value -1
    for mask in faces:
        mapped_mask=0
        image_list=[]
        remaining_mask=mask
        while remaining_mask:
            bit=remaining_mask & -remaining_mask
            remaining_mask ^= bit
            image=perm[bit.bit_length()-1]
            mapped_mask |= 1 << image
            image_list.append(image)
        if mapped_mask==mask:
            trace -= (-1 if mask.bit_count()%2 == 0 else 1) * orientation_sign(image_list)
    return trace

def cycle_type(perm):
    seen=set(); lengths=[]
    for i in range(N):
        if i in seen: continue
        v=i; length=0
        while v not in seen:
            seen.add(v); length+=1; v=perm[v]
        lengths.append(length)
    return tuple(sorted(lengths,reverse=True))

by_type=defaultdict(Counter)
chars=[]
for perm in permutations:
    c=lefschetz_character(perm)
    chars.append(c)
    by_type[cycle_type(perm)][c] += 1
assert Counter(chars)==Counter({154:1,-10:15,-6:15,6:1,4:20,0:20,-1:24,1:24})
assert sum(chars)==0
central = [permutations[i] for i,c in enumerate(chars) if c == 6]
assert len(central) == 1 and all(
    all(central[0][other[j]] == other[central[0][j]] for j in range(N))
    for other in permutations
)
print('central_involution_verified', True)
print('automorphism_cycle_type_characters',sorted(((k,sorted(v.items())) for k,v in by_type.items()),key=lambda x:x[0]))
print('full_symmetry_invariants',sum(chars)//len(chars))
print('DODECA_ROBUST4_EXACT_PASS')
