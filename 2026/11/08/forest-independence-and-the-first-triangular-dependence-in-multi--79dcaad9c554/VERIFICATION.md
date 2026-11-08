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

This package contains `checker.py`. Execute `python3 checker.py` in a standard Python 3 environment without third-party packages. The checker uses exact rational and integer arithmetic and prints `ALL_CHECKS_OK` when all finite tests pass. It enumerates complete three-order samples for sizes 2–4, independently counts compatible directed-edge triples for sizes 2–8, tests independence of small relative-order forests and dependence of triangles, and tests the derived rational formulas. The all-parameter proof is in `RESULT.md`; finite computation is supplemental. No independent audit has been performed.
