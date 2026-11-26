"""Check the Klein-four subgroup-class series against direct conjugacy orbits."""
from itertools import combinations, permutations, product


def denominator_series(degrees, max_degree):
    a = [1] + [0] * max_degree
    for d in degrees:
        for j in range(d, max_degree + 1):
            a[j] += a[j-d]
    return a


def class_series(max_degree):
    p = denominator_series([1]*4 + [2]*6 + [4], max_degree)
    t = denominator_series([1]*2 + [2]*3 + [4]*3, max_degree)
    c = denominator_series([1, 3, 4, 6, 6], max_degree)
    i = denominator_series([1, 1, 2], max_degree)
    result = []
    for a, b, d, e in zip(p, t, c, i):
        q, r = divmod(a + 3*b + 2*d, 6)
        assert r == 0
        result.append(q-e)
    return result


def multiply(g, h):
    return tuple(h[j-1] if j > 0 else -h[-j-1] for j in g)


def direct_classes(n):
    unit = tuple(range(1, n+1))
    elements = (tuple(s*j for s, j in zip(signs, p)) for p in permutations(unit)
                for signs in product((1, -1), repeat=n))
    involutions = [g for g in elements if g != unit and multiply(g, g) == unit]
    unseen = {tuple(sorted((g, h, k))) for g, h in combinations(involutions, 2)
              if (k := multiply(g, h)) == multiply(h, g)}

    # The listed generators are involutions, so conjugation uses each twice.
    generators = [(-1,) + unit[1:]] if n else []
    for j in range(n-1):
        g = list(unit)
        g[j], g[j+1] = g[j+1], g[j]
        generators.append(tuple(g))

    classes = 0
    while unseen:
        todo = [unseen.pop()]
        classes += 1
        while todo:
            H = todo.pop()
            for g in generators:
                conjugate = tuple(sorted(multiply(g, multiply(h, g)) for h in H))
                if conjugate in unseen:
                    unseen.remove(conjugate)
                    todo.append(conjugate)
    return classes


if __name__ == '__main__':
    coeffs = class_series(10)
    assert coeffs == [0, 0, 2, 7, 23, 51, 116, 223, 431, 762, 1341]
    direct = [direct_classes(n) for n in range(6)]
    assert direct == coeffs[:6], (direct, coeffs[:6])
    print('Ranks 0–5, direct subgroup conjugacy:', direct)
    print('Ranks 0–10, ordinary generating series:', coeffs)
