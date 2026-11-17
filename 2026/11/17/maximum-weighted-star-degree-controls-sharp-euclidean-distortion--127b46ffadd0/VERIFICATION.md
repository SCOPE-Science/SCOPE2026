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

The exact theorem and critical Jacobian argument are in `RESULT.md`. Run `python checker.py` with Python 3 and NumPy. The checker is standalone and deterministic; it requires no external files, network services, or downloaded data. It re-enumerates 4,754 graph/weight configurations and 31,079 chamber Jacobians, compares forward/inverse matrix norms against the radical formula, checks 9,508 point pairs and 4,732 local sharpness witnesses, and tests 116 additional weighted stars.

Expected success output:

`TRANSFER_STABILITY_PASS graphs=4754 Jacobians=31079 interior_pairs=9508 sharp_witnesses=4732 weighted_stars=116`

The proof covers every finite height-two poset and all real interpolation parameters in the unit interval; finite sampling and floating-point singular values do not independently certify the infinite mathematical statement. No independent audit is represented here.
