---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Decompose each principal symmetric matrix by the distinguished antisymmetric vector, the unmarked sum-zero subspace, and the 2x2 block [[t,k],[2,k-1]]. For t!=0, singularity occurs precisely when t(k-1)=2k, with corank one and binom(d-2,k) such subsets. The singular projective quadric of rank r has Euler characteristic s-1+1_{r even}, with s=1 handled separately. Inclusion-exclusion on the coordinate torus changes (-1)^d chi(Q cap T) by -1 for each corank-one subset. Generic ML degree is Eulerian 2^(d-1)-d by the established toric generic-degree theorem. Independent exact SymPy rational ranks and alternating Euler sums corroborate d=4..7 at six generic/exception scalings; not a proof for unbounded d.

## originality

PASS

Clarke et al. 2024 identify principal A-determinant factors and show particular d=4,5 ML-degree tables but not the all-d one-edge rational transition/jump formula. Oldekop 2026 supplies Euler/rank theory and low-dimensional classifications, but its accessible abstract does not assert this one-edge formula. This particular 1-parameter all-order binomial degeneracy evaluation is not mechanically a restatement of the generic toric ML degree; the matrix-rank and Euler contributions are essential additional work. Full Oldekop text could not be inspected; explicit risk remains, not automatic failure.

## value

PASS

The one-edge perturbation is a canonical minimal symmetry-breaking discriminant slice of the second-hypersimplex model. Determining all resonance locations and their exact binomial ML-degree jumps for arbitrary d is structurally useful for likelihood critical-point counts, especially the surprising drops while the full matrix stays nonsingular.

The dated certificate retains the supplied scientific assessment, sources and limitations.
