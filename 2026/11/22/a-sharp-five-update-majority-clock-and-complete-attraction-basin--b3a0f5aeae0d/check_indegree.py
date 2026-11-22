"""Independent functional-graph certificate for Tietze majority dynamics.

Constructs the graph via a Petersen vertex-to-triangle expansion, then
peels transient vertices by indegree. Run: python3 check_indegree.py.
"""
from collections import Counter, deque
import json

# The Petersen graph in two pentagonal layers (outer 0...4, inner 5...9).
pet_edges = set()
for i in range(5):
    pet_edges.add(tuple(sorted((i, (i + 1) % 5))))
    pet_edges.add(tuple(sorted((i, i + 5))))
    pet_edges.add(tuple(sorted((i + 5, 5 + (i + 2) % 5))))
assert len(pet_edges) == 15

# Remove old vertex 0; replace with triangle (new 9, 10, 11), connecting
# these three corners to former neighbors old 1, 4, 5 respectively.
rename = {old: old - 1 for old in range(1, 10)}
edges = {tuple(sorted((rename[a], rename[b]))) for a,b in pet_edges if a != 0 and b != 0}
for corner, old_neighbor in enumerate((1, 4, 5), start=9):
    edges.add(tuple(sorted((corner, rename[old_neighbor]))))
for a,b in ((9,10),(10,11),(9,11)):
    edges.add((a,b))
assert len(edges) == 18

neighbors = [0] * 12
for a,b in edges:
    neighbors[a] |= 1<<b
    neighbors[b] |= 1<<a
assert [m.bit_count() for m in neighbors] == [3]*12

SIZE = 1<<12
next_state = [0]*SIZE
for x in range(SIZE):
    # Uses bitwise masks and bit_count, independently of direct checker.
    next_state[x] = sum(1<<i for i, m in enumerate(neighbors) if (x&m).bit_count() >= 2)
assert all(next_state[next_state[next_state[next_state[next_state[next_state[next_state[x]]]]]]] ==
           next_state[next_state[next_state[next_state[next_state[x]]]]] for x in range(SIZE))
assert any(next_state[next_state[next_state[next_state[next_state[next_state[x]]]]]] !=
           next_state[next_state[next_state[next_state[x]]]] for x in range(SIZE))

indegree = [0]*SIZE
for y in next_state:indegree[y]+=1
queue = deque(i for i, d in enumerate(indegree) if d == 0)
removed = []
while queue:
    x = queue.popleft()
    removed.append(x)
    y = next_state[x]
    indegree[y]-=1
    if indegree[y] == 0:
        queue.append(y)

root = [-1]*SIZE
depth = [-1]*SIZE
period = [-1]*SIZE
cycles = []
for start in range(SIZE):
    if indegree[start] == 0 or root[start] >= 0:
        continue
    c = []
    y = start
    while root[y] < 0:
        root[y] = len(cycles)
        c.append(y)
        y = next_state[y]
    assert y == start
    cycles.append(tuple(c))
    for y in c:
        depth[y] = 0
        period[y] = len(c)
for x in reversed(removed):
    y = next_state[x]
    root[x] = root[y]
    depth[x] = depth[y]+1
    period[x] = period[y]
assert all(z>=0 for z in root+depth+period)

population = Counter(zip(depth,period))
basin = Counter(root)
bh = Counter((len(cycles[id]), sz) for id,sz in basin.items())
result = {
    'orbit_counts': dict(sorted(Counter(map(len, cycles)).items())),
    'entry_period': {f'{t},{p}':c for (t,p),c in sorted(population.items())},
    'basin_hist': {f'{p},{s}':c for (p,s),c in sorted(bh.items())},
    'max_depth': max(depth),
    'slow_count': sum(v==5 for v in depth),
    'consensus_basins': (basin[root[0]], basin[root[SIZE-1]]),
}
assert result['orbit_counts'] == {1:16,2:137}
assert result['max_depth'] == 5 and result['slow_count'] == 288
assert result['consensus_basins'] == (776,776)
assert result['entry_period'] == {'0,1': 16, '0,2': 274, '1,1': 136, '1,2': 994,
 '2,1': 492, '2,2': 708, '3,1': 360, '3,2': 252, '4,1': 432, '4,2': 144,
 '5,1': 216, '5,2': 72}
assert result['basin_hist'] == {'1,2': 12, '1,38': 2, '1,776': 2,
 '2,2': 6, '2,4': 12, '2,6': 18, '2,8': 36, '2,12': 18, '2,14': 18,
 '2,40': 18, '2,70': 6, '2,76': 5}
print(json.dumps(result, sort_keys=True))
print('INDEGREE_CHECK_PASSED')
