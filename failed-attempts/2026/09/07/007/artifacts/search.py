#!/usr/bin/env python3
"""Heuristic search for K4-free, alpha<=5 graphs on n=30 maximizing edges.
Method: random-order repair + densify. Bitmask representation. Stdlib only.
"""
import random, itertools, sys, time

n = 30
ALL = (1 << n) - 1

def popcount(x): return bin(x).count("1")

def bits(mask):
    while mask:
        lsb = mask & -mask
        v = (lsb.bit_length() - 1)
        yield v
        mask ^= lsb

def edge_count(adj):
    return sum(popcount(a) for a in adj) // 2

def common_has_edge(adj, C):
    # does induced subgraph on C contain an edge?
    # for each x in C, if N(x)&C != 0 -> edge
    for x in bits(C):
        if adj[x] & C:
            return True
    return False

def creates_k4(adj, u, v):
    C = adj[u] & adj[v]
    if C == 0:
        return False
    return common_has_edge(adj, C)

def add_edge(adj, u, v):
    adj[u] |= (1 << v)
    adj[v] |= (1 << u)

def del_edge(adj, u, v):
    adj[u] &= ~(1 << v)
    adj[v] &= ~(1 << u)

def has_edge(adj, u, v):
    return (adj[u] >> v) & 1

def greedy_independent_set(adj, rng):
    # randomized greedy: returns independent set (list)
    order = list(range(n))
    # randomize by picking random available vertex each step
    avail = ALL
    ind = []
    while avail:
        # pick random vertex from avail
        # to avoid O(n) list, pick random bit
        lst = list(bits(avail))
        v = rng.choice(lst)
        ind.append(v)
        avail &= ~(adj[v] | (1 << v))
    return ind

def find_I6_heuristic(adj, rng, trials=200):
    for _ in range(trials):
        ind = greedy_independent_set(adj, rng)
        if len(ind) >= 6:
            return ind[:6]
    return None

def find_I6_exact_first(adj):
    # exhaustive search for an independent 6-set, return first or None
    # iterate combinations; use bit ops with early pruning
    # order vertices; for speed use recursion with pruning
    # simple iterative over combinations with quick check
    # Use recursive branch and bound to find I6 fast
    # Here: brute force with pruning by edge checks
    adjl = adj
    # recursive search
    cand = list(range(n))
    res = []
    found = []
    # sort by degree ascending to find independent set fast? use order as is
    sys.setrecursionlimit(10000)
    def rec(start, cur):
        if found:
            return True
        if len(cur) == 6:
            found.extend(cur)
            return True
        # prune: need enough remaining
        for i in range(start, n):
            # prune by remaining count
            if len(cur) + (n - i) < 6:
                break
            v = i
            ok = True
            for u in cur:
                if (adjl[u] >> v) & 1:
                    ok = False
                    break
            if not ok:
                continue
            cur.append(v)
            if rec(i + 1, cur):
                return True
            cur.pop()
            # bound: if even taking all remaining can't... handled at loop top
        return False
    # To speed up, first try heuristic; caller does that. This exact is fallback.
    rec(0, [])
    return found if found else None

def is_independent(adj, S):
    m = 0
    for v in S:
        m |= (1 << v)
    for v in S:
        if adj[v] & m:
            return False
    return True

def alpha_le5_exact(adj):
    # return True if alpha<=5 (exhaustive), else False + witness
    # enumerate C(30,6)=593775
    for comb in itertools.combinations(range(n), 6):
        # quick check: build mask
        m = 0
        for v in comb:
            m |= (1 << v)
        indep = True
        for v in comb:
            if adj[v] & m:
                indep = False
                break
        if indep:
            return False, list(comb)
    return True, None

def is_k4_free_exact(adj):
    for comb in itertools.combinations(range(n), 4):
        a,b,c,d = comb
        if has_edge(adj,a,b) and has_edge(adj,a,c) and has_edge(adj,a,d) and has_edge(adj,b,c) and has_edge(adj,b,d) and has_edge(adj,c,d):
            return False, list(comb)
    return True, None

def try_build(rng, p0=0.35, max_steps=2000):
    adj = [0]*n
    # init: random K4-free sparse graph: iterate pairs in random order, add w.p. p0 if K4-free
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    rng.shuffle(pairs)
    for (u,v) in pairs:
        if rng.random() < p0:
            if not creates_k4(adj,u,v):
                add_edge(adj,u,v)
    # phase 1: fix I6 sets by adding edges
    for step in range(max_steps):
        s = find_I6_heuristic(adj, rng, trials=80)
        if s is None:
            # confirm with exact (fast recursive first-found)
            s2 = find_I6_exact_first(adj)
            if s2 is None:
                break  # feasible!
            s = s2
        # s is independent 6-set; try all 15 pairs, pick feasible
        rng.shuffle(s)
        pairs15 = [(s[i],s[j]) for i in range(6) for j in range(i+1,6)]
        rng.shuffle(pairs15)
        added = False
        for (u,v) in pairs15:
            if not creates_k4(adj,u,v):
                add_edge(adj,u,v)
                added = True
                break
        if not added:
            # stuck: every pair in S is K4-blocked. Pick pair with fewest
            # blocking edges inside C, delete ALL of them, then add (u,v).
            # This preserves K4-freeness by construction.
            best_pair = None
            best_blockers = None
            for (u, v) in pairs15:
                C = adj[u] & adj[v]
                edges_in_C = []
                for x in bits(C):
                    inter = adj[x] & C
                    for y in bits(inter):
                        if y > x:
                            edges_in_C.append((x, y))
                if best_blockers is None or len(edges_in_C) < len(best_blockers):
                    best_blockers = edges_in_C
                    best_pair = (u, v)
                    if len(edges_in_C) == 1:
                        break
            if best_pair is None or best_blockers is None:
                return None
            # give up if cost too high (would destroy density); restart
            if len(best_blockers) > 4:
                return None
            for (x, y) in best_blockers:
                del_edge(adj, x, y)
            u, v = best_pair
            # recheck (deletions could interact, but all edges in original C
            # removed so now safe; verify defensively)
            if creates_k4(adj, u, v):
                return None
            add_edge(adj, u, v)
    else:
        return None
    # check feasible
    # phase 2: densify to maximal K4-free (adding edges preserves alpha<=5)
    pairs = [(i,j) for i in range(n) for j in range(i+1,n) if not has_edge(adj,i,j)]
    rng.shuffle(pairs)
    for (u,v) in pairs:
        if not creates_k4(adj,u,v):
            add_edge(adj,u,v)
    # final exact check alpha<=5 (heuristic may have missed? we broke on exact so ok)
    # but densify preserves alpha, so still feasible
    return adj

def adj_to_matrix(adj):
    return [[1 if has_edge(adj,i,j) else 0 for j in range(n)] for i in range(n)]

if __name__ == "__main__":
    seed0 = int(sys.argv[1]) if len(sys.argv)>1 else 0
    seconds = float(sys.argv[2]) if len(sys.argv)>2 else 60
    trials_arg = int(sys.argv[3]) if len(sys.argv)>3 else 10**9
    t0=time.time()
    best=-1
    best_adj=None
    rng=random.Random(seed0)
    t=0
    while time.time()-t0 < seconds and t < trials_arg:
        t+=1
        a=try_build(rng)
        if a is None:
            continue
        e=edge_count(a)
        # verify quickly heuristic alpha (should hold); then exact for candidates beating best
        if e>best:
            ok,_=is_k4_free_exact(a)
            if not ok:
                print(f"trial {t}: K4 violation (bug)",flush=True)
                continue
            ok2,w=alpha_le5_exact(a)
            if not ok2:
                print(f"trial {t}: e={e} but alpha>=6 witness {w} (heuristic miss)",flush=True)
                continue
            best=e
            best_adj=[x for x in a]
            print(f"[{time.time()-t0:.1f}s] trial {t}: NEW BEST e={best}",flush=True)
            # save
            with open(f"output/artifacts/best_{best}.txt","w") as f:
                M=adj_to_matrix(best_adj)
                for row in M:
                    f.write("".join(map(str,row))+"\n")
    print(f"DONE trials={t} best={best}")
    if best_adj is not None:
        M=adj_to_matrix(best_adj)
        with open("output/artifacts/best_adj.txt","w") as f:
            for row in M:
                f.write(" ".join(map(str,row))+"\n")
        print(f"edges={best} degrees={sorted([popcount(a) for a in best_adj],reverse=True)}")
