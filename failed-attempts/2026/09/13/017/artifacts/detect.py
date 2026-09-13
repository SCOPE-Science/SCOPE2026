"""Detectors: even holes, long prisms. Validation suite included."""
import itertools, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1499/output/artifacts')
from tools import *

def all_triangles(masks, n):
    T = []
    for i in range(n):
        for j in range(i+1, n):
            if not ((masks[i] >> j) & 1): continue
            for k in range(j+1, n):
                if ((masks[i] >> k) & 1) and ((masks[j] >> k) & 1):
                    T.append((i, j, k))
    return T

def all_induced_cycles(masks, n, maxlen=None):
    """Return list of induced-cycle vertex tuples (canonical rotation/reversal). Only lengths>=4."""
    found = []
    # enumerate subsets and test (fine for n<=16)
    for s in range(4, (maxlen or n)+1):
        for combo in itertools.combinations(range(n), s):
            mask = 0
            for v in combo: mask |= (1 << v)
            ok = True
            for v in combo:
                if bin(masks[v] & mask).count('1') != 2:
                    ok = False; break
            if not ok: continue
            # connectivity
            seen = 1 << combo[0]; stack=[combo[0]]
            while stack:
                x = stack.pop()
                nb = masks[x] & mask & ~seen
                while nb:
                    lsb = nb & (-nb); nb ^= lsb
                    y = lsb.bit_length()-1
                    seen |= (1 << y); stack.append(y)
            if seen == mask:
                found.append(combo)
    return found

def has_even_hole(masks, n):
    for s in range(4, n+1, 2):
        for combo in itertools.combinations(range(n), s):
            mask = 0
            for v in combo: mask |= (1 << v)
            ok = True
            for v in combo:
                if bin(masks[v] & mask).count('1') != 2:
                    ok = False; break
            if not ok: continue
            seen = 1 << combo[0]; stack=[combo[0]]
            while stack:
                x = stack.pop()
                nb = masks[x] & mask & ~seen
                while nb:
                    lsb = nb & (-nb); nb ^= lsb
                    y = lsb.bit_length()-1
                    seen |= (1 << y); stack.append(y)
            if seen == mask:
                return combo
    return None

def simple_paths_from_to(masks, n, src, dst, forbidden, maxlen=None):
    """All simple paths src->dst avoiding `forbidden` set (bitmask, src/dst excluded from it)."""
    out = []
    def dfs(cur, tmask, plist):
        if maxlen is not None and len(plist)-1 > maxlen: return
        if cur == dst:
            out.append(tuple(plist)); return
        nb = masks[cur] & ~tmask & ~forbidden
        while nb:
            lsb = nb & (-nb); nb ^= lsb
            y = lsb.bit_length()-1
            dfs(y, tmask | (1 << y), plist + [y])
    dfs(src, 1 << src, [src])
    return out

def has_long_prism(masks, n):
    """Detect induced long prism per target definition. Returns witness or None.
    Triangles T1={a1,a2,a3}, T2={b1,b2,b3} disjoint; 3 vertex-disjoint paths Pi ai->bi
    len>=3; no edges between distinct paths except triangle edges (ai-aj, bi-bj)."""
    tris = all_triangles(masks, n)
    L = len(tris)
    for ii in range(L):
        for jj in range(ii+1, L):
            A = tris[ii]; B = tris[jj]
            if set(A) & set(B): continue
            # bijections: 6 permutations
            for perm in itertools.permutations([0,1,2]):
                b = [B[perm[0]], B[perm[1]], B[perm[2]]]
                # forbid using other triangle's vertices in paths
                # enumerate path choices per i with disjointness
                # restrict: internal vertices of Pi avoid A∪B (except endpoints)
                avoid_base = (sum(1 << v for v in A) | sum(1 << v for v in B))
                # enumerate paths for each i
                paths = []
                feasible = True
                for i in range(3):
                    ai = A[i]; bi = b[i]
                    forb = avoid_base & ~(1 << ai) & ~(1 << bi)
                    # also all other triangle verts forbidden as internal
                    pl = [p for p in simple_paths_from_to(masks, n, ai, bi, forb) if len(p)-1 >= 3]
                    if not pl:
                        feasible = False; break
                    paths.append(pl)
                if not feasible: continue
                # triple loop (cap sizes)
                # to limit blowup, cap each list at 200
                MP = [p[:200] for p in paths]
                for p1 in MP[0]:
                    s1 = set(p1)
                    for p2 in MP[1]:
                        if s1 & set(p2): continue
                        s12 = s1 | set(p2)
                        for p3 in MP[2]:
                            if s12 & set(p3): continue
                            # check cross-edge condition
                            P = [p1, p2, p3]
                            good = True
                            for x in range(3):
                                for y in range(x+1, 3):
                                    for u in P[x]:
                                        for w_ in P[y]:
                                            if (masks[u] >> w_) & 1:
                                                # allowed only triangle edges: u in A and w_ in A, or u in B and w_ in B
                                                if (u in A) and (w_ in A): continue
                                                if (u in b) and (w_ in b): continue
                                                good = False; break
                                        if not good: break
                                    if not good: break
                            if good:
                                return {'T1': A, 'T2': tuple(b), 'paths': (p1, p2, p3)}
    return None

def selftest():
    # C5: odd hole only
    n = 5
    m = from_edges(n, [(0,1),(1,2),(2,3),(3,4),(4,0)])
    assert has_even_hole(m, n) is None
    assert has_long_prism(m, n) is None
    # C6: even hole
    n = 6
    m = from_edges(n, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)])
    assert has_even_hole(m, n) is not None
    # K4: omega 4, chi 4, no holes
    n = 4
    m = from_edges(n, list(itertools.combinations(range(4),2)))
    assert max_clique_size(m, n) == 4 and chromatic_number(m, n) == 4
    assert has_even_hole(m, n) is None
    # triangular prism (short): two triangles + 3 paths length 1 -> NOT long (needs len>=3)
    n = 6
    m = from_edges(n, [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)])
    assert has_long_prism(m, n) is None, "short prism must not count"
    # long prism: subdivide each matching edge twice: 0-x1-3 etc. need disjoint paths len 3
    # T1=012, T2=345, paths 0-6-7-3, 1-8-9-4, 2-10-11-5
    n = 12
    E = [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),
         (0,6),(6,7),(7,3),(1,8),(8,9),(9,4),(2,10),(10,11),(11,5)]
    m = from_edges(n, E)
    w = has_long_prism(m, n)
    assert w is not None, "planted long prism must be found"
    # NOTE (parity lemma confirmation): this long prism (all paths length 3)
    # necessarily contains an induced even hole (3+3+2=8 via two same-parity paths).
    assert has_even_hole(m, n) is not None, "long prism must contain an even hole"
    print("selftest OK")

if __name__ == '__main__':
    selftest()
