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

The standalone script `verify.py` was run from this package with Python 3 standard-library modules. It printed `SYMMETRIC_CAYLEY_DIAMETER_EXACT_OK 407 posets 2996310 pairwise comparisons`. It independently enumerated all naturally labeled transitive posets on up to five elements, their linear extensions, and each lifted vertex; all exact squared distances were checked. The full infinite statement follows from the displayed proof in `RESULT.md`, not the finite replay. The script also checks closed antichain counts for sizes two through seven. Historical priority and independent expert auditing remain unperformed.
