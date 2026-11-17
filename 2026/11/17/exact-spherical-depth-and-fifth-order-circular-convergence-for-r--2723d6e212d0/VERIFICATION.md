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

Run the accompanying `verify.py` with Python 3 (standard library only). The completed run printed:

```
PASS: 10706 checks; n=3 probability=0.516435381445; n=5=0.499054315984; limiting coefficient=2.536695079010
```

The script compares the elementary closed formula against a separate quadrature evaluation of the underlying band probability for ten odd polygon orders. It independently enumerates favorable sector differences for more than ten thousand offset pairs, checks the triangle specialization against the published exact value, computes the quartic-convolution coefficient using `fractions.Fraction`, and checks convergence to the predicted leading coefficient.

These finite, numerical, and exact-fraction calculations corroborate separate steps. They are not an exhaustive proof for arbitrarily large side counts; Steps 1–5 of `RESULT.md` are the unrestricted analytic argument. The script uses double precision and is not intended as a high-order precision evaluator for arbitrarily large polygons, where the logarithmic expression has cancellation.
