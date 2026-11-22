"""Exact 14-spin majority-absorption census on the Fano incidence graph.

Run: python3 check_cyclic.py. No third-party dependencies.
"""
from collections import Counter
from fractions import Fraction
from math import comb

LINES = [tuple(sorted({i, (i + 1) % 7, (i + 3) % 7})) for i in range(7)]
assert len(set(LINES)) == 7
neighbors = [[] for _ in range(14)]
for j, line in enumerate(LINES):
    for i in line:
        neighbors[i].append(7+j)
        neighbors[7+j].append(i)
assert all(len(v) == 3 for v in neighbors)
masks = [sum(1 << j for j in row) for row in neighbors]
N = 1 << 14
succ = [[] for _ in range(N)]
cut = [0] * N
for s in range(N):
    cut[s] = sum(((s >> u) & 1) != ((s >> v) & 1)
                 for u in range(14) for v in neighbors[u] if u < v)
    for u in range(14):
        k = (s & masks[u]).bit_count()
        if (s >> u) & 1:
            if k <= 1:
                succ[s].append(s ^ (1 << u))
        elif k >= 2:
            succ[s].append(s ^ (1 << u))

assert all(cut[t] < cut[s] for s in range(N) for t in succ[s])
stable = [s for s in range(N) if not succ[s]]
assert Counter(s.bit_count() for s in stable) == {0: 1, 6: 28, 8: 28, 14: 1}
assert Counter(cut[s] for s in stable) == {0: 2, 6: 56}

prob = [None] * N
for s in sorted(range(N), key=lambda x: cut[x]):
    if not succ[s]:
        prob[s] = Fraction(int(s != 0 and s != N-1))
    else:
        assert all(prob[t] is not None for t in succ[s])
        prob[s] = sum((prob[t] for t in succ[s]), Fraction(0)) / len(succ[s])
assert all(0 <= x <= 1 for x in prob)
assert all(prob[s] == prob[(N-1)^s] for s in range(N))

B = [sum((prob[s] for s in range(N) if s.bit_count() == k), Fraction(0))
     for k in range(15)]
assert B[0] == B[1] == B[2] == B[12] == B[13] == B[14] == 0
assert B[3] == B[11] == Fraction(56, 15)
assert B[4] == B[10] == Fraction(169130641, 2083725)
assert B[5] == B[9] == Fraction(532194282778777, 1215630281250)
assert B[6] == B[8] == Fraction(3691264645924565219, 3413489829750000)
assert B[7] == Fraction(17228285644177485821, 11947214404125000)
assert Counter(prob[s] for s in range(N) if s.bit_count() == 3) == {Fraction(0): 308, Fraction(1,15): 56}
line_point_masks = [sum(1<<i for i in line) for line in LINES]
def noncollinear_same_shore(s):
    if s.bit_count() != 3:
        return False
    if s >> 7 == 0:
        return s not in line_point_masks
    if s & 127 == 0:
        # Three lines are concurrent exactly when a point is incident with all of them.
        return not any(sum(bool(s & (1 << (7+j))) for j,line in enumerate(LINES) if i in line) == 3
                       for i in range(7))
    return False
assert all((prob[s] > 0) == noncollinear_same_shore(s)
           for s in range(N) if s.bit_count() == 3)

C = (Fraction(56,15), Fraction(106896721,2083725),
     Fraction(216605875348939,8509411968750),
     Fraction(4672732892864737,4778885761650000))
def predicted(p):
    q = p * (1-p)
    return q**3 * sum((c * q**j for j,c in enumerate(C)), Fraction(0))
def from_bernstein(p):
    return sum((v * p**k * (1-p)**(14-k) for k,v in enumerate(B)), Fraction(0))
# Both are degree at most 14, so agreement at 15 distinct rational points is an exact identity.
assert all(predicted(Fraction(j,14)) == from_bernstein(Fraction(j,14)) for j in range(15))
qhalf = from_bernstein(Fraction(1,2))
assert qhalf == Fraction(27778302334027926533, 97871580398592000000)
print('PASS: 16384 states, 58 stable (56 mixed), 56 rare three-spin seeds (probability 1/15 each)')
print('P_mixed(1/2) =', qhalf)
print('Bernstein coefficients =', [str(x) for x in B])
print('q^3 times coefficients =', [str(x) for x in C])
