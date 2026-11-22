"""Independent finite enumeration of sparse stable-extension classifiers."""
from itertools import combinations
from functools import lru_cache
from math import comb


def matchings(n):
    edges = list(combinations(range(n), 2))
    yield ()
    for e in edges:
        yield (e,)
    for a, b in combinations(edges, 2):
        if len(set(a + b)) == 4:
            yield (a, b)


def classes(n):
    models = list(matchings(n))
    domain = [tuple(range(n))]
    domain += [tuple(i for i in range(n) if i != j) for j in range(n)]
    domain += [tuple(i for i in range(n) if i not in pair)
               for pair in combinations(range(n), 2)]
    columns = []
    universe = set(range(n))
    for S in domain:
        omitted = universe - set(S)
        truth = 0
        for index, M in enumerate(models):
            # Stable = independent and every omitted vertex attacked by S.
            independent = all(not set(e).issubset(S) for e in M)
            dominated = all(any((v in e and (set(e) - {v}).issubset(S))
                                for e in M) for v in omitted)
            if independent and dominated:
                truth |= 1 << index
        columns.append(truth)
    return models, domain, columns


def shattered_coefficients(columns, n_models):
    complete = (1 << n_models) - 1
    ans = [1, 0, 0, 0, 0]
    for size in range(1, 5):
        for qs in combinations(range(len(columns)), size):
            cells = [complete]
            for q in qs:
                mask = columns[q]
                cells = [b for c in cells for b in (c & mask, c & (complete ^ mask)) if b]
                if len(cells) < 2 ** (qs.index(q) + 1):
                    break
            if len(cells) == 2 ** size:
                ans[size] += 1
    return ans


def online_dimension(columns, n_models, maximum=5):
    complete = (1 << n_models) - 1
    @lru_cache(None)
    def feasible(state, depth):
        if depth == 0:
            return True
        if state.bit_count() < 1 << depth:
            return False
        for q in columns:
            one = state & q
            zero = state ^ one
            if one.bit_count() < 1 << (depth - 1) or zero.bit_count() < 1 << (depth - 1):
                continue
            if feasible(one, depth - 1) and feasible(zero, depth - 1):
                return True
        return False
    out = 0
    for depth in range(1, maximum + 1):
        if feasible(complete, depth):
            out = depth
        else:
            break
    return out


def prediction(n):
    if n == 1:
        return [1, 0, 0, 0, 0], 0
    if n == 2:
        return [1, 3, 0, 0, 0], 1
    if n == 3:
        return [1, 4, 3, 0, 0], 2
    if n == 4:
        return [1, 11, 18, 0, 0], 2
    N = comb(n, 2)
    return [1, 1+n+N, N + comb(N, 2), 12*comb(n,4), 0], 3


def run():
    checks = 0
    for n in range(1, 9):
        models, domain, columns = classes(n)
        coeffs = shattered_coefficients(columns, len(models))
        depth = online_dimension(columns, len(models))
        expected, exp_depth = prediction(n)
        assert coeffs == expected, (n, coeffs, expected)
        assert depth == exp_depth, (n, depth, exp_depth)
        assert len(models) == 1+comb(n,2)+(3*comb(n,4) if n >= 4 else 0)
        checks += 1
        print('n', n, 'hypotheses', len(models), 'coeffs', coeffs, 'online', depth)
    print('VERIFY_OK', checks)

if __name__ == '__main__':
    run()
