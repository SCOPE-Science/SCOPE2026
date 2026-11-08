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

# Verification

Run `python3 verify.py` (Python 3 standard library only). The script enumerates all insertion histories of small uniform generalized Stirling words, tests the exact all-selected joint probability against brute-force counts, reconstructs point probabilities by inclusion-exclusion, and checks the pair-covariance factorization, sign conditions, log-submodular subset probabilities and selected exponential-moment bounds. It passed 6,375 exact rational assertions for multiplicities 2, 3 and 4. The verifier also performs nine numerical covariance evaluations at order 4,000, which agreed with the analytic diagonal variance limit for several age fractions; those diagnostics are not used as proof.

The infinite-\(n\) proof is the analytic passage from exact pair moments to Riemann integrals with near-origin domination, given in `RESULT.md`. The asymptotic proof does not rely on finite enumeration. No independent audit, formal proof-assistant certification, or external validation was performed.
