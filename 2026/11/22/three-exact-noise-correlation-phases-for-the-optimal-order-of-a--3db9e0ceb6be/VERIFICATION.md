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

# Mathematical verification

`verify.py` is a standalone exact-arithmetic checker using Python 3.10 or newer and SymPy 1.11 or newer. It reconstructs all six three-step error expressions directly from the algorithm. Its principal check verifies all 30 endpoint inequalities over the continuum \(0<x\le1/4\) after a positive-denominator reduction and nonnegative rational Bernstein-coefficient expansions. It also tests the two algebraic crossing identities, all five strict threshold inequalities, the generic two-step comparison, twelve exact rational interior winner tests, and the two rational numerical examples.

Execute `python verify.py` after installing dependencies listed in `requirements.txt`. Expected output begins `PASS: 30 exact Bernstein endpoint comparisons`. The exact polynomial certificate and analytical affine-interpolation reduction establish infinitely many parameter comparisons; numerical examples are only corroboration. The finite-horizon theorem does not assert a general multidimensional or infinite-iteration learning-rate policy. Independent review of the mathematical proof and historical priority has not been performed.
