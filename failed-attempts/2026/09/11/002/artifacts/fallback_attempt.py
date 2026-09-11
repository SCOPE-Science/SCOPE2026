"""Fallback attempt log for lane-678 (bounded, concrete).

Fallback demands: explicitly specified minimal skew-product alpha0 on
X0 = (odometer Cantor base) x [0,1]^h with listed scale/h/skewing cocycle,
C0 = C(X0) rtimes Z simple, plus explicit a0,b0 in M_2(C0) with
d_tau(a0)+1/2 < d_tau(b0) for ALL traces and certified non-subequivalence.

This script instantiates a concrete in-class candidate (2-adic odometer at
finite level n, h=1 and h=2, explicit skewing cocycles: irrational rotation
of the fibre, fibrewise flip) and checks the fallback's first mandatory
clause: minimality of (X0,alpha0) / simplicity of C0.

Result: the manifold-boundary sub-bundle F = Omega x d([0,1]^h) is closed,
nonempty, proper, and invariant under EVERY such candidate (any genuine
fibrewise cube homeomorphism preserves the boundary setwise by invariance
of domain). Hence no in-class candidate is minimal; C0 is not simple; the
exact fallback's object clause is unsatisfiable in the pinned class.
The Cuntz-trace clause is then unauditable (no simple C0, trace simplex
unidentified, no explicit pair with uniform gap + certified
non-subequivalence closable in-session). Escape (collapse boundary /
Hilbert-cube / singular fibres) abandons the exact fallback's stated
fibre [0,1]^h, so is out of scope.
Stdlib only.
"""
import math

print("=== Fallback F1: instantiate in-class candidates, test minimality ===")
# Finite-level stand-in: Omega_n = Z/8, fibre grid for [0,1]^h.
# Candidate skewings (all genuine boundary-preserving fibre homeomorphisms):
#  (i) rotation-like twist, (ii) fibre flip, (iii) odometer-dependent shear.
# Discrete model uses boundary-preserving bijections, the exact property
# every true cube homeomorphism has.
import random
random.seed(6780)

def grid(h, k=3):
    pts = []
    def gen(prefix, depth):
        if depth == h:
            pts.append(tuple(prefix)); return
        for c in range(k + 1):
            gen(prefix + [c], depth + 1)
    gen([], 0)
    return pts

def is_bdry(p, k=3):
    return any(c in (0, k) for c in p)

for h in (1, 2):
    pts = grid(h)
    bdry = {p for p in pts if is_bdry(p)}
    N = 8
    S = lambda w: (w + 1) % N
    # three explicit skewing families, all boundary-preserving
    for name in ("twist", "flip", "shear"):
        hmap = {}
        for w in range(N):
            perm = {}
            ib = sorted([p for p in pts if p not in bdry])
            bb = sorted([p for p in pts if p in bdry])
            # deterministic pseudo-skewing shifts per family
            s = {"twist": w, "flip": N - 1 - w, "shear": (3 * w) % N}[name]
            q = ib[s % len(ib):] + ib[:s % len(ib)] if ib else []
            perm.update(dict(zip(sorted([p for p in pts if p not in bdry]), q)))
            r = bb[s % len(bb):] + bb[:s % len(bb)]
            perm.update(dict(zip(bb, r)))
            hmap[w] = perm
        F = {(w, p) for w in range(N) for p in bdry}
        inv = all((S(w), hmap[w][p]) in F for (w, p) in F)
        proper = 0 < len(F) < N * len(pts)
        print(f"  h={h} skew={name}: |F|={len(F)}/{N*len(pts)}, "
              f"proper={proper}, F invariant={inv} -> "
              f"{'NOT minimal, C0 not simple' if (inv and proper) else 'minimal?!'}")
        assert inv and proper

print("=== Fallback F2: perforation-pair clause audit ===")
print("  No simple minimal C0 exists in-class (F1), so no M_2(C0) pair (a0,b0)")
print("  with uniform gap d_tau(a0)+1/2<d_tau(b0) over all traces plus")
print("  certified non-Cuntz-subequivalence can be opened, let alone closed.")
print("  Trace simplex = alpha0-invariant measures projecting to odometer")
print("  measure: unidentified, so 'for all tau' is unauditable in-session.")
print("FALLBACK_ATTEMPT_RESULT: BLOCKED (object clause unsatisfiable in-class)")
