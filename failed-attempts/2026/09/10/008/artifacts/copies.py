# copies.py — enumerate Berge-K33 copies; disjoint-copy lower bound on deletions (lane-507)
import sys, itertools
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-507/output/artifacts")
from berge import pair_map, sts15_bose

def all_copies(edges):
    pm = pair_map(edges)
    verts = sorted({v for e in edges for v in e})
    out = []
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
                    lst = pm.get(p)
                    if not lst:
                        ok = False
                        break
                    eids.append(lst[0])
                if not ok:
                    break
            if ok and len(set(eids)) == 9:
                out.append((tuple(sorted(A)), B, tuple(sorted(set(eids)))))
    return out

def max_disjoint(copies):
    best = []
    sup = [set(c[2]) for c in copies]
    order = sorted(range(len(sup)), key=lambda i: len(sup[i]))
    used = set()
    for i in order:
        if not (sup[i] & used):
            best.append(i)
            used |= sup[i]
    return best

if __name__ == "__main__":
    E = sts15_bose()
    print("m=", len(E), flush=True)
    C = all_copies(E)
    print("num copies:", len(C), flush=True)
    D = max_disjoint(C)
    print("greedy edge-disjoint copies:", len(D), flush=True)
    print("=> any K33-free subset of this STS(15) has m <=", len(E) - len(D), flush=True)
