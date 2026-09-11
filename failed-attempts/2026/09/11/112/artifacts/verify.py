"""Replay verifier for lane-974 TARGET claim (stdlib only).
Replays: commutation, group order 64, -I absent, Shor-Laflamme A/B enumerators,
MacWilliams identities, distance 3, wmin=4 with 4 unique-support stabilizers,
and exhaustive elimination of all 3^8 Clifford-axis frames via mismatch lemma.
Prints VERIFY_OK on success.
"""
import itertools
import math

I, X, Y, Z = 0, 1, 2, 3
N = 8

def xz(p):
    return {0: (0, 0), 1: (1, 0), 2: (1, 1), 3: (0, 1)}[p]

def symp(a, b):
    s = 0
    for i in range(N):
        xa, za = xz(a[i])
        xb, zb = xz(b[i])
        s += xa * zb + xb * za
    return s % 2

def pmul(a, b):
    t = []
    for i in range(N):
        xa, za = xz(a[i])
        xb, zb = xz(b[i])
        x, z = xa ^ xb, za ^ zb
        t.append({(0, 0): 0, (1, 0): 1, (1, 1): 2, (0, 1): 3}[(x, z)])
    return tuple(t)

def wt(p):
    return sum(1 for q in p if q != 0)

GENS = [
    (1, 1, 0, 0, 3, 3, 0, 2),
    (1, 2, 3, 2, 0, 0, 1, 3),
    (2, 1, 0, 0, 0, 1, 1, 0),
    (1, 2, 0, 3, 3, 3, 2, 3),
    (2, 2, 2, 0, 3, 0, 2, 2),
    (3, 2, 3, 0, 1, 3, 2, 3),
]

# 1. commutation
for a, b in itertools.combinations(GENS, 2):
    assert symp(a, b) == 0
print("commutation OK")

# 2. group
grp = {tuple([0] * N)}
for g in GENS:
    grp = grp | {pmul(t, g) for t in grp}
assert len(grp) == 64
print("group order 64 OK")

# 3. enumerators
A = [0] * 9
for t in grp:
    A[wt(t)] += 1
assert A == [1, 0, 0, 0, 4, 12, 24, 20, 3], A
print("A =", A)
norm = []
for code in range(4 ** N):
    p = []
    c = code
    for _ in range(N):
        p.append(c % 4)
        c //= 4
    p = tuple(p)
    if all(symp(p, g) == 0 for g in GENS):
        norm.append(p)
assert len(norm) == 1024
B = [0] * 9
for p in norm:
    B[wt(p)] += 1
assert B == [1, 0, 0, 28, 86, 216, 320, 268, 105], B
print("B =", B)
for j in range(9):
    s = sum(((-1) ** u) * (3 ** (j - u)) * math.comb(i, u)
            * math.comb(N - i, j - u) * A[i]
            for i in range(9) for u in range(9)
            if 0 <= u <= i and 0 <= j - u <= N - i)
    assert s % 64 == 0 and s // 64 == B[j], j
print("MacWilliams OK")
assert min(w for w in range(1, 9) if A[w] != B[w]) == 3
print("distance 3 OK")

# 4. unique-support min-weight stabilizers
nonI = [t for t in grp if any(q != 0 for q in t)]
assert min(wt(t) for t in nonI) == 4
supps = {}
for t in nonI:
    if wt(t) == 4:
        supps.setdefault(tuple(i for i in range(N) if t[i] != 0), []).append(t)
assert len(supps) == 4 and all(len(v) == 1 for v in supps.values()), supps
uniq = [v[0] for v in supps.values()]
print("4 unique-support weight-4 stabilizers OK:", sorted(supps))

# 5. exhaustive frame elimination
n_surv = 0
for axes in itertools.product([X, Y, Z], repeat=N):
    killed = any(sum(1 for i in range(N) if s[i] != 0 and s[i] != axes[i]) >= 1
                 for s in uniq)
    if not killed:
        n_surv += 1
assert n_surv == 0
print("3^8 frames eliminated: 6561/6561, survivors 0")
print("VERIFY_OK")
