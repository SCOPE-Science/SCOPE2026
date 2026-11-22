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

The standalone `verify.py` runs with Python 3 and the standard library only. Run `python3 verify.py` in the directory containing this file.

Executed output: `PASS 1522 exact-formula, Jacobi-spectrum and asymmetric-perturbation checks`.

The tests independently diagonalize full cycle, clique and hypercube coronas, inspect the proposed optimum versus 60 budget-normalized asymmetric allocations per case, and check the exact two-rate formulas and positive budget. Floating-point tests have finite precision; they cannot prove an infinite-dimensional uniqueness or all-size theorem. The analytic proof in `RESULT.md` establishes those conclusions. No independent audit has been performed.
