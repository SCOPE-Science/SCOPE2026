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

The theorem is proved by exact disintegration over the output tail, pointwise exclusion of two opposing run-transition markers in every length-\(q\) starting window, and equality rigidity under a two-sided stationary extension. The strict upper nonattainment of the universal gap uses only continuity and positivity on a compact binary shift.

Reproduction: use Python 3 standard library and run `python3 checker.py` in the extracted artifact directory. Recorded output: 131,064 cyclic-word checks, 42 equality cases and twelve entropy formula comparisons, all passed. Tests cover \(q\in\{2,3,4,5\}\) and cycle lengths from 1 through 14; they do not establish the infinite claim, which is proved analytically in `RESULT.md`. No independent mathematical audit has been performed.
