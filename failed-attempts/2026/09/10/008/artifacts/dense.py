# dense.py — target-directed lower bounds: max Berge-K33-free subsets + greedy (lane-507)
import sys, itertools, random
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-507/output/artifacts")
from berge import pair_map, is_linear, has_berge_k33, fano, sts9, sts15_bose

def max_subset_bruteforce(E, max_check=True):
    """Exact max K33-free subset by descending-size search (feasible for |E|<=14)."""
    m = len(E)
    E = list(E)
    for k in range(m, -1, -1):
        for sub in itertools.combinations(range(m), k):
            S = [E[i] for i in sub]
            if not is_linear(S):
                continue
            r, _ = has_berge_k33(S)
            if not r:
                return S
    return []

def greedy_deletion(E, seed=0, passes=200):
    """Randomized deletion: order edges randomly, drop edge if it participates... -> use local search."""
    rng = random.Random(seed)
    E = list(E)
    best = None
    for _ in range(passes):
        order = rng.sample(range(len(E)), len(E))
        # greedy build
        S = []
        pm = {}
        for i in order:
            t = E[i]
            a, b, c = t
            ps = []
            for p in ((a,b),(a,c),(b,c)):
                p = (p[0],p[1]) if p[0]<p[1] else (p[1],p[0])
                ps.append(p)
            if any(p in pm for p in ps):
                continue
            S.append(t)
            for p in ps:
                pm[p] = len(S)-1
            r, _ = has_berge_k33(S)
            if r:
                S.pop()
                for p in ps:
                    del pm[p]
        if best is None or len(S) > len(best):
            best = list(S)
    return best

def report(name, S):
    n = len({v for e in S for v in e})
    m = len(S)
    lin = is_linear(S)
    r, wit = has_berge_k33(S)
    pd = 3*m/(n*(n-1)/2)
    print(f"{name}: n={n} m={m} pairdens={pd:.6f} rate={m/n**2:.6f} linear={lin} K33={r}")
    return S

if __name__ == "__main__":
    S = max_subset_bruteforce(sts9())
    print("== exact max K33-free subset of STS(9) ==")
    S = report("STS9-sub", S)
    print(sorted(S))
    print("== greedy deletion on STS(15)-Bose ==")
    B = greedy_deletion(sts15_bose(), passes=60)
    B = report("STS15-sub", B)
