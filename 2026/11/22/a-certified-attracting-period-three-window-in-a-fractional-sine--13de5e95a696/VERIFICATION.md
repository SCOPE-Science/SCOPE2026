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

# Verification and mathematical limits

Run `python check_certificate.py` using the standard Python library. All assertions must pass; the final line reports certification across the specified rational parameter interval. The checker constructs rational lower and upper bounds for \(\pi\) by Machin's arctangent identity and alternating-series remainders, and for sine/cosine by Taylor polynomials with Lagrange bounds. Rational interval arithmetic verifies the full three-step trapping chain and multiplier bound. No rounded output is relied on to prove an inequality.

For each \(r\) in the closed rational parameter window, the third iterate is strictly contractive on the first rational interval; the strict disjoint cycle locations imply least period three, and the negative multiplier implies local asymptotic attraction. The proof applies to a continuum of real parameters, not merely the finitely many cases displayed by a computational test.

This does not establish the sharp parameter-window endpoints, classify all invariant sets, assess cryptographic quality, or exclude another chaotic attractor. No independent audit has been performed.
