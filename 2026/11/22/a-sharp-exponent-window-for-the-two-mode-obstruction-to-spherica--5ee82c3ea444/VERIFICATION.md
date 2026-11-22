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
# Reproducibility and mathematical scope

The standalone `check.py` runs finite exact symbolic tests of the quartic coefficients for several integer exponents and dimensions, numerical root isolation for four dimensions, and direct Gauss–Jacobi quadrature of the spherical norm inequality at multiple small perturbation amplitudes. All 42 tests passed with installed SymPy and SciPy. The independent analytic argument in `RESULT.md` establishes the sign criterion for all real \(q>2\) and all integers \(d\ge4\), by a monotonic derivative and a Taylor-expansion remainder estimate.

Run `python check.py` from this directory with Python 3, SciPy and SymPy. It prints `PASS: 42 finite symbolic, transition and quadrature diagnostics`. Computations confirm special cases and are not an infinite-range certificate. The source of the 2021 motivating question is arXiv:2101.06209v1; a public later fourth-order example is explicitly credited. No independent audit has been performed.
