"""Pipeline: complete exact shortest-cycle-cover census for all connected cubic
graphs n=4,6,8 (+ named exhibits: Petersen n=10, Heawood & prism-Y7 n=14).
Stdlib only. Writes graphs.json, covers.json, solver_log.json."""
import json, itertools, heapq, time, sys

# ---------- basic graph utils (edge list, n) ----------
def deg_of(n, edges):
    d = [0]*n
    for u, v in edges:
        d[u] += 1; d[v] += 1
    return d

def adj_of(n, edges):
    a = [[] for _ in range(n)]
    for u, v in edges:
        a[u].append(v); a[v].append(u)
    return a

def connected(n, edges):
    a = adj_of(n, edges)
    seen = {0}; st = [0]
    while st:
        u = st.pop()
        for w in a[u]:
            if w not in seen:
                seen.add(w); st.append(w)
    return len(seen) == n

def bridges(n, edges):
    a = adj_of(n, edges)
    out = []
    for i, (u, v) in enumerate(edges):
        seen = {u}; st = [u]
        while st:
            x = st.pop()
            for w in a[x]:
                if (x == u and w == v) or (x == v and w == u):
                    continue
                if w not in seen:
                    seen.add(w); st.append(w)
        if v not in seen:
            out.append(i)
    return out

def bfs_diam(n, edges):
    a = adj_of(n, edges)
    from collections import deque
    D = 0
    for s in range(n):
        dist = [-1]*n; dist[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for w in a[u]:
                if dist[w] < 0:
                    dist[w] = dist[u]+1; q.append(w)
        D = max(D, max(dist))
    return D

def is_bipartite(n, edges):
    a = adj_of(n, edges)
    col = [-1]*n
    for s in range(n):
        if col[s] >= 0: continue
        col[s] = 0; st = [s]
        while st:
            u = st.pop()
            for w in a[u]:
                if col[w] < 0:
                    col[w] = col[u]^1; st.append(w)
                elif col[w] == col[u]:
                    return False
    return True

# ---------- labeled cubic enumeration with N(0)={1,2,3} fixed ----------
def enum_labeled_cubic(n):
    assert n % 2 == 0
    base = [(0, 1), (0, 2), (0, 3)]
    deg = [0]*n
    for u, v in base:
        deg[u] += 1; deg[v] += 1
    pairs = [(i, j) for i in range(1, n) for j in range(i+1, n)]
    need = 3*n//2 - len(base)
    res = []
    cur = []

    # remaining-pair-index per vertex for pruning (suffix counts)
    pos_of = {p: k for k, p in enumerate(pairs)}
    P = len(pairs)
    def rec(k, left):
        if left == 0:
            if all(d == 3 for d in deg):
                res.append(list(cur))
            return
        if k >= P:
            return
        # prune: enough pairs left?
        if P - k < left:
            return
        # prune per-vertex: need[v] <= pairs involving v in pairs[k:]
        # (cheap check only when deep)
        i, j = pairs[k]
        # try include
        if deg[i] < 3 and deg[j] < 3:
            deg[i] += 1; deg[j] += 1; cur.append((i, j))
            # quick feasibility: every vertex need <= remaining incident pairs
            ok = True
            rem = P - (k+1)
            if rem >= 0:
                for v in range(n):
                    nd = 3 - deg[v]
                    if nd <= 0: continue
                    # count pairs[t], t>k involving v
                    c = 0
                    for t in range(k+1, P):
                        a, b = pairs[t]
                        if a == v or b == v:
                            c += 1
                            if c >= nd: break
                    if c < nd:
                        ok = False; break
            if ok:
                rec(k+1, left-1)
            cur.pop(); deg[i] -= 1; deg[j] -= 1
        # try exclude
        rec(k+1, left)
    rec(0, need)
    return [base + c for c in res]

# ---------- simple cycle enumeration (edge masks), canonical min-vertex ----------
def enumerate_cycles(n, edges):
    m = len(edges)
    idx = {}
    for k, (u, v) in enumerate(edges):
        idx[(u, v)] = k; idx[(v, u)] = k
    a = adj_of(n, edges)
    for u in range(n):
        a[u].sort()
    seen = {}  # mask -> vertex list
    for s in range(n):
        stack = [(s, [s], {s})]  # current, path, set
        while stack:
            u, path, pset = stack.pop()
            for w in a[u]:
                if w == s:
                    if len(path) >= 3:
                        mask = 0
                        pp = path
                        for t in range(len(pp)):
                            mask |= 1 << idx[(pp[t], pp[(t+1) % len(pp)])]
                        if mask not in seen:
                            seen[mask] = list(path)
                elif w > s and w not in pset:
                    stack.append((w, path+[w], pset | {w}))
    masks = sorted(seen.keys())
    return masks, seen

def cycle_invariant_key(n, edges, masks):
    import math
    lens = {}
    for mm in masks:
        L = bin(mm).count('1')
        lens[L] = lens.get(L, 0)+1
    girth = min(lens) if lens else -1
    return (is_bipartite(n, edges), girth, bfs_diam(n, edges),
            tuple(sorted(lens.items())))

# ---------- explicit isomorphism search (backtracking, cubic: fast) ----------
def find_iso(n, E1, E2):
    A1 = adj_of(n, E1); A2 = adj_of(n, E2)
    S1 = [set(x) for x in A1]; S2 = [set(x) for x in A2]
    for s in range(n):
        # map 0 -> s
        f = [-1]*n; used = [False]*n
        f[0] = s; used[s] = True
        order = [0]
        ok = True
        # greedy extend in BFS order of G1
        from collections import deque
        q = deque([0]); vis = {0}
        bord = [0]
        # simple recursive
        def rec():
            # pick unmapped vertex adjacent to mapped region if possible
            u = -1
            for x in range(n):
                if f[x] < 0:
                    if any(f[y] >= 0 for y in A1[x]):
                        u = x; break
            if u == -1:
                for x in range(n):
                    if f[x] < 0:
                        u = x; break
            if u == -1:
                return True
            # candidates: unused vertices with consistent adjacency to mapped nbrs
            mapped_nbrs = [y for y in A1[u] if f[y] >= 0]
            for c in range(n):
                if used[c]: continue
                if all((c in S2[f[y]]) for y in mapped_nbrs):
                    # also non-nbrs among mapped must be non-nbrs? (induced check at end; partial: check degrees later)
                    f[u] = c; used[c] = True
                    if rec(): return True
                    f[u] = -1; used[c] = False
            return False
        if rec():
            # verify full
            T = [set() for _ in range(n)]
            good = True
            for u, v in E1:
                if f[v] not in S2[f[u]]:
                    good = False; break
            if good:
                return f
    return None

# ---------- Solver A: Dijkstra over masks, first-uncovered-edge branching ----------
def solve_A(masks, weights, m, by_edge):
    full = (1 << m) - 1
    INF = 10**18
    dist = {0: 0}
    par = {}
    heap = [(0, 0)]
    states = 0
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist.get(u, INF):
            continue
        states += 1
        if u == full:
            break
        # first uncovered edge
        e = 0
        while (u >> e) & 1:
            e += 1
        for cm, w in by_edge[e]:
            v = u | cm
            nd = d + w
            if nd < dist.get(v, INF):
                dist[v] = nd
                par[v] = (u, cm)
                heapq.heappush(heap, (nd, v))
    assert full in dist, "cover does not exist (bridged?)"
    # reconstruct
    cov = []
    u = full
    while u != 0:
        p, cm = par[u]
        cov.append(cm)
        u = p
    return dist[full], cov, states

# ---------- Solver B: independent memoized B&B with greedy UB ----------
def greedy_ub(masks, weights, m, by_edge):
    full = (1 << m) - 1
    u = 0; tot = 0; cov = []
    while u != full:
        e = 0
        while (u >> e) & 1:
            e += 1
        best = None; bestr = None
        for cm, w in by_edge[e]:
            new = bin(cm & ~u).count('1')
            if new == 0: continue
            r = w / new
            if bestr is None or r < bestr:
                bestr = r; best = cm
        assert best is not None
        cov.append(best)
        tot += weights[best]
        u |= best
    return tot, cov

def solve_B(masks, weights, m, by_edge):
    full = (1 << m) - 1
    gmax = max(weights.values()) if weights else 1
    gmin = min(weights.values()) if weights else 1
    best, bbest_cov = greedy_ub(masks, weights, m, by_edge)
    memo = {}
    nodes = {'n': 0, 'prune': 0}
    sys.setrecursionlimit(100000)
    def lb(u):
        rem = bin(full & ~u).count('1')
        if rem == 0: return 0
        return ((rem + gmax - 1)//gmax)*gmin
    # order cycles per edge by efficiency
    be = {}
    for e, lst in by_edge.items():
        be[e] = sorted(lst, key=lambda t: (t[1]/max(1, bin(t[0]).count('1')), t[1]))
    from functools import lru_cache
    best_box = [best]; sol = {'cov': list(bbest_cov)}
    def rec(u, cur, cov):
        nodes['n'] += 1
        if cur + lb(u) >= best_box[0]:
            nodes['prune'] += 1
            return
        if u == full:
            if cur < best_box[0]:
                best_box[0] = cur; sol['cov'] = list(cov)
            return
        if u in memo and memo[u] <= cur:
            nodes['prune'] += 1
            return
        memo[u] = cur
        e = 0
        while (u >> e) & 1:
            e += 1
        for cm, w in be[e]:
            if cur + w + lb(u | cm) >= best_box[0]:
                # ordered by efficiency; can't break (weights differ) -> just skip
                pass
            cov.append(cm)
            rec(u | cm, cur + w, cov)
            cov.pop()
    rec(0, 0, [])
    return best_box[0], sol['cov'], nodes, memo

def canon_edges(n, edges):
    return sorted((min(u, v), max(u, v)) for u, v in edges)

def main():
    t0 = time.time()
    log = {'graphs': [], 'timings': {}}
    table = []  # result rows
    # ---- complete strata n=4,6,8 ----
    strata = {}
    for n in (4, 6, 8):
        t = time.time()
        lab = enum_labeled_cubic(n)
        con = [E for E in lab if connected(n, E)]
        # group by invariant
        groups = {}
        for E in con:
            E = canon_edges(n, E)
            masks, _ = enumerate_cycles(n, E)
            key = cycle_invariant_key(n, E, masks)
            groups.setdefault(key, []).append(E)
        # merge within groups by explicit iso
        reps = []
        iso_notes = []
        for key, lst in groups.items():
            classes = []  # list of (rep, members)
            for E in lst:
                placed = False
                for c in classes:
                    if find_iso(n, E, c[0]) is not None:
                        c[1].append(E)
                        placed = True
                        break
                if not placed:
                    classes.append([E, [E]])
            for c in classes:
                reps.append((key, c[0], len(c[1])))
        nclass = len(reps)
        strata[n] = (len(lab), len(con), nclass)
        log['timings'][f'enum_classify_n{n}'] = round(time.time()-t, 2)
        print(f"n={n}: labeled={len(lab)} connected={len(con)} classes={nclass}", flush=True)
        # verify expected counts 1,2,5
        exp = {4: 1, 6: 2, 8: 5}[n]
        assert nclass == exp, f"n={n}: got {nclass} classes, expected {exp}"
        # solve each rep
        for gi, (key, E, mult) in enumerate(sorted(reps, key=lambda r: json.dumps(r[0], default=str))):
            m = len(E)
            assert not bridges(n, E), f"unexpected bridge at n={n}"
            masks, vrep = enumerate_cycles(n, E)
            weights = {cm: bin(cm).count('1') for cm in masks}
            by_edge = {e: [] for e in range(m)}
            for cm in masks:
                for e in range(m):
                    if (cm >> e) & 1:
                        by_edge[e].append((cm, weights[cm]))
            ta = time.time()
            LA, covA, stA = solve_A(masks, weights, m, by_edge)
            tb = time.time()
            LB, covB, nodesB, _ = solve_B(masks, weights, m, by_edge)
            tc = time.time()
            assert LA == LB, f"SOLVER MISMATCH n={n} gi={gi}: {LA} vs {LB}"
            full = (1 << m) - 1
            ua = 0
            for cm in covA: ua |= cm
            assert ua == full
            assert sum(weights[c] for c in covA) == LA
            ub = 0
            for cm in covB: ub |= cm
            assert ub == full
            row = {'family': f'cubic_n{n}', 'idx': gi, 'n': n, 'm': m,
                   'edges': E, 'L': LA, 'cover_cycles':
                   [{'verts': vrep[cm], 'len': weights[cm]} for cm in covA],
                   'ncycles_total': len(masks), 'solverA_states': stA,
                   'solverB_nodes': nodesB['n'], 'solverB_prunes': nodesB['prune'],
                   'timeA': round(tb-ta, 3), 'timeB': round(tc-tb, 3),
                   'labeled_multiplicity': mult,
                   'bound_7m_over_5': 7*m/5, 'ratio': LA/m,
                   'within_7m5': LA <= 7*m/5 + 1e-9}
            table.append(row)
            log['graphs'].append({'family': row['family'], 'idx': gi, 'L': LA,
                                  'A_states': stA, 'B_nodes': nodesB['n']})
            print(f"  class {gi}: L={LA} m={m} ratio={LA/m:.4f} "
                  f"(A:{stA} st {tb-ta:.2f}s, B:{nodesB['n']} nd {tc-tb:.2f}s)", flush=True)
    # ---- named exhibits ----
    # Petersen
    P = [(i, (i+1) % 5) for i in range(5)] + \
        [(5+((i) % 5), 5+((i+2) % 5)) for i in range(5)] + \
        [(i, 5+i) for i in range(5)]
    Pn = 10
    assert sorted(deg_of(Pn, P)) == [3]*10 and connected(Pn, P) and not bridges(Pn, P)
    # Heawood via Fano incidence (diff set {0,1,3})
    H = []
    for j in range(7):
        for d in (0, 1, 3):
            H.append((j+d) % 7 if False else ((j+d) % 7, 7+j))
    Hn = 14
    assert sorted(deg_of(Hn, H)) == [3]*14 and connected(Hn, H) and not bridges(Hn, H)
    # Prism Y7
    Y = [(i, (i+1) % 7) for i in range(7)] + \
        [(7+i, 7+((i+1) % 7)) for i in range(7)] + [(i, 7+i) for i in range(7)]
    Yn = 14
    assert sorted(deg_of(Yn, Y)) == [3]*14 and connected(Yn, Y) and not bridges(Yn, Y)
    for name, n, E in (('petersen', Pn, P), ('heawood', Hn, H), ('prismY7', Yn, Y)):
        t = time.time()
        E = canon_edges(n, E)
        m = len(E)
        masks, vrep = enumerate_cycles(n, E)
        weights = {cm: bin(cm).count('1') for cm in masks}
        by_edge = {e: [] for e in range(m)}
        for cm in masks:
            for e in range(m):
                if (cm >> e) & 1:
                    by_edge[e].append((cm, weights[cm]))
        LA, covA, stA = solve_A(masks, weights, m, by_edge)
        LB, covB, nodesB, _ = solve_B(masks, weights, m, by_edge)
        assert LA == LB, f"SOLVER MISMATCH {name}: {LA} vs {LB}"
        full = (1 << m) - 1
        ua = 0
        for cm in covA: ua |= cm
        assert ua == full and sum(weights[c] for c in covA) == LA
        ub = 0
        for cm in covB: ub |= cm
        assert ub == full
        row = {'family': name, 'idx': 0, 'n': n, 'm': m, 'edges': E, 'L': LA,
               'cover_cycles': [{'verts': vrep[cm], 'len': weights[cm]} for cm in covA],
               'ncycles_total': len(masks), 'solverA_states': stA,
               'solverB_nodes': nodesB['n'], 'solverB_prunes': nodesB['prune'],
               'time_solve': round(time.time()-t, 2),
               'bound_7m_over_5': 7*m/5, 'ratio': LA/m,
               'within_7m5': LA <= 7*m/5 + 1e-9}
        table.append(row)
        log['graphs'].append({'family': name, 'idx': 0, 'L': LA,
                              'A_states': stA, 'B_nodes': nodesB['n']})
        print(f"{name}: n={n} m={m} ncyc={len(masks)} L={LA} ratio={LA/m:.4f} "
              f"7m/5={7*m/5} t={time.time()-t:.1f}s", flush=True)
    R = max(r['L']/r['m'] for r in table)
    star = [r for r in table if abs(r['L']/r['m']-R) < 1e-12]
    log['Rstar'] = R
    log['extremal'] = [(r['family'], r['idx'], r['L'], r['m']) for r in star]
    log['total_time'] = round(time.time()-t0, 1)
    with open('output/artifacts/graphs.json', 'w') as f:
        json.dump([{'family': r['family'], 'idx': r['idx'], 'n': r['n'], 'm': r['m'],
                    'edges': r['edges'], 'labeled_multiplicity':
                    r.get('labeled_multiplicity', 1)} for r in table], f, indent=1)
    with open('output/artifacts/covers.json', 'w') as f:
        json.dump(table, f, indent=1)
    with open('output/artifacts/solver_log.json', 'w') as f:
        json.dump(log, f, indent=1)
    print(f"R*={R:.6f} extremal={log['extremal']} total={log['total_time']}s", flush=True)

if __name__ == '__main__':
    main()
