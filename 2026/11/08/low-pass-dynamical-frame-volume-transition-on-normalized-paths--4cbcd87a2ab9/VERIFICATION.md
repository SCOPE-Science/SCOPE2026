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

The reproducibility program `CHECK.py` uses only Python 3 standard-library arithmetic. It evaluates eigenvectors against the normalized-adjacency action and computes separately assembled three-time observation determinants from iterated matrix multiplication on small paths; it also enumerates candidate observation vertices to test the three-mode transition through 251 vertices and the explicit general sufficient bound through 14 low-pass modes.

Run `python3 CHECK.py`. The expected final output begins with `CHECK_OK`. Small numerical deviations use a documented tolerance in the code. This program is not a proof of statements quantified over all path lengths or all numbers of modes; those statements follow from the exact trigonometric inequalities in `RESULT.md`. No external or independent audit has been performed.
