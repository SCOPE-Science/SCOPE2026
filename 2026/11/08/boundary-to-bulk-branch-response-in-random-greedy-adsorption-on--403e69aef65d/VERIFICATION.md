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

# Verification and reproducibility

The complete analytical derivation is in `RESULT.md`. To reproduce the finite verification with Python 3 and its standard library only, execute `python3 verify.py`. The observed output on the packaged version was `VERIFY_OK 62 exact comparisons and limiting-value tests`.

The program implements a direct first-arrival recursion on vertex-induced residual graphs, checks the bivariate Taylor coefficient formula with rational arithmetic for the 36 pairs of arm sizes 0 through 5, and independently enumerates all vertex permutations on additional small graphs. It tests decreasing coefficient magnitudes at finite orders and numerically checks high-order approach to both analytically derived limits. The infinite coefficient bounds, convergence claims, strict minimization and constants are proven in the manuscript; none is extrapolated from the finite run.

Historical priority is qualified, and this verification does not constitute an independent audit or a computer-assisted proof of infinite statements.
