"""Fast exact audit of small-support pairs via integer orientations.

For point mass configurations the only small-separation primitives needed:
  seg-seg (skew/colinear handled by exact solve),
  seg-tri pierce (strict), pt-in-tet (strict),
plus closed-hull boundary contacts detected conservatively (counted as MEET,
which is sound for the DISPROOF direction: we only kill a pair when some
deletion is PROVABLY disjoint with strict separation margin).
For the disproof (all pairs killed) we need every pair to have a strictly
separated deletion -- boundary-touching deletions count as surviving, which
only makes the disproof harder (sound direction).
"""
import itertools

P = [(i, i*i, i*i*i) for i in range(10)]

def det3(M):
    (a,b,c),(d,e,f),(g,h,k) = M
    return a*(e*k-f*h)-b*(d*k-f*g)+c*(d*h-e*g)

def orient(a,b,c,d):
    pa,pb,pc,pd = P[a],P[b],P[c],P[d]
    return det3([[pb[j]-pa[j] for j in range(3)],
                 [pc[j]-pa[j] for j in range(3)],
                 [pd[j]-pa[j] for j in range(3)]])

def seg_tri(p,q,a,b,c):
    s1 = orient(p,a,b,c); s2 = orient(q,a,b,c)
    if s1 == 0 or s2 == 0 or (s1>0) == (s2>0):
        return False
    t1 = orient(p,q,a,b); t2 = orient(p,q,b,c); t3 = orient(p,q,c,a)
    if t1 == 0 or t2 == 0 or t3 == 0:
        return False
    return (t1>0) == (t2>0) == (t3>0)

def pt_in_tet(x,a,b,c,d):
    o = orient(a,b,c,d)
    assert o != 0
    return (orient(x,b,c,d)*o > 0 and
            orient(x,a,c,d)*orient(b,a,c,d) > 0 and
            orient(x,a,b,d)*orient(c,a,b,d) > 0 and
            orient(x,a,b,c)*orient(d,a,b,c) > 0)

def strict_meet(A, B):
    """Strict-interior intersection certificate (sound, incomplete on boundary)."""
    A = list(A); B = list(B)
    if len(B) >= 4:
        for x in A:
            for q in itertools.combinations(B, 4):
                if pt_in_tet(x, *q):
                    return True
    if len(A) >= 4:
        for x in B:
            for q in itertools.combinations(A, 4):
                if pt_in_tet(x, *q):
                    return True
    if len(B) >= 3:
        for e in itertools.combinations(A, 2):
            for t in itertools.combinations(B, 3):
                if seg_tri(e[0], e[1], *t):
                    return True
    if len(A) >= 3:
        for e in itertools.combinations(B, 2):
            for t in itertools.combinations(A, 3):
                if seg_tri(e[0], e[1], *t):
                    return True
    return False

def boundary_free(A2, B2):
    """True if no degeneracy (shared vertex impossible here; checks no
    coplanarity among cross-quadruples spanning both sets)."""
    for q in itertools.combinations(list(A2)+list(B2), 4):
        if orient(*q) == 0:
            return False
    return True

if __name__ == "__main__":
    import time
    t0 = time.time()
    verts = list(range(10))
    # small pairs only: sizes (2..4, 2..4)
    pairs = []
    seen = set()
    for r1 in (2,3,4):
        for s in itertools.combinations(verts, r1):
            S = frozenset(s)
            rest = tuple(v for v in verts if v not in S)
            for r2 in (2,3,4):
                if r2 > len(rest):
                    continue
                for t in itertools.combinations(rest, r2):
                    T = frozenset(t)
                    a,b = (S,T) if str(sorted(S)) <= str(sorted(T)) else (T,S)
                    if (a,b) in seen:
                        continue
                    seen.add((a,b))
                    pairs.append((sorted(a), sorted(b)))
    print("small pairs:", len(pairs))
    nfull = sum(1 for (A,B) in pairs if strict_meet(A,B))
    print("strict-meet at full strength:", nfull, "t=", round(time.time()-t0,1))
    # among full-strength survivors, check uniformity with boundary audit
    nuniform = 0
    ex = []
    nonclean = 0
    for (A,B) in pairs:
        if not strict_meet(A,B):
            continue
        ok_all = True
        clean = True
        for v in range(10):
            A2 = [x for x in A if x != v]; B2 = [x for x in B if x != v]
            if not strict_meet(A2,B2):
                if not boundary_free(A2,B2):
                    clean = False
                else:
                    ok_all = False
                    break
        if ok_all:
            nuniform += 1
            if len(ex) < 8:
                ex.append((A,B,clean))
        elif not clean:
            nonclean += 1
    print("uniform-or-touching survivors:", nuniform, ex)
    print("total t=", round(time.time()-t0,1))
