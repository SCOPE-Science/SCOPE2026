# berge.py — stdlib-only utilities for linear 3-graph Berge-K_{3,3} work (lane-507, target-directed)
import itertools, random

def pair_map(edges):
    d = {}
    for i, e in enumerate(edges):
        a, b, c = e
        for p in ((a, b), (a, c), (b, c)):
            p = (p[0], p[1]) if p[0] < p[1] else (p[1], p[0])
            d.setdefault(p, []).append(i)
    return d

def is_linear(edges):
    d = pair_map(edges)
    return all(len(v) == 1 for v in d.values())

def has_berge_k33(edges):
    """Exhaustive: core 6-set + 3+3 split, 9 cross pairs in 9 DISTINCT edges."""
    pm = pair_map(edges)
    verts = sorted({v for e in edges for v in e})
    for six in itertools.combinations(verts, 6):
        s = set(six)
        # 10 unordered 3+3 splits
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
                return True, (tuple(sorted(A)), B)
    return False, None

def fano():
    return [(0,1,3),(0,2,5),(0,4,6),(1,2,4),(1,5,6),(2,3,6),(3,4,5)]

def sts9():
    # AG(2,3): points (x,y), lines
    pts = [(x,y) for x in range(3) for y in range(3)]
    idx = {p:i for i,p in enumerate(pts)}
    edges = set()
    for p in pts:
        for d in [(1,0),(0,1),(1,1),(1,2)]:
            e = tuple(sorted(idx[((p[0]+k*d[0])%3,(p[1]+k*d[1])%3)] for k in range(3)))
            edges.add(e)
    return sorted(edges)

def sts15_bose():
    # Bose construction for 6t+3=15, t=2: points Z5 x Z3
    def pt(x,i): return x*3+i
    E = []
    for x in range(5):
        E.append(tuple(sorted([pt(x,0),pt(x,1),pt(x,2)])))
    for i in range(3):
        for x in range(5):
            for y in range(x+1,5):
                z = ((x+y)*3) % 5  # (x+y)/2 mod 5
                E.append(tuple(sorted([pt(x,i),pt(y,i),pt(z,(i+1)%3)])))
    return sorted(set(E))

def greedy_berge_free(n, trials=200, seed=0):
    """Randomized greedy: random triple order, add if linear & keeps Berge-free (incremental check)."""
    rng = random.Random(seed)
    allt = [tuple(sorted(t)) for t in itertools.combinations(range(n),3)]
    best = []
    for _ in range(trials):
        rng.shuffle(allt)
        edges = []
        pm = {}
        verts_of = {}
        for t in allt:
            a,b,c = t
            ps = []
            for p in ((a,b),(a,c),(b,c)):
                p = (p[0],p[1]) if p[0]<p[1] else (p[1],p[0])
                ps.append(p)
            if any(p in pm for p in ps):
                continue
            # incremental Berge check: new Berge copy must use new edge for >=1 cross pair.
            # For each new pair p={x,y}, each role (x in A or B side), choose partners.
            ei = len(edges)
            found = False
            others = [v for v in range(n) if v not in t]
            for (x,y) in ps:
                for (xa, yb) in ((x,y),(y,x)):  # xa in A-side, yb in B-side
                    for A2 in itertools.combinations([v for v in range(n) if v!=xa and v!=yb],2):
                        # quick: need pairs (xa2,yb),(xa3,yb) covered distinctly etc. -> do full local test
                        for B2 in itertools.combinations([v for v in range(n) if v!=xa and v!=yb and v not in A2],2):
                            A = (xa,)+A2; B = (yb,)+B2
                            eids = set()
                            ok = True
                            for aa in A:
                                for bb in B:
                                    if (aa==x and bb==y) or (aa==y and bb==x):
                                        eids.add(ei)
                                        continue
                                    p2 = (aa,bb) if aa<bb else (bb,aa)
                                    if p2 not in pm:
                                        ok=False; break
                                    eids.add(pm[p2])
                                if not ok: break
                            if ok and len(eids)==9:
                                found=True; break
                        if found: break
                    if found: break
                if found: break
            if found:
                continue
            edges.append(t)
            for p in ps: pm[p]=ei
        if len(edges) > len(best):
            best = list(edges)
    return best

if __name__ == "__main__":
    for name, E in (("Fano STS(7)", fano()), ("STS(9)", sts9()), ("STS(15)-Bose", sts15_bose())):
        n = len({v for e in E for v in e})
        print(name, "n=",n,"m=",len(E),"linear=",is_linear(E))
        r, wit = has_berge_k33(E)
        print("  Berge-K33 present:", r, wit if r else "")
