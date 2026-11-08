---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

Execute `python verification/check_rook_moments.py` using Python 3 and only its standard library. It enumerates integer dilates of the two-row partial permutation polytope, forms weighted lattice-point sums, extracts their highest Ehrhart coefficients by exact finite differences, and compares them against the claimed moment integral. The weighted counting route is distinct from integrating the disjoint caps.

A successful run reports `TWO_ROW_ROOK_EXACT_CHECKS_PASSED 31`. The actual run produced normalized volumes \(1,4,17,66\) for \(n=1,2,3,4\). Checks include volumes for all four dimensions, several lower moments and one cubic moment for \(n=2,3\), and signs of the three covariance classes for those dimensions. These finite experiments do not prove the formula for every \(n\) or arbitrary degree; the analytical cap integration and inequalities provide that proof. No external verification was commissioned or performed.
