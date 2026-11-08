#!/usr/bin/env python3
"""Exact verification of dimension-three locality-two batch-code witnesses."""
import json
from itertools import combinations_with_replacement
from pathlib import Path

BASE = Path(__file__).resolve().parent
cert = json.loads((BASE / 'certificates' / 'recovery_witnesses.json').read_text(encoding='utf8'))
assert set(cert) == {'6', '7'}
for t, expected_columns, expected_rows in (
    (6, [a for a in range(1,7) for _ in range(2)], 924),
    (7, [a for a in range(1,7) for _ in range(2)]+[7], 1716),
):
    entry = cert[str(t)]
    assert set(entry)== {'columns', 'witnesses'}
    columns = entry['columns']
    assert columns == expected_columns
    assert (1 in columns and 2 in columns and 4 in columns)
    witness_rows = entry['witnesses']
    assert len(witness_rows) == expected_rows
    count = 0
    for targets, subsets in zip(combinations_with_replacement(range(1,8),t),witness_rows):
        assert type(subsets) is list and len(subsets)==t
        used=0
        for target,mask in zip(targets,subsets):
            assert type(mask) is int and mask > 0
            assert mask < (1 << len(columns))
            assert mask.bit_count() in (1,2)
            assert not (mask & used)
            used |= mask
            recovered = 0
            for j,c in enumerate(columns):
                if (mask >> j)&1: recovered ^= c
            assert recovered == target
        count += 1
    assert count == expected_rows
    print(f'UPPER_OK t={t} all_multisets={count} columns={len(columns)}')

# Lower obstruction: any n nonzero columns use n distributed among 7 labels.
# Let N_a be the maximum number of disjoint size<=2 recoveries of a.
# Sum_a N_a = 4*n - 1/2 * sum_{i<j} |x_i-x_j|.
# The discrepancy is minimized by balanced x_i.
for n, target, expected_discrepancy in [(11,6,12),(12,7,10)]:
    r = n % 7
    assert expected_discrepancy == r*(7-r)
    capacity_sum_bound_twice = 8*n-expected_discrepancy
    assert capacity_sum_bound_twice < 14*target
    # Exact finite-domain cross-check of the balancing bound.
    count = 0
    smallest = None
    def visit(prefix, left):
        global count,smallest
        if len(prefix)==6:
            xs = prefix + [left]
            discrepancy = sum(abs(xs[i]-xs[j]) for i in range(7) for j in range(i+1,7))
            smallest=discrepancy if smallest is None else min(smallest,discrepancy)
            count += 1
            return
        for k in range(left+1): visit(prefix+[k],left-k)
    visit([],n)
    assert smallest == expected_discrepancy
    print(f'LOWER_OK no_length_{n}_code_for_{target}_requests compositions={count} min_discrepancy={smallest}')
print('ALL_CERTIFICATES_OK')
