"""Exact bounded-depth non-contingency types on fixed irreflexive paths.
Python 3 stdlib. Recomputes all 2^n valuations and all n roots.
"""
from collections import defaultdict


def path_types(n):
    states = tuple((mask, root) for mask in range(1 << n) for root in range(n))
    colors = {s: ((s[0] >> s[1]) & 1) for s in states}
    profiles = []
    table = None
    for depth in range(2*n+5):
        # Each previous signature is an immutable tuple built recursively;
        # assigning consecutive IDs cannot change equality of signatures.
        distinct = sorted(set(colors.values()), key=repr)
        ids = {v: i for i, v in enumerate(distinct)}
        colors = {s: ids[color] for s, color in colors.items()}
        profiles.append(len(distinct))
        if depth and profiles[-1] == profiles[-2]:
            return profiles[:-1], colors
        next_colors = {}
        for mask, root in states:
            successors = []
            if root:
                successors.append(colors[(mask, root-1)])
            if root < n-1:
                successors.append(colors[(mask, root+1)])
            signature = tuple(sorted(successors)) if len(set(successors)) == 2 else ()
            next_colors[(mask, root)] = (colors[(mask, root)], signature)
        colors = next_colors
    raise AssertionError('Not stabilized within chosen safe limit')

EXPECTED = {
 2:[2], 3:[2,4], 4:[2,4,12,14],
 5:[2,4,14,36,40], 6:[2,4,14,52,110,122],
 7:[2,4,14,58,172,274,286],
 8:[2,4,14,58,220,504,728,758],
 9:[2,4,14,58,242,738,1316,1688,1720],
}
for n, expectation in EXPECTED.items():
    counts, stable = path_types(n)
    assert counts == expectation, (n, counts)
    print(f'P{n}: depths 0..{len(counts)-1}: {counts}, stabilized')
print('REFINEMENT_OK')
