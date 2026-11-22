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

# Reproduction and limitations

The analytical proof is in `RESULT.md`. Run `python checker.py` in the same directory with Python, NumPy, SymPy and SciPy to replay a finite-state and symbolic cross-check. A completed run reported 154 passing assertions.

The checker independently constructs the full finite-state Markov matrix for each ring with \(N\in\{5,6,7\}\) and three rational values of \(q\), solves the stationary distribution for an iid fair-sign global reset source, and compares reconstructed correlations to the claimed formula. Exact SymPy arithmetic checks the pair recurrence, strict witness positivity and the Gibbs-equilibrium residual for five ring sizes, while an analytic renewal and generator argument proves all parameter values and both domains.

The finite numerical comparisons are corroboration, not an exhaustive proof of the infinite-system or all-rate claim. The stated four-spin discrepancy bound may not be sharp, and no finite-sample power, thermodynamic entropy-production identity or implementation cost is established. Independent scientific audit has not been performed.
