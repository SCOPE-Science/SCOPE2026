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

The analytic argument in `RESULT.md` establishes every infinite-time assertion, including positivity, global extinction, the single-peak result, stable-ratio tracking to cubic error, and reciprocal-square inversion. `verify.py` is a standalone supplementary test: it checks the critical reduction and asymptotic coefficient identities symbolically, plus numerical trajectories for both sides of the peak criterion. Numerical integration at finite time is only a diagnostic; it does not verify the universal limiting quantifiers.

Reproduce with `python verify.py` using Python 3, SymPy, SciPy, and NumPy. The verifier exits nonzero on failed assertions and prints `VERIFY_OK` on success. No stochastic, lattice, finite-population, or outside-parameter numerical claim is verified.
