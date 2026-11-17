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

# Reproducibility and evidence limits
Run `python3 verify_facets.py` from the extracted package directory. This executes exact-rational polynomial recurrences, independently enumerates alternating permutations through nine vertices, checks the normal-Jacobian-corrected individual facet measures, and checks the two aggregate facet-area identities. For dimension forty it compares six facet/volume ratios with the analytic limits. The checker uses the Python standard library, requires no network and reports `PATH_FACET_AREA_PASS` on success.

The finite tests do **not** prove the unrestricted theorem. That follows from the generating-function identity, the simple pole at \(\pi/2\), the uniform coefficient bound after pole subtraction, and exact geometric slicing. No independent external scientific review has been performed.
