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

# Reproducible checks

Run `python VERIFY.py` using Python 3 and SciPy. The script completes 46 finite diagnostics for the critical parameter example \(c=1\), \(r=0.65\), \(\kappa=1\). It independently computes \(y=3.146193220621\), \(\delta=0.329615288875\), \(\eta=0.256539722667\) and the slow-class finishing probability \(0.547275686561\). It checks two-color intensity normalization by direct quadrature, exact Gamma-tail quantile identities for four sample sizes, the predicted power/log scale within finite-sample bounds, positive finite class intensities and local exponential-tail ratios.

The infinite distributional limit does not follow from these 46 finite checks. It follows from the explicit Poisson-tail asymptotic, convergence of independent rare-event point processes, localization of their maxima, and a conditional mean/variance control on the Poissonization clock. The only numerical libraries used are SciPy and the Python standard library (the environment also has NumPy, but the script does not require it). No Monte Carlo approximation is used. All mathematical parameters and endpoints in the proof are stated in `RESULT.md`.
