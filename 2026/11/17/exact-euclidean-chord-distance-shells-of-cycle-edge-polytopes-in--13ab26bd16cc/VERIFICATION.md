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

# Reproduction and proof boundaries

Run `python checks/cycle_hypersimplex.py` from the package root with Python 3 and `numpy`/`scipy` installed. The exact-rational component needs only the Python standard library. The script checks all unordered pairs of hypersimplex vertices for every integer order from 3 to 40, with rational convex weights, residuals, and variational inequalities. It checks the complete distance-level multiplicities and that the farthest vertices have pairwise distinct residuals. A separate numerical constrained optimization phase compares the formulas for 219 instances of orders 3 through 11.

Observed successful output:

`CYCLE_HYPERSIMPLEX_PASS exact_pairs=10659 independent_qps=219 max_squared_gap=1.01e-14 farthest_residuals_distinct=PASS`

The exact mathematical argument is the finite-form variational projection certificate with a uniform case distinction; the program's finite tests are consistency checks, not proofs for unbounded dimension. The residual vectors, support conditions, equality cases, and farthest-point variance argument are given explicitly in the proof. No independent mathematical audit is claimed.
