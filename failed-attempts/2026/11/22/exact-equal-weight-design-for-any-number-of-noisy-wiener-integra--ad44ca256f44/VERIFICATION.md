---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The quadratic regression risk follows from stochastic Fubini and Itô isometry. Compactness of the sorted site simplex gives attainment. After merging positive repeated sites the Brownian precision matrix plus the inverse noise matrix is a strictly diagonally dominant M-matrix; the computed K^{-1}k is strictly positive, giving positive weights at every positive site. Replacing an unused zero site is a strict improvement by a nonzero residual partial covariance. At an interior knot of multiplicity m, symmetric splitting changes the loss at first order by -2(m-1)v² times the displacement; at 1, moving one of m copies left changes it by -(2m-1)v² times the displacement. Subtracting the interior normal equations forces consecutive weights equal because the multiplier is η+(v_i+v_{i+1})/8>0. The smaller quadratic root is the only feasible one; the larger lies above 2/(2n-1). The projection identity then gives the claimed risk. Uniqueness is of the sorted design, or up to permutation of sensor labels. The companion verify.py was inspected, not executed; it uses rational perturbations for n≤4 and does not certify the continuous search. The proof, not the finite checks, establishes global optimality.

## originality

FAIL

The distinct indexed joint precision-and-time theorem covers the complete submitted fixed-variance theorem as an exact restriction; in particular its broader optimum is feasible for the restricted problem. Both records bear the same UTC calendar date in the catalogue, so this establishes coverage, not which result came first.

## value

FAIL

The exact noisy design is a useful result in itself, but the frozen contribution as a distinct finding is a direct budget substitution into an indexed theorem that already gives equal weights, uniqueness, nonreplication and exact risk. No separately motivated new invariant or structural result remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
