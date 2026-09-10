# construct.py — target-directed: dense linear Berge-K3,3-free constructions (lane-507)
import sys, itertools
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-507/output/artifacts")
from berge import pair_map, is_linear, has_berge_k33, fano

def fano_blowup(t):
    """Balanced Latin blow-up of Fano plane. Vertices (v,a), v in [7], a in Z_t.
    For each Fano edge {x,y,z} with fixed orientation, triples ((x,a),(y,b),(z,-a-b)).
    n=7t, m=7t^2."""
    F = fano()
    E = []
    for (x, y, z) in F:
        for a in range(t):
            for b in range(t):
                c = (-a - b) % t
                E.append(tuple(sorted([(x, a), (y, b), (z, c)])))
    # relabel to ints
    mp = {}
    def id_(v):
        if v not in mp:
            mp[v] = len(mp)
        return mp[v]
    return [tuple(sorted([id_(u) for u in e])) for e in E]

def single_edge_latin(t):
    """Balanced blow-up of a single edge: X=Y=Z=Z_t, triples (x,y,-x-y). n=3t, m=t^2."""
    E = []
    for a in range(t):
        for b in range(t):
            c = (-a - b) % t
            E.append((a, t + b, 2 * t + c))
    return [tuple(sorted(e)) for e in E]

def rate_report(name, E):
    n = len({v for e in E for v in e})
    m = len(E)
    lin = is_linear(E)
    r, wit = (False, None) if not lin else has_berge_k33(E)
    import math
    pairdens = 3 * m / (n * (n - 1) / 2) if n > 1 else 0
    print(f"{name}: n={n} m={m} linear={lin} pairdens={pairdens:.6f} rate m/n^2={m/n**2:.6f} BergeK33={r}" + (f" wit={wit}" if r else ""))
    return n, m, lin, r

if __name__ == "__main__":
    for t in (2, 3):
        E = fano_blowup(t)
        rate_report(f"Fano blow-up t={t}", E)
    for t in (3, 5):
        E = single_edge_latin(t)
        rate_report(f"Single-edge Latin t={t}", E)
