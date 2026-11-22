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

The included `checker.py` uses only Python standard-library arithmetic and was executed against its actual package path. Output: `PASS: 59170 deterministic assertions`. The assertions include four sets of exact rational tangency identities, multiple kinetic parameter cases, grid comparisons against arbitrary two-point input laws, cap-transition equality and the high-cap limit. These diagnostics are not an exhaustive search over distributions: the proof in `RESULT.md` uses an exact global supporting-line certificate and Jensen's inequality. Independent validation and audit have not been performed.
