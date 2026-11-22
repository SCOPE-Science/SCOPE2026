"""Exhaustive exact certificate for the type-F4 Schubert Betti-duality defect.

Requires only Python 3 standard library. All arithmetic is integral. Executes
without data files or third-party packages. The group is given in the basis
of simple roots. Run: python3 verify_f4.py
"""
from collections import deque, Counter

C = ((2, -1, 0, 0),
     (-1, 2, -2, 0),
     (0, -1, 2, -1),
     (0, 0, -1, 2))
I = tuple(int(i == j) for i in range(4) for j in range(4))

def product(a, b):
    return tuple(sum(a[4*i+k]*b[4*k+j] for k in range(4))
                 for i in range(4) for j in range(4))

def matvec(a, v):
    return tuple(sum(a[4*i+j]*v[j] for j in range(4)) for i in range(4))

S = []
for k in range(4):
    a = list(I)
    for j in range(4):
        a[4*k+j] -= C[j][k]
    S.append(tuple(a))
assert all(product(s, s) == I for s in S)

# Breadth-first Cayley traversal: the first word at each group matrix is reduced.
word = {I: ()}
queue = deque([I])
while queue:
    a = queue.popleft()
    for j, s in enumerate(S):
        b = product(a, s)
        if b not in word:
            word[b] = word[a] + (j,)
            queue.append(b)
assert len(word) == 1152
W = sorted(word, key=lambda a: (len(word[a]), word[a]))
where = {a: i for i, a in enumerate(W)}
length = [len(word[a]) for a in W]
assert max(length) == 24 and length.count(24) == 1
right = [[where[product(a, s)] for s in S] for a in W]

# Independent length test: each root lies in exactly one of the positive
# and negative root cones. Word length counts positive roots sent negative.
roots = set()
queue = deque(tuple(int(i == j) for i in range(4)) for j in range(4))
while queue:
    a = queue.popleft()
    if a in roots:
        continue
    roots.add(a)
    for s in S:
        queue.append(matvec(s, a))
positive = [a for a in roots if all(v >= 0 for v in a)]
assert len(roots) == 48 and len(positive) == 24
for i, a in enumerate(W):
    negatives = 0
    for r in positive:
        z = matvec(a, r)
        if all(v <= 0 for v in z):
            negatives += 1
        else:
            assert all(v >= 0 for v in z)
    assert negatives == length[i]

# Subword theorem: x <= w in Bruhat order iff some subword of any reduced
# expression of w equals x. Bitsets encode all subexpressions, not samples.
P = []
for a in W:
    mask = 1    # identity has index zero
    for letter in word[a]:
        updated = mask
        scan = mask
        while scan:
            low_bit = scan & -scan
            j = low_bit.bit_length() - 1
            updated |= 1 << right[j][letter]
            scan ^= low_bit
        mask = updated
    coefficients = [0] * (len(word[a]) + 1)
    scan = mask
    while scan:
        low_bit = scan & -scan
        j = low_bit.bit_length() - 1
        coefficients[length[j]] += 1
        scan ^= low_bit
    P.append(tuple(coefficients))

# All group elements occur beneath the unique longest element; the full
# Poincare polynomial is the Coxeter-exponent product [2][6][8][12].
flag = [1]
for m in (2, 6, 8, 12):
    next_flag = [0] * (len(flag) + m - 1)
    for i, a in enumerate(flag):
        for j in range(m):
            next_flag[i+j] += a
    flag = next_flag
assert P[length.index(24)] == tuple(flag)

# Sum of the nonnegative lower-half coefficients of D_w(q).
def duality_defect(p):
    d = len(p) - 1
    differences = [p[d-i] - p[i] for i in range((d + 1)//2)]
    assert min(differences, default=0) >= 0
    return sum(differences)

T = [duality_defect(p) for p in P]
assert max(T) == 252
extremal = [i for i, v in enumerate(T) if v == 252]
assert len(extremal) == 2 and set(len(word[W[i]]) for i in extremal) == {18}
assert max(v for v in T if v < 252) == 249
assert sum(v == 0 for v in T) == 174
assert len({tuple(p[len(p)-1-i] - p[i] for i in range(len(p)))
            for p in P}) == 231

witness = '132132432132343213'
q = I
for letter in witness:
    q = product(q, S[int(letter)-1])
assert where[q] in extremal
assert product(q, q) == I
psi = I
for letter in witness:
    psi = product(psi, S[4-int(letter)])
assert where[psi] in extremal and where[psi] != where[q]
assert product(psi, psi) == I
assert P[where[q]] == P[where[psi]] == (
    1,4,9,16,25,36,48,60,71,80,87,92,94,89,74,51,26,8,1)
assert [P[where[q]][18-i] - P[where[q]][i] for i in range(9)] == \
    [0,4,17,35,49,53,46,32,16]
print('PASS: W(F4) order 1152, maximum length 24, root-length and flag checks')
print('PASS: all 1152 Bruhat intervals checked; 174 palindromic, 231 defects')
print('PASS: total defect maximum 252, attained exactly twice; next best 249')
print('PASS: witnesses are involutions exchanged by Coxeter-graph reversal')
print('witness reduced word:', witness)
print('other reduced word:', ''.join(str(5-int(j)) for j in witness))
print('extremal Betti coefficients:', P[where[q]])
print('lower-half differences:', (0,4,17,35,49,53,46,32,16))
