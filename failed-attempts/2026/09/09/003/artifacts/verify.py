"""Independent verifier: replays covers, re-enumerates cycles from scratch,
checks census counts, and proves optimality via IDA* (no cover with total <= L-1).
Exits nonzero on any failure."""
import json, sys
from collections import deque

def adj_of(n, edges):
    a = [[] for _ in range(n)]
    for u, v in edges:
        a[u].append(v); a[v].append(u)
    return a

def bridges(n, edges):
    a = adj_of(n, edges)
    out = 0
    for (u, v) in edges:
        seen = {u}; st = [u]
        while st:
            x = st.pop()
            for w in a[x]:
                if (x == u and w == v) or (x == v and w == u):
                    continue
                if w not in seen:
                    seen.add(w); st.append(w)
        if v not in seen:
            out += 1
    return out

def enum_cycles(n, edges):
    idx = {}
    for k, (u, v) in enumerate(edges):
        idx[(u, v)] = k; idx[(v, u)] = k
    a = adj_of(n, edges)
    for u in range(n):
        a[u].sort()
    seen = {}
    for s in range(n):
        stack = [(s, (s,), frozenset([s]))]
        while stack:
            u, path, pset = stack.pop()
            for w in a[u]:
                if w == s:
                    if len(path) >= 3:
                        mask = 0
                        for t in range(len(path)):
                            mask |= 1 << idx[(path[t], path[(t+1) % len(path)])]
                        if mask not in seen:
                            seen[mask] = list(path)
                elif w > s and w not in pset:
                    stack.append((w, path+(w,), pset | {w}))
    return seen

def valid_cycle(n, edges, verts):
    es = set()
    for u, v in edges:
        es.add((u, v)); es.add((v, u))
    k = len(verts)
    if k < 3 or len(set(verts)) != k:
        return False
    return all((verts[t], verts[(t+1) % k]) in es for t in range(k))

def ida_no_cover(masks_by_edge, weights, m, bound):
    """Prove no cover with total length <= bound. Depth-first, first-uncovered
    edge branching, remaining-budget prune. Independent of Dijkstra/B&B."""
    full = (1 << m) - 1
    cands = {}
    for e, lst in masks_by_edge.items():
        cands[e] = sorted(lst, key=lambda c: weights[c])
    nodes = [0]
    def first_free(u):
        for e in range(m):
            if not (u >> e) & 1:
                return e
        return -1
    def rec(u, budget):
        nodes[0] += 1
        e = first_free(u)
        if e == -1:
            return True  # covered within budget -> cover of total<=bound exists
        for c in cands[e]:
            w = weights[c]
            if w > budget:
                break
            if rec(u | c, budget - w):
                return True
        return False
    found = rec(0, bound)
    return (not found), nodes[0]

def main():
    graphs = json.load(open('output/artifacts/graphs.json'))
    covers = json.load(open('output/artifacts/covers.json'))
    assert len(graphs) == len(covers) == 11, (len(graphs), len(covers))
    byfam = {}
    for r in covers:
        byfam.setdefault(r['family'], []).append(r)
    # census: complete strata counts must be 1,2,5 (OEIS A002851 prefix)
    assert len(byfam['cubic_n4']) == 1
    assert len(byfam['cubic_n6']) == 2
    assert len(byfam['cubic_n8']) == 5
    # labeled-multiplicity cross-check: 1, 7, 552
    assert sum(r.get('labeled_multiplicity', 1) for r in byfam['cubic_n4']) == 1
    assert sum(r.get('labeled_multiplicity', 1) for r in byfam['cubic_n6']) == 7
    assert sum(r.get('labeled_multiplicity', 1) for r in byfam['cubic_n8']) == 552
    for r in covers:
        n, m, E, L = r['n'], r['m'], [tuple(e) for e in r['edges']], r['L']
        assert m == 3*n//2, (r['family'], m, n)
        assert sorted(sum(([u, v] for u, v in E), [])) is not None
        from collections import Counter
        deg = Counter()
        for u, v in E:
            deg[u] += 1; deg[v] += 1
        assert sorted(deg.values()) == [3]*n, (r['family'], 'cubic')
        assert bridges(n, E) == 0, (r['family'], 'must be bridgeless')
        cyc = enum_cycles(n, E)
        assert len(cyc) == r['ncycles_total'], (r['family'], len(cyc), r['ncycles_total'])
        weights = {cm: bin(cm).count('1') for cm in cyc}
        girth = min(weights.values())
        # replay listed cover
        tot = 0; u = 0
        for c in r['cover_cycles']:
            v = c['verts']
            assert valid_cycle(n, E, v), (r['family'], 'listed object not a cycle')
            assert c['len'] == len(v)
            mask = 0
            idx = {}
            for k, (a, b) in enumerate(E):
                idx[(a, b)] = k; idx[(b, a)] = k
            for t in range(len(v)):
                mask |= 1 << idx[(v[t], v[(t+1) % len(v)])]
            assert mask in weights, (r['family'], 'cover cycle not simple/induced ok')
            tot += weights[mask]; u |= mask
        assert tot == L, (r['family'], tot, L)
        assert u == (1 << m) - 1, (r['family'], 'cover misses edges')
        # 7m/5 audit
        assert (L <= 7*m/5 + 1e-9) == r['within_7m5']
        # independent optimality: no cover with total <= L-1 (IDA*)
        mbe = {e: [] for e in range(m)}
        for cm in cyc:
            for e in range(m):
                if (cm >> e) & 1:
                    mbe[e].append(cm)
        opt, nn = ida_no_cover(mbe, weights, m, L-1)
        assert opt, (r['family'], 'SHORTER COVER EXISTS')
        print(f"OK {r['family']}[{r['idx']}]: n={n} m={m} girth={girth} "
              f"ncyc={len(cyc)} L={L} ratio={L/m:.4f} IDA*nodes={nn}", flush=True)
    Rs = max(r['L']/r['m'] for r in covers)
    print(f"VERIFY_OK all 11 graphs; R*={Rs:.6f}", flush=True)

if __name__ == '__main__':
    main()
