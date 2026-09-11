"""Adversarial convex-position audit: 10 vertices on stacked 5-gons.

Config: two regular-pentagon layers z=+1 (vertices 0..4) and z=-1 (5..9),
angles aligned. All coordinates are exact Fractions involving sqrt(5)? Use
exact integer pentagon via (cos multiples) -- instead use RATIONAL pentagon
approximation? For a SOUND disproof we need exactness. Alternative exact
family: vertices of a triangular prism stack / cube-plus: use integer points
in convex position: the 8 cube corners + 2 face centers pushed out?
Simplest exactly-convex integer 10-set: take points (i, i^2 mod 31, i^3 mod 37)
lifts? Convex position is hard over Z. Instead: use the cyclic polytope C(10,3)
over integers = moment curve (already positive). Adversarial idea #2: NON-vertex
images: PL map sending some vertices to INTERIOR points (repeated images),
so hulls become thin/low-dimensional and easily separable. E.g. send vertices
0..8 to 9 points in a plane (thin triangle lattice) and vertex 9 far above:
any pair using 9 vs not... must audit. Even simpler: send several vertices to
the SAME point? f need not be injective! If f(0)=f(1)=p, then any pair split
across... wait repeated images only CREATE intersections, bad for disproof.
For disproof want images SPREAD so hulls are small and disjoint: send the 10
vertices to 10 points in "separated clusters": pairs spanning clusters are
disjoint unless hulls bridge. With points in general position, big hulls tend
to meet (moment curve: positive). Thin arrangement: 10 COLINEAR points
0..9 on x-axis (degenerate!): conv(A) cap conv(B) = interval overlap. Uniform
pair needs overlap surviving every deletion: A={0..4},B={5..9} disjoint always;
A={0,9},B={4,5}: conv {0,9}=[0,9] meets everything. Hmm colinear: pair
({0,9},{1,8}): delete 0: [1,9]vs[1,8] meet; ... every deletion leaves intervals
overlapping? [0,9]v[1,8] always overlap. So colinear fails (has uniform pairs).
Adversarial idea #3 (topological, non-affine): use a map that WRAPS: f maps
Delta_9 onto S^2 (hollow sphere): images of faces are patches; two disjoint
faces' images are disjoint patches unless they cover the sphere. With 10
vertices spread on S^2, small faces map to small patches; disjoint small
patches are disjoint! Deletion barely changes patches. So NO pair meets at
all -> every pair trivially killed -> DISPROOF (even of non-uniform Radon?
No: big complementary faces, e.g. two 5-sets, cover S^2 and must meet by
Lusternik-Schnirelmann-type reasons... but faces here are subcomplexes, their
images = spherical polygons; two complementary 5-patches DO overlap).
So the audit: use vertices = 10 nearly-uniform points on S^2 (exact rational
approx on sphere x^2+y^2+z^2=1 scaled to integers: use Pythagorean points),
f = PL extension (linear on each simplex = convex hull chords inside ball).
Then conv-hulls are 3D chords; audit small pairs: small disjoint face-hulls
near the sphere surface are disjoint (chords of disjoint patches don't meet).
Large pairs (5v5) may still meet. Uniform needs ALL deletions to meet: big
hulls meeting at full strength usually keep meeting. So again positive?
The REAL question: does ANY pair survive all deletions. Killing ledger needs
EVERY pair killed. Big 5v5 hulls are hard to kill (deleting one vertex rarely
separates two interlocked 5-hulls). So convex-inclusion maps look positive.
CONCLUSION of this script: audit integer-sphere config; if positive again,
the disproof (if any) needs genuinely wild continuous maps (not PL-vertex maps
with images in convex position), which strengthens the case that the target
may be TRUE and the index route (positive proof) is the right one.
"""
import itertools

# exact integer points near S^2: 10 Pythagorean-ish points, scaled
SPH = [(20,0,21),(0,20,21),(-20,0,21),(0,-20,21),(20,0,-21),
       (0,20,-21),(-20,0,-21),(0,-20,-21),(21,20,0),(-21,-20,0)]
P = SPH

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
    if o == 0:
        return False
    return (orient(x,b,c,d)*o > 0 and
            orient(x,a,c,d)*orient(b,a,c,d) > 0 and
            orient(x,a,b,d)*orient(c,a,b,d) > 0 and
            orient(x,a,b,c)*orient(d,a,b,c) > 0)

def strict_meet(A, B):
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

if __name__ == "__main__":
    import time
    t0 = time.time()
    verts = list(range(10))
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
    nfull = sum(1 for (A,B) in pairs if strict_meet(A,B))
    print("small pairs:", len(pairs), "strict-meet full:", nfull)
    nuniform = 0
    ex = []
    for (A,B) in pairs:
        if not strict_meet(A,B):
            continue
        if all(strict_meet([x for x in A if x != v],
                           [x for x in B if x != v]) for v in range(10)):
            nuniform += 1
            if len(ex) < 8:
                ex.append((A,B))
    print("strict-uniform small pairs:", nuniform, ex,
          "t=", round(time.time()-t0,1))
