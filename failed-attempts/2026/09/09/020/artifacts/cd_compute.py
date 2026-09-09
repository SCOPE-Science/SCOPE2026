"""Fast exact CD lattices from committed explicit mult tables (stdlib only).

Usage: python3 cd_compute.py <GroupName>   # writes results/<GroupName>.json
       python3 cd_compute.py ALL            # runs all except VSPACE ones
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tables import BUILDERS

def mask_elems(m):
    e = []
    i = 0
    while m:
        if m & 1: e.append(i)
        m >>= 1; i += 1
    return e

def cd_of_table(mult, abelian=False):
    n = len(mult)
    # associativity + inverses
    for a in range(n):
        Ma = mult[a]
        assert len(Ma) == n
        for b in range(n):
            ab = Ma[b]
            Mb = mult[b]
            for c in range(n):
                if mult[ab][c] != Ma[Mb[c]]:
                    raise AssertionError(f"nonassoc {(a,b,c)}")
    assert all(mult[0][a] == a and mult[a][0] == a for a in range(n))
    inv = [None]*n
    for a in range(n):
        for b in range(n):
            if mult[a][b] == 0 and mult[b][a] == 0:
                inv[a] = b; break
        assert inv[a] is not None
    bit = [1 << a for a in range(n)]
    if abelian:
        for a in range(n):
            Ma = mult[a]
            for b in range(n):
                assert Ma[b] == mult[b][a], "claimed abelian but not"
    # cyclic subgroups
    cycs = set()
    for g in range(n):
        s = 0; x = 0
        while True:
            s |= bit[x]
            x = mult[x][g]
            if x == 0: break
        cycs.add(s)
    cycs = sorted(cycs)
    def close(m):
        while True:
            elems = mask_elems(m)
            new = m
            for a in elems:
                new |= bit[inv[a]]
                Ma = mult[a]
                for b in elems:
                    new |= bit[Ma[b]]
            if new == m:
                return m
            m = new
    # single-element adjunction (complete: every H reached adjoining its elts)
    subs = {1}
    order_g = list(range(n)) if not abelian else sorted(range(n))
    for g in order_g:
        c = 1 << g
        news = set()
        for H in subs:
            J = close(H | c)
            if J not in subs:
                news.add(J)
        subs |= news
    for c in cycs:
        assert c in subs, "cyclic missing"
    # verify all are subgroups (closure) — by construction yes; spot check count>0
    subs = sorted(subs, key=lambda m: (bin(m).count('1'), m))
    order = {m: bin(m).count('1') for m in subs}
    if abelian:
        csize = {H: n for H in subs}
    else:
        csize = {}
        for H in subs:
            Hs = mask_elems(H)
            c = 0
            for g in range(n):
                ok = True
                Mg = mult[g]
                for h in Hs:
                    if Mg[h] != mult[h][g]:
                        ok = False; break
                if ok: c |= bit[g]
            csize[H] = bin(c).count('1')
    meas = {H: order[H]*csize[H] for H in subs}
    mval = max(meas.values())
    cd = sorted([H for H in subs if meas[H] == mval],
                key=lambda m: (order[m], m))
    cdset = set(cd)
    least = min(cd, key=lambda m: (order[m], m))
    assert all((least & ~H) == 0 for H in cd), "no least CD member!"
    def le(A, B): return (A & ~B) == 0
    covers = []
    for A in cd:
        for B in cd:
            if A != B and le(A, B):
                if not any(C != A and C != B and le(A, C) and le(C, B) for C in cd):
                    covers.append([mask_elems(A), mask_elems(B)])
    chain = all(le(A, B) or le(B, A) for A in cd for B in cd)
    # exact width (matching-based Dilworth; only for small CD lattices)
    k = len(cd)
    if k <= 400:
        from collections import deque
        adj = [[] for _ in range(k)]
        for i, A in enumerate(cd):
            for j, B in enumerate(cd):
                if i != j and le(A, B):
                    adj[i].append(j)
        matchR = [-1]*k
        def bpm(u, seen):
            for v in adj[u]:
                if seen[v]: continue
                seen[v] = True
                if matchR[v] == -1 or bpm(matchR[v], seen):
                    matchR[v] = u; return True
            return False
        matching = sum(1 for u in range(k) if bpm(u, [False]*k))
        width = k - matching
        matchL = [-1]*k
        for v in range(k):
            if matchR[v] != -1: matchL[matchR[v]] = v
        visL = [False]*k; visR = [False]*k
        q = deque([u for u in range(k) if matchL[u] == -1])
        for u in q: visL[u] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if matchL[u] != v and not visR[v]:
                    visR[v] = True
                    w = matchR[v]
                    if w != -1 and not visL[w]:
                        visL[w] = True; q.append(w)
        anti_idx = [i for i in range(k) if visL[i] and not visR[i]]
        assert len(anti_idx) == width
        for a in range(len(anti_idx)):
            for b in range(a+1, len(anti_idx)):
                A, B = cd[anti_idx[a]], cd[anti_idx[b]]
                assert not le(A, B) and not le(B, A)
        witness = [mask_elems(cd[i]) for i in anti_idx]
    else:
        width = None; witness = None
    mins = [H for H in cd if all(le(H, K) for K in cd)]
    maxs = [H for H in cd if all(le(K, H) for K in cd)]
    qa = False
    if len(mins) == 1 and len(maxs) == 1:
        mid = [H for H in cd if H != mins[0] and H != maxs[0]]
        if all(not le(A, B) and not le(B, A)
               for x, A in enumerate(mid) for B in mid[x+1:]):
            qa = True
    return {
        "n": n, "nsub": len(subs), "m": mval,
        "cd_size": k, "width": width,
        "is_chain": chain, "is_quasi_antichain": qa,
        "cd_subgroup": mask_elems(least),
        "cd_members": [mask_elems(H) for H in cd],
        "cd_orders": [order[H] for H in cd],
        "cd_covers": covers,
        "width_witness": witness,
        "subgroups": [{"elems": mask_elems(H), "order": order[H],
                        "cent_order": csize[H], "m": meas[H],
                        "in_cd": H in cdset} for H in subs],
    }

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    rd = os.path.join(here, "results")
    os.makedirs(rd, exist_ok=True)
    which = sys.argv[1] if len(sys.argv) > 1 else "ALL"
    names = [which] if which != "ALL" else [k for k in BUILDERS if BUILDERS[k][0] != "vspace"]
    for name in names:
        fam, build, ab = BUILDERS[name]
        t0 = time.time()
        r = cd_of_table(build(), abelian=ab)
        r["family"] = fam
        r["group"] = name
        r["time_s"] = round(time.time()-t0, 2)
        with open(os.path.join(rd, name + ".json"), "w") as f:
            json.dump(r, f)
        print(f"{name:12s} nsub={r['nsub']:5d} m={r['m']:6d} |CD|={r['cd_size']:3d} "
              f"width={r['width']} chain={r['is_chain']} QA={r['is_quasi_antichain']} "
              f"cd_orders={r['cd_orders']} t={r['time_s']}s", flush=True)
