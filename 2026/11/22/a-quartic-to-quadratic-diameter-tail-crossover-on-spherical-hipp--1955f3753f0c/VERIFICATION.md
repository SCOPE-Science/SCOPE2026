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

# Verification of the geometric probability statement

The proof uses the exact sphere--cylinder parameterization, algebraic determination of the antipodal set, an independently checked fixed-parameter quadratic form, and the exact trigonometric identity for near-antipodal pair sums. A single local rescaling produces the quartic crossover sublevel set. Compact localization, dominated convergence, and the arclength normalization establish the stated constants and total-variation limit. The distinction between numerical evidence and mathematical proof is retained.

Execute `python CHECK.py` after installing the packages in `requirements.txt`. The checker reports sample finite-deficit approximations and asserts key exact identities and normalization constants. It is finite numerical corroboration, not proof of an asymptotic statement or an exhaustive literature search.

Independent audit: not performed.
