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

# Reproducibility and scope

The full argument is the coordinate formula and strict-diagonal-dominance maximum principle in `RESULT.md`. The finite checker is corroboration, not an exhaustive argument over arbitrary real Gram matrices.

Run `python verify.py` in a Python environment with SymPy. The checker uses exact rational arithmetic for 60 positive-definite rational Gram matrices from invertible integer generators, 420 sample points, 31,500 individual face projections, two exact three-dimensional Gram-volume-ratio examples, and two empty-kernel instances. It raises an exception upon failure and prints `PASS` upon success.

The first-public dates of both cited motivating sources were checked against their arXiv version-one submission histories on 10 November 2026. The motivating theorem gives the all-face kernel definition but does not imply a tiling theorem above dimension three.

There has been no independent mathematical or priority audit.
