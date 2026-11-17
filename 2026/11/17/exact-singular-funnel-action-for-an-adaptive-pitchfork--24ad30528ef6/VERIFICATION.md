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

# Reproducibility

Run `python verification/check_funnel.py` from the package root with Python 3, NumPy and SciPy. It computes the exact saddle eigenvector slope, follows the backward stable branch in logarithmic coordinates, and compares scaled logarithmic section positions against the stated action for \(a=3\), \(b=2\), at sections \(\mu=2,5\) and rates \(\varepsilon=0.1,0.03,0.01\). It also checks the exact cancellation of feedback coefficient \(a\) between two section actions for two admissible feedback values.

The numerical values of \(-\varepsilon\log x_\varepsilon(2)\) for these three rates are approximately 0.490688604821, 0.445150093903 and 0.431534509124, compared with the analytical action 0.424635855096. The analogous values at \(\mu=5\) are approximately 2.371986030580, 2.325918526007 and 2.312302933252, compared with 2.305404279226.

The essential verification is symbolic and in the written proof: \(r^2+b=ar\); the saddle determinant \(\varepsilon r(2r-a)<0\); the global graph and fixed-interior-point estimate \(0\le\mu_\varepsilon(\eta)-r^2\le(a\varepsilon/r)\log(r/\eta)\); the exact logarithmic integral; and the uniform small-\(\eta\) integrand bound. These verify the limit for all admissible real parameters; the program only samples finitely many instances. No prefactor or section-uniform estimate was derived. Independent validation has not been performed.
