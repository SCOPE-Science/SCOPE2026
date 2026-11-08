"""Direct finite checks for clique-substitution minimum independent domination reconfiguration.

Requires Python 3 standard library only. This constructs and checks the original
independent domination and token-slide definitions, by direct graph-definition tests alongside separate projected formulas.
"""
from itertools import combinations, product
from collections import deque
from math import comb


def edges_of_mask(n, mask):
    pairs = list(combinations(range(n), 2))
    return [e for j, e in enumerate(pairs) if mask >> j & 1]


def adj_from_edges(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def minimum_independent_dominating_sets(adj):
    n = len(adj)
    ans = []
    best = n + 1
    for mask in range(1 << n):
        S = {i for i in range(n) if (mask >> i) & 1}
        if len(S) > best:
            continue
        if any(u in adj[v] for u in S for v in S if u != v):
            continue
        if any(v not in S and not (adj[v] & S) for v in range(n)):
            continue
        if len(S) < best:
            best, ans = len(S), []
        ans.append(frozenset(S))
    return best, ans


def slide_graph(adj, sets):
    ix = {S: j for j, S in enumerate(sets)}
    E = set()
    for j, S in enumerate(sets):
        for u in S:
            for v in adj[u]:
                if v in S:
                    continue
                k = ix.get((S - {u}) | {v})
                if k is not None:
                    E.add(tuple(sorted((j, k))))
    return E


def substitution(adj, sizes):
    starts = []
    orig = []
    for i, mi in enumerate(sizes):
        starts.append(len(orig))
        orig.extend([i] * mi)
    B = [set() for _ in orig]
    for u in range(len(orig)):
        for v in range(u + 1, len(orig)):
            if orig[u] == orig[v] or orig[v] in adj[orig[u]]:
                B[u].add(v); B[v].add(u)
    return B, orig


def lift_nodes(base_sets, orig, sizes):
    out = []
    offsets = [sum(sizes[:i]) for i in range(len(sizes))]
    for S in base_sets:
        s = sorted(S)
        for labels in product(*(range(sizes[u]) for u in s)):
            out.append(frozenset(offsets[u] + c for u, c in zip(s, labels)))
    return out


def lifted_edge_formula(base_sets, base_edges, sizes):
    k = len(base_sets[0])
    nodes = sum(__import__('math').prod(sizes[v] for v in S) for S in base_sets)
    local = sum(sum(comb(sizes[v], 2) * __import__('math').prod(sizes[w] for w in S if w != v) for v in S) for S in base_sets)
    remote = sum(__import__('math').prod(sizes[w] for w in (base_sets[i] & base_sets[j]))
                 * sizes[next(iter(base_sets[i] - base_sets[j]))]
                 * sizes[next(iter(base_sets[j] - base_sets[i]))]
                 for i, j in base_edges)
    return nodes, local + remote


def components_count(N, edges):
    A = [[] for _ in range(N)]
    for u, v in edges:
        A[u].append(v); A[v].append(u)
    seen = set(); c = 0
    for i in range(N):
        if i in seen:
            continue
        c += 1
        todo = [i]; seen.add(i)
        for u in todo:
            for v in A[u]:
                if v not in seen:
                    seen.add(v); todo.append(v)
    return c


def bfs_distances(num, edges, s):
    A = [[] for _ in range(num)]
    for i, j in edges:
        A[i].append(j); A[j].append(i)
    d = {s: 0}; q = deque([s])
    while q:
        u = q.popleft()
        for v in A[u]:
            if v not in d:
                d[v] = d[u] + 1; q.append(v)
    return d


def projected_distance(A, B, base_sets, base_edges, orig):
    # Optimization over all base walks, with a 1-cost charge for any changed
    # fiber label that persists through every base state of that walk.
    s = frozenset(orig[x] for x in A)
    t = frozenset(orig[x] for x in B)
    ix = {S: i for i, S in enumerate(base_sets)}
    SA, SB = {orig[x]: x for x in A}, {orig[x]: x for x in B}
    mismatches = frozenset(v for v in s & t if SA[v] != SB[v])
    A_base = [[] for _ in base_sets]
    for u, v in base_edges:
        A_base[u].append(v); A_base[v].append(u)
    start = (ix[s], mismatches)
    d = {start: 0}; q = deque([start]); ans = float('inf')
    while q:
        u, keep = q.popleft()
        dist = d[(u, keep)]
        if u == ix[t]:
            ans = min(ans, dist + len(keep))
        for v in A_base[u]:
            nxt = (v, keep & base_sets[v])
            if nxt not in d:
                d[nxt] = dist + 1; q.append(nxt)
    return ans


def test_profile(n, mask, sizes, do_metrics=False):
    G = adj_from_edges(n, edges_of_mask(n, mask))
    k, base_sets = minimum_independent_dominating_sets(G)
    base_edges = slide_graph(G, base_sets)
    H, orig = substitution(G, sizes)
    kb, direct_sets = minimum_independent_dominating_sets(H)
    assert kb == k, (n, mask, sizes, 'min')
    lifted = lift_nodes(base_sets, orig, sizes)
    assert set(lifted) == set(direct_sets), (n, mask, sizes, 'vertices')
    direct_edges = slide_graph(H, direct_sets)
    X = {S: i for i, S in enumerate(direct_sets)}
    # Classify all direct edges by projected base supports and label changes.
    expected_edges = set()
    for i, A in enumerate(lifted):
        for j in range(i + 1, len(lifted)):
            B = lifted[j]
            if len(A-B) != 1 or len(B-A) != 1: continue
            u = next(iter(A-B)); v = next(iter(B-A))
            if v in H[u]:
                expected_edges.add(tuple(sorted((X[A], X[B]))))
    assert expected_edges == direct_edges, (n, mask, sizes, 'edge characterization')
    assert (len(direct_sets),len(direct_edges)) == lifted_edge_formula(base_sets,base_edges,sizes), (n,mask,sizes,'counts')
    assert components_count(len(direct_sets),direct_edges) == components_count(len(base_sets),base_edges), (n,mask,sizes,'components')
    pairs=0
    if do_metrics and len(direct_sets)<130:
        # Independent shortest paths in the actual token-slide graph.
        for i in range(len(direct_sets)):
            dist = bfs_distances(len(direct_sets), direct_edges, i)
            for j in range(i+1,len(direct_sets)):
                predicted = projected_distance(direct_sets[i],direct_sets[j],base_sets,base_edges,orig)
                actual = dist.get(j, float('inf'))
                assert predicted == actual,(n,mask,sizes,'metric',i,j,predicted,actual)
                pairs += 1
    return len(direct_sets),len(direct_edges),pairs


def cycle_test():
    num = 0
    for n in range(4,45):
        G = adj_from_edges(n, [(i,(i+1)%n) for i in range(n)])
        k = (n+2)//3
        d = 3*k-n
        patterns = set()
        # All minimal independent dominating supports by cyclic compositions.
        for start in range(n):
            for indices2 in combinations(range(k), d):
                gaps = [2 if i in indices2 else 3 for i in range(k)]
                x=start; S=[]
                for gap in gaps:
                    S.append(x); x=(x+gap)%n
                patterns.add(frozenset(S))
        ss = sorted(patterns, key=lambda s: sorted(s))
        def C(a,b): return comb(a,b) if 0<=b<=a else 0
        num_formula=n*C(k,d)//k
        edge_formula=n*C(k-2,d-1)
        ee=slide_graph(G,ss)
        assert len(ss)==num_formula and len(ee)==edge_formula,(n,k,d,len(ss),len(ee),num_formula,edge_formula)
        num+=1
    # Independently enumerate all subsets of small cycles using original tests.
    for n in range(4, 15):
        G = adj_from_edges(n, [(i, (i+1)%n) for i in range(n)])
        k, orig_sets = minimum_independent_dominating_sets(G)
        d = 3*k-n
        C = lambda a,b: comb(a,b) if 0<=b<=a else 0
        assert len(orig_sets) == n*C(k,d)//k
        assert len(slide_graph(G, orig_sets)) == n*C(k-2,d-1)
    return num


def main():
    prof=0; vertices=0; edges=0; pairs=0
    for n in range(1,5):
        for mask in range(1 << comb(n,2)):
            for sizes in [[2]*n, [1+(i%3) for i in range(n)]]:
                v,e,p=test_profile(n,mask,sizes,do_metrics=(n<=3 or mask%7==0))
                prof+=1; vertices+=v;edges+=e;pairs+=p
    for n in [5]:
        for mask in [0,1,3,7,13,21,31,45,73,91,127,255,341,511,1023]:
            for sizes in [[2]*n, [1+(i%3) for i in range(n)]]:
                v,e,p=test_profile(n,mask,sizes,do_metrics=(mask in (0,31,341)))
                prof+=1;vertices+=v;edges+=e;pairs+=p
    c=cycle_test()
    print(f'VERIFY_OK profiles={prof} direct_i_graph_nodes={vertices} direct_edges={edges} shortest_path_pairs={pairs} cyclic_parameters={c} direct_cycles=11 independent_domination=PASS lifted_adjacency=PASS nonuniform_edge_counts=PASS component_preservation=PASS shortest_path_formula=PASS cycle_counts=PASS')

if __name__=='__main__': main()
