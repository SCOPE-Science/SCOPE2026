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

The standalone `verify_friendship.py` uses exact rational Gauss–Jordan inversion and an independently specified graph edge list. It completed 2,712 grounded-matrix checks, 28 exhaustive budget optimizations, 11,900 count-profile comparisons, and one strict nonnesting check.

Command: `python verify_friendship.py` (Python 3 standard library). The infinite-family classification is proved analytically in `RESULT.md`; finite checks are not a proof for all sizes. Reproducibility does not constitute independent validation.
