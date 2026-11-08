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

The analytic proof in `RESULT.md` is the evidence for all dimensions and all real positive parameters. The modal factorization and necessary/sufficient endpoint conditions are explicitly derived there. The accompanying `check.py` requires Python 3 and NumPy and can be run as `python check.py`. On the reviewed package it reports 9456 passing diagnostic checks, including full-matrix eigenvalue calculations for hundreds of nondegenerate modal examples, parameter perturbations, and an exact-rational test case. Repeated polynomial roots are especially sensitive to floating-point square-root calculations, so a relaxed tolerance is used there, while the strict result follows analytically.

The exact test case has \((\beta,B,c)=(1,3,4)\), optimum \(r_*=1/2\), \(q_*=36\), small-mode roots \(1/2\) and \(1/18\), and large-mode roots \((5\pm2i\sqrt{14})/18\); at the comparison scale \(q=25\), the spectral radius is \(3/5\). These values are independently checkable by substitution into the displayed quadratic. The code does not address arbitrary noncommuting saddle-point blocks, floating-point convergence theory, or the novelty of the theorem.
