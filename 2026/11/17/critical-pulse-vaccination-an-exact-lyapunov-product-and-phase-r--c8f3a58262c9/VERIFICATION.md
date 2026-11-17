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

The exact weighted-logarithmic derivative is verified symbolically in `check.py`, after substituting the critical identity \(\delta=\beta(A+\log q/T)\). The script also integrates three positive trajectories with distinct positive parameters to check positivity, the exact reciprocal-product period identity (using numerical quadrature), the infection coefficient at phases \(0\) and \(T/2\), and the leading post-pulse susceptible correction. Each numerical trajectory has 3000 completed periods, using fourth-order Runge–Kutta with 40 steps per period.

Reproduce with `python check.py` (Python 3, SymPy, mpmath). The check prints the observed and predicted values and asserts explicit finite tolerances; convergence can be slow and the finite tolerances are not certified asymptotic error bounds. The proof in `RESULT.md` is responsible for all infinite-time statements. The pulse-continuity identity, global positive susceptible floor, and all quantified phase limits are analytic. No independent audit has been performed.
