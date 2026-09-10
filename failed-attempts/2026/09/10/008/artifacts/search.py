# search.py — aggressive heuristic max K33-free on 15 vertices (lane-507)
import sys, itertools, random, time
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-507/output/artifacts")
from berge import pair_map, is_linear, has_berge_k33, sts15_bose

def fast_free(edges_pm_S, S):
    r, _ = has_berge_k33([ALLT[i] for i in S])
    return not r

def greedy_order(n, order, ALLT, TPAIR):
    S, pm = [], {}
    for i in order:
        if any(p in pm for p in TPAIR[i]):
            continue
        S.append(i)
        for p in TPAIR[i]:
            pm[p] = len(S) - 1
        r, _ = has_berge_k33([ALLT[j] for j in S])
        if r:
            S.pop()
            for p in TPAIR[i]:
                del pm[p]
    return S

if __name__ == "__main__":
    n = 15
    ALLT = [tuple(sorted(t)) for t in itertools.combinations(range(n), 3)]
    PAIRS = {p: i for i, p in enumerate(itertools.combinations(range(n), 2))}
    TPAIR = [{PAIRS[(t[i], t[j]) if t[i] < t[j] else (t[j], t[i])] for i, j in ((0, 1), (0, 2), (1, 2))} for t in ALLT]
    rng = random.Random(12345)
    t0 = time.time()
    best = []
    # seed with STS15-sub structure: start from STS15-Bose edge indices
    E0 = sts15_bose()
    idx = {t: i for i, t in enumerate(ALLT)}
    sts_idx = [idx[t] for t in E0]
    # 1) deletion orders on STS15
    for trial in range(120):
        order = sts_idx[:]
        rng.shuffle(order)
        S = greedy_order(n, order, ALLT, TPAIR)
        if len(S) > len(best):
            best = S[:]
            print(f"t={time.time()-t0:.0f}s STS-del trial={trial} m={len(best)}", flush=True)
    # 2) full-triple orders
    for trial in range(60):
        order = list(range(len(ALLT)))
        rng.shuffle(order)
        S = greedy_order(n, order, ALLT, TPAIR)
        if len(S) > len(best):
            best = S[:]
            print(f"t={time.time()-t0:.0f}s FULL trial={trial} m={len(best)}", flush=True)
    print("BEST m=", len(best))
    print(sorted(ALLT[i] for i in best))
