"""Reproduce the full six-letter unclustered-BWT input-run spectrum.

Run with `python3 verify.py` from this directory. Only Python's standard
library is needed. This verifies two separate exhaustive enumerations and
all records of the accompanying normalized census.
"""
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path

import cycle_enumerator as c
import rotation_enumerator as r

EXPECTED = {
    (3, 4): 5, (3, 6): 1,
    (4, 4): 14, (4, 5): 44, (4, 6): 20,
    (5, 5): 72, (5, 6): 108,
    (6, 6): 120,
}

def part(word):
    return tuple(sorted(Counter(word).values(), reverse=True))

def run_checks():
    images = c.census()
    preimages = r.census()
    assert set(images) == set(preimages)
    assert all(images[key] == preimages[key][1] for key in images)
    assert c.histogram() == r.histogram() == Counter(EXPECTED)
    assert len(images) == 384

    expected_partitions = {
        (3, (2, 2, 2), 4): 1,
        (3, (2, 2, 2), 6): 1,
        (3, (3, 2, 1), 4): 4,
        (4, (2, 2, 1, 1), 4): 14,
        (4, (2, 2, 1, 1), 5): 36,
        (4, (2, 2, 1, 1), 6): 20,
        (4, (3, 1, 1, 1), 5): 8,
        (5, (2, 1, 1, 1, 1), 5): 72,
        (5, (2, 1, 1, 1, 1), 6): 108,
        (6, (1, 1, 1, 1, 1, 1), 6): 120,
    }
    ph = Counter((t, part(L), runs) for (t, L), runs in images.items())
    assert ph == Counter(expected_partitions)

    lines = ['alphabet_size\tbwt_image\tlyndon_input\tcyclic_runs\tpartition']
    for (t, last), (word, runs) in sorted(preimages.items()):
        lines.append(f"{t}\t{''.join(map(str,last))}\t{''.join(map(str,word))}\t{runs}\t{','.join(map(str,part(last)))}")
    text = '\n'.join(lines) + '\n'
    assert Path(__file__).with_name('census.tsv').read_text(encoding='utf-8') == text

    for q in range(1, 12):
        predicted = {j: sum(v * comb(q, t) for (t, rr), v in EXPECTED.items()
                            if rr == j and t <= q) for j in (4, 5, 6)}
        brute = Counter()
        for L in product(range(q), repeat=6) if q <= 4 else []:
            if any(L[i] == L[i+1] for i in range(5)):
                continue
            if c.single_cycle(c.lf_permutation(L)):
                brute[sum(x != y for x,y in zip(L, sorted(L)))] += 1
        if q <= 4:
            assert all(predicted[j] == brute[j] for j in (4, 5, 6))
        assert sum(predicted.values()) == sum(v * comb(q,t) for (t,_),v in EXPECTED.items() if t <= q)
    print('BWT_LENGTH_SIX_CENSUS_OK 384 8_HISTOGRAM_CELLS 10_PARTITION_CELLS')

if __name__ == '__main__':
    run_checks()
