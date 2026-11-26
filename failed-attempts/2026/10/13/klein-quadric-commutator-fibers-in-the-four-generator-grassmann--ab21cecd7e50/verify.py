"""Independent finite-field consistency checks for four-generator exterior algebra.

Run: python3 verify.py.  Uses only the Python standard library.
The general statement is proved symbolically in RESULT.md; finite checks do not
substitute for that proof.
"""
from collections import Counter
from itertools import product
from random import Random

DEG1 = (1, 2, 4, 8)
DEG3 = (7, 11, 13, 14)
DEG2 = (3, 5, 9, 6, 10, 12)
ODD = DEG1 + DEG3
EVEN = (0, 3, 5, 9, 6, 10, 12, 15)


def wedge_scalar(a, b):
    if a & b:
        return 0, -1
    inversions = sum((b & ((1 << j) - 1)).bit_count()
                     for j in range(4) if (a >> j) & 1)
    return (-1 if inversions & 1 else 1), a | b


def exterior_product(x, y, q):
    out = [0] * 16
    for i, xi in enumerate(x):
        if not xi:
            continue
        for j, yj in enumerate(y):
            if not yj:
                continue
            sign, mask = wedge_scalar(i, j)
            if sign:
                out[mask] = (out[mask] + sign * xi * yj) % q
    return tuple(out)


def comm(x, y, q):
    xy = exterior_product(x, y, q)
    yx = exterior_product(y, x, q)
    return tuple((a - b) % q for a, b in zip(xy, yx))


def norm_comm(x, y, q):
    return tuple((v * pow(2, -1, q)) % q for v in comm(x, y, q))


def odd_embed(coords):
    out = [0] * 16
    for mask, v in zip(ODD, coords):
        out[mask] = v
    return tuple(out)


def bi(u, v, q):
    return tuple((u[i] * v[j] - u[j] * v[i]) % q
                 for (i, j) in ((0, 1), (0, 2), (0, 3),
                                (1, 2), (1, 3), (2, 3)))


def pfaff(a, q):
    return (a[0] * a[5] - a[1] * a[4] + a[2] * a[3]) % q


def rank_mod(mat, q):
    mat = [list(row) for row in mat]
    if not mat:
        return 0
    h, w = len(mat), len(mat[0])
    rank = 0
    for c in range(w):
        pivot = next((r for r in range(rank, h) if mat[r][c] % q), None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        iv = pow(mat[rank][c], -1, q)
        mat[rank] = [(z * iv) % q for z in mat[rank]]
        for r in range(h):
            if r == rank:
                continue
            coef = mat[r][c]
            if coef:
                mat[r] = [(z - coef * t) % q for z, t in zip(mat[r], mat[rank])]
        rank += 1
        if rank == h:
            break
    return rank


def verify_prime(q, full_ranks):
    assert q in (3, 5)
    vs = tuple(product(range(q), repeat=4))
    wedge_counts = Counter(bi(u, v, q) for u in vs for v in vs)
    zeros = (0,) * 6
    c0 = q**5 + q**4 - q
    sl2 = q * (q**2 - 1)
    gaussian = (q**2 + 1) * (q**2 + q + 1)
    assert wedge_counts[zeros] == c0
    assert sum(wedge_counts.values()) == q**8
    num_simple = 0
    for a in product(range(q), repeat=6):
        n = wedge_counts[a]
        if a == zeros:
            assert n == c0
        elif pfaff(a, q) == 0:
            num_simple += 1
            assert n == sl2, (q, a, n, sl2)
        else:
            assert n == 0, (q, a, n)
    assert num_simple == (q - 1) * gaussian

    # Direct linear algebra: the top-degree term is a nonzero linear
    # functional of the two trivector variables unless u=v=0.
    zero = [0] * 16
    odds = []
    for mask in ODD:
        t = zero.copy()
        t[mask] = 1
        odds.append(tuple(t))
    rank_distribution = Counter()
    rng = Random(121 * q)
    xcoords = (product(range(q), repeat=8) if full_ranks else
               (tuple(rng.randrange(q) for _ in range(8)) for _ in range(250)))
    for coords in xcoords:
        x = odd_embed(coords)
        cols = [norm_comm(x, y, q) for y in odds]
        mat = [[col[mask] for col in cols] for mask in DEG2 + (15,)]
        rank = rank_mod(mat, q)
        u, c = coords[:4], coords[4:]
        expected = 4 if any(u) else (1 if any(c) else 0)
        assert rank == expected, (q, coords, rank, expected)
        rank_distribution[rank] += 1
    if full_ranks:
        assert rank_distribution == Counter({0: 1, 1: q**4-1,
                                             4: q**4*(q**4-1)})

    # Check exterior multiplication and the two-degree decomposition with
    # a deterministic collection of full algebra elements.
    for _ in range(700):
        x = tuple(rng.randrange(q) for _ in range(16))
        y = tuple(rng.randrange(q) for _ in range(16))
        z = norm_comm(x, y, q)
        u = tuple(x[mask] for mask in DEG1)
        v = tuple(y[mask] for mask in DEG1)
        assert tuple(z[mask] for mask in DEG2) == bi(u, v, q)
        assert all(z[mask] == 0 for mask in range(16)
                   if mask not in DEG2 + (15,))
        # Directly rebuild the top coefficient from degree-one/trivector terms.
        cu = [0] * 16
        dv = [0] * 16
        x1 = [0] * 16
        y1 = [0] * 16
        for mask in DEG1:
            x1[mask], y1[mask] = x[mask], y[mask]
        for mask in DEG3:
            cu[mask], dv[mask] = x[mask], y[mask]
        pred = (exterior_product(tuple(x1), tuple(dv), q)[15] +
                exterior_product(tuple(cu), tuple(y1), q)[15]) % q
        assert z[15] == pred

    # Fiber formulas are independently summed over all possible target
    # bivectors/top forms and checked against total ordered pairs.
    def fiber(a, top):
        if a == zeros:
            return q**16 * ((c0-1)*q**7 + (q**8 if top == 0 else 0))
        if pfaff(a, q) == 0:
            return q**16 * sl2*q**7
        return 0
    mass = sum(fiber(a, b) for a in product(range(q), repeat=6)
               for b in range(q))
    assert mass == q**32, (q, mass, q**32)
    assert fiber(zeros, 0) == q**28 + q**27 - q**23
    support = q * (1 + num_simple)
    assert support == q * (1+(q-1)*gaussian)
    # The degree-two part of e12+e34 is nondecomposable, so two
    # commutators are needed, and those two elementary wedges suffice.
    a = tuple(1 if mask in (3, 12) else 0 for mask in DEG2)
    assert pfaff(a, q) == 1
    print(f"F_{q}: simple_nonzero={num_simple}, support={support}, "
          f"central_fiber={fiber(zeros, 0)}, rank_checks={sum(rank_distribution.values())}")


if __name__ == '__main__':
    verify_prime(3, True)
    verify_prime(5, False)
    print('VERIFY_OK')
