#!/usr/bin/env python3
"""Exact arithmetic checker for a finite binary three-deletion two-list profile.

Run: python3 check.py
Only the Python standard library is required. All subsequence tests,
constraints, and rational upper bounds are reconstructed from definitions.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json


def is_subsequence(small, large):
    # Independent greedy subsequence membership test, not deletion-position enumeration.
    pos = 0
    for symbol in large:
        if pos < len(small) and symbol == small[pos]:
            pos += 1
    return pos == len(small)


def check(entry):
    n, m, optimum = entry['n'], entry['n'] - 3, entry['optimum']
    words = [''.join(v) for v in product('01', repeat=n)]
    outputs = [''.join(v) for v in product('01', repeat=m)]
    witness = entry['witness']
    assert 3 <= n <= 10 and isinstance(optimum, int)
    assert len(set(witness)) == len(witness) == optimum
    assert all(w in words for w in witness)

    capacities = {y: sum(is_subsequence(y, x) for x in witness) for y in outputs}
    assert all(0 <= count <= 2 for count in capacities.values())

    den = entry['dual_denominator']
    assert isinstance(den, int) and den > 0
    given = entry['dual_weights']
    assert all(y in outputs and isinstance(v, int) and v >= 0 for y, v in given.items())
    weights = {y: Fraction(given.get(y, 0), den) for y in outputs}

    # The coefficient assigned to each word not covered to weight one by
    # the output weights is an exact nonnegative supplementary dual weight.
    supplement = {}
    for x in words:
        exposure = sum((weights[y] for y in outputs if is_subsequence(y, x)), Fraction(0))
        supplement[x] = max(Fraction(0), Fraction(1) - exposure)
        assert exposure + supplement[x] >= 1

    bound = 2 * sum(weights.values(), Fraction(0)) + sum(supplement.values(), Fraction(0))
    assert bound == Fraction(entry['dual_bound'])
    assert optimum <= bound < optimum + 1
    return n, optimum, str(bound), len(words), len(outputs), len(witness), sum(v > 0 for v in supplement.values())


def main():
    data = json.loads(Path(__file__).with_name('CERTIFICATE.json').read_text(encoding='utf-8'))
    assert data['model'] == {'alphabet': '01', 'deletions': 3, 'max_list_size': 2}
    assert [e['n'] for e in data['entries']] == list(range(3, 11))
    for e in data['entries']:
        print('PASS n=%s optimum=%s upper=%s source_words=%s outputs=%s witness=%s slack=%s' % check(e))
    print('ALL EIGHT EXACT OPTIMA VERIFIED')


if __name__ == '__main__':
    main()
