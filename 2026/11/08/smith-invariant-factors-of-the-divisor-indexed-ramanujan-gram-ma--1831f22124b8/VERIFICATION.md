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

## Reproducibility

Run `python3 verify.py` using Python 3.8 or later. No third-party dependencies are required. The code calculates Ramanujan sums by the Kluyver divisor formula, builds the Gram matrix as an integer product, and independently derives its Smith invariants from gcds of all square minors computed by the Bareiss integer determinant algorithm.

The checked execution returned:

`VERIFY_OK cases=27 determinant_minors=22203 independent_smith=PASS determinant=PASS cokernel_exponent=PASS modular_ranks=PASS`

## Boundaries

The 27 finite test moduli include powers of 2, 3, 5, 7, 11 and mixed-prime moduli. This is not a computational proof for arbitrary moduli. The full theorem follows from the incidence-factorization and local block-elimination proof in `RESULT.md`. The normal form and all derived formulas have undergone the stated self-review only; no independent audit has been performed.
