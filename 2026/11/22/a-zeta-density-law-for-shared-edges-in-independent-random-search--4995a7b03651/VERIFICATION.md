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

`check.py` requires only Python 3. Run `python check.py` in the same directory. The checker enumerates all insertion permutations for sizes 2 through 7, compares oriented parent-edge probabilities with exact rational formulas, verifies the resulting overlap expectation, checks the independent finite decomposition at six sizes, and compares three larger sizes with a stated bounded numerical tolerance. Observed output terminates with `PASS 133 exact-or-controlled assertions; c=0.289868133696; C=1.112335167121`.

The infinite \(L^1\) limit relies on stationary infinite priorities, the nearest-smaller-priority parent rule, ergodicity, and explicit boundary-excess bounds as given in `RESULT.md`. Exhaustive finite enumeration neither proves this limit nor independently establishes novelty.
