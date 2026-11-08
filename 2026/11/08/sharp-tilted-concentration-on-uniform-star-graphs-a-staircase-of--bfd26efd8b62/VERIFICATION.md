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

The exact theorem concerns the maximization, for every integer \(n\ge3\) and every real tilt \(t\), of the centered exponential moment over **all** real one-Lipschitz functions on the unit-edge star with uniform vertex probabilities. It is proved in `RESULT.md` by strict convexity on the leaf cube, the monotone ratio of consecutive signed-leaf profiles, the derivative-sign inequality for the threshold function, and a direct limit calculation. The infinite quantifiers rely on the written proof, not enumeration.

The included `scripts/check_star_laplace.py` is executable using standard Python only:

```sh
python scripts/check_star_laplace.py
```

The checker enumerates all sign choices for small stars and compares the predicted maximal signing counts with exact rational moment expressions at 77 rational exponential tilts. For such a tilt, \(t=(n+1)\log r\) with positive rational \(r>1\), all centered moments are rational. It additionally checks the small-tilt parity law exactly for 199 star sizes, samples the monotone optimizer count for 26 sizes, and compares fixed-tilt large-star values to the analytical limit at five tilt values. Exact enumeration is limited to the stated small instances, and floating-point sampling does not certify global monotonicity. The proof's hyperbolic-identity argument certifies monotonicity for all orders and tilts.

No external verifier or independent review has been performed.
