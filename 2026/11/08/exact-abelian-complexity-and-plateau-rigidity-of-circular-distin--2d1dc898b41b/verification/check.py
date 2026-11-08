"""Finite checks of the circular Parikh-complexity classification.
Run with Python 3: python check.py. This is corroboration, not a proof.
"""
from itertools import product
from random import Random

def direct(lengths, r):
    word = tuple(i for i, size in enumerate(lengths) for _ in range(size))
    p = len(word)
    return len({tuple(sum(word[(s+j) % p] == i for j in range(r))
                      for i in range(len(lengths))) for s in range(p)})

def formula(lengths, r):
    p = sum(lengths)
    r %= p
    if r == 0:
        return 1
    return p - sum(max(0,a-r)+max(0,a-p+r) for a in lengths)

def check(lengths):
    p = sum(lengths)
    profile = [direct(lengths,r) for r in range(p)]
    expect = [formula(lengths,r) for r in range(p)]
    assert profile == expect, (lengths,profile,expect)
    m = max(lengths)
    plateau = set(range(min(m,p-m),max(m,p-m)+1))
    maximizers = {r for r in range(1,p) if profile[r] == max(profile[1:])}
    assert maximizers == plateau, (lengths,maximizers,plateau)
    assert max(profile[1:]) == min(p,2*(p-m))
    assert profile[1:] == profile[:0:-1]
    diffs = [profile[r+1]-profile[r] for r in range(1,p-1)]
    assert all(diffs[i]>=diffs[i+1] for i in range(len(diffs)-1))

count=0
for q, upper in ((3,6),(4,5),(5,4),(6,3)):
    for lengths in product(range(1,upper+1), repeat=q):
        check(lengths)
        count += 1
rng = Random(20261105)
for i in range(750):
    q = rng.randrange(3,9)
    check(tuple(rng.randrange(1,13) for _ in range(q)))
    count += 1
print('PASS: %d run-length profiles with exact Parikh counts, plateau, symmetry and concavity' % count)
