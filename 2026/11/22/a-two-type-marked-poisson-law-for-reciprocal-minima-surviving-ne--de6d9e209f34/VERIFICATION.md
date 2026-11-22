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

# Reproducibility and limitations

Execute `python3 verify.py` with Python 3 standard libraries. The script performs exact rational checks of the two expectation formulas and exhaustive orderings of small square matrices, checks the intersection moments of independent two-by-two arrays, compares the exact integral with a direct two-dimensional quadrature, and checks the asymptotic intensity constants by quadrature.

The analytic justification for the arbitrary-size marked Poisson limit is the exact simultaneous-event integral and its dominated-convergence/factorial-moment proof in `RESULT.md`. Numerical checks and exhaustive finite enumerations are cross-checks only, not certificates for the infinite theorem. The input cost law must be continuous and shared among cells, with independent entrywise refresh decisions and independent replacements.

No separate mathematical validation has been performed.
