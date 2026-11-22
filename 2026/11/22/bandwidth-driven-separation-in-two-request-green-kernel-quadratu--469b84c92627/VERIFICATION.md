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

# Reproducibility and limits

`verify_bridge_dropout.py` is a standalone Python 3 script using only the standard library. Run `python verify_bridge_dropout.py` from a directory containing the extracted file. It executed successfully with `PASS 6443 conditional-Green-kernel, dropout-risk, root, grid and asymptotic checks`.

The script computes the scalar target variance both from the exact gap-cost formula and from Gaussian conditioning of the explicit Dirichlet Green covariance, including one- and two-site patterns. It covers inverse lengthscale \(\kappa\in\{0,0.25,0.6,1,2,4,7\}\), randomly chosen valid sites and delivery probabilities, independent checks of the zero-tension quadratic root, comparison grids for various parameter pairs, and the large-\(\kappa\) logarithmic coefficient. The independent computational route is direct two-by-two matrix inversion, not a restatement of the minimizing first-order condition.

The analytic proof in `RESULT.md` establishes the Gaussian Markov decomposition, the strict global convexity, the unique stationarity root, the two-parameter monotonicity via a strictly ordered derivative-kernel likelihood ratio, and the limiting formulas. Finite computations alone cannot prove those continuum statements. Numerical checks use finite precision and are supplemental. The stated historical-priority status is provisional; external audit has not been performed.
