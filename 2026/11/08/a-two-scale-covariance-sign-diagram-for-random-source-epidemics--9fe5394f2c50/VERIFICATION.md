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

Execute `python3 verify_star_covariance.py` in the directory containing the packaged files. The verifier uses only the Python standard library and enumerates exact rational event probabilities over all seed and bond configurations for \(1\le k\le9\). It checks the four derived moments, both covariance expressions, exact threshold-order algebra on a rational grid, and representative exact sign witnesses. The separate large-degree root diagnostics use floating-point bisection and are not certificates of infinite asymptotics.

The packaged execution passed 5,503 exact rational assertions and 12 finite numerical asymptotic checks, reported together as 5,515 checks. Infinite ranges and unique-root assertions are proved analytically in `RESULT.md`; finite enumeration is not substituted for those arguments. No independent audit has been performed.
