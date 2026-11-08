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

# Verification of the exact founder-site switch

The theorem has a symbolic analytic proof in `RESULT.md`. The standalone Python script `founder_check.py` uses exact SymPy rational algebra for the endpoint-middle elimination, critical quadratic and displayed witness. It uses SciPy's nonlinear solver to cross-check 120 migration-rate comparisons and additional points in admissible parameter cones. The command `python founder_check.py` completed with status zero and printed `PASS: exact polynomial/root identities, 120 rate-grid comparisons, and parameter-cone tests`.

The finite numerical cases are not a proof of uniqueness or the universal ordering; those statements follow from a maximum-ratio uniqueness argument and the crossing polynomial plus continuity. The environment requires Python 3, NumPy, SymPy and SciPy. Neither the proof nor the checker verifies priority among all earlier publications. No independent audit has been performed.
