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

# Reproducibility and verification

The proof is self-contained in `RESULT.md`, with explicit Fourier multiplier, cyclotomic norm calculation, the closure-constrained implicit-function argument and the sharp derivative-loss test. The standalone `checker.py` uses only the Python standard library. Invoke `python3 checker.py` and check that it prints a PASS count.

The checker computes fixed-arclength chord integrals from first principles, forms centered finite-difference derivatives and compares their Fourier coefficients against the claimed multipliers. It also tests multiplier nonvanishing at many odd orders and integer cyclotomic norm identities. Numerical discretization errors are bounded by the stated tolerances on these finite cases. Neither these finite checks nor this review independently certify the infinite theorem. The key infinite claims rely on the written cyclotomic argument and analytic inverse-function theorems.

Limitations: numerical examples are non-exhaustive; unpublished work may anticipate the theorem; the result assumes near-circle convexity, closure and odd-denominator rational perimetral separation. Independent mathematical audit has not been performed.
