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

# Reproduction and mathematical boundaries

Run `python verify.py` with SymPy installed. The executable verifies the exact Beta/Gamma constants, quadratic convexity, sharp power-weight integrability threshold, and the angular coarea exponent. Its observed output was:

```
Radial constants, convexity, critical exponents and spherical kernel: PASS
```

The general proof is analytic. In particular, the checker does not exhaust all integrable functions, directions or dimensions; those universal quantifiers are discharged by the explicitly stated coarea estimate and convexity/Fourier-slice uniqueness arguments in RESULT.md.

The primary source was first public March 11, 2026 (arXiv:2603.10804v1). A later November 17, 2026 paper was compared for coverage, including its planar example and its weighted Fourier estimate. No expert or independent audit has been conducted.
