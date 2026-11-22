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

# Reproduction and limits

With Python 3, NumPy and SciPy available, place `check.py` in the same directory and run `python check.py`. It performs 1,000 algebraic support-identity tests on normalized random directions, 100 comparisons with 1,440-point sampling of each of the two generating circles, exact-angle minimum/maximum tests, and independent one-dimensional quadrature for the lower and upper tail events at multiple small deficits. Expected terminal statement: `All diagnostic assertions passed`.

Numerical evaluations of the reproducible quadratures give lower-tail ratios at deficits 0.05, 0.025, 0.0125, and 0.00625 were approximately 0.8825258102, 0.8905902746, 0.8952358299, and 0.8977203917, approaching the proved coefficient 0.9003163162. The extracted second upper-tail coefficients at deficits 0.02, 0.01, and 0.005 were approximately 0.01573328684, 0.01567892625, and 0.01565190918, approaching the proved coefficient 0.015625.

The analytic proof, not these diagnostics, establishes the global extrema, all asymptotic orders and coefficients, and the marked total-variation limits. No exhaustive numeric range test, formal prover certificate, independent historical-priority investigation, or independent mathematical audit is claimed.
