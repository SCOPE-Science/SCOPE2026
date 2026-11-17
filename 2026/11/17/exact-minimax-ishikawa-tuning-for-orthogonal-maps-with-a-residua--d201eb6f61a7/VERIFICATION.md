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

The mathematical proof uses a normal-operator spectral reduction, a complete parametrization of the degree-two probability polynomials, a two-endpoint lower certificate, and explicit saturating real rotations. Neither endpoint optimization nor infinite-dimensional spectral calculus is inferred from sampling.

The accompanying `verify.py` checks exact rational formulas and endpoint inequalities over many rational spectral gaps, followed by reproducible numerical samples of competing coefficients and unit-circle phases. Run with `python3 verify.py` (Python standard library only). Passing tests are supplementary rather than an exhaustive continuum certificate. Universal correctness rests on the proof in `RESULT.md`.

A publication-priority limitation remains: the full text of the motivating 2026 article could not be read through accessible routes; only its indexed abstract, metadata and reference list were compared. Independent audit and independent validation have not been performed.
