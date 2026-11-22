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

# Verification

`CHECKER.py` is a standalone Python 3 program using SymPy and NumPy. Running `python CHECKER.py` from a directory containing the file checks both exact four-by-four determinant identities and the algebra for the shared variance coefficient, both quartic eigenvalue coefficients, the fourth-cumulant contrast, its derivative, and its inverse. It then independently propagates the complete order-four conditional moment hierarchy over 3000 steps for six strictly positive coins and compares the resulting axial-minus-diagonal fourth-cumulant rate to the exact limit. The largest observed absolute error was below 0.01 per step.

The exact symbolic identities support the finite-dimensional algebra, while the theorem's infinite-time limit and derivative/range quantifiers rest on the Perron spectral argument and strict inequalities in `RESULT.md`. Finite time runs are not exhaustive and do not certify asymptotics by themselves. Originality is compared to published sources, with an explicit unresolved risk that earlier broad forward formulas may imply parts of this inverse theorem after nontrivial specialization.
