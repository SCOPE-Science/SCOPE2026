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

# Reproducibility and verification

Run the standalone `verify.py` with Python 3.9 or later and NumPy. The executable checks exactly integrated Fourier coefficients of finite unions of grid arcs, randomized disjoint three-color partitions, explicit both-branch extremizers, the acute Gram supporting plane, and the two-block matrix commutator normalization. The observed execution output was:

```
PASS: 12316 finite checks; global sharp determinant=0.065810039231830
```

The proof in `RESULT.md` is analytic: the circle Fourier cap follows from rearrangement, the sharp area inequality from square-root determinant concavity, and the constructive equality from circular arcs. Numerical checks are finite and do not establish an infinite-dimensional, ultrafilter, or all-measurable-event assertion independently. No separate independent audit has been performed.
