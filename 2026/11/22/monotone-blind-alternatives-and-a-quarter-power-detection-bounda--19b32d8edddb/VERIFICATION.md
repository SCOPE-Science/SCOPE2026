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

## Reproducible checks

Run `python VERIFY_CODE.py` with SymPy installed. The checker passes 18 exact-arithmetic assertions covering the two exact representations of the population target, the monotone blind family, the rational example, the first-projection variance, and the finite-sample order-statistic identity.

The statistical limit claims are justified by bounded-kernel Hoeffding decomposition, a triangular-array Lindeberg theorem, and the continuous mapping theorem, as detailed in `RESULT.md`. Polynomial tests do not certify those infinite-sample conclusions. Independent mathematical audit has not been performed.
