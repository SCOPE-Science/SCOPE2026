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

# Reproducibility checks

From the extracted directory run `python3 check.py` with Python 3 and the standard library; no third-party modules, datasets or network access are required. The checker verifies exactly the polynomial factorization for the one-to-three difference, the polynomial reduction for the three-versus-two gap at \(z=3^{-1/4}\), and exact rational inequalities establishing strict positivity. It separately enumerates the viability patterns for 27 exact rational parameter configurations and tests two numerical budgets bracketing the transition.

The proof in `RESULT.md` is the argument for all positive budgets, sample counts and viability parameters; finite checks are supplementary and are not represented as exhaustive or external validation. The experiment is an idealized independent-Poisson model, not a measured laboratory or field validation. Independent external audit has not been performed.
