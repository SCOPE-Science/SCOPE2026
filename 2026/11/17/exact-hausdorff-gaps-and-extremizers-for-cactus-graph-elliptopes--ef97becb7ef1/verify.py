#!/usr/bin/env python3
"""Finite corroboration of the cycle/cactus elliptope Hausdorff theorem.

Requires only Python's standard library. These finite tests do not prove
statements for all cycle lengths, all weights, or all cactus graphs.
"""
import itertools
import math
import random


def odd_signs(n):
    for head in itertools.product((-1, 1), repeat=n - 1):
        yield head + (-math.prod(head),)


def cut_signs(n):
    for head in itertools.product((-1, 1), repeat=n - 1):
        yield head + (math.prod(head),)


def gram_cycle(n, signs):
    # A planar Gram representation of an extremal cycle-elliptope point.
    phase_signs = [1]
    for s in signs[:-1]:
        phase_signs.append(phase_signs[-1] * s)
    a = math.pi / n
    vectors = [(phase_signs[i] * math.cos(i * a),
                phase_signs[i] * math.sin(i * a)) for i in range(n)]
    edges = [sum(vectors[i][k] * vectors[(i + 1) % n][k]
                 for k in (0, 1)) for i in range(n)]
    return vectors, edges


def norm(vec):
    return math.sqrt(sum(x*x for x in vec))


def test():
    count = 0
    rng = random.Random(93017)
    for n in range(3, 13):
        t = math.cos(math.pi / n)
        delta = (n * t - (n - 2)) / math.sqrt(n)
        assert delta > 0
        count += 1
        patterns = list(odd_signs(n)) if n <= 9 else [next(odd_signs(n))]
        for xi in patterns:
            v, x = gram_cycle(n, xi)
            assert all(abs(sum(z*z for z in a) - 1) < 1e-12 for a in v)
            assert all(abs(x[i] - t * xi[i]) < 3e-12 for i in range(n))
            y = [(n - 2) / n * si for si in xi]
            avg = [0.] * n
            for j in range(n):
                z = [xi[i] * (-1 if i == j else 1) for i in range(n)]
                assert math.prod(z) == 1
                for i in range(n):
                    avg[i] += z[i] / n
            assert all(abs(avg[i] - y[i]) < 2e-12 for i in range(n))
            assert abs(norm([x[i] - y[i] for i in range(n)]) - delta) < 2e-12
            assert abs(sum(xi[i] * y[i] for i in range(n)) - (n-2)) < 2e-12
            assert abs(sum(xi[i] * x[i] for i in range(n)) - n*t) < 2e-12
            count += 6 + n
        if n <= 8:
            cuts = list(cut_signs(n))
            for _ in range(150):
                w = [rng.uniform(-3, 3) for _ in range(n)]
                hs = max(sum(wi*zi for wi,zi in zip(w,z)) for z in cuts)
                # With nonzero weights, the cut support has a closed formula.
                absw = [abs(z) for z in w]
                odd = math.prod(1 if z > 0 else -1 for z in w) == -1
                theoretical = sum(absw) - (2 * min(absw) if odd else 0)
                assert abs(hs - theoretical) < 1e-10
                xi = tuple(1 if wi > 0 else -1 for wi in w)
                if not odd:
                    xi = xi[:-1] + (-xi[-1],)
                _, z = gram_cycle(n, xi)
                assert sum(wi*zi for wi,zi in zip(w,z)) - hs <= norm(w)*delta + 1e-10
                count += 2
        # Sharp directional gap and the signed adjacency top eigenvalue.
        assert abs((n*t - (n-2)) / math.sqrt(n) - delta) < 1e-12
        top = max(2 * math.cos((2*k + 1) * math.pi / n) for k in range(n))
        assert abs(top - 2*t) < 2e-12
        count += 2
    # Product nearest-point identity for two cycles and three free edges.
    for a, b in itertools.product(range(3, 9), repeat=2):
        pa = next(odd_signs(a))
        pb = next(odd_signs(b))
        _, xa = gram_cycle(a, pa)
        _, xb = gram_cycle(b, pb)
        ya = [(a-2)/a * s for s in pa]
        yb = [(b-2)/b * s for s in pb]
        xs = xa + xb + [0.1, -0.6, 0.99]
        ys = ya + yb + [0.1, -0.6, 0.99]
        da = (a*math.cos(math.pi/a)-(a-2))/math.sqrt(a)
        db = (b*math.cos(math.pi/b)-(b-2))/math.sqrt(b)
        assert abs(norm([x-y for x,y in zip(xs,ys)]) - math.hypot(da,db)) < 1e-12
        count += 1
    print(f'PASS: {count} finite numerical and combinatorial assertions')

if __name__ == '__main__':
    test()
