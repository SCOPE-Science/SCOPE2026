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

The exact checker `verify_panhandle_two_faces.py` independently constructs incidence vertices from the panhandle basis restriction. It forms all supporting coordinate faces and the tail-cap face, closes under intersections, and computes exact affine ranks by rational row reduction. Two-face vertex counts are compared with the closed formulas, without using those formulas to construct or identify faces.

Command: `python3 verify_panhandle_two_faces.py`.

Observed pass marker: `PANHANDLE_TWO_FACE_EXACT_PASS cases=8 algebraic_parameter_checks=315`.

The eight tested triples were \((p,t,r)=(2,2,2),(3,2,2),(3,3,2),(3,3,3),(4,2,2),(4,3,2),(4,3,3),(4,3,4)\). The checker also evaluates two independent combinatorial identities for 315 further integer parameter triples.

A fixed-rank asymptotic expansion and a derivative-based global optimum argument are provided symbolically in the proof. They apply beyond the finite test set and are not certified by finite enumeration alone. No independent validation has been performed.
