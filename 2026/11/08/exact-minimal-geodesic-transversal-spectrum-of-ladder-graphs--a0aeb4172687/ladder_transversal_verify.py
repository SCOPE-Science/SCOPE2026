"""Independent finite checks for geodesic transversals on ordinary ladder graphs.

Run with Python 3: python ladder_transversal_verify.py
No third-party dependencies. Finite checks corroborate, not prove, all orders.
"""
from collections import Counter, deque


def graph(h):
    n = 2 * h
    adj = [[] for _ in range(n)]
    for i in range(h):
        a, b = 2*i, 2*i + 1
        adj[a].append(b)
        adj[b].append(a)
        if i:
            for c in (0, 1):
                u, v = 2*(i-1)+c, 2*i+c
                adj[u].append(v)
                adj[v].append(u)
    return adj


def distances(adj, s):
    d = [-1]*len(adj)
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u]+1
                q.append(v)
    return d


def shortest_paths(adj):
    n = len(adj)
    all_dist = [distances(adj, i) for i in range(n)]
    ans = []
    for s in range(n):
        for t in range(s+1, n):
            dist_s = all_dist[s]
            dist_t = all_dist[t]
            d = dist_s[t]
            def visit(path):
                u = path[-1]
                if u == t:
                    ans.append(tuple(path))
                else:
                    for v in adj[u]:
                        if dist_s[v] == dist_s[u]+1 and dist_s[v]+dist_t[v] == d:
                            visit(path+[v])
            visit([s])
    return ans, all_dist


def maximal_paths(h):
    paths, all_dist = shortest_paths(graph(h))
    # Maximality checked as directed contiguous subpath in every other shortest path.
    max_paths = []
    for p in paths:
        if not any(len(q)>len(p) and
                   any(q[k:k+len(p)] == p or q[k:k+len(p)] == p[::-1]
                       for k in range(len(q)-len(p)+1))
                   for q in paths):
            max_paths.append(p)
    assert max(all_dist[0]) == h
    return max_paths


def predicted(h):
    ans = set()
    # An entire column's boundary pair.
    for c in (0, 1):
        ans.add((1 << c) | (1 << (2*(h-1)+c)))
    # Two opposing vertices on equal or adjacent rungs.
    for a in range(h):
        for b in range(h):
            if abs(a-b) <= 1:
                ans.add((1 << (2*a)) | (1 << (2*b+1)))
    # Two in a column and an intervening singleton in the other column.
    for c in (0, 1):
        for a in range(h):
            for b in range(a+2, h):
                for mid in range(a+2, b-1):
                    if not (a == 0 and b == h-1):
                        ans.add((1 << (2*a+c)) | (1 << (2*b+c)) |
                                (1 << (2*mid+(1-c))))
    return ans


def main():
    maximal_geodesic_checks = 0
    for h in range(2, 9):
        paths = maximal_paths(h)
        actual_paths = {tuple(p) for p in paths}
        want = set()
        for a in (0, 1):
            b = 1-a
            for t in range(h):
                path = tuple([2*i+a for i in range(t+1)] + [2*t+b] +
                             [2*i+b for i in range(t+1, h)])
                want.add(min(path, path[::-1]))
        canonical = {min(p, p[::-1]) for p in actual_paths}
        assert canonical == want, (h, 'maximal geodesic set disagrees')
        assert len(paths) == 2*h
        maximal_geodesic_checks += len(paths)

    total = 0
    total_facets = 0
    for h in range(2, 10):
        paths = []
        for a in (0, 1):
            b = 1-a
            for t in range(h):
                indices = [2*i+a for i in range(t+1)] + [2*t+b] + [2*i+b for i in range(t+1,h)]
                paths.append(sum(1 << v for v in indices))
        facets = set()
        for mask in range(1 << (2*h)):
            total += 1
            if all(mask & p for p in paths):
                if all(not all((mask ^ (1 << bit)) & p for p in paths)
                       for bit in range(2*h) if mask & (1 << bit)):
                    facets.add(mask)
        expect = predicted(h)
        assert facets == expect, (h, len(facets), len(expect), facets^expect)
        coefficient3 = h*(h-4)*(h-5)//3 if h >= 4 else 0
        assert Counter(x.bit_count() for x in facets) == Counter({2:3*h, **({3:coefficient3} if coefficient3 else {})})
        total_facets += len(facets)
    # The algebraic enumeration has its own large-parameter check, independent
    # of the 2**(2h)-subset census.
    for h in range(4, 100):
        direct = 2*sum((b-1)*(h-b-2)-1 for b in range(2, h-2))
        assert direct == h*(h-4)*(h-5)//3
    print('VERIFY_OK independent_shortest_path_orders=2..8',
          f'maximal_geodesics_checked={maximal_geodesic_checks}',
          'all_subset_orders=2..9', f'subsets={total}',
          f'inclusion_minimal_sets={total_facets}',
          'geodesic_paths=PASS', 'facet_classification=PASS',
          'cardinality_polynomial=PASS', 'finite_algebra=PASS')

if __name__ == '__main__':
    main()
