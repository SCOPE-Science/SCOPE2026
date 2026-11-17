---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The centered edge-difference Minkowski sum has x_i=t_i-t_{i-1}, |t_i|<=1/2. Feasibility of cyclic differences is exactly that partial-sum range <=1, equivalent to all proper cyclic-interval inequalities |sum_I x_i|<=1. The intrinsic normal of a length-s interval has squared norm s(n-s)/n and gives the displayed inradius and all ball-center inequalities. Odd n=2k+1: all k-block equalities imply c_i=c_{i+k}; gcd(k,2k+1)=1 gives c=0. Even n=2k: all k-block equalities force c_i=c_{i+k} and zero half-sum, while near-balanced lengths k±1 force |y_i|<=beta_k. Any other block length k±j has center sum bounded by j beta; convex f(j)=1-sqrt(1-j^2/k^2) >= j f(1) establishes sufficiency. Exact cube-hyperplane vertices have >=k-1 coordinate endpoints, yielding parity-dependent closed counts. Independently all 5,880 stated even-cycle interval inequalities were tested for candidate vertices n<=12. Analytical proof, not the finite test, covers all n.

## originality

PASS

A 2026-10-11 published general weighted graphical-zonotope cut theorem already gives the scalar inradius and one centered optimum; it explicitly disclaims classification of all Chebyshev centers. The 2026-10-25 in-in zonotope result concerns ambient full-dimensional cube PLUS graphical-zonotope segments (not affinely/isometrically equivalent to edge-only intrinsic K_n), and its even-cycle center segment is not this k-1-dimensional cube section. Padrol–Pilaud–Poullot (2025) handle graph-zonotope deformations, not Euclidean center classification. Existing K_{p,q} center theorems include C4 as one special case but do not dominate all cycle orders or vertex counts. The entire parity split center polytope is genuinely additional to known radius, best knowledge with historical-risk proviso.

## value

PASS

The full Euclidean incenter set is a canonical geometric invariant of graphical zonotopes. Here a previously known sharp radius unexpectedly has a unique center at odd orders but a high-dimensional cube-section family at even orders; all endpoint vertices and a reduced inequality description are explicit. This is a motivated complete all-cycle classification, not a known-radius recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
