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

Run `python3 verify_facets.py` from a directory containing the extracted script. It performs direct complex-arithmetic support checks for the non-simple facets and the two-edge tetrahedral facet family for every `n` from 3 through 80, and asserts the analytic formulas for each instance. The exhaustive proof of those statements for all dimensions is in `RESULT.md`; this finite check serves only to detect mistakes in signs, indexing, and boundary conditions. No independent audit has been performed.
