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

Run `python checks/verify_inverse.py` from the package root using Python 3. The checker has no external dependencies. It enumerates inverse points both by the explicit phase/quadratic construction and by interval monotonic-phase counts; these separate calculations agreed for 270 parameter/target/cutoff cases. Direct substitution and the exact determinant formula were checked at 21,424 regular preimages. Additional tests covered the inclusion of exact critical phase levels and three shrinking-cutoff tests for each of five phase regimes.

The standalone code is evidence of consistency for finite inputs, **not** an infinite proof. The proof in RESULT.md separately shows the phase list is exhaustive, that the positive quadratic root is unique, that exactly the phase levels \(0<\zeta\le b\pi\) reach \(x=0\), and that every branch contributes the claimed integer count and transport rate. Computation precision is finite and cannot independently certify all real parameters or uniform constants. No independent mathematical audit has been performed.
