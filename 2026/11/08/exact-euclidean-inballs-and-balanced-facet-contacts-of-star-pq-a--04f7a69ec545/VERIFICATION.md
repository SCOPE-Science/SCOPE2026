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

Run `python check_pqstar.py` with Python 3, NumPy and SciPy. The checker constructs each original ordered-pair vertex, determines the affine tangent space by an orthonormal null-space basis, and projects all claimed facet normals into that space. For \(1\le m\le12\) it solves an unrestricted-center Euclidean inball linear program and compares its optimal radius with the exact expression. It separately counts facet contacts at the proposed center. For \(m\le4\) it computes hull hyperplanes directly from the vertices and repeats the independent radius optimization.

Recorded executed outcome: `PQ_STAR_INTRINSIC_INBALL_LP_CHECKS_PASSED 12`.

Floating-point tolerances in the checker are not rigorous certificates for arbitrary \(m\); the proof in `RESULT.md` handles every integer \(m\ge1\) independently of these computations. No independent audit has been performed.
