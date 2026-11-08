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

Run `python3 verify.py` with Python 3. The program directly computes GCDs of selected binomial coefficients for all `k=2..40`, cross-checks a separate exact prime-factor valuation implementation, and enumerates all `n` through `1,000,001` to check the large-prime versus prime-power-exception decomposition and to report finite first-moment values. The exact output is embedded in `verify_output.txt`. No external packages are needed.

Finite enumeration does not prove the unconditional analytic asymptotic: the infinite-domain proof uses the published prime-support criterion, Newton interpolation, power-saving exception counting, and the weighted prime number theorem. No independent mathematical audit was performed.
