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
# Reproduction and limits

Run `python verify_line_tubes.py` with Python 3, NumPy and SciPy. It evaluates the inverse-chord integral for ellipses and performs a separate numerical Crofton sampling diagnostic on circular tubes. Finite checks do not prove the r-to-zero limit: the proof is the curvature-controlled lens and averaged-shadow argument in RESULT.md. The tested circle uses a Euclidean-invariant direction/offset law and explicit quartic line intersections; the numerical uncertainty is sampling uncertainty. Independent audit has not been performed.
