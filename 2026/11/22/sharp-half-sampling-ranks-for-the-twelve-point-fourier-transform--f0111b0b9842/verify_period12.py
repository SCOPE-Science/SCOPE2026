"""Independent subgroup-period enumeration and modular rank check for Fourier order 12."""
import csv
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
N = 12
P = (1000033, 1001017)
Z = (385966, 72098)

def shift(mask, offset):
    return sum(1 << ((i + offset) % N) for i in range(N) if mask & (1 << i))

def support(mask):
    return tuple(i for i in range(N) if mask & (1 << i))

def stabilizer(mask):
    return tuple(t for t in range(N) if shift(mask, t) == mask)

def period_condition(rmask, cmask):
    stab = stabilizer(rmask)
    # The annihilator of the row stabilizer consists of c with z^(c*t) = 1.
    annihilator = tuple(x for x in range(N) if all(x*t % N == 0 for t in stab))
    return all(shift(cmask, x) == cmask for x in annihilator)

def rank_mod(rmask, cmask, prime, root):
    roots = [pow(root, i, prime) for i in range(N)]
    r, c = support(rmask), support(cmask)
    a = [[roots[(i*j) % N] for j in c] for i in r]
    rank = 0
    for j in range(6):
        index = next((i for i in range(rank, 6) if a[i][j]), None)
        if index is None: continue
        a[index], a[rank] = a[rank], a[index]
        inv = pow(a[rank][j], prime-2, prime)
        for i in range(rank+1, 6):
            factor = a[i][j]*inv % prime
            a[i] = [(a[i][k]-factor*a[rank][k]) % prime for k in range(6)]
        rank += 1
    return rank

def isprime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))
assert all(isprime(p) for p in P)
assert P[0]*P[1] > 6**12

all_masks = [sum(1<<i for i in c) for c in combinations(range(N), 6)]
assert len(all_masks) == 924
rep_orbit = {}
for mask in all_masks:
    rep = min(shift(mask, s) for s in range(N))
    rep_orbit.setdefault(rep, set()).add(mask)
assert len(rep_orbit) == 80
assert all(len(orb) == len({shift(rep,s) for s in range(N)}) for rep,orb in rep_orbit.items())
# Counting extremizers without any matrix rank routine: 2 parity cosets and 20 unions
# of three antipodal pairs, with the 4 overlap pairs subtracted once.
parities = [sum(1<<i for i in range(s, N, 2)) for s in (0,1)]
antipodal = [sum((1<<i)|(1<<(i+6)) for i in t) for t in combinations(range(6),3)]
assert len(antipodal) == 20 and set(parities).issubset(set(antipodal))
expected = {(r,c) for r in all_masks for c in all_masks if (r in parities and c in antipodal) or (c in parities and r in antipodal)}
assert len(expected) == 76

path = Path(__file__).with_name('rank_orbits.csv')
rows = list(csv.DictReader(path.open(newline='', encoding='utf-8')))
assert len(rows) == 6400
counts = Counter()
seen = set()
for row in rows:
    rm, cm, k, a, b = (int(row[x]) for x in ('rows','cols','rank','row_size','col_size'))
    assert (rm,cm) not in seen
    seen.add((rm,cm))
    assert rm in rep_orbit and cm in rep_orbit
    assert len(rep_orbit[rm]) == a and len(rep_orbit[cm]) == b
    truth = period_condition(rm,cm)
    assert truth == (k == 3)
    for p,z in zip(P,Z):
        assert pow(z,12,p)==1 and pow(z,6,p)==p-1 and pow(z,4,p)!=1 and pow(z,3,p)!=1
        assert rank_mod(rm,cm,p,z) == k
    counts[k] += a*b
assert counts == {3:76, 4:5376, 5:150564, 6:697760}
assert sum(counts.values()) == comb(N,6)**2
print('PERIOD_AND_ORBIT_VERIFY_OK')
print('rank histogram', dict(sorted(counts.items())))
print('sharp-rank pairs',len(expected))
