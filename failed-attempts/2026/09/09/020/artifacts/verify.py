"""Independent verifier: recomputes CD data from committed tables via a
different lattice route (cyclic-join closure + direct maximality scan) and
cross-checks results/*.json. Prints VERIFY_OK or FAIL. Skips C2x6 (not run).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tables import BUILDERS

here = os.path.dirname(os.path.abspath(__file__))
rd = os.path.join(here, "results")

def mask_elems(m):
    e = []; i = 0
    while m:
        if m & 1: e.append(i)
        m >>= 1; i += 1
    return e

def verify_group(name):
    fam, build, ab = BUILDERS[name]
    mult = build()
    n = len(mult)
    # independent assoc check (different loop order)
    for b in range(n):
        for a in range(n):
            for c in range(n):
                assert mult[mult[a][b]][c] == mult[a][mult[b][c]], (name, "nonassoc")
    assert all(mult[0][a] == a and mult[a][0] == a for a in range(n))
    bit = [1 << a for a in range(n)]
    inv = []
    for a in range(n):
        for b in range(n):
            if mult[a][b] == 0:
                inv.append(b); break
    # route B: cyclic subgroups then pairwise-join closure to fixpoint
    cyc = set()
    for g in range(n):
        s = 0; x = g
        while not (s >> x) & 1:
            s |= bit[x]; x = mult[x][g]
        cyc.add(s)
    def close(m):
        el = mask_elems(m); s = m
        for a in el: s |= bit[inv[a]]
        el = mask_elems(s)
        for a in el:
            for b in el: s |= bit[mult[a][b]]
        return s if s == m else close(s)
    subs = set(cyc) | {1}
    while True:
        cur = list(subs); new = set()
        for i in range(len(cur)):
            for j in range(i, len(cur)):
                h = close(cur[i] | cur[j])
                if h not in subs: new.add(h)
        if not new: break
        subs |= new
    subs = sorted(subs)
    assert all(close(h) == h for h in subs)
    order = {h: bin(h).count("1") for h in subs}
    cent = {}
    for h in subs:
        hs = mask_elems(h); c = 0
        for g in range(n):
            if all(mult[g][x] == mult[x][g] for x in hs): c |= bit[g]
        cent[h] = bin(c).count("1")
    meas = {h: order[h]*cent[h] for h in subs}
    m = max(meas.values())
    cd = sorted([h for h in subs if meas[h] == m], key=lambda h: (order[h], h))
    rec = json.load(open(os.path.join(rd, name + ".json")))
    assert rec["n"] == n, (name, "n")
    assert rec["nsub"] == len(subs), (name, "nsub", rec["nsub"], len(subs))
    assert rec["m"] == m, (name, "m")
    assert rec["cd_size"] == len(cd), (name, "cdsize")
    assert sorted(rec["cd_orders"]) == sorted(order[h] for h in cd), (name, "cdorders")
    assert sorted(rec["cd_subgroup"]) == mask_elems(min(cd, key=lambda h: (order[h], h))), (name, "cdsub")
    # width recheck for small CD
    if len(cd) <= 60 and rec.get("width") is not None:
        les = lambda A, B: (A & ~B) == 0
        # brute-force max antichain
        best = 0
        k = len(cd)
        for mask in range(1 << k):
            idx = [i for i in range(k) if (mask >> i) & 1]
            if len(idx) <= best: continue
            if all(not les(cd[i], cd[j]) and not les(cd[j], cd[i])
                   for x, i in enumerate(idx) for j in idx[x+1:]):
                best = len(idx)
        assert best == rec["width"], (name, "width", best, rec["width"])
    # membership-set equality
    assert sorted(map(sorted, rec["cd_members"])) == sorted(mask_elems(h) for h in cd), (name, "members")
    return f"{name}: OK nsub={len(subs)} m={m} |CD|={len(cd)} w={rec['width']}"

if __name__ == "__main__":
    names = [k for k in BUILDERS if BUILDERS[k][0] != "vspace" and k != "C2x6"]
    for name in names:
        print(verify_group(name), flush=True)
    # vspace file special checks
    r = json.load(open(os.path.join(rd, "C3x4.json")))
    assert r["rank_sizes"] == [1, 40, 130, 40, 1]
    assert r["sublattice_width"] == 130
    assert r["cd_size"] == 1 and r["cd_orders"] == [81] and r["m"] == 6561
    print("C3x4: OK (abelian CD={G}; subgroup-lattice ranks [1,40,130,40,1], width 130)")
    print("VERIFY_OK")
