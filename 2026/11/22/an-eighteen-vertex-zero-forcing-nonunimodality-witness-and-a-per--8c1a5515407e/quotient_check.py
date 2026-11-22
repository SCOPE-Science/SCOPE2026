#!/usr/bin/env python3
"""Exact block-state zero-forcing certificate, requiring Python 3.8+."""
SIZES = (1,1,1,2,1,1,1,1,2,3,2,2)
MASKS = (3721,3628,3646,511,3708,3550,3768,3817,3624,2007,3063,3575)

def success(w):
    # Every omitted vertex belongs to a distinct block.
    while w:
        force = 0
        for j in range(12):
            if SIZES[j] - ((w >> j) & 1) < 1:
                continue
            candidates = MASKS[j] & w
            if candidates and (candidates & (candidates - 1)) == 0:
                force = candidates
                break
        if not force:
            return False
        w ^= force
    return True

counts = {k: [0,0,0] for k in (3,4,5)}
for w in range(1 << 12):
    k = w.bit_count()
    if k not in counts or not success(w):
        continue
    multiplicity = 1
    for j in range(12):
        if w & (1 << j):
            multiplicity *= SIZES[j]
    counts[k][0] += 1
    counts[k][1] += multiplicity
    if w & (1 << 3):
        counts[k][2] += multiplicity // SIZES[3]
expected = {3: [214,680,112], 4: [247,678,64], 5: [214,690,68]}
assert counts == expected, (counts, expected)
for k in (3,4,5):
    print('MISSING', k, 'MASKS', counts[k][0], 'BASE', counts[k][1], 'SLOPE', counts[k][2])
print('QUOTIENT_4096_AND_AFFINE_SLOPES_PASS')
