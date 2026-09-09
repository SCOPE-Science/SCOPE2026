import json
arch=json.load(open("output/artifacts/mycielski_adj.json"))
for name in ["M4","M5"]:
    n=arch[name]["n"]; E=arch[name]["edges"]
    adj=[set() for _ in range(n)]
    for a,b in E: adj[a].add(b); adj[b].add(a)
    # alpha via branch and bound
    best=[0]; bestset=[None]
    order=list(range(n))
    def bb(cand, cur):
        # bound
        if len(cur)+(len(cand))<=best[0]: return
        if not cand:
            if len(cur)>best[0]: best[0]=len(cur); bestset[0]=list(cur)
            return
        v=cand[0]
        # include v
        nc=[u for u in cand[1:] if u not in adj[v]]
        bb(nc, cur+[v])
        # exclude v
        if len(cur)+len(cand)-1>best[0]:
            bb(cand[1:], cur)
    bb(order, [])
    print(f"{name}: n={n} m={len(E)} alpha={best[0]} example={sorted(bestset[0])}")
    # omega (triangle check already)
    # For M5: identify apex and shadows under our construction
    # M5 built from M4 (11 verts: 0..10) + shadows 11..21 + apex 22
    if name=="M5":
        V=list(range(11)); U=list(range(11,22)); z=22
        print(" apex neighbors == U?", sorted(adj[z])==U)
        # U independent?
        print(" U independent?", all(adj[u]&set(U)==set() for u in U))
        # each shadow nbrs == N_M4(x)?
        M4E=arch["M4"]["edges"]; M4adj=[set() for _ in range(11)]
        for a,b in M4E: M4adj[a].add(b); M4adj[b].add(a)
        ok=all(sorted(adj[11+x])==sorted(M4adj[x]|{22}) for x in range(11))
        print(" shadow neighborhoods correct?", ok)
        for x in range(11):
            print(f"  shadow of {x}: N_M4({x})={sorted(M4adj[x])} deg={len(M4adj[x])}")
    if name=="M4":
        V=list(range(5)); U=list(range(5,10)); z=10
        print(" apex neighbors == U?", sorted(adj[z])==U)
        print(" U independent?", all(adj[u]&set(U)==set() for u in U))
