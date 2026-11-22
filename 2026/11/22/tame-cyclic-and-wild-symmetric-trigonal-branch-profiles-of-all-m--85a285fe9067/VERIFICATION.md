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

The embedded program `verify_filling43_branch.py` is standalone and requires only Python 3 and SymPy. From the extracted package directory run:

```text
python verify_filling43_branch.py
```

It exhausts the binary linear space of 2048 filling forms, tests all nonzero forms for geometric smoothness by the four affine Jacobian ideals, computes all 36 ambient coordinate symmetries, and checks the branch polynomials, their factorization, repeated-root criterion, and fiberwise deck transformations for each of four representatives. The expected terminal marker is `FILLING43_RAMIFICATION_VERIFIED equations=2048 smooth=66 orbits=4 cyclic_tame=12 S3_wild=54 branch_cycle_profiles=(8)x3,(2+6)x1`.

The local different exponent is deduced from the explicitly checked branch support and genus-six Riemann–Hurwitz, not inferred solely from finite extension point searches. The conclusion is limited to the first-ruling degree-three covers of the specified geometrically smooth binary filling curves. No independent mathematical audit has been performed.
