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

# Reproducibility and mathematical verification

The complete proof is analytical: spectral-calculus distance reduction, exact cosine-power binomial integration, triangular moment inversion, Chebyshev identity, and at-most-\(2n\)-node Vandermonde uniqueness. This establishes the theorem for all positive integers \(n\), every admissible unitary, and all real \(p\ge1\) claimed in the equivalences.

Run `python verify_inverse.py` using Python 3 standard library. The executed checker reported `PASS: 1637 numerical and algebraic consistency assertions`, comparing phase quadrature to exact gap moments for small sizes, recursively recovering sine sums, validating the Chebyshev relation, and checking equality of the entire sampled profile for noncongruent four-point gap orders. All finite numerical checks have finite precision and are diagnostic only, not a proof of any universal claim.

No independent mathematical audit or independent publication-priority certification has been conducted. The information-limitation example cannot be overcome by increasing the number of exponent samples because the exact gap formula holds for every real exponent.
