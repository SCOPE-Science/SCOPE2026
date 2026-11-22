"""Standalone exact validator of homopolymer-free one-erasure code certificates.

Usage: python3 verify.py   (run beside cert5.json and cert7.json)
No third-party dependencies are required.
"""
import itertools
import json
from pathlib import Path


def hd(a, b):
    return sum(u != v for u, v in zip(a, b))


def check(n, expected_code, expected_cycles, expected_pairs):
    evidence = json.loads((Path(__file__).resolve().parent / ('cert%d.json' % n)).read_text(encoding='utf-8'))
    assert evidence['length'] == n and evidence['alphabet'] == '012'
    words = {''.join(a) for a in itertools.product('012', repeat=n)
             if all(a[j] != a[j + 1] for j in range(n - 1))}
    assert len(words) == 3 * (2 ** (n - 1))
    code = evidence['codewords']
    assert len(code) == expected_code and len(set(code)) == len(code)
    assert set(code) <= words
    for i, x in enumerate(code):
        for y in code[i + 1:]:
            assert hd(x, y) >= 2, ('bad code pair', x, y)
    cycles = evidence['odd_cycles']
    pairs = evidence['paired_edges']
    assert len(cycles) == expected_cycles and len(pairs) == expected_pairs
    covered = []
    for cyc in cycles:
        assert len(cyc) % 2 == 1 and len(cyc) == 3 * n
        assert len(cyc) == len(set(cyc))
        assert all(hd(cyc[j], cyc[(j + 1) % len(cyc)]) == 1 for j in range(len(cyc)))
        covered.extend(cyc)
    for a, b in pairs:
        assert a != b and hd(a, b) == 1
        covered.extend((a, b))
    assert len(covered) == len(words) and set(covered) == words
    assert len(set(covered)) == len(covered)
    bound = sum(len(cyc) // 2 for cyc in cycles) + len(pairs)
    assert bound == len(code) == expected_code
    print('CERT_OK', n, 'states', len(words), 'code', len(code),
          'cycles', len(cycles), 'edges', len(pairs))


if __name__ == '__main__':
    check(5, 23, 2, 9)
    check(7, 92, 8, 12)
    print('VERIFY_OK')
