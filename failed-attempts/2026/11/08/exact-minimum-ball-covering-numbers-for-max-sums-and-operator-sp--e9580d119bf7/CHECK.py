"""Finite exact-grid diagnostics for off-origin max-norm sphere coverings.

These tests sample finite grids. The theorem for all normed spaces is proved analytically.
"""
from fractions import Fraction as F
from itertools import product

def max_norm(v):
    return max(map(abs, v))

def balls(d):
    for j in range(d):
        for s in (-1, 1):
            v = [F(0)] * d
            v[j] = F(2) * s
            yield tuple(v), F(3, 2)

def test_grid(d):
    grid = (F(-1), F(-1, 2), F(0), F(1, 2), F(1))
    covers = tuple(balls(d))
    assertions = 0
    for c, r in covers:
        assert max_norm(c) > r
        assertions += 1
        touched_axes = []
        for j in range(d):
            for s in (-1, 1):
                u = [F(0)] * d
                u[j] = s
                if max_norm([a - b for a, b in zip(u, c)]) <= r:
                    touched_axes.append(j)
        assert len(set(touched_axes)) == 1
        assertions += 1
    for x in product(grid, repeat=d):
        if max_norm(x) != 1:
            continue
        assert any(max_norm([a - b for a, b in zip(x, c)]) <= r for c, r in covers)
        assertions += 1
    return assertions

if __name__ == "__main__":
    checks = sum(test_grid(d) for d in (1, 2, 3, 4, 5))
    print(f"PASS: {checks} exact rational diagnostic assertions")
