"""Independent exhaustive check via four row symbols and integer GF(2) elimination.
Run: python3 verify_plucker_python.py. No third-party libraries are used.
"""
from itertools import combinations, permutations, product
from collections import Counter, defaultdict


def binary_rank(columns):
    pivots = {}
    for z in columns:
        while z:
            b = z.bit_length() - 1
            if b in pivots:
                z ^= pivots[b]
            else:
                pivots[b] = z
                break
    return len(pivots)


def check(n):
    edges = list(combinations(range(n), 2))
    forms = set()
    for colors in product(range(4), repeat=n):
        x = sum((colors[i] != 0 and colors[j] != 0 and colors[i] != colors[j]) << b
                for b, (i, j) in enumerate(edges))
        if x: forms.add(x)
    assert len(forms) == ((2**n - 1)*(2**n - 2))//6
    supports = set()
    hist = Counter()
    for subset in range(1 << len(edges)):
        k = subset.bit_count()
        if 1 << k > len(forms): continue
        if len({h & subset for h in forms}) == 1 << k:
            hist[k] += 1
            supports.add(subset)
    facets = [s for s in supports if all((s | 1 << b) not in supports
                 for b in range(len(edges)) if not (s >> b & 1))]
    fby = Counter(s.bit_count() for s in facets)
    # Canonical S_n orbit representative for each facet.
    def canon(s):
        out = None
        for p in permutations(range(n)):
            t = 0
            for b, (u,v) in enumerate(edges):
                if s >> b & 1:
                    edge = tuple(sorted((p[u],p[v])))
                    t |= 1 << edges.index(edge)
            if out is None or t < out: out = t
        return out
    orbits = Counter((s.bit_count(), canon(s)) for s in facets)
    f = {k: sorted(s for s in supports if s.bit_count() == k) for k in hist}
    boundary = {1: 1}
    for k in range(2, max(hist)+1):
        ix = {u: j for j,u in enumerate(f[k-1])}
        cols = [sum(1 << ix[s ^ (1 << b)] for b in range(len(edges))
                    if s >> b & 1) for s in f[k]]
        boundary[k] = binary_rank(cols)
    homology = {k-1:len(f[k])-boundary[k]-boundary.get(k+1,0)
                for k in f if k > 0}
    assert all(v >= 0 for v in homology.values())
    print('n',n,'concepts',len(forms),'face_polynomial',
          ' '.join(str(hist[k]) for k in sorted(hist)))
    print('facet_sizes',' '.join(f'{k}:{fby[k]}' for k in sorted(fby)))
    print('facet_orbits',' '.join(f'{k}:{count}:{canonical}'
          for (k,canonical),count in sorted(orbits.items())))
    print('boundary_ranks',' '.join(f'{k}:{boundary[k]}' for k in sorted(boundary) if k>1))
    print('reduced_F2_homology',' '.join(f'{k}:{v}' for k,v in sorted(homology.items()) if v))

if __name__ == '__main__':
    for n in (4,5,6):check(n)
