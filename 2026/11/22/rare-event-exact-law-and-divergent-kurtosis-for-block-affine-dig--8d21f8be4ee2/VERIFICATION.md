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

# Mathematical verification

The exact law reduces every suffix digit to one uniformly sampled \(em\)-bit linear form. The zero form occurs with probability \(1/N\); nonzero forms average exactly \(1/2\) over the full input cube. Independent random matrices and shifts make the rare signed terms independent across all suffix bits. Elementary geometric-series moment calculations then establish the exact variance and fourth moment, and a geometric first-activation time proves the limiting logarithmic law. The fully nested counterpart is the average of \(N\) independent centered uniform jitters.

The included standalone exact-rational `verify.py` was executed against its actual embedded source prior to delivery and printed `VERIFY_OK 96`. It checks full finite-suffix probability laws, finite second/fourth moments, explicit binary row enumeration, and exact algebra at six sample sizes. Those finite checks do not constitute an infinite proof. The argument uses complete, infinite-digit scrambling and fixes \(f(x)=x\); it does not describe finite-precision approximations, general function classes, or independently audited mathematical correctness.
