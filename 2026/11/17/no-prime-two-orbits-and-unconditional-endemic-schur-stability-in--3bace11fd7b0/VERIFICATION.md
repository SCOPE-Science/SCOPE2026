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

# Verification of the mathematical statement

The comparison recurrence is checked directly from the published transition probabilities at the one-stage endpoint. The proof does not rely on floating-point root searches: the two-cycle impossibility is a global sign contradiction and the example is verified with rational arithmetic. Differentiation of the competing-risk response and the Schur--Jury inequalities are shown explicitly in `RESULT.md`.

Run `python checks/check_one_stage.py` with Python 3 (standard library only) to reproduce the exact rational cycle, the bump-normalization comparisons, and bounded numerical tests of the incidence derivative, absence of a \(-1\) eigenvalue, positive equilibrium equation, and stability inequalities. The script is finite diagnostic evidence, not a theorem prover and not an exhaustive search. No independent review has been performed.
