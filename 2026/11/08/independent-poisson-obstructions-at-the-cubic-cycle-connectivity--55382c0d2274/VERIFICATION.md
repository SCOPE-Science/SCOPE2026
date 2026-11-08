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

The reproduced finite verification is `python3 artifacts/verify.py`. In the prepared package it completed 53,256 assertions with exit status zero. The checked objects are six-edge isolation and gap supports in cycle cubes, all overlapping pairs of these supports, small connected-component boundary sizes, exhaustive cut minimum comparisons in cycles of length 12, 14, and 16, and the arithmetic equality of isolation/gap deletion exponents at bandwidth three.

The program does not approximate the limiting connectivity probability or prove the factorial-moment convergence. Those steps, along with the cyclic component classification and exception probability estimates, are given in the mathematical proof in `RESULT.md`. No independent external audit or computer-verified infinite proof is asserted.
