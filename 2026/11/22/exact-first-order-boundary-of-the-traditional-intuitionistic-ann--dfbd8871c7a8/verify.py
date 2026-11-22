"""Independent finite checks for the announcement-necessity frame correspondence.

Uses only Python's standard library. A complete search over finite frames is
supporting evidence; the general all-cardinalities result has a symbolic proof.
"""
from itertools import product


def matrices(n):
    for mask in range(1 << (n * n)):
        yield tuple(tuple((mask >> (i * n + j)) & 1 for j in range(n))
                    for i in range(n))


def preorders(n):
    for leq in matrices(n):
        if all(leq[i][i] for i in range(n)) and all(
            not (leq[i][j] and leq[j][k]) or leq[i][k]
            for i, j, k in product(range(n), repeat=3)
        ):
            yield leq


def upsets(leq):
    n = len(leq)
    return [s for s in range(1 << n) if all(
        not ((s >> i) & 1 and leq[i][j]) or (s >> j) & 1
        for i, j in product(range(n), repeat=2)
    )]


def has(s, i):
    return bool(s & (1 << i))


def criterion(leq, rel):
    n = len(leq)
    for v, u, w in product(range(n), repeat=3):
        if rel[v][u] and leq[u][w]:
            if not any(
                leq[v][vp] and rel[vp][up] and leq[up][w]
                and (leq[v][up] or leq[w][up])
                for vp, up in product(range(n), repeat=2)
            ):
                return False
    return True


def atomic_reduction_valid(leq, rel):
    # Evaluate [p] Box q and (p -> Box [p]q) from the forcing clauses,
    # not by using the theorem's first-order relational criterion.
    n = len(leq)
    for p, q, s in product(upsets(leq), upsets(leq), range(n)):
        lhs = all(
            not (leq[s][v] and has(p, v) and rel[v][u] and has(p, u))
            or has(q, u)
            for v, u in product(range(n), repeat=2)
        )
        rhs = all(
            not (leq[s][v] and has(p, v) and rel[v][u]
                 and leq[u][w] and has(p, w))
            or has(q, w)
            for v, u, w in product(range(n), repeat=3)
        )
        if lhs != rhs:
            return False
    return True


def ordinary_confluence(leq, rel):
    n = len(leq)
    return all(
        not (rel[v][u] and leq[u][w]) or any(
            leq[v][vp] and rel[vp][w] for vp in range(n)
        )
        for v, u, w in product(range(n), repeat=3)
    )


def exhaustive_preorders():
    results = []
    for n in (1, 2, 3):
        npre, nframes, nvalid = 0, 0, 0
        for leq in preorders(n):
            npre += 1
            for rel in matrices(n):
                prediction = criterion(leq, rel)
                observation = atomic_reduction_valid(leq, rel)
                assert prediction == observation, (n, leq, rel)
                nframes += 1
                nvalid += prediction
        results.append((n, npre, nframes, nvalid))
    assert results == [(1, 1, 2, 2), (2, 4, 64, 56),
                       (3, 29, 14848, 9571)]
    return results


def chain_census():
    results = []
    for n in (2, 3, 4):
        leq = tuple(tuple(int(i <= j) for j in range(n)) for i in range(n))
        valid = strict = 0
        for rel in matrices(n):
            if criterion(leq, rel):
                valid += 1
                strict += not ordinary_confluence(leq, rel)
        results.append((n, valid, strict))
    assert results == [(2, 12, 1), (3, 224, 26), (4, 14592, 1215)]
    return results


def examples():
    leq = ((1, 1), (0, 1))
    strict = ((1, 0), (0, 0))
    failure = ((0, 0), (1, 0))
    assert criterion(leq, strict) and not ordinary_confluence(leq, strict)
    assert not criterion(leq, failure)
    assert atomic_reduction_valid(leq, strict)
    assert not atomic_reduction_valid(leq, failure)


if __name__ == '__main__':
    examples()
    counts = exhaustive_preorders()
    chains = chain_census()
    print('VERIFY_OK all_preorders=' + repr(counts) + ' chain_counts=' + repr(chains))
