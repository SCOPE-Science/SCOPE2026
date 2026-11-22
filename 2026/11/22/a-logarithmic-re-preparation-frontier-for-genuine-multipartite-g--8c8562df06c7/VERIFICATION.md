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

Run `python check.py` with Python 3, NumPy and SciPy. The local full-state checks form the independent \(4^n\)-dimensional Markovian Lindblad-plus-reset linear system, solve its trace-one stationary equations and compare the complete matrix to the beta-mixture construction for several small sizes and rate choices. Further checks evaluate Gamma and beta functions, roots of the sharp concurrence threshold, monotonicity, and large-size trends. The script produced `PASS 413 assertions` in the evaluated environment.

The analytic proof does not rely on the checker: uniqueness uses an exact sign of the logarithmic derivative, while the asymptotics use beta concentration and uniform Gamma ratios. Computations cover finitely many parameter combinations and cannot establish a universal statement by themselves. No external independent validation or audit has been performed.
