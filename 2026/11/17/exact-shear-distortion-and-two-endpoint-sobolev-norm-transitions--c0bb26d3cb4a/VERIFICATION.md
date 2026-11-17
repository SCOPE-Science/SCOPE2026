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

The derivation is self-contained conditional on the classical Ornstein same-order \(L^1\) non-inequality, whose published proof was inspected. At each derivative level the chain-rule coefficients are triangular binomial coefficients, with exact column sums \(P_{j,s}(q)\). The top-order coefficient is attained as a supremum via Ornstein derivative-concentrating tests and dilation; no individual extremizer exists for nonzero shear.

Run `python3 check_shear.py` using Python 3 standard library. It checks rational coefficient matrices and column sums, all levels through order eight over a rational grid, strict domination by the top order, and piecewise formulas for orders two and three. Finite tests are **not** a proof of the continuous all-orders statement, of the existence of the Ornstein test sequences, or of publication priority.

The mathematical scope is the real \(W^{k,1}(\mathbb R^2)\) norm with each weak partial derivative up to order \(k\) counted exactly once. No independent audit has been performed.
