"""Independent exact finite checks of closed-neighborhood shattering in Hamming graphs.

Run: python check_closed_hamming.py
Standard Python 3, no external dependencies. The general theorem is proved separately.
"""
from itertools import combinations, product
from math import comb
from random import Random


def expected(d, q):
    v = q ** d
    if d == 1:
        return (1, 0, 0, 0)
    if (d, q) == (2, 2):
        return (1, v, 0, 0)
    pairs = v * (d * (q - 1) + comb(d, 2) * (q - 1) ** 2) // 2
    if d >= 3:
        triples = v * (
            comb(d, 2) * (q - 1) ** 2
            + comb(d, 3) * (q - 1) ** 3
            + d * (d - 1) * comb(q - 1, 2) * (q - 1)
        )
    elif q >= 4:
        triples = v * (q - 1) ** 2 * (q - 2)
    else:
        triples = 0
    return (1, v, pairs, triples)


def hamming(x, y):
    return sum(a != b for a, b in zip(x, y))


def check(d, q, sample=False):
    words = tuple(product(range(q), repeat=d))
    n = len(words)
    # An entirely explicit incidence matrix, independent of the symbolic proof.
    inc = tuple(tuple(int(hamming(c, s) <= 1) for s in words) for c in words)
    predicted = expected(d, q)
    counts = [1, 0, 0, 0, 0]
    tests = 0
    rng = Random(1729 + 101 * d + q)
    for k in range(1, 5):
        if k > n:
            break
        if sample and k == 4:
            sets = set()
            for _ in range(9000):
                sets.add(tuple(sorted(rng.sample(range(n), k))))
        else:
            sets = combinations(range(n), k)
        for indices in sets:
            traces = set()
            for row in inc:
                traces.add(sum(row[index] << j for j, index in enumerate(indices)))
                if len(traces) == 1 << k:
                    break
            good = len(traces) == 1 << k
            counts[k] += good
            tests += 1
            if k == 3:
                # Structural classification obtained from coordinates, checked
                # independently against the raw incidence traces.
                pattern = False
                for c in words:
                    if any(hamming(c, words[i]) > 1 for i in indices):
                        continue
                    arms = []
                    centercount = 0
                    for idx in indices:
                        s = words[idx]
                        diff = [t for t in range(d) if s[t] != c[t]]
                        if not diff:
                            centercount += 1
                        else:
                            arms.append(diff[0])
                    if centercount == 1:
                        pattern |= d >= 3 and len(set(arms)) == 2
                    elif centercount == 0:
                        groups = sorted(arms.count(t) for t in set(arms))
                        pattern |= (groups == [1, 1, 1]) or (
                            groups == [1, 2] and (d >= 3 or q >= 4)
                        )
                assert pattern == good, (d, q, indices, 'triple shape')
            if k == 4:
                assert not good, (d, q, indices, 'four-point counterexample')
    assert tuple(counts[:4]) == predicted, (d, q, counts, predicted)
    return tests, tuple(counts[:4])


def main():
    total = 0
    full = [(1, 2), (1, 5), (2, 2), (2, 3), (2, 4), (2, 5),
            (3, 2), (3, 3), (3, 4), (4, 2), (5, 2)]
    for d, q in full:
        tested, counts = check(d, q)
        total += tested
        print(f'FULL d={d} q={q} supports={tested} counts={counts}', flush=True)
    for d, q in [(4, 3)]:
        # Full exhaustive sizes one through three; reproducible sample of size four.
        tested, counts = check(d, q, sample=True)
        total += tested
        print(f'SAMPLED-FOUR d={d} q={q} supports={tested} counts={counts}', flush=True)
    print(f'ALL_CLOSED_HAMMING_CHECKS_PASS grids={len(full) + 1} supports={total}', flush=True)


if __name__ == '__main__':
    main()
