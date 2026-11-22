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

# Verification boundaries

The mathematical argument is reproduced in `RESULT.md`, with critical polynomial equalities and a global three-adic isometry, so no finite search is used as a proof of an all-level statement.

The included pure-Python `check.py` uses ordinary integer binomial coefficients to count all values in a complete period modulo \(3^k\) for every \(1\le k\le8\), checking each of the \(3^k\) target multiplicities against the independent modular square-root formula. It additionally checks a period obstruction, the singular polynomial decomposition, explicit modular square-root lifting and bijectivity of the normal-form change of variables. The captured actual output is `check_output.txt` and ends with `PASS: checks= 45544`.

Limitations: the direct computations stop at \(k=8\); arbitrarily deep congruences, surjectivity and Haar measures rely on the proof. Historical priority against all possible older general p-adic distribution theorems has not been independently established. The claim does not address ordinary rational or integer-square values of the binomial numbers.
