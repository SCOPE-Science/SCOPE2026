"""Exact finite checks for deletion coding of noncrossing set partitions.

Usage: python3 verify.py  (certificate.json must be in the same directory)
Only standard-library modules are required.
"""
import json
from math import comb
from pathlib import Path


def restricted_growth(n):
    if n == 0:
        yield ()
        return
    def walk(w, maximum):
        if len(w) == n:
            yield tuple(w)
            return
        for s in range(maximum + 2):
            w.append(s)
            yield from walk(w, max(maximum, s))
            w.pop()
    yield from walk([0], 0)


def is_noncrossing(w):
    # The forbidden configuration is a<b<c<d with w[a]=w[c]!=w[b]=w[d].
    for a in range(len(w)):
        for b in range(a+1, len(w)):
            for c in range(b+1, len(w)):
                if w[a] != w[c] or w[a] == w[b]:
                    continue
                for d in range(c+1, len(w)):
                    if w[b] == w[d]:
                        return False
    return True


def recanonicalize(w):
    labels = {}
    return tuple(labels.setdefault(a, len(labels)) for a in w)


def deletion_shadow(w):
    return frozenset(recanonicalize(w[:i]+w[i+1:]) for i in range(len(w)))


def compatibility_graph(shadows):
    n = len(shadows)
    neighbors = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if shadows[i].isdisjoint(shadows[j]):
                neighbors[i] |= (1 << j)
                neighbors[j] |= (1 << i)
    return neighbors


def exact_maximum_clique(neighbors):
    """Complete branch-and-bound with proper-color upper bounds.

    At each node, color the induced subgraph on candidates greedily:
    each color class is independent. Thus any clique in its first i
    ordered candidates has at most color[i] vertices. All branches
    that could exceed the incumbent are explored; pruning is exact.
    """
    maximum = 0
    calls = 0

    def color_order(candidates):
        order = []
        color_upper = []
        color = 0
        while candidates:
            color += 1
            independent_pool = candidates
            while independent_pool:
                bit = independent_pool & -independent_pool
                v = bit.bit_length() - 1
                order.append(v)
                color_upper.append(color)
                candidates ^= bit
                independent_pool ^= bit
                independent_pool &= ~neighbors[v]
        return order, color_upper

    def visit(candidates, chosen):
        nonlocal maximum, calls
        calls += 1
        if not candidates:
            maximum = max(maximum, chosen)
            return
        order, bounds = color_order(candidates)
        for index in range(len(order)-1, -1, -1):
            if chosen + bounds[index] <= maximum:
                return
            v = order[index]
            visit(candidates & neighbors[v], chosen+1)
            candidates &= ~(1 << v)

    visit((1 << len(neighbors))-1, 0)
    return maximum, calls


def verify():
    data = json.loads(Path(__file__).with_name('certificate.json').read_text('utf-8'))
    assert set(data) == {str(x) for x in range(1, 7)}
    integer_sizes = []
    lp_values = []
    for n in range(1, 7):
        c = data[str(n)]
        sources = sorted(w for w in restricted_growth(n) if is_noncrossing(w))
        assert len(sources) == comb(2*n,n)//(n+1) == c['source_count']
        outputs = sorted(set().union(*(deletion_shadow(w) for w in sources)))
        assert len(outputs) == c['output_count']
        seen = {r:i for i,r in enumerate(outputs)}
        shadows = [frozenset(seen[z] for z in deletion_shadow(w)) for w in sources]
        chosen = [tuple(map(int, w)) for w in c['code']]
        assert all(w in sources for w in chosen)
        assert len(set(chosen)) == len(chosen)
        used = set()
        for w in chosen:
            assert used.isdisjoint(deletion_shadow(w))
            used.update(deletion_shadow(w))
        primal = c['primal']
        dual = c['dual']
        pd, dd = c['primal_denom'], c['dual_denom']
        assert len(primal) == len(sources) and len(dual) == len(outputs)
        assert pd > 0 and dd > 0 and min(primal) >= 0 and min(dual) >= 0
        for i in range(len(outputs)):
            assert sum(primal[j] for j, shadow in enumerate(shadows) if i in shadow) <= pd
        for shadow in shadows:
            assert sum(dual[i] for i in shadow) >= dd
        # Rational primal and dual match and thereby prove LP optimality.
        assert sum(primal)*dd == sum(dual)*pd
        integer, calls = exact_maximum_clique(compatibility_graph(shadows))
        assert integer == len(chosen) and calls == c['expected_calls']
        integer_sizes.append(integer)
        lp_values.append((sum(primal), pd))
        print(f'n={n} sources={len(sources)} outputs={len(outputs)} integer={integer} fractional={sum(primal)}/{pd} calls={calls}')
    assert integer_sizes == [1,1,2,3,5,12]
    assert all(integer_sizes[i] == lp_values[i][0]//lp_values[i][1] for i in range(5))
    assert lp_values[-1][0]//lp_values[-1][1] == 13 > integer_sizes[-1]
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
