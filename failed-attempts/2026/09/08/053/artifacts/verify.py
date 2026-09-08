"""Independent verifier for mu_results.json (stdlib only).

Re-derives from each stored Cayley table, with independently written code:
 1. group axioms (exhaustive assoc/identity/inverse);
 2. each witness set is a subgroup (closure) of the claimed order;
 3. each witness core = brute-force intersection of ALL conjugates;
 4. family core-intersection trivial  => coset action faithful (kernel = intersection
    of cores, standard lemma), degree = index sum = claimed mu;
 5. minimality: independent exact shortest-path over the normal-subgroup lattice
    (recomputed subgroup lattice + recomputed cores, separate implementation);
 6. cross-checks abelian values against Johnson's formula sum of prime-power cyclic orders.
"""
import json, sys, itertools, heapq

def load():
    with open("output/artifacts/mu_results.json") as f:
        return json.load(f)["groups"]

JOHNSON = {
    "C32": 32, "C16xC2": 18, "C8xC4": 12, "C8xC2xC2": 12, "C4xC4xC2": 10,
    "C4xC2xC2xC2": 10, "C2xC2xC2xC2xC2": 10, "C64": 64, "C32xC2": 34,
    "C16xC4": 20, "C8xC8": 16, "C4xC4xC4": 12, "C4xC4xC2xC2": 12, "C2^6": 12,
}

def main():
    groups = load()
    assert len(groups) == 29, f"expected 29 groups, got {len(groups)}"
    for G in groups:
        n, name = G["order"], G["name"]
        flat = G["mul_flat"]
        assert len(flat) == n*n
        mul = [flat[i*n:(i+1)*n] for i in range(n)]
        # 1. axioms
        assert all(mul[0][g] == g and mul[g][0] == g for g in range(n)), f"{name}: identity"
        inv = []
        for g in range(n):
            hs = [h for h in range(n) if mul[g][h] == 0 and mul[h][g] == 0]
            assert len(hs) == 1, f"{name}: inverse {g}"
            inv.append(hs[0])
        for a in range(n):
            for b in range(n):
                ab = mul[a][b]
                for c in range(n):
                    assert mul[ab][c] == mul[a][mul[b][c]], f"{name}: assoc"
        # subgroup lattice (independent: closure of every singleton-extension, iterative)
        subs = {1}
        stack = [1]
        def close(m):
            els = [g for g in range(n) if m >> g & 1]
            while True:
                grown = False
                for s in els:
                    for t in els:
                        for h in (mul[s][t], inv[s]):
                            if not (m >> h & 1):
                                m |= (1 << h); els.append(h); grown = True
                if not grown: return m
        while stack:
            s = stack.pop()
            for g in range(n):
                if s >> g & 1: continue
                t = close(s | (1 << g))
                if t not in subs:
                    subs.add(t); stack.append(t)
        assert len(subs) == G["n_subgroups"], f"{name}: subgroup count {len(subs)} vs {G['n_subgroups']}"
        conj = [[mul[mul[g][h]][inv[g]] for h in range(n)] for g in range(n)]
        def core_of(m):
            c = (1 << n) - 1
            for g in range(n):
                cc = 0
                mm = m
                while mm:
                    l = mm & (-mm); h = l.bit_length() - 1
                    cc |= (1 << conj[g][h]); mm ^= l
                c &= cc
                if c == 1: break
            return c
        # 2-4. witness checks
        tot = 0; inter = (1 << n) - 1
        for w in G["family"]:
            m = w["witness_mask"]
            assert m in subs, f"{name}: witness not a subgroup"
            assert bin(m).count("1") == w["order"] == n // w["index"], f"{name}: order/index"
            c = core_of(m)
            assert c == w["core_mask"], f"{name}: core mismatch"
            assert bin(c).count("1") == w["core_order"], f"{name}: core order"
            tot += w["index"]; inter &= c
        assert inter == 1, f"{name}: family not faithful"
        assert tot == G["mu"], f"{name}: degree sum"
        assert sorted(w["index"] for w in G["family"]) == G["family_indices"]
        # 5. minimality: cheapest index per core + Dijkstra over normal lattice
        cheap = {}
        for s in subs:
            if s == (1 << n) - 1: continue
            o = bin(s).count("1")
            if n % o: continue
            c = core_of(s); idx = n // o
            if c not in cheap or idx < cheap[c]:
                cheap[c] = idx
        INF = 10**30
        dist = {(1 << n) - 1: 0}; pq = [(0, (1 << n) - 1)]
        while pq:
            d, N = heapq.heappop(pq)
            if d != dist[N]: continue
            if N == 1: break
            for C, idx in cheap.items():
                M = N & C
                if d + idx < dist.get(M, INF):
                    dist[M] = d + idx; heapq.heappush(pq, (d + idx, M))
        assert dist.get(1) == G["mu"], f"{name}: minimality {dist.get(1)} vs {G['mu']}"
        # 6. Johnson cross-check for abelian cases
        if name in JOHNSON:
            assert G["mu"] == JOHNSON[name], f"{name}: Johnson mismatch"
    # family maxima
    o32 = [(g["name"], g["mu"]) for g in groups if g["order"] == 32]
    o64 = [(g["name"], g["mu"]) for g in groups if g["order"] == 64]
    m32 = max(m for _, m in o32); m64 = max(m for _, m in o64)
    w32 = sorted(n for n, m in o32 if m == m32); w64 = sorted(n for n, m in o64 if m == m64)
    assert m32 == 32 and set(w32) == {"C32", "Q32"}, (m32, w32)
    assert m64 == 64 and set(w64) == {"C64", "Q64"}, (m64, w64)
    # gaps within surveyed family
    s32 = sorted(set(m for _, m in o32), reverse=True)
    s64 = sorted(set(m for _, m in o64), reverse=True)
    assert s32[1] == 18 and s64[1] == 34, (s32, s64)
    print(f"ALL 29 GROUPS VERIFIED. order-32 max={m32} {w32} gap={m32-s32[1]}; "
          f"order-64 max={m64} {w64} gap={m64-s64[1]}.")

if __name__ == "__main__":
    main()
