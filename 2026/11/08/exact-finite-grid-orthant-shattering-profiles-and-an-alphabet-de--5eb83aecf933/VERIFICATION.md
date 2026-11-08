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

# Reproducibility

Run `python verify.py` using Python 3 with its standard library. The program constructs the concepts from their actual threshold definition, evaluates every Boolean trace on all supports of size up to one beyond ambient dimension in eleven small grids, separately tests the private-coordinate criterion, and compares all support counts to the inclusion–exclusion formula.

The observed terminal status is `ALL_ANCHORED_ORTHANT_PROFILE_CHECKS_PASS 11`. Examples separately checked include profiles \(1+4z+z^2\) for the Boolean square, \(1+8z+9z^2+z^3\) for the Boolean cube, and \(1+27z+162z^2+125z^3\) for a three-level three-dimensional grid.

These finite calculations are confirmatory only. The all-grid identity, the exact distribution at finite parameters and its universal limiting law are established by the explicit combinatorial and analytic proofs in RESULT.md. Full historical priority and independent scientific audit have not been established.
