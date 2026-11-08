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
# Verification

The analytic argument provides a finite-dilation inclusion witness for **each** facet and each query point, and separately proves that all missing translates satisfy a one-facet upper bound. Those two inequalities are exact and require no numerical estimates.

The package includes `check_depth.py`. Executing it with Python's standard library gave:

```text
d=2: 280 exact rational support/query checks at t=3
d=3: 280 exact rational support/query checks at t=4
d=4: 280 exact rational support/query checks at t=4
d=5: 280 exact rational support/query checks at t=5
triangle: 360 exact rational support/query checks at t=4
PASS: 1480 exact finite-support checks and 4 Gaussian strictness checks
```

The finite-support tests include atomic ties, support-boundary points, and query points both inside and outside the support. The non-axis-aligned triangle uses three rational unit facet normals and is tested at the exact sufficient cutoff. All sampled facet inclusions are checked using exact rational arithmetic. Gaussian tests use the positive complementary error function; they do not attempt an exhaustive verification for all dimensions or dilations.

The full theorem is established by the written proof, not by this finite test suite. No independent external review or formal proof assistant verification has been performed.
