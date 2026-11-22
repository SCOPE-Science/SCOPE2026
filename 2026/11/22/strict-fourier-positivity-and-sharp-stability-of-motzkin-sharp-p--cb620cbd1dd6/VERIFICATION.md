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

Exact reproducibility: run `python3 verify_peak_spectrum.py` using Python 3 standard library. The checker constructs all ordinary Motzkin excursions for lengths 2 through 12, directly aggregates the adjacent-sharp-peak profile distribution, performs the integer Walsh–Hadamard transform, and checks the same 4,094 multipliers against (a) a separate signed dynamic program on height and previous-up-step status and (b) the separated-forced-peak inclusion-exclusion formula. It also checks positivity/minimization and the exceptional small ranks. No floating-point arithmetic is used in these checks.

Limits: the exhaustive checks cover only those finite lengths and provide no proof for larger lengths. The proof in `RESULT.md` separately establishes the infinite-order theorem by path deletion, induction and first-return decomposition; its asymptotic statement follows from the stated algebraic generating functions. No independent audit was performed.
