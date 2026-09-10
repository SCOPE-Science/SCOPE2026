# greedy8.py — target-directed: heuristic max K33-free search on n=8,9 (lane-507)
import sys, itertools, random
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-507/output/artifacts")
from berge import pair_map, is_linear, has_berge_k33

def rand_greedy(n, trials, seed):
    rng = random.Random(seed)
    allt = [tuple(sorted(t)) for t in itertools.combinations(range(n), 3)]
    best = []
    for _ in range(trials):
        rng.shuffle(allt)
        S = []
        pm = {}
        for t in allt:
            a, b, c = t
            ps = tuple((u, v) if u < v else (v, u) for u, v in ((a, b), (a, c), (b, c)))
            if any(p in pm for p in ps):
                continue
            S.append(t)
            for p in ps:
                pm[p] = len(S) - 1
            r, _ = has_berge_k33(S)
            if r:
                S.pop()
                for p in ps:
                    del pm[p]
        if len(S) > len(best):
            best = list(S)
    return best

if __name__ == "__main__":
    for n, tr, sd in ((8, 40, 1), (9, 40, 2)):
        B = rand_greedy(n, tr, sd)
        print(f"n={n} greedy m={len(B)} linear={is_linear(B)} K33={has_berge_k33(B)[0]}")
        print("  ", sorted(B))
