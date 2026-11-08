"""Independent exhaustive line-graph evaluation and matching-polynomial check.

Requires Python 3.8+; uses only the standard library.
"""
from collections import defaultdict
from itertools import product


def cube_edges():
    return tuple((u, v) for u in range(8) for v in range(u + 1, 8)
                 if bin(u ^ v).count('1') == 1)


def line_edges(base_edges):
    return tuple((i, j) for i in range(len(base_edges))
                 for j in range(i + 1, len(base_edges))
                 if any(a == b for a in base_edges[i] for b in base_edges[j]))


def sector_table(base_edges):
    n_edges = len(base_edges)
    lines = line_edges(base_edges)
    out = {}
    for assignment in product(range(3), repeat=n_edges):
        k = assignment.count(0)
        b = sum(assignment[i] == assignment[j] for i, j in lines)
        if k not in out or b < out[k][0]:
            out[k] = (b, 1)
        elif b == out[k][0]:
            out[k] = (b, out[k][1] + 1)
    return out


def matching_vector(n, edges):
    adj = [set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)
    from functools import lru_cache
    @lru_cache(None)
    def rec(mask):
        if mask == 0:
            return (1,)
        first = (mask & -mask).bit_length() - 1
        ans = list(rec(mask ^ (1 << first)))
        for neighbor in adj[first]:
            if mask & (1 << neighbor):
                sub = rec(mask ^ (1 << first) ^ (1 << neighbor))
                if len(ans) < len(sub) + 1:
                    ans += [0] * (len(sub) + 1 - len(ans))
                for i, val in enumerate(sub):
                    ans[i + 1] += val
        return tuple(ans)
    return rec((1 << n) - 1)


def check_graph(n, edges):
    assert len(edges) * 2 == n * 3
    tab = sector_table(edges)
    xvals = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
    for x in xvals:
        exact = min(b - x * k for k, (b, _) in tab.items())
        local_bound = n * min(1, -x / 2, 1 - x, 3 - 3 * x / 2)
        assert exact == local_bound, (n, x, exact, local_bound)
    match = matching_vector(n, edges)
    weighted = sum(2**j * c for j, c in enumerate(match))
    x4 = min(b - 4 * k for k, (b, _) in tab.items())
    d4 = sum(count for k,(b,count) in tab.items() if b - 4*k == x4)
    assert d4 == weighted
    pm = match[n // 2]
    assert tab[n][1] == 2**(n//2)*pm, (n,tab[n],pm)
    return tab, match


def main():
    cube = cube_edges()
    expected = {0:(8,450),1:(6,1248),2:(4,1044),3:(2,288),4:(0,24),5:(2,288),6:(4,912),7:(6,864),8:(8,144),9:(12,352),10:(16,168),11:(20,24),12:(24,1)}
    tab, match = check_graph(8, cube)
    assert tab == expected
    assert match == (1, 12, 42, 44, 9)
    crossing = {-2:3054, 2:2232, 4:689}
    for x, expected_deg in crossing.items():
        e = min(b - x*k for k,(b,count) in tab.items())
        total = sum(count for k,(b,count) in tab.items() if b - x*k == e)
        assert total == expected_deg, (x,total)
    # Distinct cubic three-edge-colorable examples test the analytic all-size law.
    k4 = tuple((u,v) for u in range(4) for v in range(u+1,4))
    k33 = tuple((u,v) for u in range(3) for v in range(3,6))
    prism = tuple((i,(i+1)%3) for i in range(3)) + tuple((i+3,(i+1)%3+3) for i in range(3)) + tuple((i,i+3) for i in range(3))
    for n, e in ((4,k4),(6,k33),(6,prism)):
        check_graph(n,e)
    print('DIRECT_OK cube states=531441 edges=24; matching count=',match)
    print('K4, K3,3 and triangular prism verified')
    for k in sorted(tab):
        print(k,*tab[k])

if __name__ == '__main__':
    main()
