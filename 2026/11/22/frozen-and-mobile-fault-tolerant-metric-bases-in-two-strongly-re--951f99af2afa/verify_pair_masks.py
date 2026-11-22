"""Independent exhaustive verification using shortest-path distance masks.

Run: python3 verify_pair_masks.py
Only Python 3 standard-library modules are required.
"""
from collections import Counter, deque
from itertools import combinations, product, permutations

N = 16
V = tuple(range(N))


def graph(which):
    # Vertex (r,c) is labelled 4*r+c, for r,c in Z/4Z.
    coords = [divmod(x, 4) for x in V]
    steps = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    adj = [set() for _ in V]
    for u, (r, c) in enumerate(coords):
        for v, (s, t) in enumerate(coords):
            if u != v and ((r == s or c == t) if which == 'rook'
                    else ((r-s) % 4, (c-t) % 4) in steps):
                adj[u].add(v)
    assert all(len(a) == 6 for a in adj)
    assert all(len(adj[u] & adj[v]) == 2 for u in V for v in V if u < v)
    d = []
    for s in V:
        ds = [-1] * N
        ds[s] = 0
        q = deque([s])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if ds[y] == -1:
                    ds[y] = ds[x] + 1
                    q.append(y)
        assert all(v >= 0 for v in ds) and max(ds) == 2
        d.append(ds)
    return d


def all_bases(d):
    distinguishing = [sum(1 << w for w in V if d[w][u] != d[w][v])
                       for u in V for v in range(u+1, N)]
    def valid(mask):
        return all((mask & witness).bit_count() >= 2 for witness in distinguishing)

    # The family of fault-tolerant resolving sets is upward-closed. Testing
    # five-sets rules out ALL smaller sets, and six-sets establish the optimum.
    assert not any(valid(sum(1 << v for v in c)) for c in combinations(V, 5))
    bases = {sum(1 << v for v in c) for c in combinations(V, 6)
             if valid(sum(1 << v for v in c))}
    assert bases
    return bases


def exchange(bases, moves):
    neighbors = {s: set() for s in bases}
    for s in bases:
        selected = [v for v in V if s & (1 << v)]
        vacant = [v for v in V if not s & (1 << v)]
        for rm in combinations(selected, moves):
            stripped = s
            for x in rm:
                stripped ^= 1 << x
            for add in combinations(vacant, moves):
                out = stripped
                for x in add:
                    out ^= 1 << x
                if out in bases:
                    neighbors[s].add(out)
    degree = Counter(len(nb) for nb in neighbors.values())
    edges = sum(map(len, neighbors.values())) // 2
    remaining = set(bases)
    sizes = []
    while remaining:
        root = next(iter(remaining))
        reached = {root}
        queue = [root]
        remaining.remove(root)
        for x in queue:
            for y in neighbors[x]:
                if y in remaining:
                    remaining.remove(y)
                    reached.add(y)
                    queue.append(y)
        sizes.append(len(reached))
    stats = {'edges': edges, 'degrees': degree, 'components': Counter(sizes)}
    if len(sizes) == 1:
        eccentricities = Counter()
        distpairs = Counter()
        for root in sorted(bases):
            d = {root: 0}
            q = deque([root])
            while q:
                x = q.popleft()
                for y in neighbors[x]:
                    if y not in d:
                        d[y] = d[x] + 1
                        q.append(y)
            assert len(d) == len(bases)
            eccentricities[max(d.values())] += 1
            distpairs.update(dist for y, dist in d.items() if y > root)
        stats['eccentricities'] = eccentricities
        stats['distances'] = distpairs
    return stats


def permutations_of_graph(which):
    coords = [divmod(v, 4) for v in V]
    address = {a: v for v, a in enumerate(coords)}
    if which == 'rook':
        for a in permutations(range(4)):
            for b in permutations(range(4)):
                yield tuple(address[a[x], b[y]] for x, y in coords)
                yield tuple(address[a[y], b[x]] for x, y in coords)
    else:
        steps = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
        for a, b, c, d in product(range(4), repeat=4):
            if {((a*x + b*y) % 4, (c*x + d*y) % 4) for x, y in steps} != steps:
                continue
            for tx, ty in coords:
                yield tuple(address[((a*x+b*y+tx) % 4), ((c*x+d*y+ty) % 4)]
                            for x, y in coords)


def orbit_sizes(bases, perms):
    available = set(bases)
    out = []
    while available:
        seed = next(iter(available))
        orbit = {sum(1 << p[x] for x in V if seed & (1 << x)) for p in perms}
        assert orbit <= bases
        out.append(len(orbit))
        available -= orbit
    return sorted(out)


def main():
    for which in ('shrikhande', 'rook'):
        d = graph(which)
        bases = all_bases(d)
        perms = list(permutations_of_graph(which))
        assert len(perms) == (192 if which == 'shrikhande' else 1152)
        orbits = orbit_sizes(bases, perms)
        x1 = exchange(bases, 1)
        print(which, 'min_size=6', 'bases=', len(bases), 'orbits=', orbits)
        print('one-exchange', x1)
        if which == 'shrikhande':
            x2 = exchange(bases, 2)
            print('two-exchange', x2)
            assert len(bases) == 448 and x1['edges'] == 0
            assert x1['components'] == Counter({1:448})
            assert x2['edges'] == 10080 and x2['degrees'] == Counter({45:448})
            assert x2['components'] == Counter({448:1})
            assert x2['eccentricities'] == Counter({3:448})
            assert x2['distances'] == Counter({1:10080,2:70560,3:19488})
            assert orbits == [16,16,32,32,48,48,64,96,96]
        else:
            assert len(bases) == 1600 and x1['edges'] == 12816
            assert x1['components'] == Counter({1600:1})
            assert x1['eccentricities'] == Counter({6:1600})
            assert x1['distances'] == Counter({1:12816,2:102096,3:357744,4:521376,5:244944,6:40224})
            assert orbits == [16,96,144,192,288,288,576]
    print('ALL ASSERTIONS PASSED')


if __name__ == '__main__':
    main()
