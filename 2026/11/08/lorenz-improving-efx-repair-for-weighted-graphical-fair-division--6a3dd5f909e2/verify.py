"""Finite exact checks for symmetric-edge EFX Lorenz repair.

Run: python verify.py
All arithmetic is integral; this is a finite check, not an infinite proof.
"""
from itertools import combinations, combinations_with_replacement, product
import random


def loads(edges, choices, n):
    d = [0] * n
    for (i, j, w), choice in zip(edges, choices):
        d[(i, j)[choice]] += w
    return tuple(d)


def efx(edges, choices, n):
    d = loads(edges, choices, n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            shared_in_j = [w for (a, b, w), c in zip(edges, choices)
                           if (a, b)[c] == j and (a, b)[1-c] == i]
            if shared_in_j and d[i] < sum(shared_in_j) - min(shared_in_j):
                return False
    return True


def repair(edges, choices, n):
    choices = list(choices)
    previous = sum(t*t for t in loads(edges, choices, n))
    while not efx(edges, choices, n):
        d = loads(edges, choices, n)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                incoming = [(w, k) for k, ((a, b, w), c) in enumerate(zip(edges, choices))
                            if (a, b)[c] == j and (a, b)[1-c] == i]
                if incoming and d[i] < sum(w for w, k in incoming) - min(w for w, k in incoming):
                    w, k = min(incoming)
                    assert d[j] > d[i] + w
                    choices[k] = 1 - choices[k]
                    current = sum(t*t for t in loads(edges, choices, n))
                    assert current < previous
                    previous = current
                    break
            else:
                continue
            break
        else:
            raise AssertionError('EFX obstruction without legal transfer')
    return tuple(choices)


def majorized_by(final, initial):
    a = sorted(final)
    b = sorted(initial)
    return sum(a) == sum(b) and all(
        sum(a[:k]) >= sum(b[:k]) for k in range(1, len(a))
    )


def exhaustive(n, maximum_edges):
    types = [(*pair, w) for pair in combinations(range(n), 2) for w in (1, 2, 3)]
    instances = orientations = 0
    for m in range(maximum_edges+1):
        for edges in combinations_with_replacement(types, m):
            instances += 1
            best_peak = float('inf')
            best_peak_efx = float('inf')
            best_square = float('inf')
            best_square_efx = float('inf')
            for choices in product((0, 1), repeat=m):
                orientations += 1
                before = loads(edges, choices, n)
                peak, square = max(before), sum(t*t for t in before)
                best_peak = min(best_peak, peak)
                best_square = min(best_square, square)
                if efx(edges, choices, n):
                    best_peak_efx = min(best_peak_efx, peak)
                    best_square_efx = min(best_square_efx, square)
                after_choice = repair(edges, choices, n)
                after = loads(edges, after_choice, n)
                assert efx(edges, after_choice, n)
                assert majorized_by(after, before)
                assert max(after) <= max(before)
            assert best_peak == best_peak_efx, (n, edges, best_peak, best_peak_efx)
            assert best_square == best_square_efx
    return instances, orientations


def different_weights_boundary():
    # Two goods each worth 1 to agent 0 and 10 to agent 1.
    # Assigning both to 0 has makespan 2 and is not EFX; splitting has peak 10.
    values = ((1, 10), (1, 10))
    peaks = []
    for bits in product((0, 1), repeat=2):
        u = [sum(values[k][i] for k,b in enumerate(bits) if b == i) for i in range(2)]
        fair = all(u[i] >= sum(values[k][i] for k,b in enumerate(bits)
                                    if b == j and k != z)
                   for i in range(2) for j in range(2) if i != j
                   for z,b in enumerate(bits) if b == j)
        peaks.append((max(u), fair, bits))
    assert min(x[0] for x in peaks) == 2
    assert min(x[0] for x in peaks if x[1]) == 10


def no_global_lorenz_maximum():
    edges = ((0, 1, 2), (0, 1, 3), (0, 1, 5), (0, 2, 4), (0, 2, 4))
    outcomes = [(bits, loads(edges, bits, 3)) for bits in product((0, 1), repeat=5)]
    shapes = set(tuple(sorted(d)) for _,d in outcomes)
    p = (5, 5, 8)
    q = (4, 7, 7)
    assert p in shapes and q in shapes
    assert not majorized_by(p, q) and not majorized_by(q, p)
    assert not any(all(majorized_by(x, y) for y in shapes) for x in shapes)
    assert any(tuple(sorted(d)) == p and efx(edges, b, 3) for b,d in outcomes)
    assert any(tuple(sorted(d)) == q and efx(edges, b, 3) for b,d in outcomes)


def random_instances():
    random.seed(43017)
    for trial in range(500):
        n = random.randrange(2, 7)
        m = random.randrange(1, 12)
        pairs = list(combinations(range(n), 2))
        edges = [(*random.choice(pairs), random.randrange(1, 19)) for _ in range(m)]
        bits = tuple(random.randrange(2) for _ in edges)
        final = repair(edges, bits, n)
        assert majorized_by(loads(edges, final, n), loads(edges, bits, n))
    return 500


if __name__ == '__main__':
    total = [0, 0]
    for n, m in ((2, 6), (3, 5), (4, 4)):
        a, b = exhaustive(n, m)
        print('exhaustive', n, a, 'instances', b, 'orientations')
        total[0] += a
        total[1] += b
    print('random', random_instances(), 'instances')
    different_weights_boundary()
    no_global_lorenz_maximum()
    print('asymmetric boundary: checked')
    print('PASS', total[0], 'weighted multigraph instances', total[1], 'orientations')
