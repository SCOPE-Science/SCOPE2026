"""Independent Heawood edge-domination census using Fano difference sets.
Run: python3 verify_cyclic.py
"""
from array import array
from collections import Counter, deque

# A difference-set presentation of the Fano plane, independent of binary dot products.
lines = [{j % 7, (j + 1) % 7, (j + 3) % 7} for j in range(7)]
assert all(len(x) == 3 for x in lines)
assert all(sum(p in l for l in lines) == 3 for p in range(7))
assert all(sum(p in l and q in l for l in lines) == 1
           for p in range(7) for q in range(p+1, 7))
edges = [(p, j) for p in range(7) for j in range(7) if p in lines[j]]
assert len(edges) == 21
m = 21; N = 1 << m
ends = [(1 << p) | (1 << (7+j)) for p,j in edges]
# A vertex set C covers every graph edge iff its complement is independent.
covered_ok = bytearray(1 << 14)
for C in range(1 << 14):
    covered_ok[C] = all(C & ends[i] for i in range(m))
cover = array('H', [0]) * N
for mask in range(1, N):
    b = mask & -mask
    cover[mask] = cover[mask ^ b] | ends[b.bit_length()-1]

all_counts = Counter(); minimal = Counter(); maximal_matchings = Counter(); opt=[]
for mask in range(N):
    C = cover[mask]
    if not covered_ok[C]:
        continue
    k = mask.bit_count()
    all_counts[k] += 1
    # Minimality: removing ANY edge must expose a previously uncovered graph edge.
    if all(not covered_ok[cover[mask ^ (1<<i)]]
           for i in range(m) if mask >> i & 1):
        minimal[k] += 1
    # For a matching, endpoints of different selected edges are disjoint.
    if C.bit_count() == 2*k:
        maximal_matchings[k] += 1
    if k == 5:
        opt.append(mask)

assert minimal == {5:42,6:1246,7:24}, minimal
assert maximal_matchings == {5:42,6:168,7:24}, maximal_matchings
assert len(opt) == 42
# Every five-edge optimum is a matching, and each uncovered point pair has 2 optima.
assert all(cover[s].bit_count() == 10 for s in opt)
spare_pairs=Counter()
for s in opt:
    untouched = [p for p in range(7) if not (cover[s] >> p) & 1]
    spare_pairs[tuple(untouched)] += 1
assert len(spare_pairs) == 21 and set(spare_pairs.values()) == {2}

# Swapping r edges means Hamming distance exactly 2r between size-five edge masks.
move_dist = Counter((a ^ b).bit_count() // 2
                    for i,a in enumerate(opt) for b in opt[i+1:])
assert move_dist == {2:84,3:84,4:525,5:168}, move_dist
adj = [[j for j,t in enumerate(opt) if j != i and (s ^ t).bit_count() == 4]
       for i,s in enumerate(opt)]
assert all(len(row) == 4 for row in adj)
profiles=[]
for root in range(len(opt)):
    distances={root:0}; pending=deque([root])
    while pending:
        u=pending.popleft()
        for v in adj[u]:
            if v not in distances:
                distances[v] = distances[u]+1
                pending.append(v)
    assert len(distances) == 42
    profiles.append(tuple(Counter(distances.values()).get(i,0) for i in range(6)))
assert set(profiles) == {(1,4,8,16,12,1)}, set(profiles)
print('ALL_EDGE_DOMINATION_COUNTS', sorted(all_counts.items()))
print('INCLUSION_MINIMAL_COUNTS', sorted(minimal.items()))
print('MAXIMAL_MATCHING_COUNTS', sorted(maximal_matchings.items()))
print('OPTIMAL_SPARE_PAIRS', len(spare_pairs), 'MULTIPLICITY', 2)
print('TWO_EDGE_EXCHANGE: 42 vertices, 84 edges, 4-regular, diameter 5')
print('DISTANCE_PROFILE', profiles[0]);print('VERIFY_CYCLIC_OK')
