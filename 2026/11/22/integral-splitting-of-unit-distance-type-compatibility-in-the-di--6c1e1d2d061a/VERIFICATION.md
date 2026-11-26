---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The triangle inequalities over the named equilateral distance-four base classify the nonalgebraic vectors as the core {2,3,4}^n and n exceptional classes with a unique 1 and all remaining coordinates in {3,4}. Extending the base by two distinct points at distance 1 imposes exactly the coordinate differences ≤1; sums ≥1 are automatic, so the diagonal is included. The core D=T tensor-powered n times is unimodular (det T=−1), and off-core cross-class entries vanish. The mixed rows are tensors with one factor e=(1,0,0) and other factors r3=(1,1,1), r4=(0,1,1). The row eT⁻¹=(0,1,−1) pairs to zero with all three, so every entry of HD⁻¹Hᵀ vanishes integrally. The displayed determinant-one upper block change thus gives the claimed congruence, not just equivalence over a field. Each Jq contributes exactly one unit Smith factor and one positive eigenvalue. T has two positive and one negative eigenvalue, and the tensor sign difference is (2−1)^n=1. The principal selection has Schur complement I_n and determinant (−1)^(n·3^(n−1))=(−1)^n. At n=1 the four types yield T⊕[1], consistent with rank 4, inertia (3,1,0) and no zeros.

## originality

PASS

The entry criterion and an aggregate unit-pair count are covered and not credited as new. The supported distinct claim is the explicit integral congruence and its arithmetic and inertia consequences. Neither Sauer’s possible-distance theorem nor the nearest compared metric or ultrametric calculations provides that congruence or the integral Schur cancellation for this matrix.

## value

PASS

For a natural metric extension question on a named homogeneous space the theorem explains why an exponentially sized compatibility matrix has no finite cokernel torsion in any size, via an integral orthogonality rather than enumerated ranks. It also gives the exact real signature and a full-rank principal unimodular witness. These determine distinct arithmetic and real invariants not supplied by type-count data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
