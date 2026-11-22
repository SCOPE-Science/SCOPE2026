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

The accompanying `VERIFY.py` uses exact rational arithmetic for the exponential interval certificate (100-term positive Taylor enclosure and rigorous remainder), tests 40 closed curvature panels, and verifies the signs that bracket the unique theta-function minimizer. The analytic proof also requires the explicit spectral decomposition, a midpoint quadrature bound, dominated convergence and the Gaussian Poisson identity, all stated in RESULT.md.

The finite matrix checks in the program illustrate the location scaling but do not prove the infinite-family limit. The continuum derivative-tail estimates are stated explicitly in RESULT.md; the program encloses the five dominant exponential terms and certifies the margin needed to absorb those tails.

Run `python VERIFY.py` with Python, SymPy, NumPy and SciPy. The independent audit status remains not performed.
