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

# Reproducibility of the finite checks

Run `python verify.py` using Python 3 (stdlib only). The script independently generates the rotating-memory recurrence rather than inferring its terms from the closed form. For all \(2\le k<\ell\le42\), it checks predicted positive-value intersections, pairwise synchronized indices, the exact cardinality formulas, and their exceptional cases. It also compares recurrence-generated terms against the explicit factorization at 77,859 parameter-index positions. Exact arbitrary-precision integer arithmetic is used.

These are finite corroborative calculations. The infinite-parameter result follows from the proof in RESULT.md, especially prime-factor uniqueness and the exhaustive integer intervals for common floor quotients. Neither finite testing nor a negative database search independently certifies the theorem's priority. The experiment requires no external dependencies or inputs.
