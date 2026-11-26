---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The determinant of the augmented second-moment matrix is the covariance determinant by the Schur complement and is the sum of squared minors by Cauchy–Binet. Independence makes it the product of the four variances. Independent exact reproduction (/workspace/bernoulli_reproduction.py, Python 3) subtracts the first vertex from the other four and evaluates the resulting 4-by-4 determinants by the 24-term Leibniz formula across all 4,368 subsets. It gives counts (1360,2672,320,16) and excess totals 480, 64 for each single unbalanced coordinate, and 0 otherwise. Coordinate reflection averaging after division by q_i gives q_i/2 and (1-3q_i)/2 for the two respective types, producing 4e_3-18e_4 for the loss. For z=4q, the affine-in-each-coordinate certificate has values (0,23,46,37,0)/512 by corner Hamming weight. Convex interpolation gives nonnegativity, strictness away from the fair point for positive z, and sharpness by z approaching zero, where the original ratio itself is undefined. Finally e_3>=16e_4 proves R<1 on the stated domain. The frozen checker and verification notes were inspected, not executed.

## originality

FAIL

The central advertised result, the exact heterogeneous product-Bernoulli profile, is stated verbatim in equivalent factored form by the earlier October 18 Resultary finding. Its absence from the frozen comparison makes the novelty claim materially incorrect. The earlier result's quantitative deficit is not the specific squared-bias inequality, but that does not restore novelty to the exact profile. The squared-bias inequality follows by multi-affine interpolation directly from the known polynomial, with the coefficient forced by the all-deterministic corner limit.

## value

FAIL

The biased simplex invariant is naturally motivated, but it is already published. The residual squared-bias estimate is a direct corner interpolation of that known profile; the all-deterministic limit forces the coefficient, and the intermediate corners settle it by elementary arithmetic. The alternative weighted determinant tabulation is useful to check correctness, but no separate scientific use for those strata is established here. No substantive surviving result warrants a repaired finding on this evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
