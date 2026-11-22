"""Independent 3-core peeling certificate for degree-six, threshold-four contagion.

For each vertex mask, delete vertices of residual degree at most two in
parallel. No graph packages or external data are required.
"""
from collections import Counter
from itertools import product

N = 16
FULL = (1 << N) - 1
D = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}

def coord(v):
    return divmod(v, 4)

def index(a, b):
    return 4 * (a % 4) + (b % 4)

def build(shrikhande):
    adj = [set() for _ in range(N)]
    for v in range(N):
        a, b = coord(v)
        for w in range(N):
            if v == w:
                continue
            c, d = coord(w)
            adjacent = ((c-a)%4, (d-b)%4) in D if shrikhande else (a == c or b == d)
            if adjacent:
                adj[v].add(w)
    assert all(len(nb) == 6 for nb in adj)
    assert all((v in adj[w]) == (w in adj[v]) for v in range(N) for w in range(N))
    assert all(len(adj[v] & adj[w]) == 2 for v in range(N) for w in range(v+1, N))
    return adj

def rounds_to_empty_core(initial_seed, adj):
    remaining = {v for v in range(N) if not (initial_seed >> v) & 1}
    rounds = 0
    while remaining:
        peel = {v for v in remaining if len(adj[v] & remaining) <= 2}
        if not peel:
            return -1
        remaining -= peel
        rounds += 1
    return rounds

def analyze(shrikhande):
    adj = build(shrikhande)
    tm = [rounds_to_empty_core(s, adj) for s in range(1 << N)]
    successes = Counter()
    minimal = Counter()
    minimal_masks = set()
    degree_signature = set()
    for seed in range(1 << N):
        k = seed.bit_count()
        if k == 7 and sorted(len(adj[v] & {w for w in range(N) if (seed >> w) & 1})
                              for v in range(N) if (seed >> v) & 1) == [2,2,2,3,3,3,3]:
            degree_signature.add(seed)
        if tm[seed] < 0:
            continue
        successes[k] += 1
        if all(tm[seed ^ (1 << v)] < 0 for v in range(N) if (seed >> v) & 1):
            minimal[k, tm[seed]] += 1
            minimal_masks.add(seed)
    if shrikhande:
        assert minimal == Counter({(6,3):96, (6,4):336, (6,5):1152, (6,6):576, (7,3):64})
        assert successes == Counter({6:2160,7:7504,8:11658,9:11328,10:8008,11:4368,12:1820,13:560,14:120,15:16,16:1})
        assert len(degree_signature) == 64
        assert {s for s in minimal_masks if s.bit_count() == 7} == degree_signature
        # All 64 exceptional seeds form one orbit of affine automorphisms.
        mats = [(a,b,c,d) for a,b,c,d in product(range(4), repeat=4)
                if {((a*x+b*y)%4, (c*x+d*y)%4) for x,y in D} == D]
        assert len(mats) == 12
        seed = {1,2,4,5,7,8,12}
        orbit = set()
        for a,b,c,d in mats:
            for x,y in product(range(4), repeat=2):
                orbit.add(sum(1 << index(a*u+b*v+x, c*u+d*v+y)
                              for z in seed for u,v in [coord(z)]))
        assert len(orbit) == 64 and orbit == degree_signature
    else:
        assert minimal == Counter({(6,3):288, (6,5):576})
        assert successes == Counter({6:864,7:4272,8:8010,9:9312,10:7432,11:4272,12:1812,13:560,14:120,15:16,16:1})
        assert not degree_signature
        assert all(s.bit_count() == 6 for s in minimal_masks)
    print(('Shrikhande' if shrikhande else 'Rook'), 'minimal=',sorted(minimal.items()),
          'all successful=',sorted(successes.items()),'degree signature=',len(degree_signature))

if __name__ == '__main__':
    analyze(True)
    analyze(False)
    print('PASS independent 3-core peeling and affine orbit')
