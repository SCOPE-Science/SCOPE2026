# agmatch.py — target-directed: affine-plane matching construction tests (lane-507)
import sys, itertools
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-507/output/artifacts")
from berge import pair_map, is_linear, has_berge_k33

def ag_matching(q):
    pts = [(x, y) for x in range(q) for y in range(q)]
    lines = []
    for c in range(q):
        lines.append([(c, y) for y in range(q)])
    for m in range(q):
        for b in range(q):
            lines.append([((y - b) * pow(m, -1, q)) % q if m else None for y in range(q)])
    # careful: for slope m != 0 parametrize by x
    lines = []
    for c in range(q):
        lines.append([(c, y) for y in range(q)])
    for m in range(q):
        for b in range(q):
            lines.append([(x, (m * x + b) % q) for x in range(q)])
    E = []
    for L in lines:
        for i in range(0, len(L) - 2, 3):
            E.append(tuple(sorted(L[i:i + 3])))
    # relabel
    mp = {}
    def id_(v):
        if v not in mp:
            mp[v] = len(mp)
        return mp[v]
    return [tuple(sorted([id_(u) for u in e])) for e in E]

def latin_single(t):
    E = []
    for a in range(t):
        for b in range(t):
            c = (-a - b) % t
            E.append((a, t + b, 2 * t + c))
    return [tuple(sorted(e)) for e in E]

if __name__ == "__main__":
    import time
    for q in (3, 4):
        E = ag_matching(q)
        n = len({v for e in E for v in e})
        print(f"AG-match q={q}: n={n} m={len(E)} linear={is_linear(E)}", flush=True)
        t0 = time.time()
        r, wit = has_berge_k33(E)
        print(f"  K33={r} {wit if r else ''} ({time.time()-t0:.1f}s)", flush=True)
    # single-edge latin exact threshold
    for t in (2, 3, 4):
        E = latin_single(t)
        n = len({v for e in E for v in e})
        r, wit = has_berge_k33(E)
        print(f"Latin1 t={t}: n={n} m={len(E)} linear={is_linear(E)} K33={r}", flush=True)
