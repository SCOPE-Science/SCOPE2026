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

Run `python CHECKER.py` in the same directory. The checker uses only the Python standard library and a fixed random seed. The observed execution passed **90,810** checks and printed the root \(1.793282132900761\), optimal ratio \(1.298425607525639\) and percent advantage \(29.842560752564\). The numerical experiments include randomized parameter identities, Jensen comparisons for nondegenerate two-point renewal gaps, stochastic competitor reset simulations under both visit clocks, and derivative signs away from the critical point.

The mathematical certificate is the proof in `RESULT.md`: solve the affine expectation recursion, exploit strict Jensen/monotonicity, maximize first in harvest fraction and then in normalized mean interval using the unique positive root of \(e^x=1+x+x^2\). Neither finite tests nor numerical root estimates alone certify the full-domain theorem. No independent audit has been performed.
