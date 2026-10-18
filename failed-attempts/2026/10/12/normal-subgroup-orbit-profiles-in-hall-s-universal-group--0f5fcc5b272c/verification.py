from collections import deque
from itertools import combinations, product


def gaussian_binom(n, k, q):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = den = 1
    for i in range(k):
        num *= q ** (n - i) - 1
        den *= q ** (k - i) - 1
    return num // den


def galois(n, q):
    return sum(gaussian_binom(n, k, q) for k in range(n + 1))


def rref_subspaces(n, q):
    """Enumerate each subspace of F_q^n once as an RREF row basis."""
    yield tuple()
    for r in range(1, n + 1):
        for pivots in combinations(range(n), r):
            pivot_set = set(pivots)
            free_positions = []
            for i, p in enumerate(pivots):
                for j in range(p + 1, n):
                    if j not in pivot_set:
                        free_positions.append((i, j))
            for vals in product(range(q), repeat=len(free_positions)):
                rows = [[0] * n for _ in range(r)]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, j), v in zip(free_positions, vals):
                    rows[i][j] = v
                yield tuple(tuple(row) for row in rows)



def homocyclic_subgroup_count(p, a, n):
    """Birkhoff formula summed over subgroup types of (Z/p^a Z)^n."""
    total = 0

    def walk(prefix, ceiling):
        nonlocal total
        if len(prefix) == a:
            r = list(prefix) + [0]
            term = 1
            exponent = 0
            for i in range(a):
                ri, rip1 = r[i], r[i + 1]
                exponent += rip1 * (n - ri)
                term *= gaussian_binom(n - rip1, ri - rip1, p)
            total += (p ** exponent) * term
            return
        for x in range(ceiling, -1, -1):
            walk(prefix + (x,), x)

    walk(tuple(), n)
    return total


def add(a, b, m):
    return tuple((x + y) % m for x, y in zip(a, b))


def cyclic_subgroup(g, m):
    z = (0,) * len(g)
    out = {z}
    x = z
    while True:
        x = add(x, g, m)
        if x in out:
            break
        out.add(x)
    return out


def generated_with(H, g, m):
    C = cyclic_subgroup(g, m)
    return frozenset(add(h, c, m) for h in H for c in C)


def all_subgroups(m, n):
    """Brute-force subgroup lattice of (Z/mZ)^n by generator closure."""
    elems = list(product(range(m), repeat=n))
    zero = (0,) * n
    start = frozenset([zero])
    seen = {start}
    queue = deque([start])
    while queue:
        H = queue.popleft()
        for g in elems:
            if g in H:
                continue
            K = generated_with(H, g, m)
            if K not in seen:
                seen.add(K)
                queue.append(K)
    return seen


def crt_image(H, p, q):
    return frozenset((tuple(x % p for x in v), tuple(x % q for x in v)) for v in H)


def projection_pair(H, p, q):
    image = crt_image(H, p, q)
    Hp = frozenset(a for a, _ in image)
    Hq = frozenset(b for _, b in image)
    return image, Hp, Hq


def quotient_kernel_signature(K, m, n):
    """Marked quotient signature: for every coefficient vector, its coset of K.

    Cosets are canonically represented by their lexicographically least element.
    The zero coset recovers the relation kernel without using K as an output field.
    """
    elems = list(product(range(m), repeat=n))
    Kset = set(K)
    rep = {}
    for v in elems:
        coset = frozenset(add(v, k, m) for k in Kset)
        rep[v] = min(coset)
    # include images of the standard marked generators and the full evaluation table
    gens = []
    for i in range(n):
        e = [0] * n
        e[i] = 1
        gens.append(rep[tuple(e)])
    table = tuple(rep[v] for v in elems)
    return tuple(gens), table


checks = 0

# Galois numbers from an independent RREF enumeration.
for q, max_n in [(2, 6), (3, 5), (5, 4)]:
    for n in range(max_n + 1):
        direct = sum(1 for _ in rref_subspaces(n, q))
        assert direct == galois(n, q), (q, n, direct, galois(n, q))
        checks += 1

# Brute subgroup lattices of the abelian exponent-m free objects.
expected = {
    (2, 1): 2, (2, 2): 5, (2, 3): 16, (2, 4): 67,
    (3, 1): 2, (3, 2): 6, (3, 3): 28,
    (4, 1): 3, (4, 2): 15,
    (6, 1): 4, (6, 2): 30, (6, 3): 448,
}
subgroup_cache = {}
for key, want in expected.items():
    m, n = key
    subs = all_subgroups(m, n)
    subgroup_cache[key] = subs
    assert len(subs) == want, (key, len(subs), want)
    checks += 1

# Birkhoff formula for homocyclic p-groups, checked against brute subgroup lattices.
for p, a, n, direct in [
    (2, 1, 4, len(subgroup_cache[(2, 4)])),
    (3, 1, 3, len(subgroup_cache[(3, 3)])),
    (2, 2, 1, len(subgroup_cache[(4, 1)])),
    (2, 2, 2, len(subgroup_cache[(4, 2)])),
]:
    assert homocyclic_subgroup_count(p, a, n) == direct
    checks += 1

# Further exact formula values beyond the brute-force cache.
assert homocyclic_subgroup_count(2, 3, 1) == 4   # subgroups of Z/8Z
assert homocyclic_subgroup_count(2, 3, 2) == 37  # subgroups of (Z/8Z)^2
checks += 2

# Prime case: subgroup counts equal Galois numbers.
for p, max_n in [(2, 4), (3, 3)]:
    for n in range(1, max_n + 1):
        assert len(subgroup_cache[(p, n)]) == galois(n, p)
        checks += 1

# Squarefree m=6: every subgroup splits under CRT, and counts multiply.
for n in range(1, 4):
    subs = subgroup_cache[(6, n)]
    for H in subs:
        image, H2, H3 = projection_pair(H, 2, 3)
        assert image == frozenset(product(H2, H3)), (n, H)
        checks += 1
    assert len(subs) == galois(n, 2) * galois(n, 3)
    checks += 1

# Distinct kernels give distinct coordinate-marked quotient signatures.
for m, n in [(4, 2), (6, 2)]:
    sigs = {}
    for K in subgroup_cache[(m, n)]:
        sig = quotient_kernel_signature(K, m, n)
        assert sig not in sigs, (m, n, K, sigs.get(sig))
        sigs[sig] = K
        # independently recover the kernel as all coefficient vectors evaluating to zero coset
        elems = list(product(range(m), repeat=n))
        zero_rep = sig[1][0]  # first ambient vector is zero
        recovered = frozenset(v for v, rv in zip(elems, sig[1]) if rv == zero_rep)
        assert recovered == K
        checks += 2

# Elementary asymptotic sandwiches.  The coarse upper bound is enough for
# the O_m(log n) statement; here p^a is a harmless fixed multiplicative base factor.
for p in (2, 3, 5, 7):
    for n in range(1, 30):
        G = galois(n, p)
        peak = p ** (n * n // 4)
        assert peak <= G <= (n + 1) * peak * (p ** n)
        checks += 1

for p, a in [(2, 2), (2, 3), (3, 2)]:
    for n in range(1, 12):
        S = homocyclic_subgroup_count(p, a, n)
        peak = p ** (a * (n * n // 4))
        # Coarser than the proof's C_p^a(n+1)^a bound, but independent verification
        # that the leading exponent is a*floor(n^2/4) on a nontrivial range.
        assert peak <= S <= peak * (n + 1) ** a * (p ** (a * n))
        checks += 1

print('G_n(2), n=0..8:', [galois(n, 2) for n in range(9)])
print('G_n(3), n=0..7:', [galois(n, 3) for n in range(8)])
print('m=6 orbit/subgroup counts, n=0..3:', [1] + [len(subgroup_cache[(6, n)]) for n in range(1, 4)])
print('m=4 subgroup counts, n=1..2:', [len(subgroup_cache[(4, n)]) for n in range(1, 3)])
print('Birkhoff S_{3,n}(2), n=1..4:', [homocyclic_subgroup_count(2,3,n) for n in range(1,5)])
print('checks:', checks)
print('VERIFY_OK')
