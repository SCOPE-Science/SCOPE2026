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

# Verification of the exact local identities

Run `python verify.py` in Python 3. The script enumerates all \((n-1)!\) recursive parent arrays at every size \(2\le n\le8\) and every legal next parent, using `fractions.Fraction`. It checks the exact updates for path length, leaf count, external path length, mean depth, centered covariance, empirical depth dispersion, conditional innovation, the corrected finite-size drift, and the identity for conditional quadratic variation. Run output records the exact assertion count.

This does **not** check the infinitely many random trees needed for the Gaussian limit. The proof instead invokes the standard martingale array central limit theorem after deriving its conditional variance and Lindeberg hypotheses analytically. The uniform height fourth-moment bound is established using exponential moments of fixed-node depth and a union bound. No independent review has been performed; historical priority remains provisional.
