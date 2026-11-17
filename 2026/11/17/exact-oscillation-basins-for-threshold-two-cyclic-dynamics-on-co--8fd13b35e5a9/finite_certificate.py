#!/usr/bin/env python3
"""Finite, executable certificate for the split-graph threshold-two CCA theorem.

Only Python 3 standard library is required. For each of 729 clipped
initial population vectors, the six original colour classes are tagged.
The actual class sizes can be any integers with these 0/1/2 clips.
"""
from collections import Counter
from itertools import product


def transition(colours, sizes):
    clique = [0, 0, 0]
    leaves = [0, 0, 0]
    for i in range(3):
        clique[colours[i]] = min(2, clique[colours[i]] + sizes[i])
        leaves[colours[i + 3]] = min(2, leaves[colours[i + 3]] + sizes[i + 3])
    result = []
    for i, c in enumerate(colours):
        target = (c + 1) % 3
        quota = clique[target] + leaves[target] if i < 3 else clique[target]
        result.append((c + (quota >= 2)) % 3)
    return tuple(result)


def multiply(P, Q):
    R = Counter()
    for k, v in P.items():
        for j, w in Q.items():
            R[tuple(k[i] + j[i] for i in range(4))] += v * w
    return +R


def power(P, n):
    R = {(0, 0, 0, 0): 1}
    for _ in range(n):
        R = multiply(R, P)
    return R


def addition(*polys):
    R = Counter()
    for P in polys:
        R.update(P)
    return +R


def scalar(P, n):
    return {k: n * v for k, v in P.items()}


def variable(i):
    ex = [0, 0, 0, 0]
    ex[i] = 1
    return {tuple(ex): 1}


def main():
    zero = {(0, 0, 0, 0): 1}
    z, U, w, V = [variable(i) for i in range(4)]
    E = addition(zero, w, V)
    target = addition(
        multiply(power(U, 3), power(E, 3)),
        scalar(multiply(multiply(power(U, 2), power(E, 2)),
                        addition(V, multiply(z, addition(V, w)))), 3),
        scalar(multiply(power(V, 3), addition(z, power(z, 2))), 3),
        multiply(power(z, 3), power(addition(V, w), 3)),
    )
    coefficients = Counter()
    oscillating = 0
    max_entry = 0
    invalid_cycles = 0
    for sizes in product(range(3), repeat=6):
        colours = (0, 1, 2, 0, 1, 2)
        times = [colours]
        for _ in range(7):
            colours = transition(colours, sizes)
            times.append(colours)
        active = [i for i, s in enumerate(sizes) if s > 0]
        equivalent = lambda p, q: all(times[p][i] == times[q][i] for i in active)
        assert equivalent(4, 7), ('identity fails', sizes)
        entry = next(t for t in range(5) if equivalent(t, t + 3))
        max_entry = max(max_entry, entry)
        if not equivalent(4, 5):
            oscillating += 1
            signature = (sizes[:3].count(1), sizes[:3].count(2),
                         sizes[3:].count(1), sizes[3:].count(2))
            coefficients[signature] += 1
        elif not equivalent(4, 6):
            invalid_cycles += 1
    assert invalid_cycles == 0
    assert dict(coefficients) == dict(target), ('EGF failed', coefficients, target)
    assert (oscillating, len(coefficients), max_entry) == (122, 31, 4)
    print('CLIPPED_CLASSES=729')
    print('OSCILLATING_CLASSES=122')
    print('EGF_MONOMIALS=31')
    print('UNIVERSAL_IDENTITY=F^7=F^4')
    print('SHARP_MAX_ENTRY=4')
    print('EGF_COEFFICIENT_CHECK=PASS')
    print('ALL_ASSERTIONS=PASS')

if __name__ == '__main__':
    main()
