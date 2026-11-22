"""Reproducible integral discrete-Morse certificate for transposition word complexes.

Execute: python3 transposition_morse.py
Uses only the Python standard library; no external data.
"""

from itertools import combinations
from collections import Counter
from pathlib import Path
import json


def enumerate_cells(n):
    by_dim = [set() for _ in range(n)]
    for i, j in combinations(range(1, n + 1), 2):
        word = list(range(1, n + 1))
        word[i - 1], word[j - 1] = word[j - 1], word[i - 1]
        for bits in range(1, 1 << n):
            face = tuple(word[t] for t in range(n) if bits & (1 << t))
            by_dim[len(face) - 1].add(face)
    cells = [face for layer in by_dim for face in sorted(layer)]
    address = {face: t for t, face in enumerate(cells)}
    low, up = [[] for _ in cells], [[] for _ in cells]
    for t, face in enumerate(cells):
        for j in range(len(face)):
            if len(face) == 1:
                continue
            s = address[face[:j] + face[j + 1:]]
            low[t].append(s)
            up[s].append(t)
    return cells, low, up


def verify_boundary_squared(cells, low):
    for upper, face in enumerate(cells):
        if len(face) < 3:
            continue
        coefficient = {}
        for j, mid in enumerate(low[upper]):
            for h, lower in enumerate(low[mid]):
                coefficient[lower] = coefficient.get(lower, 0) + (-1) ** (j+h)
        assert all(value == 0 for value in coefficient.values()), (
            'nonzero boundary squared', face, coefficient)


def elementary_matching(cells, low, up):
    n = len(cells)
    alive = [True] * n
    upper_counts = [len(upper) for upper in up]
    pairs, critical = [], []
    count_alive = n
    while count_alive:
        free = [i for i in range(n) if alive[i] and upper_counts[i] == 1]
        if free:
            i = max(free)
            j = next(t for t in up[i] if alive[t])
            assert len(cells[j]) == len(cells[i]) + 1
            removed = (i, j)
            pairs.append((i, j))
        else:
            i = max(t for t in range(n) if alive[t])
            assert not any(alive[t] for t in up[i]), 'critical cell must be maximal'
            critical.append(i)
            removed = (i,)
        for t in removed:
            assert alive[t]
            alive[t] = False
            count_alive -= 1
        for t in removed:
            for lower in low[t]:
                if alive[lower]:
                    upper_counts[lower] -= 1
    return pairs, critical


def verify_acyclic(cells, low, pairs):
    matched = set(pairs)
    arrows = [[] for _ in cells]
    for upper, lowers in enumerate(low):
        for lower in lowers:
            if (lower, upper) in matched:
                arrows[lower].append(upper)
            else:
                arrows[upper].append(lower)
    visited = [0] * len(cells)

    def visit(i):
        assert visited[i] != 1, 'closed directed V-path'
        if visited[i] == 2:
            return
        visited[i] = 1
        for j in arrows[i]:
            visit(j)
        visited[i] = 2

    for i in range(len(cells)):
        if visited[i] == 0:
            visit(i)


def verify_integral_reduction(cells, low, pairs, critical):
    # Signed deletion differential on the actual ordered-word cells.
    boundary = [{} for _ in cells]
    for t, face in enumerate(cells):
        if len(face) == 1:
            continue
        boundary[t] = {s: 1 if j % 2 == 0 else -1 for j, s in enumerate(low[t])}
    remaining = set(range(len(cells)))
    for i, j in pairs:
        coeff = boundary[j].get(i, 0)
        assert coeff in (-1, 1), ('nonunit integral pivot', cells[i], cells[j], coeff)
        for z in tuple(remaining):
            if z != j and len(cells[z]) == len(cells[j]) and i in boundary[z]:
                quotient = boundary[z][i] // coeff
                for target, value in boundary[j].items():
                    next_value = boundary[z].get(target, 0) - quotient * value
                    if next_value:
                        boundary[z][target] = next_value
                    else:
                        boundary[z].pop(target, None)
        remaining.remove(i)
        remaining.remove(j)
        for z in remaining:
            boundary[z].pop(i, None)
    assert remaining == set(critical), 'critical cells differ from survivors'
    for i in critical:
        assert not boundary[i], ('nonzero Morse boundary', cells[i], boundary[i])
    return sorted((len(cells[i]) - 1) for i in critical)


def run(n):
    cells, low, up = enumerate_cells(n)
    verify_boundary_squared(cells, low)
    pairs, critical = elementary_matching(cells, low, up)
    verify_acyclic(cells, low, pairs)
    degrees = verify_integral_reduction(cells, low, pairs, critical)
    tally = Counter(len(face)-1 for face in cells)
    return {
        'n': n,
        'f_vector': [tally.get(i, 0) for i in range(n)],
        'cell_count': len(cells),
        'pair_count': len(pairs),
        'critical_words': [''.join(map(str, cells[i])) for i in critical],
        'critical_dimensions': degrees,
        'pairs': [[list(cells[i]), list(cells[j])] for i, j in pairs]
    }


def main():
    expectations = {2: [0], 3: [0, 1], 4: [0, 2, 2, 2], 5: [0, 2, 2, 3]}
    for n in (2, 3, 4, 5):
        result = run(n)
        assert result['critical_dimensions'] == expectations[n], (n, result)
        print('n={}, cells={}, pairs={}, critical={}, f_vector={}'.format(
            n, result['cell_count'], result['pair_count'], result['critical_words'],
            result['f_vector']))
    assert run(5)['cell_count'] == 124
    r5 = run(5)
    assert r5['pair_count'] == 60
    certificate_path = Path(__file__).with_name('MORSE_MATCHING.json')
    if certificate_path.exists():
        certificate = json.loads(certificate_path.read_text(encoding='utf-8'))
        assert certificate['pairs'] == r5['pairs']
        assert certificate['critical_words'] == [list(map(int, word)) for word in r5['critical_words']]
        assert certificate['f_vector'] == r5['f_vector']
        print('all 60 published matching pairs agree with the certificate')
    print('all integer, boundary-squared, and acyclicity checks passed')


if __name__ == '__main__':
    main()
