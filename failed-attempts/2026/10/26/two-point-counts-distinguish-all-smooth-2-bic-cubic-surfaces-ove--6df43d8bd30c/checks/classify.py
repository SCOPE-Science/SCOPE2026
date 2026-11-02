"""Exhaustive congruence-orbit and point-count verification for binary 2-bic cubic surfaces."""
from collections import deque
from itertools import product

N = 4

def rank(rows):
    r = 0
    rows = list(rows)
    for c in range(N):
        piv = next((i for i in range(r, N) if rows[i] & (1 << c)), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(N):
            if i != r and (rows[i] & (1 << c)):
                rows[i] ^= rows[r]
        r += 1
    return r

def elementary_congruence(A, i, j):
    """G=I+E_ij, A -> G^t A G, for i != j."""
    b = list(A)
    for k in range(N):
        if b[k] & (1 << i):
            b[k] ^= 1 << j
    b[j] ^= b[i]
    return tuple(b)

def pair(A, u, v):
    return sum(((A[i] & v).bit_count() & 1)
               for i in range(N) if (u >> i) & 1) & 1

def counts(A):
    n1 = sum(pair(A, u, u) == 0 for u in range(1, 16))
    total = 0
    for u, v in product(range(16), repeat=2):
        if u == v == 0:
            continue
        c = pair(A, u ^ v, u) ^ pair(A, v, v)
        d = pair(A, u ^ v, v) ^ pair(A, v, u) ^ pair(A, v, v)
        total += c == d == 0
    assert total % 3 == 0
    return n1, total // 3

all_forms = {tuple((bits >> (4 * i)) & 15 for i in range(4))
             for bits in range(65536)
             if rank(tuple((bits >> (4 * i)) & 15 for i in range(4))) == 4}
assert len(all_forms) == 20160
reps = []
while all_forms:
    rep = min(all_forms)
    q = deque([rep]); orbit = {rep}; all_forms.remove(rep)
    while q:
        A = q.popleft()
        for i in range(4):
            for j in range(4):
                if i == j: continue
                B = elementary_congruence(A, i, j)
                if B not in orbit:
                    assert B in all_forms
                    orbit.add(B); all_forms.remove(B); q.append(B)
    reps.append((rep, len(orbit), counts(rep)))
assert len(reps) == 10
assert sum(k for _, k, _ in reps) == 20160
assert len({sig for _, _, sig in reps}) == 10
assert len({sig[0] for _, _, sig in reps}) < 10
for i, (r, k, (n1, n2)) in enumerate(reps):
    assert 20160 % k == 0
    print(i, ','.join(map(str, r)), 'orbit', k, 'stabilizer', 20160//k, 'N1', n1, 'N2', n2)
print('PASS: ten complete congruence orbits; distinct (N1,N2); N1 not injective')
