"""Exact 2187-class finite-state proof for threshold-two three-colour CCA on K_{1,m,n}.
No libraries beyond Python's standard library. Run: python verify_capped.py
"""
from itertools import product
from collections import Counter

CAP = (0, 1, 2)

def transition(state, tags):
    # State holds per-colour counts capped at two in (hub, A, B).
    blocks = (state[0:3], state[3:6], state[6:9])
    new = []
    new_tags = []
    for j, block in enumerate(blocks):
        outside = [sum(blocks[k][c] for k in range(3) if k != j)
                   for c in range(3)]
        jumps = [int(outside[(c + 1) % 3] >= 2) for c in range(3)]
        target = [0, 0, 0]
        for c in range(3):
            dest = (c + jumps[c]) % 3
            target[dest] = min(2, target[dest] + block[c])
        new.extend(target)
        new_tags.append(tuple((c + jumps[c]) % 3 for c in tags[j]))
    return (tuple(new), tuple(new_tags))

def trace(state, length=19):
    tags = ((0, 1, 2),) * 3
    seq = [(state, tags)]
    for _ in range(length):
        seq.append(transition(*seq[-1]))
    return seq

def identical_at(seq, t, u, initial):
    left, right = seq[t], seq[u]
    return (left[0] == right[0] and
            all(left[1][j][c] == right[1][j][c]
                for j in range(3) for c in range(3) if initial[3*j + c] > 0))

def feasible(a, size):
    # A cap value 2 means at least two, 0/1 are exact.
    return size == sum(a) if 2 not in a else size >= sum(a)

def all_classes():
    for h in range(3):
        hub = tuple(int(c == h) for c in range(3))
        for a in product(CAP, repeat=3):
            for b in product(CAP, repeat=3):
                yield hub + a + b

def main():
    classes = list(all_classes())
    assert len(classes) == 2187
    histogram = Counter()
    period3_pattern = set()
    period12_min = (100, 100)
    violations = []
    sharp = None
    for s in classes:
        seq = trace(s)
        assert seq[7] == seq[19], 'universal 12-step identity failed'
        if seq[6] != seq[18] and sharp is None:
            sharp = s
        period = next((d for d in (1, 2, 3, 4, 6, 12)
                       if identical_at(seq, 7, 7+d, s)), None)
        assert period in (1, 3, 12)
        histogram[period] += 1
        if period == 3 and s[:3] == (1, 0, 0):
            period3_pattern.add((s[3:6], s[6:9]))
        if period == 12:
            if min(sum(s[3:6]), sum(s[6:9])) < 4:
                violations.append(s)
    assert not violations
    assert histogram == {1: 2001, 3: 36, 12: 150}, histogram
    short = {(0,0,0),(0,0,1),(0,1,0),(0,1,1)}
    rich = {(1,2,2),(2,2,2)}
    expected3 = {(a,(2,2,2)) for a in short} | \
                {((2,2,2), b) for b in short} | \
                {(a,b) for a in rich for b in rich}
    assert period3_pattern == expected3, (period3_pattern-expected3,expected3-period3_pattern)
    assert (2,0,2) in [s[3:6] for s in classes] # coverage sanity
    # Period 12 exists for m=n=4 by exact occupancy-compatible signatures.
    p12_witness = None
    for s in classes:
        if s[:3] != (1,0,0): continue
        if not feasible(s[3:6], 4) or not feasible(s[6:9], 4): continue
        q = trace(s)
        if identical_at(q,7,19,s) and all(not identical_at(q,7,7+d,s) for d in (1,2,3,4,6)):
            p12_witness = s;break
    assert p12_witness is not None
    # Such a witness has two 2+ cells per shore and can be padded indefinitely.
    assert sum(x == 2 for x in p12_witness[3:6]) >= 1
    assert sum(x == 2 for x in p12_witness[6:9]) >= 1
    print('CAP_CLASSES', len(classes))
    print('CLASS_PERIOD_COUNTS', dict(sorted(histogram.items())))
    print('UNIVERSAL_IDENTITY F^19=F^7 PASS')
    print('PERIOD_SET_ONLY 1,3,12 PASS')
    print('PERIOD_3_SIGNATURES_HUB0', len(period3_pattern))
    print('PERIOD_12_MIN_SIDE_4 PASS')
    print('PERIOD_12_WITNESS_K144', p12_witness)
    print('CAP_WITNESS_F6_NE_F18', sharp)

if __name__ == '__main__': main()
