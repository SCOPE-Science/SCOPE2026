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

# Reproducibility
Run `python3 verify.py` using the Python standard library. The test enumerates every representation in 408 *finite* CRT witness cases, verifies exact congruences and interval bounds, and checks three explicit witnesses. No computation establishes the infinite limit or the prime number theorem. The proof of the infinite claim is in `RESULT.md`.

Expected terminal text ends with:

```
VERIFY_OK finite_only=True analytic_asymptotic_not_computationally_certified=True
```

The statement remains subject to independent mathematical review; none has been performed.
