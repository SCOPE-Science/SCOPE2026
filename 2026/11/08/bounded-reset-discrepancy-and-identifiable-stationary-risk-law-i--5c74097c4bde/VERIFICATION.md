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

# Reproducible verification and limits

Run `python3 check.py` using Python 3 and its standard library; no external dependencies are needed. Exact rational branch checks were run for four rational parameter pairs satisfying the theorem's open inequalities, over more than one thousand rational initial states per pair across both signs and both return-time regimes. These test the one-step and two-step formulas and the image endpoints.

The checker separately evaluates the normalizing constant, atom weight, first two absolute/second risk moments, and parameter inversion for the exactly irrational example \(a=1/2\), \(b=5/3\). It runs the original two-coordinate map for 150,000 iterations and checks the maximum observed zero-risk count discrepancy, then compares the time fraction at zero, the mean absolute risk, and the second moment against the analytical law. Three independent polynomial observables are used for numerical quadrature of the proposed stationary integral before and after applying the original map. The quadrature explicitly splits at the discontinuous branch threshold to avoid a numerical integration artifact.

A passing finite or numerical check supports the analytical calculation but is not exhaustive over the continuum of parameters or initial conditions. The proof in `RESULT.md` is the evidence for infinite statements; the stationary probability is not asserted to be globally unique. No independent external audit was conducted.
