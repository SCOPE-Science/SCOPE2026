"""Finite reproducibility checks for counting logic on connected Ferrers graphs.

Standard library only. Finite checks corroborate but do not prove the theorem.
"""
import collections
import itertools


def compositions(n, k):
    for cuts in itertools.combinations(range(1, n), k - 1):
        p = (0,) + cuts + (n,)
        yield tuple(p[i + 1] - p[i] for i in range(k))


def graphs(n):
    for a_size in range(1, n):
        b_size = n - a_size
        for h in range(1, min(a_size, b_size) + 1):
            for a in compositions(a_size, h):
                for b in compositions(b_size, h):
                    flipped = (tuple(reversed(b)), tuple(reversed(a)))
                    if (a, b) > flipped:
                        continue
                    verts = [('A', i) for i, s in enumerate(a, 1) for _ in range(s)]
                    verts += [('B', j) for j, s in enumerate(b, 1) for _ in range(s)]
                    adj = [set() for _ in range(n)]
                    for x in range(n):
                        for y in range(x + 1, n):
                            a0, i = verts[x]
                            b0, j = verts[y]
                            edge = (a0 == 'A' and b0 == 'B' and i >= j)
                            edge |= (a0 == 'B' and b0 == 'A' and j >= i)
                            if edge:
                                adj[x].add(y)
                                adj[y].add(x)
                    yield (a, b), verts, adj


def refine(graphset):
    colors = [[0] * len(adj) for _, _, adj in graphset]
    for _ in range(max(len(a) for _, _, a in graphset) + 1):
        palette = {}
        new = []
        for (_, _, adj), co in zip(graphset, colors):
            row = []
            for i, neighbors in enumerate(adj):
                signature = (co[i], tuple(sorted(collections.Counter(co[j] for j in neighbors).items())))
                row.append(palette.setdefault(signature, len(palette)))
            new.append(row)
        if new == colors:
            break
        colors = new
    else:
        raise AssertionError('refinement did not stabilize')
    return colors


def test():
    total = 0
    overall_fo2 = set()
    for n in range(2, 14):
        gs = list(graphs(n))
        co = refine(gs)
        distinct_signatures = set()
        histogram_check = 0
        for (key, verts, adj), colors in zip(gs, co):
            sig = tuple(sorted(collections.Counter(colors).items()))
            assert sig not in distinct_signatures, ('C2 collision', n, key)
            distinct_signatures.add(sig)
            deg = [len(s) for s in adj]
            all_degrees = [len(adj[v]) for v in range(n)]
            classes = collections.defaultdict(list)
            for i, c in enumerate(colors):
                classes[c].append(i)
            mixed = [c for c, vs in classes.items() if len({verts[i][0] for i in vs}) == 2]
            if mixed:
                assert len(mixed) == len(classes)
                assert any(sum(j in adj[i] for j in vs) > 0 for vs in classes.values() for i in vs)
                for vs in classes.values():
                    count = collections.Counter(verts[i][0] for i in vs)
                    assert count['A'] == count['B']
            for vs in classes.values():
                for i in vs:
                    for ws in classes.values():
                        expected = len(adj[i] & set(ws))
                        assert all(len(adj[j] & set(ws)) == expected for j in vs)
            # FO2: complete edge, nontrivial star, or nonstar.
            if n == 2:
                typ = 'edge'
            elif max(deg) == n - 1:
                typ = 'star'
            else:
                typ = 'nonstar'
                assert all(0 < d < n - 1 for d in deg)
            overall_fo2.add(typ)
            histogram_check += 1
        total += len(gs)
        print('order', n, 'chain types', len(gs), 'unique C2 signatures', histogram_check)
    assert overall_fo2 == {'edge', 'star', 'nonstar'}
    print('PASS: graphs', total, 'C2 collisions 0, FO2 classes 3, equitable-cell tests PASS')


if __name__ == '__main__':
    test()
