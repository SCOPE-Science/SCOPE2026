"""Exact finite mesh corroboration of the three-arm geodesic polygon slimness formula.
No external dependencies. Mesh checks do not constitute the continuum proof.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations


def mesh_graph(lengths, scale):
    assert len(lengths) == 3 and all(isinstance(x, int) and x > 0 for x in lengths)
    adj = {0: set(), 1: set()}
    arms = []
    nxt = 2
    for length in lengths:
        nodes = [0]
        for _ in range(length * scale - 1):
            nodes.append(nxt)
            adj[nxt] = set()
            nxt += 1
        nodes.append(1)
        for u, v in zip(nodes, nodes[1:]):
            adj[u].add(v)
            adj[v].add(u)
        arms.append(nodes)
    return adj, arms


def all_distances(adj):
    result = {}
    for root in adj:
        d = {root: 0}
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if w not in d:
                    d[w] = d[v] + 1
                    queue.append(w)
        result[root] = d
    return result


def simple_paths(adj, source, target):
    stack = [(source, [source], {source})]
    while stack:
        v, path, used = stack.pop()
        if v == target:
            yield tuple(path)
            continue
        for w in adj[v]:
            if w not in used:
                stack.append((w, path + [w], used | {w}))


def verify_case(lengths, scale):
    adj, arms = mesh_graph(lengths, scale)
    d = all_distances(adj)
    expected = Fraction(lengths[2] + min(lengths[1], 3 * lengths[0]), 4)
    observed = Fraction(0)
    n_paths = 0
    for x, y in combinations(adj, 2):
        paths = list(simple_paths(adj, x, y))
        for s in paths:
            if len(s) - 1 != d[x][y]:
                continue
            for q in paths:
                if set(s[1:-1]) & set(q[1:-1]):
                    continue
                separation = max(min(d[z][w] for w in q) for z in s)
                observed = max(observed, Fraction(separation, scale))
                n_paths += 1
                assert separation <= expected * scale, (lengths, scale, s, q, separation)
    assert observed == expected, (lengths, scale, observed, expected)
    return len(adj), n_paths, observed


def verify_witness(lengths):
    a, b, c = map(Fraction, lengths)
    u = (c + a) / 2
    v = min(a, (b-a)/2)
    assert 0 <= u <= c and 0 <= v <= b
    assert u <= (c+a)/2 and v <= (b+a)/2 and u+v <= (b+c)/2
    gap = (u + v)/2
    assert gap == (c + min(b, 3*a))/4
    return gap


def main():
    cases = [((1,1,1), 4), ((1,1,3), 2), ((1,2,3), 4),
             ((1,3,8), 4), ((1,4,5), 2), ((2,3,5), 2),
             ((2,5,5), 2)]
    pairs = 0
    for lengths, scale in cases:
        nodes, checks, observed = verify_case(lengths, scale)
        assert observed == verify_witness(lengths)
        print(f'{lengths}, mesh=1/{scale}: {nodes} nodes; {checks} disjoint geodesic/alternate path pairs; maximum={observed}')
        pairs += checks
    witness_cases = 0
    for aa in range(1, 9):
        for bb in range(aa, 10):
            for cc in range(bb, 12):
                verify_witness((aa, bb, cc))
                witness_cases += 1
    print(f'PASS: {pairs} exact mesh path-pair comparisons; {witness_cases} integer-triple witness checks')

if __name__ == '__main__':
    main()
