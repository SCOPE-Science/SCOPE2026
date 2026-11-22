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

The full-radius-two enumeration is proved in `RESULT.md` by an exhaustive classification of disjoint and overlapping adjacent swaps. `verify.py` performs independent finite breadth-first exploration and transfer-weight calculations, checking 33,730 words over three alphabet sizes; all tested instances passed. It also checks exact finite mean and maximizing-center counts. Finite tests cannot prove the all-length statements or the Gaussian/Poisson limits; those follow from the displayed counting arguments and the binomial limit theorems. No external independent review or certification has been performed.
