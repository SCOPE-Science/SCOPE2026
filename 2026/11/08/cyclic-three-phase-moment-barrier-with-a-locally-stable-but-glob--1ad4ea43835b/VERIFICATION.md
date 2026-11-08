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

The proof is analytical and does not depend on a finite search. The standalone `verify.py` reproduces exact symbolic polynomial identities, the local quadratic coefficient, the two-profile difference, the rational strict witness, and 30 additional exact-rational samples.

Run `python verify.py` with SymPy installed. The script reports PASS only after all assertions finish. The omitted cases of arbitrary three-state Markov generators, general Runge--Kutta tableaux, and global optimality for return probabilities below the stated benchmark crossing remain unproved. Only the specified cycle, its continuous positive holding-time parameters, and its explicitly defined boundary limit are covered.
