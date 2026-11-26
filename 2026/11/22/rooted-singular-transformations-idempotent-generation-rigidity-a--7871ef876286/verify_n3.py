"""Test the ordinary and idempotent generating ranks on three points."""
from itertools import combinations, product


def compose(f, g):
    return tuple(g[i] for i in f)


def closure(generators):
    visited = set(generators)
    pending = list(generators)
    while pending:
        f = pending.pop()
        for g in generators:
            fg = compose(f, g)
            if fg not in visited:
                visited.add(fg)
                pending.append(fg)
    return visited


def rank(target, candidates):
    return min(len(gs) for size in range(1, len(candidates) + 1)
               for gs in combinations(candidates, size)
               if closure(gs) == target)


singular = {(0, i, j) for i, j in product(range(3), repeat=2)
            if len({0, i, j}) < 3}
assert len(singular) == 7
idempotents = sorted(f for f in singular if compose(f, f) == f)
a, b, c = (0, 0, 1), (0, 2, 0), (0, 1, 1)
assert {a, b, c, compose(a, b), compose(b, a), compose(c, b), compose(a, a)} == singular
ordinary_rank = rank(singular, sorted(singular))
idempotent_rank = rank(singular, idempotents)
assert (ordinary_rank, idempotent_rank) == (3, 4)
print('n=3 ordinary rank:', ordinary_rank)
print('n=3 idempotent rank:', idempotent_rank)
