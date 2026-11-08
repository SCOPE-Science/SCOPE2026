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

The exact proof is the root-budget and constructive inequality argument in `RESULT.md`. A self-contained checker `verify.py` uses Python 3 with no packages. It constructs rational birth/death stationary weights, tests detailed balance between neighboring labeled epidemic configurations, evaluates the four-person rational example, and verifies the constructive three-mode pattern for population sizes 4 through 200. It also tests 2,916 finite model/rate combinations for the polynomial mode ceiling and a separate exact four-person parameter grid.

Command: `python verify.py`. Observed result: `VERIFY_OK exact stationary distribution, generator edge-balance, root mode ceilings, 4-person chamber and rational witness 2916 parameter/case checks 12168 edge comparisons attempted`.

Finite tests do not prove the infinite-population-size theorem. The algebraic proof gives all-size coverage; the checker tests its encoding and selected boundaries. This is a scientific reproducibility check, not an independent external audit.
