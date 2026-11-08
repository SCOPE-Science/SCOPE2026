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

The theorem follows analytically by reducing unilateral stability to an exact inequality for the number of opposing actions in each part. A mixed part forces equality; separating profiles with zero, one, and multiple mixed parts gives the complete exhaustive classification and exact counting formula. Tripartite parity follows by substituting three parts. Global welfare optimality follows from coordinate-wise affinity of the cut-size polynomial; the even-size frequency estimate follows from the central-binomial asymptotic.

Run `python3 verify.py` in the same directory as `RESULT.md`. The included standard-library verifier compares the closed formula with an independent occupancy-vector enumeration at 34 parameter pairs. It also exhaustively enumerates labeled binary profiles and tests individual actual neighbor payoffs for 17 smaller instances, and checks tripartite formulas at 11 orders. It prints `VERIFY_OK macro_cases=34 labeled_cases=17 tripartite_formula_cases=11`. These checks were executed against the supplied verifier; only the analytic argument proves unbounded orders. The implementation does not certify originality, dynamic convergence, or robustness to unequal edge weights. No independent mathematical audit has been performed.
