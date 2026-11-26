"""Independent finite checks for cyclic superstrings covering 111-free words.

The proof in RESULT.md establishes the all-k theorem. This verifier checks
its explicit balancing bijection, generating function, and constructed cycles.
Requires only Python's standard library; optional NetworkX cross-checks the
minimum directed-postman augmentation for k <= 10.
"""
from collections import Counter
from itertools import product


def allowed(k):
    return [''.join(b) for b in product('01', repeat=k) if '111' not in ''.join(b)]


def recurrence(k):
    a = [1, 2, 4]
    for _ in range(3, k + 1):
        a.append(sum(a[-3:]))
    # E(x)=x^4(1+2x)/((1-x-x^2)(1-x-x^2-x^3))
    cc = [0] * (k + 1)
    prod = [0] * (k + 1)
    prod[0] = 1
    for i in range(1, k + 1):
        prod[i] = (prod[i-1] if i>=1 else 0) + (prod[i-2] if i>=2 else 0)
    trib = [1, 1, 2]
    for i in range(3, k + 1):
        trib.append(sum(trib[-3:]))
    for i in range(k + 1):
        cc[i] = sum(prod[j] * trib[i-j] for j in range(i+1))
    e = (cc[k-4] if k>=4 else 0) + (2*cc[k-5] if k>=5 else 0)
    return a[k], e


def euler_cycle(adjacencies, edge_count):
    start = '0' * len(next(iter(adjacencies)))
    stack = [start]
    traversed = []
    while stack:
        u = stack[-1]
        if adjacencies[u]:
            w = adjacencies[u].pop()
            stack.append(w)
        else:
            traversed.append(stack.pop())
    assert len(traversed) == edge_count + 1
    traversed.reverse()
    assert traversed[0] == traversed[-1]
    return traversed


def constructed(k):
    m = k - 1
    vertices = allowed(m)
    words = allowed(k)
    in_degree, out_degree = Counter(), Counter()
    edges = {v: [] for v in vertices}
    for w in words:
        a, b = w[:-1], w[1:]
        edges[a].append(b)
        out_degree[a] += 1
        in_degree[b] += 1
    sources = {v for v in vertices if in_degree[v] - out_degree[v] == 1}
    targets = {v for v in vertices if out_degree[v] - in_degree[v] == 1}
    assert sources == {v for v in vertices if v.endswith('11') and not v.startswith('11')}
    assert targets == {v for v in vertices if v.startswith('11') and not v.endswith('11')}
    expected_targets = set()
    added = 0
    for v in sorted(sources):
        r = v.index('11')
        assert 1 <= r <= m - 2
        p, s = v[:r], v[r+2:]
        assert p.endswith('0') and '11' not in p
        w = v
        for c in p[::-1]:
            gram = w[-m:] + c
            assert len(gram) == k and '111' not in gram
            a, b = gram[:-1], gram[1:]
            edges[a].append(b)
            w += c
            added += 1
        t = '11' + s + p[::-1]
        assert w[-m:] == t and t in targets
        assert t not in expected_targets
        expected_targets.add(t)
    assert expected_targets == targets
    a, e = recurrence(k)
    assert a == len(words) and e == added, (k, a, len(words), e, added)
    traversed = euler_cycle(edges, len(words) + added)
    cyc = ''.join(x[0] for x in traversed[:-1])
    assert len(cyc) == len(words) + added
    assert '111' not in cyc + cyc[:2]
    observed = Counter((cyc + cyc[:k-1])[i:i+k] for i in range(len(cyc)))
    assert set(observed) == set(words)
    assert len(observed) == len(words)
    return len(words), len(sources), added, len(cyc)


def independent_optimum(k, candidate, unrestricted=False):
    try:
        import networkx as nx
    except ImportError:
        return 'networkx_unavailable'
    vertices = allowed(k-1)
    words = allowed(k)
    g = nx.DiGraph()
    g.add_nodes_from(vertices)
    if unrestricted:
        g.add_nodes_from(''.join(w) for w in product('01', repeat=k-1))
    for w in ([''.join(x) for x in product('01', repeat=k)] if unrestricted else words):
        g.add_edge(w[:-1], w[1:])
    # Imbalances arise from the *required* words even when forbidden
    # transitions may be used for additional occurrences.
    indeg, outdeg = Counter(), Counter()
    for w in words:
        outdeg[w[:-1]] += 1
        indeg[w[1:]] += 1
    sources = [v for v in vertices if indeg[v] > outdeg[v]]
    targets = [v for v in vertices if outdeg[v] > indeg[v]]
    if not sources:
        assert candidate == 0
        return 'zero'
    flow = nx.DiGraph()
    for v in sources:
        flow.add_node(('s',v), demand=-1)
    for v in targets:
        flow.add_node(('t',v), demand=1)
    for v in sources:
        distances = nx.single_source_shortest_path_length(g,v)
        for u in targets:
            flow.add_edge(('s',v),('t',u),capacity=1,weight=distances[u])
    optimum=nx.min_cost_flow_cost(flow)
    assert optimum == candidate, (k, optimum, candidate)
    return str(optimum)


def main():
    values=[]
    mincost_done = True
    for k in range(3, 17):
        a, ns, add, length = constructed(k)
        values.append((k,a,ns,add,length))
        if k<=10:
            first = independent_optimum(k,add)
            second = independent_optimum(k,add,unrestricted=True)
            mincost_done &= first != 'networkx_unavailable' and second != 'networkx_unavailable'
    print('VERIFY_OK constructed_exact_cycles_k=3..16 ' +
          ('independent_constrained_and_unrestricted_mincost_k=3..10'
           if mincost_done else 'optional_networkx_mincost_skipped'))
    print('k allowed_words imbalanced_sources excess optimal_length')
    for row in values:
        print(*row)


if __name__ == '__main__':
    main()
