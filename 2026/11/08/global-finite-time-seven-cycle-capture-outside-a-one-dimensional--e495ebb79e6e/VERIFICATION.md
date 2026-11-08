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

Verification uses `check.py` with Python 3 and the standard-library `fractions.Fraction` type. Execute `python3 check.py` in the directory containing this file. It checks both seven-cycle identities as affine functions of the parameter, sign stability on the stated half-line, and the rational-denominator obstruction. It also samples exact-rational forward orbits for five admissible rational parameters.

The countable-union proof of planar nullity, Baire meagerness, and Hausdorff-dimension upper bound is analytical; no finite computation can certify it. Global graph capture and graphwise finite-time absorption are used as published lemmas from Cima–Gasull–Mañosa–Mañosas (Propositions 17, 18 and 25). The parameter exception for reduced denominators divisible by \(15\) is unresolved rather than declared noncapturing.
