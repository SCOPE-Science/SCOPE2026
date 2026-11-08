"""Exact integer checks for the nine-ray toric fan and its obstructing triple."""
from itertools import product

rays = [(1, 0), (0, 1), (-1, 1), (-2, 1), (-3, 1),
        (-1, 0), (1, -1), (3, -2), (2, -1)]
A = (1, 4, 7)

def det(u, v):
    return u[0]*v[1] - u[1]*v[0]

assert len(rays) == 9
assert [det(rays[i], rays[(i+1) % 9]) for i in range(9)] == [1]*9
assert [det(rays[A[i]], rays[A[(i+1) % 3]]) for i in range(3)] == [3]*3
assert [((A[(i+1) % 3]-A[i]-1) % 9) for i in range(3)] == [2, 2, 2]
assert rays[A[0]][0] + rays[A[1]][0] + rays[A[2]][0] == 0
assert rays[A[0]][1] + rays[A[1]][1] + rays[A[2]][1] == 0

count = 0
for a, b in product(range(-25, 26), repeat=2):
    if (a, b) == (0, 0):
        continue
    v = [a*rays[i][0]+b*rays[i][1] for i in A]
    assert sum(v) == 0
    assert len({v[0] % 3, v[1] % 3, v[2] % 3}) == 1
    assert min(sum(max(x,0) for x in v),sum(max(-x,0) for x in v)) >= 2
    count += 1
print('NINE_RAY_FAN_OK', len(rays), 'TRIPLE_GAPS_OK', 'INTEGER_TESTS_OK', count)
print('UNBOUNDED_IDEAL_CONTAINMENT_REQUIRES_THE_WRITTEN_CONGRUENCE_PROOF')
