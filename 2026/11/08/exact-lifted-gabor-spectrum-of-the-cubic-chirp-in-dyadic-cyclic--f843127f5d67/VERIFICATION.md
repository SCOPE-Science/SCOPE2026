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

# Verification of the dyadic cubic Gabor lifting spectrum

Run `python check_dyadic_cubic.py` with Python 3 and NumPy. On each modulus 2, 4, 8, 16, 32, 64, 128, the checker recomputes each quadratic ambiguity coefficient as an integral polynomial in the primitive root of unity; exact vanishing follows from the coefficient-pair test against the cyclotomic polynomial \(X^{N/2}+1\). It compares every zero to the proposed valuation criterion and the complete multiplicity histogram.

For dimensions through 32, it independently evaluates every complex ambiguity sum numerically. For dimensions 2, 4 and 8, it constructs all Gabor rank-one projectors and diagonalizes their actual full Gram matrices. Every check passed on the packaged copy.

The terminal success marker is `DYADIC_CUBIC_GABOR_CERTIFICATE_PASS`. Exact finite checks confirm the enumerated finite cases only; the proof in RESULT.md establishes arbitrary dyadic orders. No independent external mathematical audit has been performed.
