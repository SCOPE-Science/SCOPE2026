import networkx as nx, itertools, time, sys, random
sys.path.insert(0, "work")
from cyc import all_cycles, min_cover_k

def two_factor_two_circuits(G, max_matchings=2000):
    # 2-factor = complement of perfect matching; check if any gives exactly 2 cycles
    nodes = list(G.nodes())
    mates = []
    # enumerate perfect matchings via DFS
    matchings = []
    def dfs(unmatched, cur):
        if len(matchings) >= max_matchings:
            return
        if not unmatched:
            matchings.append(list(cur))
            return
        u = next(iter(unmatched))
        for v in G.neighbors(u):
            if v in unmatched and v != u:
                cur.append((u, v))
                dfs(unmatched - {u, v}, cur)
                cur.pop()
                if len(matchings) >= max_matchings:
                    return
    dfs(set(nodes), [])
    out = []
    for M in matchings:
        H = G.copy()
        H.remove_edges_from(M)
        # H should be 2-regular
        if any(d != 2 for _, d in H.degree()):
            continue
        nc = nx.number_connected_components(H)
        if nc == 2:
            # check each component is a circuit (connected 2-regular => cycle)
            out.append(M)
            break
    return out

def kb_family(n1, n2, internal1, internal2, cross):
    # C1 = 0..n1-1, C2 = n1..n1+n2-1
    G = nx.Graph()
    G.add_nodes_from(range(n1 + n2))
    for i in range(n1):
        G.add_edge(i, (i + 1) % n1)
    for j in range(n2):
        u = n1 + j
        v = n1 + ((j + 1) % n2)
        G.add_edge(u, v)
    for u, v in internal1:
        G.add_edge(u, v)
    for u, v in internal2:
        G.add_edge(n1 + u, n1 + v)
    for u, v in cross:
        G.add_edge(u, n1 + v)
    return G

def antipodal(n, skip):
    # perfect matching of Z_n minus skip set, pairing i with i+n/2
    skip = set(skip)
    M = []
    used = set(skip)
    for i in range(n):
        if i in used:
            continue
        j = (i + n // 2) % n
        if j in used or j == i:
            return None
        M.append((i, j))
        used.add(i); used.add(j)
    return M

def check(G, name, timelimit=90):
    m = G.number_of_edges()
    if list(nx.bridges(G)):
        print(f"{name}: HAS BRIDGE, skip", flush=True)
        return None
    best, bt, masks, lens, nc, timed = min_cover_k(G, 4, timelimit=timelimit)
    print(f"{name}: n={G.number_of_nodes()} m={m} bound={8*m/5:.1f} ncyc={nc} opt4={best} ratio={best/m:.4f} timed={timed}", flush=True)
    return best / m

if __name__ == "__main__":
    # k=2 antipodal gluings, growing n
    for n1 in [6, 8, 10, 12]:
        n2 = n1
        A = antipodal(n1, {0, n1 // 2})
        B = antipodal(n2, {0, n2 // 2})
        if A is None or B is None:
            print(f"n1={n1}: antipodal failed", flush=True)
            continue
        G = kb_family(n1, n2, A, B, [(0, 0), (n1 // 2, n2 // 2)])
        check(G, f"anti-k2-{n1}-{n2}")
    # k=2 adjacent cross, antipodal internal
    for n1 in [8, 10]:
        n2 = n1
        A = antipodal(n1, {0, 1})
        B = antipodal(n2, {0, 1})
        if A is None or B is None:
            print(f"adj n1={n1}: antipodal failed", flush=True)
            continue
        G = kb_family(n1, n2, A, B, [(0, 0), (1, 1)])
        check(G, f"anti-k2adj-{n1}-{n2}")
