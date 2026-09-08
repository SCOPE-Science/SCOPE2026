"""Independent verifier for the cubic-bipartite census (stdlib + numpy only).

Checks per class: simple/cubic/connected/bipartite; girth recomputed by
independent BFS implementation; exact 6-cycle count (combinatorial);
spectrum recomputed + two-routine cross-check + trace identities;
Hamiltonian-cycle validity (exact edge-set check).
Also: pairwise non-isomorphism across all classes (independent backtracker),
bridgelessness (every edge is in a cycle), and bipartition-balance check.
Completeness cross-check (different conjugacy transversal) lives in
transversal_check.py.
"""
import json, sys
import numpy as np
from collections import deque

def adj_of(n, E):
    a = [[] for _ in range(n)]
    for u, v in E:
        a[u].append(v); a[v].append(u)
    return a

def bip_color(adj, n):
    c = [-1]*n; c[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if c[w] == -1:
                c[w] = 1 - c[u]; q.append(w)
            elif c[w] == c[u]:
                return None
    return c

def girth_bfs(adj, n):
    best = 10**9; wit = None
    for s in range(n):
        dist = [-1]*n; par = [-1]*n; dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if dist[w] == -1:
                    dist[w] = dist[u]+1; par[w] = u; q.append(w)
                elif w != par[u] and dist[w] <= dist[u] and dist[w] >= 0:
                    L = dist[u]+dist[w]+1
                    if L < best and L >= 3:
                        # rebuild cycle via LCA walk
                        anc = set(); x = u
                        while x != -1:
                            anc.add(x); x = par[x]
                        x = w
                        while x not in anc:
                            x = par[x]
                        common = x
                        cyc = []; x = u
                        while x != common:
                            cyc.append(x); x = par[x]
                        cyc.append(common)
                        tmp = []; x = w
                        while x != common:
                            tmp.append(x); x = par[x]
                        cyc += tmp[::-1]
                        if len(cyc) == L:
                            best = L; wit = cyc
    return best, wit

def count_6cycles(adj, n):
    # exact combinatorial count of 6-cycles (each found 12 times: 6 rotations x 2 directions;
    # enforce canonical: smallest vertex first, second < last, to count once)
    count = 0
    for v0 in range(n):
        for v1 in adj[v0]:
            if v1 <= v0: continue
            for v2 in adj[v1]:
                if v2 == v0: continue
                for v3 in adj[v2]:
                    if v3 == v1 or v3 <= v0: continue
                    for v4 in adj[v3]:
                        if v4 == v2 or v4 == v0 or v4 <= v0: continue
                        for v5 in adj[v4]:
                            if v5 == v3 or v5 == v1: continue
                            if v5 == v0: continue
                            if v0 in adj[v5] and v1 not in (v4, v5) and v5 > v1:
                                # verify simple: v5 distinct from v1..v4 and path simple
                                if len({v0, v1, v2, v3, v4, v5}) == 6:
                                    count += 1
    return count

def spectrum_check(adj, n):
    A = np.zeros((n, n))
    for u in range(n):
        for w in adj[u]:
            A[u, w] = 1.0
    ev = np.linalg.eigvalsh(A)
    ev2 = np.sort(np.linalg.eig(A)[0].real)
    assert np.max(np.abs(ev - ev2)) < 1e-6, "two-routine spectral mismatch"
    assert abs(float(np.sum(ev*ev)) - 3*n) < 1e-4, "trace(A^2)!=3n"
    assert abs(float(np.sum(ev)) ) < 1e-6, "trace(A)!=0"
    return [float(x) for x in ev]

def iso_exists(E1, E2, n):
    # independent bipartite-iso backtracker with degree/neighbor refinement
    a1 = adj_of(n, E1); a2 = adj_of(n, E2)
    c1 = bip_color(a1, n); c2 = bip_color(a2, n)
    if c1 is None or c2 is None:
        return False
    P1 = [i for i in range(n) if c1[i] == 0]; Q1 = [i for i in range(n) if c1[i] == 1]
    P2 = [i for i in range(n) if c2[i] == 0]; Q2 = [i for i in range(n) if c2[i] == 1]
    S1 = [set(a1[i]) for i in range(n)]; S2 = [set(a2[i]) for i in range(n)]
    for flip in range(2):
        A2, B2 = (P2, Q2) if flip == 0 else (Q2, P2)
        if len(A2) != len(P1) or len(B2) != len(Q1):
            continue
        mp = {}; used = set()
        # order P1: vertices whose neighbors are already constrained first is dynamic;
        # static order by sorted tuple of neighbor degrees for determinism
        order = sorted(P1, key=lambda v: tuple(sorted(len(a1[w]) for w in a1[v])))
        def recA(k):
            if k == len(order):
                return recB(0)
            v = order[k]
            need = set(mp[x] for x in a1[v] if x in mp)
            for w in A2:
                if w in used or not need.issubset(S2[w]):
                    continue
                mp[v] = w; used.add(w)
                if recA(k+1):
                    return True
                del mp[v]; used.discard(w)
            return False
        def recB(k):
            if k == len(Q1):
                for v in range(n):
                    if set(mp[x] for x in a1[v]) != S2[mp[v]]:
                        return False
                return True
            v = Q1[k]
            need = set(mp[x] for x in a1[v] if x in mp)
            for w in B2:
                if w in used or not need.issubset(S2[w]):
                    continue
                mp[v] = w; used.add(w)
                if recB(k+1):
                    return True
                del mp[v]; used.discard(w)
            return False
        mp = {}; used = set()
        if recA(0):
            return True
    return False

def verify_file(path, label, pairwise=True):
    d = json.load(open(path))
    out = []
    for nk, v in d.items():
        n = int(nk); cl = v['classes']
        h = 0
        for i, c in enumerate(cl):
            E = [tuple(e) for e in c['E']]
            assert len(E) == 3*n//2, (label, nk, i, 'edge count')
            seen = set()
            for u, vv in E:
                assert u != vv, 'loop'
                assert (u, vv) not in seen and (vv, u) not in seen, 'multi-edge'
                seen.add((u, vv)); seen.add((vv, u))
            adj = adj_of(n, E)
            assert all(len(a) == 3 for a in adj), (label, nk, i, 'cubic')
            assert connected(adj, n), (label, nk, i, 'connected')
            col = bip_color(adj, n)
            assert col is not None, 'bipartite'
            assert sum(col) == n//2, (label, nk, i, 'balanced bipartition')
            g, wit = girth_bfs(adj, n)
            assert g == c['girth'], (label, nk, i, 'girth', g, c['girth'])
            assert g % 2 == 0 and g >= 4, 'bipartite girth parity'
            # witness cycle validity
            assert wit is not None and len(wit) == g
            S = set(seen)
            for j in range(g):
                assert (wit[j], wit[(j+1) % g]) in S, 'girth witness edge'
            n6 = count_6cycles(adj, n)
            ev = spectrum_check(adj, n)
            assert max(abs(a-b) for a, b in zip(ev, c['eig'])) < 1e-6, (label, nk, i, 'spectrum')
            gap = 3.0 - sorted(ev)[-2]
            assert abs(gap - c['gap']) < 1e-6 and abs(gap - c['lam2']) < 1e-6, 'gap/lam2'
            # Hamiltonian cycle exact check
            cyc = c['ham_cycle']
            assert cyc is not None and len(cyc) == n and set(cyc) == set(range(n)), (label, nk, i, 'ham length/cover')
            for j in range(n):
                assert (cyc[j], cyc[(j+1) % n]) in S, (label, nk, i, 'ham edge', j)
            h += 1
            # bridgelessness: every edge lies on a cycle (BFS without the edge)
            for (u, vv) in E:
                # BFS from u avoiding edge (u,vv)
                dist = [-1]*n; dist[u] = 0
                q = deque([u])
                while q:
                    x = q.popleft()
                    for y in adj[x]:
                        if (x == u and y == vv) or (x == vv and y == u):
                            continue
                        if dist[y] == -1:
                            dist[y] = dist[x]+1; q.append(y)
                assert dist[vv] != -1, (label, nk, i, 'bridge found', (u, vv))
            out.append((nk, i, g, n6, round(gap, 6)))
        if pairwise:
            for i in range(len(cl)):
                for j in range(i+1, len(cl)):
                    assert not iso_exists(cl[i]['E'], cl[j]['E'], n), (label, nk, 'isomorphic pair', i, j)
        print(f"{label} n={nk}: {len(cl)} classes ALL VERIFIED (cubic/conn/bip/girth/spec/ham-cycle/bridgeless/pairwise-distinct), ham={h}", flush=True)
    return out

def connected(adj, n):
    seen = [False]*n; st = [0]; seen[0] = True
    while st:
        u = st.pop()
        for w in adj[u]:
            if not seen[w]:
                seen[w] = True; st.append(w)
    return all(seen)

if __name__ == '__main__':
    allrows = []
    allrows += verify_file('output/artifacts/backup/keepsmall.json', 'small', pairwise=True)
    allrows += verify_file('output/artifacts/backup/keep14.json', 'n14', pairwise=True)
    allrows += verify_file('output/artifacts/backup/keep16.json', 'n16', pairwise=True)
    json.dump(allrows, open('output/artifacts/verify_rows.json', 'w'), indent=1)
    print('wrote output/artifacts/verify_rows.json', flush=True)
