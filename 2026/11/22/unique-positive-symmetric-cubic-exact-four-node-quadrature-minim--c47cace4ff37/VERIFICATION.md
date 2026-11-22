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

# Reproducible verification and boundaries

Execute `python3 check_quadrature.py` with Python 3; the optional four-point Gauss benchmark additionally uses SciPy. The program uses `fractions.Fraction` to verify a rational bracket for the unique algebraic root, verifies the four cubic moment equations numerically at high precision, checks two exact-discrepancy step witnesses, samples admissible rules and the analytic moment envelope, and independently computes the Gauss-Legendre benchmark.

Expected terminal marker: `ALL_FOUR_NODE_MOMENT_DISCREPANCY_CHECKS_PASS`. An actual successful execution also reported 12,827 admissible rules among 35,000 random parameter draws and completed 10,000 moment-envelope checks. These checks supplement the self-contained universal analytic argument in `RESULT.md`. They do not establish uniqueness or all-parameter inequalities by exhaustive computation.

The mathematical result applies only to centrally symmetric nonnegative at-most-four-node formulas that integrate cubic polynomials exactly. The close 1991 article on BV quadrature error could not be read in full, and historical priority remains qualified. Independent audit has not been performed.
