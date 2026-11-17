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

# Reproduction and scope

Run `python verify.py` using Python 3.10 or later. The script imports only standard-library modules, evaluates the fixed-pair constants, uses composite Simpson integration after analytically reducing one angular variable in the small-tail range, checks an independently derived exact cross-polytope coefficient, and compares noncritical exact CDF values against separately generated Haar-uniform sphere samples. Expected final output: `ALL TESTS PASSED`.

The computation checks seven pairs and finite thresholds only. The exact general CDF, the classification of deepest directions, the cubic coefficient and its fourth-order remainder are proven analytically in `RESULT.md`. No inference from a sample to an infinite statement is used. The independent cross-polytope calculation uses the volume of a three-simplex in a tangent hyperplane and supplies a genuinely different local-volume derivation for one special case.
