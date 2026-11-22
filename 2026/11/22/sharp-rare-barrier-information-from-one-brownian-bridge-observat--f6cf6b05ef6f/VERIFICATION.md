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

The stand-alone `check.py` requires Python and `mpmath` and checks 8 finite-time Gaussian integrals by two independent formulas, 5 exact midpoint identities, and 5 rare-threshold asymptotic trends at two thresholds each. All passed in the documented run. The proof of the limiting regimes and the fixed-time exponential-rate comparison is analytic, not inferred from finite numerical experiments. Numerical evaluation of cancellations at large thresholds uses 95-digit precision; reproducing the code is not an independent audit. No finite-threshold global optimal-time theorem or moving-time uniform asymptotic is claimed.
