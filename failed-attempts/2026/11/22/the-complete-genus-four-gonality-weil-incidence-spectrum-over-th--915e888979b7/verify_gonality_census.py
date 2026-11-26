#!/usr/bin/env python3
"""Verify the incidence of ground-field gonality and Jacobian Weil classes.

Usage:
    python verify_gonality_census.py [certificate.hex] [Xarles_source.txt]

The compact certificate is an independently inspectable derived table, not a
copy of any paper. With the optional published Magma data file this script
also checks every record against the original curve equations and Weil labels.
"""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import re
import sys

QUADRICS = (
    'X^2 + X*Y + Y^2 + Z*T',  # anisotropic, no rational ruling
    'X*Y + T^2',             # cone, one rational ruling
    'X*Y + Z*T',             # split, two rational rulings
)
EXPECTED_CLASSES = {'2': 99, '3': 230, '4': 112, '5': 1,
                    '23': 68, '24': 29, '34': 60, '234': 21}
EXPECTED_GONALITIES = {2: 264, 3: 526, 4: 253, 5: 1}
EXPECTED_BY_POINT_COUNT = [40, 151, 260, 267, 175, 100, 39, 11, 1]
EXPECTED_HYP_BY_POINT_COUNT = [9, 32, 58, 66, 58, 32, 9, 0, 0]


def enclosed_lists(source: str):
    """Split a sequence of bracketed lists without evaluating Magma code."""
    depth = 0
    start = None
    output = []
    for index, char in enumerate(source):
        if char == '[':
            if depth == 0:
                start = index
            depth += 1
        elif char == ']':
            depth -= 1
            if depth < 0:
                raise ValueError('excess right bracket')
            if depth == 0:
                output.append(source[start:index+1])
    if depth:
        raise ValueError('unclosed bracket')
    return output


def parse_primary(source: str):
    import ast
    blocks = enclosed_lists(source)
    if len(blocks) != 3:
        raise AssertionError(('number of primary blocks', len(blocks)))
    nrows = [ast.literal_eval(x) for x in enclosed_lists(blocks[0][1:-1])]
    hrows = [enclosed_lists(x[1:-1]) for x in enclosed_lists(blocks[1][1:-1])]
    trows = [enclosed_lists(x[1:-1]) for x in enclosed_lists(blocks[2][1:-1])]
    if len(nrows) != len(hrows) or len(nrows) != len(trows):
        raise AssertionError('misaligned original source lists')
    rows = []
    for pts, hypo, trig in zip(nrows, hrows, trows):
        quadric_counts = [0, 0, 0]
        for pair in trig:
            match = re.match(r'\[\s*(.*?),\s*\n', pair)
            if not match:
                raise AssertionError('missing quadric in source pair')
            if match.group(1) not in QUADRICS:
                raise AssertionError(('unexpected quadric', match.group(1)))
            quadric_counts[QUADRICS.index(match.group(1))] += 1
        rows.append(tuple(pts[:2]) + (len(hypo),) + tuple(quadric_counts))
    return rows


def verify(certificate: Path, primary=None):
    raw_lines = certificate.read_text(encoding='ascii').splitlines()
    assert len(raw_lines) == 31
    assert all(len(s) == 120 and re.fullmatch('[0-9a-z]+', s) for s in raw_lines)
    raw = ''.join(raw_lines)
    rows = [tuple(int(raw[i + j], 36) for j in range(6))
            for i in range(0, len(raw), 6)]
    assert len(rows) == 620, len(rows)
    assert rows[0] == (0, 0, 0, 1, 0, 0)
    assert sum(h for _, _, h, _, _, _ in rows) == 264
    assert sum(n for _, _, _, n, _, _ in rows) == 254
    assert sum(c for _, _, _, _, c, _ in rows) == 274
    assert sum(s for _, _, _, _, _, s in rows) == 252
    assert sum(sum(r[2:]) for r in rows) == 1044
    assert [sum(r[2] for r in rows if r[0] == j) for j in range(9)] == EXPECTED_HYP_BY_POINT_COUNT
    assert [sum(sum(r[2:]) for r in rows if r[0] == j) for j in range(9)] == EXPECTED_BY_POINT_COUNT
    assert all((b-a) % 2 == 0 and b>=a for a,b,*_ in rows)
    assert sum(1 for a,b,*_ in rows if a==0 and b==0) == 3
    assert sum(1 for a,b,_,n,_,_ in rows if a==b==0 and n>0) == 1
    classes, gonalities = Counter(), Counter()
    for index, (n1, n2, h, non, cone, split) in enumerate(rows):
        # Hyperelliptic degree 2, split and cone degree 3, nonsplit degree 4
        # except the unique nonsplit curve without any effective divisor degree 2.
        is_excessive = n1 == n2 == 0 and non > 0
        counts = {2: h, 3: cone + split,
                  4: non - int(is_excessive), 5: int(is_excessive)}
        assert all(v >= 0 for v in counts.values())
        classes[''.join(str(g) for g in (2,3,4,5) if counts[g])] += 1
        gonalities.update(counts)
    assert dict(gonalities) == EXPECTED_GONALITIES, gonalities
    assert dict(classes) == EXPECTED_CLASSES, classes
    assert sum(classes.values()) == len(rows)
    assert sum(v for k,v in classes.items() if len(k)>1) == 178
    assert classes['234'] == 21
    if primary is not None:
        source_rows = parse_primary(primary.read_text(encoding='utf-8'))
        assert source_rows == rows, 'derived certificate differs from source'
        print('PRIMARY_MAGMA_DATA_FULLY_RECONCILED')
    print('GENUS4_F2_GONALITY_WEIL_INCIDENCE_VERIFIED')
    print('isomorphism_classes=1044; Weil_classes=620')
    print('curve_gonalities=', dict(sorted(gonalities.items())))
    print('Weil_class_gonality_support=', dict(sorted(classes.items())))


if __name__ == '__main__':
    certify = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('weil_gonality_certificate.hex')
    source = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    verify(certify, source)
