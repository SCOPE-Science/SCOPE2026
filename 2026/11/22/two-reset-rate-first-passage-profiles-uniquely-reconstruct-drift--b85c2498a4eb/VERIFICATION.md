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

# Verification of the mathematical claim

The exact proof derives the renewal identity, boundary-value problem, positive integrating-factor representation, strict first-hitting Laplace order, the nonzero reconstruction determinant, and one-rate ambiguity. All statements are for \(x\in(0,L)\), with endpoint coefficients obtained by continuity.

Run `python CHECK.py` with NumPy and SciPy to independently recompute the two-rate inverse on 185 interior points for a nonconstant diffusivity and variable-sign drift, plus three constant-coefficient test cases. Reported numerical residuals are finite checks only; the analytic proof in RESULT.md establishes the universal quantifiers. No third-party independent audit or formal theorem-prover certification has been performed.
