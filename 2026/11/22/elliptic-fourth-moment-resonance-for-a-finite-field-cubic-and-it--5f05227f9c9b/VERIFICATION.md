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

# Reproducibility and limits

The accompanying `verify.py` enumerates the exact support, the ordered twofold convolution at every target, and the resulting additive energy for fourteen prime fields and four quadratic extension fields. For all extension fields of prime characteristic greater than three, it also checks the elliptic trace relation for the quadratic extension. Run `python3 verify.py`; the observed output is:

```
VERIFY_OK prime_cases=14 quadratic_extension_cases=4 exact_fibers=yes max_order=121
```

All checks use exact finite-field integer arithmetic, not floating-point approximations. No enumeration can certify the theorem for arbitrarily large field orders; this follows from the discriminant calculation, character sums and characteristic-three subgroup argument in `RESULT.md`. The stated source dates are earliest public preprint dates rather than journal or revision dates. An external independent mathematical audit has not been performed.
