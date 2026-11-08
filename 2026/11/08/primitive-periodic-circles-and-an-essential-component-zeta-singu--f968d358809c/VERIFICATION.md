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

# Mathematical verification and limits

The proof reconstructs all iterations from the finite binomial expansion of a nilpotent Jordan block; the fixed-set fibers are kernels of an integer triangular matrix of determinant \(n^{d-1}\). Möbius inversion is valid because the least period is constant on every fixed circle. The multiplicative primitive share follows from the Jordan totient identity. For \(d\ge3\), the Euler product has a strictly positive limit, whereas for \(d=2\) it tends to zero. The connected-component zeta series is the exponential of a rational function with poles at the relevant roots of unity, yielding essential singularities.

The standalone `verify.py` executed with ordinary Python 3 and no external dependencies. It checked 36 dimension/denominator/period configurations in dimensions two through five, including 4,092 exact-rational fixed-fiber representatives by direct iteration and their least periods. It checked 380 additional logarithmic-zeta coefficients. Observed output:

`VERIFY_OK dimensions=2..5 exact_parameter_cases=36 exact_circle_representatives=4092 zeta_coefficients=380`

The finite verification is not a substitute for the all-integer proof. Historical novelty is assessed against the named accessible literature and prior results, not asserted as a theorem about all publications. No independent mathematical audit or external validation has been performed.
