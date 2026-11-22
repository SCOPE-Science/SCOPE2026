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
# Reproduction and scope

Run `python verify.py` with `mpmath` installed. The included `CHECKS.txt` records the 81 diagnostics from a completed local execution of the embedded script. Diagnostic calculations exercise representative finite parameters and independent quadrature identities, but the proof's quantifiers range over all positive bandwidths for odd signs and over all sufficiently large bandwidths and all even frequencies for the sharp asymptotic threshold. The analytic proof of uniformity is contained in RESULT.md. No independent external mathematical audit has been performed.
