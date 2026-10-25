"""Exact elementary-collapse certificate for a finite graph complex."""
import json
from collections import Counter
from pathlib import Path

N = 11

def graph():
    edges = set()
    for i in range(5):
        for a, b in ((i, (i + 1) % 5), (5 + i, (i + 1) % 5),
                     (5 + i, (i - 1) % 5), (10, 5 + i)):
            edges.add(tuple(sorted((a, b))))
    adj = [0] * N
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return edges, adj


def enumerate_faces(adj):
    ordinary, two = set(), set()
    for mask in range(1, 1 << N):
        degrees = [(mask & adj[v]).bit_count()
                   for v in range(N) if mask & (1 << v)]
        if not any(degrees):
            ordinary.add(mask)
        if all(d <= 1 for d in degrees):
            two.add(mask)
    return ordinary, two


def main():
    edges, adj = graph()
    assert len(edges) == 20
    ordinary, two = enumerate_faces(adj)
    assert len(ordinary) == 102 and len(two) == 312
    assert ordinary < two
    cert = json.loads(Path(__file__).with_name('relative_collapse_pairs.json').read_text(encoding='utf8'))
    assert cert['graph'] == 'mycielski_C5'
    pairs = cert['pairs']
    assert len(pairs) == 105
    current = set(two)
    all_removed = set()
    for step, pair in enumerate(pairs, 1):
        assert len(pair) == 2 and all(isinstance(x, int) for x in pair)
        lower, upper = pair
        assert lower in current and upper in current, step
        assert lower not in ordinary and upper not in ordinary, step
        assert lower & upper == lower, step
        assert upper.bit_count() == lower.bit_count() + 1, step
        proper_cofaces = [x for x in current if x != lower and x & lower == lower]
        assert proper_cofaces == [upper], (step, lower, proper_cofaces)
        current.remove(lower)
        current.remove(upper)
        all_removed.add(lower)
        all_removed.add(upper)
        # The remaining collection is closed under nonempty subsets.
        for f in current:
            for v in range(N):
                if f & (1 << v):
                    sub = f ^ (1 << v)
                    assert sub == 0 or sub in current, (step, f, sub)
    assert current == ordinary
    assert all_removed == two - ordinary
    print('graph: 11 vertices; 20 edges')
    print('nonempty faces: ordinary=102, two-independence=312')
    print('exact free-face pairs: 105')
    print('remaining faces equal ordinary independence complex: yes')
    print('every intermediate simplicial complex closed under faces: yes')
    print('relative elementary collapse: VERIFIED')

if __name__ == '__main__':
    main()
