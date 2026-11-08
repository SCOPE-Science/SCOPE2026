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

# Verification and scope

Run `python3 check_simplex.py` using Python 3 standard library. The check performed on the packaged script yielded `PASS: 138033 exact-rational assertions (dimensions 3 through 7)`.

The code verifies the centered regular-simplex Euclidean orthogonal projection against the barycentric reset formula with rational arithmetic; exact periodic witness vectors; all cyclic orders for small dimensions; the proposed one-step gap matrix; and representative trajectories with positive-coordinate ties. It does not prove the result for all dimensions or certify prior-art priority. The all-dimensional assertions rest on the explicit geometry and primitive finite-dimensional Markov matrix proof given in `RESULT.md`.

The source was inspected through the full published article, including its 2D definition and final higher-dimensional question. The related indexed 2D claim was available as a ranked summary; its full package was not accessed. Publication-priority residual risk is explicitly recorded in the review.
