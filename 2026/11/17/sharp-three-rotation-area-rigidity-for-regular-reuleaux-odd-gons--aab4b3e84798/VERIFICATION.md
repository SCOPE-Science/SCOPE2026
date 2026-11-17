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
# Verification record

The accompanying `verify.py` is a self-contained Python 3 numerical regression checker. In the completed run it printed:

```
PASS 10692 finite checks; analytical proof required for all parameters
```

Checks independently sum thousands of odd Fourier terms, evaluate the exact closed cosine kernel, test six odd orders, compare all 41-by-41 pairs of discretized phases with the analytic equal-step candidate, and reconstruct the convex boundary using direct curvature-radius integration and shoelace polygon areas. The numerical angular mesh is not exhaustive over the continuum and is not the basis for global uniqueness.

The all-odd-order proof is in `RESULT.md`: support-function Fourier identity, closed analytic pair kernel, strict global gap minimization (including boundary collisions), exact positive residual harmonic, and nondegenerate local second variation. The researcher's self-review is recorded in `REVIEW.md` and `AUDIT.json`; there has been no independent audit or independent formal certification.

The formulas concern only equal-weight triple means of regular Reuleaux odd-gons. Unindexed older overlap remains possible.
