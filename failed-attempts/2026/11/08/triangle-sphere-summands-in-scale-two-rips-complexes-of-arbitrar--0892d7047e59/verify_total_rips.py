#!/usr/bin/env python3
"""Exact finite checks for scale-two Rips complexes of graph subdivisions.
Uses only the Python standard library. The universal theorem has a separate proof.
"""
from itertools import combinations
from collections import deque


def graph_edges(n, mask):
    pairs = list(combinations(range(n), 2))
    return [p for i, p in enumerate(pairs) if (mask >> i) & 1]


def connected(n, edges):
    neighbors = [set() for _ in range(n)]
    for a, b in edges:
        neighbors[a].add(b); neighbors[b].add(a)
    seen = {0}; todo = [0]
    for v in todo:
        for u in neighbors[v] - seen:
            seen.add(u); todo.append(u)
    return len(seen) == n


def total_and_subdivision(n, edges):
    m = len(edges)
    tot = [set() for _ in range(n+m)]
    sub = [set() for _ in range(n+m)]
    def add(adj, a, b):
        adj[a].add(b); adj[b].add(a)
    for i, (a,b) in enumerate(edges):
        e = n+i
        add(tot, a, b); add(tot, a, e); add(tot, b, e)
        add(sub, a, e); add(sub, b, e)
    for i, (a,b) in enumerate(edges):
        for j, (c,d) in enumerate(edges[:i]):
            if len({a,b,c,d}) < 4:
                add(tot, n+i, n+j)
    return tot, sub


def distances(adj, v):
    d = [-1]*len(adj); d[v] = 0; queue = deque([v])
    while queue:
        x = queue.popleft()
        for y in adj[x]:
            if d[y] < 0:
                d[y] = d[x] + 1; queue.append(y)
    return d


def clique_faces(adj):
    out = [[] for _ in range(len(adj))]
    def extend(pick, common):
        for i, v in enumerate(common):
            p = pick | (1 << v)
            out[p.bit_count()-1].append(p)
            extend(p, [w for w in common[i+1:] if w in adj[v]])
    extend(0, list(range(len(adj))))
    return [group for group in out if group]


def mod2_betti(groups):
    ranks = [0] * (len(groups) + 1)
    for k in range(1, len(groups)):
        prev = {f: j for j, f in enumerate(groups[k-1])}
        pivots = {}
        for face in groups[k]:
            b = 0; bit = face
            while bit:
                v = bit & -bit; bit ^= v
                b ^= 1 << prev[face ^ v]
            while b:
                pivot = b.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot] = b; break
                b ^= pivots[pivot]
        ranks[k] = len(pivots)
    ranks[-1] = 0
    answer = [len(groups[k]) - ranks[k] - ranks[k+1] for k in range(len(groups))]
    answer[0] -= 1
    return answer


def complex_of_G(n, edges):
    adj = [set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    return adj


def k0_faces(n, edges):
    # The subcomplex without the extra pure-midpoint triangle disks.
    all_faces = set(f for g in clique_faces(complex_of_G(n,edges)) for f in g)
    for i,(a,b) in enumerate(edges):
        e = 1 << (n+i)
        all_faces.update((e, e|(1<<a), e|(1<<b), e|(1<<a)|(1<<b)))
    for v in range(n):
        inc = [n+i for i,(a,b) in enumerate(edges) if v in (a,b)]
        for size in range(1, len(inc)+1):
            for comb in combinations(inc,size):
                s = sum(1<<x for x in comb)
                all_faces.add(s); all_faces.add(s | (1<<v))
    return all_faces


def verify_collapses(n, edges):
    f = k0_faces(n, edges)
    pairs = []
    for v in range(n):
        inc = [n+i for i,(a,b) in enumerate(edges) if v in (a,b)]
        for r in range(len(inc),1,-1):
            for c in combinations(inc,r):
                s = sum(1<<x for x in c)
                pairs.append((s, s | (1<<v)))
    pairs.sort(key=lambda p: -p[0].bit_count())
    for small,big in pairs:
        assert small in f and big in f
        assert not any(x not in (small,big) and (x&small)==small for x in f), ('star',n,edges,small)
        f.remove(small); f.remove(big)
    for i,(a,b) in enumerate(edges):
        e = 1<<(n+i)
        small = (1<<a)|e; big = small|(1<<b)
        assert small in f and big in f
        assert not any(x not in (small,big) and (x&small)==small for x in f), ('triangle',n,edges,i)
        f.remove(small); f.remove(big)
        small = e; big = e|(1<<b)
        assert small in f and big in f
        assert not any(x not in (small,big) and (x&small)==small for x in f), ('midpoint',n,edges,i)
        f.remove(small); f.remove(big)
    assert f == set(x for group in clique_faces(complex_of_G(n,edges)) for x in group)


def check_graph(n,edges, do_distance=True):
    total, subdiv = total_and_subdivision(n,edges)
    if do_distance:
        dd = [distances(subdiv,v) for v in range(len(total))]
        assert all((dd[v][w] <= 2) == (w in total[v]) for v in range(len(total)) for w in range(v+1,len(total)))
    src = mod2_betti(clique_faces(complex_of_G(n,edges)))
    got = mod2_betti(clique_faces(total))
    t = sum(all({a,b} in [set(e) for e in edges] for a,b in combinations(c,2)) for c in combinations(range(n),3))
    for k in range(max(len(src),len(got),3)):
        p = (src[k] if k<len(src) else 0) + (t if k==2 else 0)
        g = got[k] if k<len(got) else 0
        assert p==g, ('Betti',n,edges,k,p,g)
    verify_collapses(n,edges)
    return t


def main():
    checked = 0; triangles = 0; by_n = {}
    for n in range(1,6):
        count=0
        for mask in range(1 << (n*(n-1)//2)):
            edges=graph_edges(n,mask)
            if not connected(n,edges):
                continue
            triangles += check_graph(n,edges)
            count += 1; checked += 1
        by_n[n]=count
    assert by_n=={1:1,2:1,3:4,4:38,5:728}
    assert checked==772
    print('CONNECTED_LABELED_GRAPHS_BY_ORDER',by_n)
    print('CHECKED_TOTAL',checked)
    print('TRIANGLE_SUM',triangles)
    print('TOTAL_GRAPH_SCALE_TWO_RIPS_COLLAPSE_PASS')

if __name__=='__main__':
    main()
