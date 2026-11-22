"""Exhaustive exact arithmetic check for majority basins on T(6) and KG(6,2).
Usage: python3 verify_iterates.py
No dependencies outside the standard library.
"""
from collections import Counter
from itertools import combinations

PAIRS = tuple(combinations(range(6), 2))
assert len(PAIRS) == 15
EXPECTED = {
    "triangular": {
        "degree": 8,
        "entry": {(1, 0): 164, (1, 1): 8544, (1, 2): 15600,
                  (1, 3): 6660, (2, 0): 1080, (2, 1): 720},
        "basins": {(1, 1): 120, (1, 22): 30, (1, 236): 12,
                   (1, 13678): 2, (2, 2): 180, (2, 4): 360},
    },
    "kneser": {
        "degree": 6,
        "entry": {(1, 0): 502, (1, 1): 4426, (1, 2): 13680,
                  (1, 3): 5040, (2, 0): 5340, (2, 1): 3780},
        "basins": {(1, 1): 360, (1, 10): 140, (1, 10944): 2,
                   (2, 2): 2460, (2, 20): 210},
    },
}

def check(which):
    meet = which == "triangular"
    masks = []
    for i, u in enumerate(PAIRS):
        masks.append(sum(1 << j for j, v in enumerate(PAIRS)
                         if j != i and (len(set(u) & set(v)) == 1) == meet))
    degree = masks[0].bit_count()
    assert all(a.bit_count() == degree for a in masks)
    def update(x):
        answer = 0
        for i, mask in enumerate(masks):
            d = (x & mask).bit_count()
            if 2*d > degree or (2*d == degree and ((x >> i)&1)):
                answer |= 1 << i
        return answer
    f = [update(x) for x in range(1 << 15)]
    entry = Counter()
    basin = Counter()
    orbit_period = {}
    for x in range(1 << 15):
        seq = [x]
        for _ in range(5):
            seq.append(f[seq[-1]])
        assert seq[5] == seq[3], (which, x)
        d = next(t for t in range(4) if seq[t] == seq[t+2])
        p = 1 if seq[d] == seq[d+1] else 2
        assert seq[d] == seq[d+p]
        entry[p, d] += 1
        rep = min(seq[3], seq[4])
        basin[rep] += 1
        orbit_period[rep] = p
    shape = Counter((orbit_period[rep], size) for rep, size in basin.items())
    assert degree == EXPECTED[which]["degree"]
    assert entry == EXPECTED[which]["entry"], (which,entry)
    assert shape == EXPECTED[which]["basins"], (which,shape)
    assert sum(entry.values()) == 32768
    assert sum(basin.values()) == 32768
    print(which, "degree", degree, "entrance", sorted(entry.items()),
          "basin-shape", sorted(shape.items()), "CHECKED 32768")

if __name__ == "__main__":
    for kind in EXPECTED:
        check(kind)
