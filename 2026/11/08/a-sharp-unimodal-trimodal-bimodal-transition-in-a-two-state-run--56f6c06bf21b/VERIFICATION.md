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

# Verification and reproducibility

The analytically proved claim is stated in `RESULT.md`. The standalone `check_modes.py` uses only the Python standard library, does not download data, and checks exact rational polynomial identities, the triple-angle-derived critical polynomial, derivative-factor signs and independently computed numerical derivatives and integrals. The packaged replay printed `Exact and numeric diagnostic assertions passed: 60`.

The core exact identities are \(U'(z)=3(5z-1)(z+3)/(1+2z-3z^2)^2\), \(U(1/5)=25/4\), \(U(0)=7\), and, at \(u=13/2\), the derivative numerator \(-\tfrac12(13z-1)(3z-1)\). These provide a finite symbolic route to reconstruct the proof independently of the numerical diagnostics.

For the numerical demonstrations at \(u=13/2\), the code reports positive minimum and maximum positions \(0.043816776925899\) and \(0.101304453609601\) and relative heights \(0.999343155092512\) and \(1.001088504664840\). These approximate values are not used to establish the all-parameter mode counts.

The model assumes exact stationary sampling, no translational Brownian noise, positive parameters and idealized two-orientation switching. This package has not undergone an independent scientific audit or experimental validation.
