"""Exact elementary directed-cycle enumeration (Johnson-style brute force, 72 states)."""
import pickle, sys
WDIR = "output/artifacts"
D = pickle.load(open(f"{WDIR}/track_data.pkl", "rb"))
branches = D["branches"]
NB = len(branches)
WSTAR = {0: 2, 1: 3, 2: 0, 3: 1}
bkey = {}
for b, members in enumerate(branches):
    for s in members:
        bkey[s] = b
def build(rule):
    slist, sindex = [], {}
    for b, members in enumerate(branches):
        ((i1, v1), j1), ((i2, v2), j2) = members
        for (tb, sb) in [((i1, v1), j1), ((i2, v2), j2)]:
            sindex[(b, tb, sb)] = len(slist)
            slist.append((b, tb, sb))
    NS = len(slist)
    adj = [[] for _ in range(NS)]
    for si, (b, tb, sb) in enumerate(slist):
        if rule == 0:
            L = WSTAR[tb[1]]
        else:
            sides = sorted(j for j in range(4) if j != tb[1])
            L = sides[(sides.index(WSTAR[tb[1]]) + rule) % 3]
        smalls = [j for j in range(4) if j != tb[1] and j != L]
        for se in (smalls if sb == L else [L]):
            b2 = bkey[(tb, se)]
            m2 = branches[b2]
            nxt = m2[1] if m2[0] == (tb, se) else m2[0]
            adj[si].append(sindex[(b2, (nxt[0][0], nxt[0][1]), nxt[1])])
    return slist, adj
for rule in [0, 1, 2]:
    slist, adj = build(rule)
    NS = len(slist)
    # elementary cycles: DFS from each node, only visit nodes > start (by index) except closing
    cycles = []
    sys.setrecursionlimit(100000)
    def dfs(s0, cur, path, onpath):
        for nb in adj[cur]:
            if nb == s0 and len(path) >= 3:
                cycles.append(list(path))
            elif nb > s0 and nb not in onpath:
                onpath.add(nb); path.append(nb)
                dfs(s0, nb, path, onpath)
                path.pop(); onpath.discard(nb)
    for s0 in range(NS):
        dfs(s0, s0, [s0], {s0})
    # dedupe by branch multiset
    BR = [s[0] for s in slist]
    seen = set(); uniq = []
    for c in cycles:
        key = tuple(sorted(BR[x] for x in c))
        if key not in seen:
            seen.add(key); uniq.append(c)
    lens = sorted(set(len(c) for c in uniq))
    print(f"RULE {rule}: elementary directed cycles: {len(uniq)}; lengths: {lens}", flush=True)
    for c in uniq[:10]:
        print("   len", len(c), "branches", sorted(BR[x] for x in c), flush=True)
