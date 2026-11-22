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

The analytic proof uses a standard Stieltjes-to-complete-Bernstein reciprocal representation, Fourier coefficients of a shifted discrete Laplacian resolvent, and two applications of a lattice maximum principle. Its strict inequality depends on the mixing law having more than one support point.

`checker.py` uses only Python's standard library and exact rational arithmetic. It checks finitely many mixing laws, degrees, harmonic spacings, extreme rays, and interior cone points. This is supplemental verification, not certification of the infinite theorem. The explicit three-knot example was independently recomputed from the exact matrix.

Limitations: no assertion for mixing support approaching the endpoints without further summability hypotheses; no signed mixing measures; no independent external mathematical or priority review.
