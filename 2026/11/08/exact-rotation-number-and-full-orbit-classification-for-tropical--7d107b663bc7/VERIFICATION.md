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

Verification of the mathematical claim uses the direct piecewise-affine case analysis, the exact four-quadrant area integrals, and the area-conjugacy argument in `RESULT.md`. They are analytic proofs for all positive real parameters with \(pq<4\); no finite enumeration is treated as a universal proof.

The accompanying standalone `verify_rotation.py` uses only Python's standard library. Invoking `python verify_rotation.py` produced `TROPICAL_ROTATION_EXACT_AND_AREA_CHECK_OK 22756`. The program exactly checks seven rational parameter pairs and rational starts over all signs, their invariant values and primitive periods, and corroborates analytic area and ray-angle formulas with numerical quadrature at five asymmetric real parameter pairs. These are supplementary checks; floating-point agreement does not establish infinite or exact identities.

The first-public source date used for the originating mutation is 2021-09-14, according to the initial arXiv submission of arXiv:2109.06927; the journal publication date is later. The original paper's invariant and special-period theorems are attributed as prior literature. The independent audit status is not performed.
