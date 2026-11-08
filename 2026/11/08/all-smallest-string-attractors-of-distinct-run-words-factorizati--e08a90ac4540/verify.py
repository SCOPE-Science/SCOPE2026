"""Standalone definition-level finite checks of the distinct-run attractor classification."""
from itertools import product
from math import comb


def direct_attractor(word, positions):
    """Check the definition using every distinct factor and all its occurrences."""
    spans = {}
    n = len(word)
    for i in range(n):
        for j in range(i + 1, n + 1):
            spans.setdefault(word[i:j], []).append((i, j))
    return all(any(any(i <= p < j for p in positions) for i, j in v)
               for v in spans.values())


def boundary_characterization(lengths, positions):
    endpoints = []
    start = 0
    for a in lengths:
        endpoints.append((start, start + a - 1))
        start += a
    return all(positions[i] == endpoints[i][1]
               or positions[i+1] == endpoints[i+1][0]
               for i in range(len(lengths) - 1))


def formula(lengths):
    answer = 1
    surplus = 0
    for a in lengths:
        if a == 1:
            if surplus:
                answer *= 1 + surplus
                surplus = 0
        else:
            surplus += a - 1
    if surplus:
        answer *= 1 + surplus
    return answer


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for a in range(1, total - parts + 2):
        for tail in compositions(total-a, parts-1):
            yield (a,) + tail


def verify():
    tested_vectors = 0
    tested_selections = 0
    for q in range(2, 6):
        for lengths in product(range(1, 4), repeat=q):
            if sum(lengths) > 12:
                continue
            word = ''.join(chr(65+i)*a for i, a in enumerate(lengths))
            ranges = []
            offset = 0
            for a in lengths:
                ranges.append(range(offset, offset + a))
                offset += a
            count = 0
            for sel in product(*ranges):
                direct = direct_attractor(word, sel)
                criterion = boundary_characterization(lengths, sel)
                assert direct == criterion, (lengths, sel, direct, criterion)
                count += direct
                tested_selections += 1
            assert count == formula(lengths), (lengths, count, formula(lengths))
            tested_vectors += 1
    coefficient_checks = 0
    for q in range(2, 8):
        for n in range(q, q + 9):
            total = sum(formula(c) for c in compositions(n, q))
            closed = sum(comb(q-1, j) * comb(n-j, q)
                         for j in range(min(q-1, n-q) + 1))
            assert total == closed, (q, n, total, closed)
            coefficient_checks += 1
    print(f'PASS parameter vectors={tested_vectors}; direct minima={tested_selections}; '
          f'global generating-function coefficients={coefficient_checks}')

if __name__ == '__main__':
    verify()
