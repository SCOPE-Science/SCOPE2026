"""Bounded recovery test for lane-678 target.

Question: can a skew product alpha(omega,x) = (S omega, h_omega(x)) on
X = Omega x [0,1]^d (Omega = odometer Cantor set, each h_omega a genuine
homeomorphism of the d-cube) be minimal?

Topological fact under test: every homeomorphism h of [0,1]^d preserves
the manifold boundary setwise (invariance of domain: interior points have
a neighbourhood homeomorphic to an open set in R^d; boundary points do
not). Hence F = Omega x d([0,1]^d) is closed, nonempty, proper, and
alpha-invariant for ANY choice of fibrewise homeomorphisms -> no such
skew product is minimal -> C(X) rtimes Z is not simple.

This script checks:
 (1) d=1 endpoint preservation (every homeomorphism of [0,1] is strictly
     monotone, so {f(0),f(1)} = {0,1});
 (2) a finite-level odometer x grid model: with boundary-preserving
     fibrewise bijections (the property every true cube homeomorphism has),
     the boundary sub-bundle is invariant -> non-minimal (obstruction);
 (3) recovery attempt: allow fibrewise bijections that MIX boundary and
     interior points (not realizable by genuine cube homeomorphisms);
     only then can the boundary set fail to be invariant. This shows the
     only escape abandons the pinned class (genuine cube-fibre
     homeomorphisms), so no recovery exists inside the target scope.
Stdlib only.
"""
import random

print("=== (1) d=1 endpoint preservation ===")
# Any homeomorphism of [0,1] is a strictly monotone continuous bijection.
# Monotone samples: increasing and decreasing families all send {0,1} to {0,1}.
for name, f in [
    ("id", lambda t: t),
    ("flip", lambda t: 1 - t),
    ("power up", lambda t: t ** 3),
    ("power down", lambda t: t ** (1 / 3)),
    ("piecewise", lambda t: 2 * t * t if t < 0.5 else 1 - 2 * (1 - t) ** 2),
]:
    assert {round(f(0.0), 12), round(f(1.0), 12)} == {0.0, 1.0}, name
    print(f"  {name}: f({{0,1}}) = {{0,1}} OK")

print("=== (2) finite-level skew product: boundary sub-bundle invariant ===")
random.seed(678)
for d in (1, 2, 3):
    n = 4            # odometer level: Omega_n = Z/2^n
    N = 2 ** n
    k = 3            # fibre grid {0..k}^d discretizing [0,1]^d
    pts = []

    def is_bdry(p):
        return any(c in (0, k) for c in p)

    # enumerate grid points
    def gen(prefix, depth):
        if depth == d:
            pts.append(tuple(prefix))
            return
        for c in range(k + 1):
            gen(prefix + [c], depth + 1)
    gen([], 0)
    interior = [p for p in pts if not is_bdry(p)]
    bdry = [p for p in pts if is_bdry(p)]
    assert bdry and interior and len(bdry) + len(interior) == len(pts)
    # random fibrewise bijections PRESERVING discrete boundary (as any true
    # cube homeomorphism must preserve the true boundary)
    h = {}
    for w in range(N):
        bi = interior[:]
        bb = bdry[:]
        random.shuffle(bi)
        random.shuffle(bb)
        perm = dict(zip(interior, bi))
        perm.update(dict(zip(bdry, bb)))
        h[w] = perm
    S = lambda w: (w + 1) % N  # odometer adding machine at level n
    F = {(w, p) for w in range(N) for p in bdry}
    assert 0 < len(F) < N * len(pts)  # closed, nonempty, proper
    ok = all((S(w), h[w][p]) in F for (w, p) in F)
    # orbit of a boundary point never leaves F -> not minimal
    w0, p0 = next(iter(F))
    orb = set()
    w, p = w0, p0
    for _ in range(N * len(pts)):
        orb.add((w, p))
        w, p = S(w), h[w][p]
    trapped = orb <= F
    print(f"  d={d}: |F|={len(F)}/{N*len(pts)}, F invariant={ok}, "
          f"bdry-orbit trapped={trapped} -> NOT minimal")
    assert ok and trapped

print("=== (3) recovery attempt: allow boundary-mixing fibre maps ===")
# Only non-homeomorphic fibre maps (swap a boundary with an interior grid
# point) can break F-invariance. Such maps are NOT cube homeomorphisms.
d, n, k = 2, 3, 3
N = 2 ** n
pts = [(a, b) for a in range(k + 1) for b in range(k + 1)]
is_bdry = lambda p: any(c in (0, k) for c in p)
bdry = [p for p in pts if is_bdry(p)]
F = {(w, p) for w in range(N) for p in bdry}
h = {}
for w in range(N):
    q = pts[:]
    random.shuffle(q)
    h[w] = dict(zip(pts, q))  # arbitrary bijections: mix bdry/interior
S = lambda w: (w + 1) % N
broken = any((S(w), h[w][p]) not in F for (w, p) in F)
print(f"  arbitrary (non-homeomorphic) fibre maps break F-invariance: {broken}")
print("  -> escape requires abandoning genuine cube homeomorphisms,")
print("     i.e. leaving the pinned target class. No in-scope recovery.")

print("RECOVERY_TEST_RESULT: OBSTRUCTION_CONFIRMED (no in-scope recovery)")
