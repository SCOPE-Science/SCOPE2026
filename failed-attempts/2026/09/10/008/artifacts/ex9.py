# ex9.py — target-directed exact BB: max linear Berge-K33-free family on 9 vertices (lane-507)
import sys, itertools, time
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-507/output/artifacts")
from berge import has_berge_k33

N = 9
ALLT = [tuple(sorted(t)) for t in itertools.combinations(range(N), 3)]
PAIRS = {p: i for i, p in enumerate(itertools.combinations(range(N), 2))}
TPAIR = [{PAIRS[(t[i], t[j]) if t[i] < t[j] else (t[j], t[i])] for i, j in ((0, 1), (0, 2), (1, 2))} for t in ALLT]
# triples containing each pair
BYPAIR = [[] for _ in range(len(PAIRS))]
for i, ps in enumerate(TPAIR):
    for p in ps:
        BYPAIR[p].append(i)

T0 = ALLT.index((0, 1, 2))
best = [None]
nodes = [0]
t_start = time.time()
TIMEOUT = 230

def berge_free(chosen):
    E = [ALLT[i] for i in chosen]
    # incremental-ish full check (n=9 cheap)
    pm = {}
    for k, t in enumerate(E):
        a, b, c = t
        for p in ((a, b), (a, c), (b, c)):
            pm[p if p[0] < p[1] else (p[1], p[0])] = k
    verts = list(range(N))
    for six in itertools.combinations(verts, 6):
        s = set(six)
        seen = set()
        for A in itertools.combinations(six, 3):
            A = set(A)
            B = tuple(sorted(s - A))
            key = (tuple(sorted(A)), B)
            if key in seen:
                continue
            seen.add(key)
            eids = []
            ok = True
            for a in A:
                for b in B:
                    p = (a, b) if a < b else (b, a)
                    if p not in pm:
                        ok = False
                        break
                    eids.append(pm[p])
                if not ok:
                    break
            if ok and len(set(eids)) == 9:
                return False
    return True

def dfs(chosen, used_pairs, alive, cur):
    nodes[0] += 1
    if time.time() - t_start > TIMEOUT:
        raise StopIteration
    # bound: cur + uncovered/3
    nuncovered = sum(1 for p in range(len(PAIRS)) if p not in used_pairs)
    if cur + nuncovered // 3 <= len(best[0]):
        return
    if not alive:
        if cur > len(best[0]):
            best[0] = list(chosen)
        return
    # pick uncovered pair with fewest alive options
    pairs_in_alive = {}
    for i in alive:
        for p in TPAIR[i]:
            if p not in used_pairs:
                pairs_in_alive.setdefault(p, []).append(i)
    if not pairs_in_alive:
        if cur > len(best[0]):
            best[0] = list(chosen)
        return
    p = min(pairs_in_alive, key=lambda q: len(pairs_in_alive[q]))
    opts = pairs_in_alive[p]
    # branch include each option
    for i in opts:
        nused = used_pairs | TPAIR[i]
        chosen.append(i)
        if berge_free(chosen):
            nalive = [j for j in alive if j != i and not (TPAIR[j] & TPAIR[i])]
            dfs(chosen, nused, nalive, cur + 1)
        chosen.pop()
    # branch leave p uncovered: remove all alive triples containing p
    nalive = [j for j in alive if p not in TPAIR[j]]
    dfs(chosen, used_pairs | {p}, nalive, cur)

if __name__ == "__main__":
    seed = [(0, 1, 2), (0, 3, 6), (0, 4, 8), (0, 5, 7), (1, 3, 8), (1, 4, 7), (1, 5, 6), (2, 3, 7), (2, 4, 6), (3, 4, 5)]
    best[0] = [ALLT.index(tuple(sorted(t))) for t in seed]
    print("seed size:", len(best[0]), flush=True)
    init_used = set()
    for i in best[0]:
        init_used |= TPAIR[i]
    print("seed pair-cover check:", len(init_used) == 30, flush=True)
    init = [i for i in range(len(ALLT)) if i != T0 and not (TPAIR[i] & TPAIR[T0])]
    dfs([T0], set(TPAIR[T0]), init, 1)
    print("NODES:", nodes[0], flush=True)
    print("OPT:", len(best[0]), flush=True)
    print(sorted(ALLT[i] for i in best[0]), flush=True)
