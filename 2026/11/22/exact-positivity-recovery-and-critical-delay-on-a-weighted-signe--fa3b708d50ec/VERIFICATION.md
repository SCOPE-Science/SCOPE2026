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

# Reproducibility notes

The analytic verification is contained in `RESULT.md` under **Proof**, including the spectral-projector identity, zero-count argument, sign census, norm peak, and endpoint asymptotics. To repeat the finite supplemental checks, run:

```sh
python3 check_signed_triangle.py
```

The checker uses only the Python standard library. It verifies the quadratic minimal-polynomial identity in exact rational arithmetic for four sample triples, independently computes the matrix exponential via scaled Taylor series and squaring for sixteen stable parameter configurations, compares selected entries and sharp induced norms at five times per configuration, and probes the near-critical limit for three perturbation sizes.

The observed standalone result is:

`PASS: four exact rational identities, 16 parameter configurations, five time samples each, and three boundary probes`

Finite samples cannot verify an infinite-parameter theorem, and no formal proof-assistant or independent mathematical review is claimed. The algebraic and analytic arguments in the main result are the actual basis of correctness.
