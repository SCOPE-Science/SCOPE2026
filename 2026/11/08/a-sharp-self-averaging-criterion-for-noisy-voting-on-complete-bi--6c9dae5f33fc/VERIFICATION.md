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

The exact finite-state verifier in `verify.py` ran under Python 3 with standard-library rational arithmetic, reporting 48 stationary count-chain solutions and 714 assertions. It independently solves the Markov stationary equations, compares two-point correlations and total spin variance, and checks monotonicity for fixed total size. The all-size formulas, all parameter ranges and limiting criterion require the symbolic generator derivation and inequalities in `RESULT.md`, not extrapolation from tests. No independently conducted audit has been performed.
