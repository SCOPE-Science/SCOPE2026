"""Reproducible checks for the Kneser triple-neighborhood homology character.

Python 3 standard library only. Direct simplicial Lefschetz checks are finite;
the result for all n is established by the symbolic argument in RESULT.md.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from fractions import Fraction
from math import factorial, comb


def partitions(n, bound=None):
    if n == 0:
        yield ()
        return
    bound = n if bound is None else min(n, bound)
    for first in range(bound, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def polynomial(a, b):
    numerator = (a**4 - 10*a**3 - 4*a*a*b + 31*a*a +
                 12*a*b - 30*a + 4*b*b - 12*b + 4)
    assert numerator % 4 == 0
    return numerator // 4


def top_character(cycles):
    n = sum(cycles)
    return (-1)**(n - len(cycles)) * polynomial(cycles.count(1), cycles.count(2))


def representative(cycles):
    result = []
    offset = 0
    for c in cycles:
        result.extend(offset + (i + 1) % c for i in range(c))
        offset += c
    return result


def all_faces(n):
    triples = tuple(combinations(range(n), 3))
    index = {t: i for i, t in enumerate(triples)}
    faces = {0}
    for vertices in combinations(range(n), n - 3):
        bits = [1 << index[t] for t in combinations(vertices, 3)]
        for selector in range(1 << len(bits)):
            mask = 0
            for j, b in enumerate(bits):
                if (selector >> j) & 1:
                    mask |= b
            faces.add(mask)
    return triples, faces


def direct_lefschetz(n, cycles, triples, faces):
    perm = representative(cycles)
    indices = {t: i for i, t in enumerate(triples)}
    induced = [indices[tuple(sorted(perm[v] for v in t))] for t in triples]
    # Each invariant face contributes -(-1)^(number of induced vertex orbits).
    signed_orbit_sum = 0
    for face in faces:
        moved = 0
        members = []
        x = face
        while x:
            low = x & -x
            v = low.bit_length() - 1
            members.append(v)
            moved |= 1 << induced[v]
            x -= low
        if moved != face:
            continue
        remaining = set(members)
        orbit_count = 0
        while remaining:
            orbit_count += 1
            v = min(remaining)
            while v in remaining:
                remaining.remove(v)
                v = induced[v]
        signed_orbit_sum += (-1) ** orbit_count
    return (-1) ** (n - 6) * (-signed_orbit_sum)


def contained(mu, lam):
    return len(mu) <= len(lam) and all(x <= y for x, y in zip(mu, lam))


@lru_cache(None)
def rim_hooks(lam, length):
    out = []
    for mu in partitions(sum(lam) - length):
        if not contained(mu, lam):
            continue
        cells = {(r, c) for r, row_length in enumerate(lam)
                 for c in range(mu[r] if r < len(mu) else 0, row_length)}
        if len(cells) != length or any(
                (r + 1, c) in cells and (r, c + 1) in cells and
                (r + 1, c + 1) in cells for (r, c) in cells):
            continue
        reached = {next(iter(cells))}
        pending = list(reached)
        while pending:
            r, c = pending.pop()
            for nxt in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if nxt in cells and nxt not in reached:
                    reached.add(nxt)
                    pending.append(nxt)
        if len(reached) == length:
            out.append((mu, (-1)**(len({r for r, _ in cells}) - 1)))
    return tuple(out)


@lru_cache(None)
def specht_char(lam, cycles):
    if not cycles:
        return int(not lam)
    return sum(sign * specht_char(mu, cycles[1:])
               for mu, sign in rim_hooks(lam, cycles[0]))


def targets(n):
    return ((5,) + (1,) * (n - 5),
            (4, 2) + (1,) * (n - 6),
            (3, 3) + (1,) * (n - 6))


def pieri(mu, n):
    return {
        lam for lam in partitions(n)
        if contained(mu, lam)
        and all((mu[r] if r < len(mu) else 0) >=
                (lam[r + 1] if r + 1 < len(lam) else 0)
                for r in range(len(lam)))
    }


def check_induced_module_identity(n):
    # Frobenius characteristic of the untwisted character; each
    # h_(n-r) s_mu is expanded by the horizontal-strip Pieri rule.
    coefficients = {
        (): 1, (1,): -2, (2,): 1, (1, 1): 3,
        (2, 1): -2, (1, 1, 1): -2, (2, 2): 1,
        (2, 1, 1): 1, (1, 1, 1, 1): 1,
    }
    conjugate_shapes = {
        (n - 4, 1, 1, 1, 1),
        (n - 4, 2, 1, 1),
        (n - 4, 2, 2),
    }
    values = Counter()
    for mu, coefficient in coefficients.items():
        for lam in pieri(mu, n):
            values[lam] += coefficient
    assert all(values[lam] == int(lam in conjugate_shapes)
               for lam in partitions(n))


def check():
    for n in range(7, 12):
        assert polynomial(n, 0) == n * (n - 5) * (n - 3) * (n - 2) // 4 + 1
        for cycle_type in partitions(n):
            assert top_character(cycle_type) == sum(
                specht_char(lam, cycle_type) for lam in targets(n))
        check_induced_module_identity(n)
        print('SPECHT_OK', n, 'classes', len(list(partitions(n))))
    for n in (7, 8):
        triples, faces = all_faces(n)
        print('FACES', n, len(faces))
        for cycle_type in partitions(n):
            observed = direct_lefschetz(n, cycle_type, triples, faces)
            expected = top_character(cycle_type)
            assert observed == expected, (n, cycle_type, observed, expected)
        print('DIRECT_LEFSCHETZ_OK', n, 'classes', len(list(partitions(n))))
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
