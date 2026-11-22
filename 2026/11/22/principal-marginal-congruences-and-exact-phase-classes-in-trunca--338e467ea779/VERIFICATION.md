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

The standalone verifier `check_margins.py` uses exact modular-exponent arithmetic in a decorated partial-map model. It enumerates each admissible matrix in the indicated finite parameters and tests all defining power-word equations within every common support. Rank-one multiplier tests separate different supports. A union--find congruence closure from one marginal pair confirms that all and only equal-support matrices are identified. The run prints `VERIFY_OK` and `PRINCIPAL_OK`.

The infinite proof is independent of the finite enumeration and uses the explicit Duan--Zhang margin formula, singleton support separation, phase-preserving conjugation, and compatible closure of a single pair. The verifier does not test arbitrary ambient degrees or certify historical originality. Independent audit has not been performed.
