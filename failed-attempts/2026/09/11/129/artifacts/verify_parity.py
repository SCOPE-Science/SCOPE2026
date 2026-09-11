"""Independent replay checker for the parity obstruction (lane-1027).

Verifies, with stdlib only:
 (a) CRT fact: on Z_10 = Z_2 x Z_5, adding 5 flips the Z_2 bit and fixes Z_5;
     tau(n) = n+5 is a fixed-point-free involution = 5 disjoint transpositions.
 (b) Orbit-xor lemma: two complementary G-orbits covering the same Z_5 pair
     in two columns always have xor-values summing to 1 (mod 2).
 (c) UNSAT of the column-parity system w_j + w_k = 1 for all pairs (3 and
     5 columns) by exhaustive search over all assignments.
 (d) Empirical base case (m=1): no 2x2 Latin square admits the triple-tau
     symmetry L(r+1,c+1) = L(r,c)+1 -- the smallest instance of the theorem.
 (e) The oddness m^2 = 25 needed so the 25 orbit-pair contributions sum to 1.
"""
import itertools

# (a) CRT action of +5 on Z_10
for n in range(10):
    e, a = n % 2, n % 5
    e2, a2 = (n + 5) % 2, (n + 5) % 5
    assert e2 == 1 - e, (n, e, e2)
    assert a2 == a, (n, a, a2)
# tau is a fixed-point-free involution with exactly 5 transpositions
seen = set()
trans = 0
for n in range(10):
    m = (n + 5) % 10
    assert m != n
    assert (m + 5) % 10 == n
    if n not in seen:
        seen.add(n)
        seen.add(m)
        trans += 1
assert trans == 5
print("(a) CRT flip/fix + 5-transposition profile: OK")

# (b) orbit-xor lemma over Z_2^2
combos = [(0, 0), (0, 1), (1, 0), (1, 1)]
comp = lambda p: (1 - p[0], 1 - p[1])
for u in combos:
    o1 = {u, comp(u)}
    rest = [c for c in combos if c not in o1]
    assert len(rest) == 2 and rest[1] == comp(rest[0])
    s1 = (u[0] + u[1]) % 2
    s2 = (rest[0][0] + rest[0][1]) % 2
    assert (s1 + s2) % 2 == 1, (u, rest)
print("(b) orbit-xor lemma (complementary orbits sum to 1): OK")

# (c) UNSAT of w_j + w_k = 1 systems
bad3 = [w for w in itertools.product([0, 1], repeat=3)
        if (w[0] + w[1]) % 2 == 1 and (w[0] + w[2]) % 2 == 1
        and (w[1] + w[2]) % 2 == 1]
assert bad3 == [], bad3
bad5 = [w for w in itertools.product([0, 1], repeat=5)
        if all((w[j] + w[k]) % 2 == 1
               for j in range(5) for k in range(j + 1, 5))]
assert bad5 == [], bad5
print("(c) parity system UNSAT for 3 cols (8/8 fail) and 5 cols (32/32 fail): OK")

# (d) order-2 base case by brute force
sym_count = 0
for vals in itertools.product([0, 1], repeat=4):
    L = [list(vals[0:2]), list(vals[2:4])]
    if sorted(L[0]) != [0, 1] or sorted(L[1]) != [0, 1]:
        continue
    if sorted([L[0][0], L[1][0]]) != [0, 1]:
        continue
    if sorted([L[0][1], L[1][1]]) != [0, 1]:
        continue
    if all(L[(r + 1) % 2][(c + 1) % 2] == (L[r][c] + 1) % 2
           for r in (0, 1) for c in (0, 1)):
        sym_count += 1
assert sym_count == 0, sym_count
print("(d) order-2 brute force: 0 of the Latin squares admit triple-tau symmetry: OK")

# (e) oddness of the number of Z_5 pairs
for m in [1, 3, 5, 7, 9]:
    assert (m * m) % 2 == 1
assert (5 * 5) % 2 == 1
print("(e) m^2 odd for odd m (25 orbit-pair contributions sum to 1 mod 2): OK")

print("ALL CHECKS PASSED")
