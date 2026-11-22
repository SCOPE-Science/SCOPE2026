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

Reproduction: run `python checker.py` using NumPy and SciPy. The supplied source evaluates Poisson power sums independently against a closed-form influence covariance, verifies its sparse expansion, checks the exact finite-sample expectation, and simulates the three null regimes using count histograms. A completed run returned 164 passing assertions, including the critical-level check (theoretical 0.139292; simulated 0.134556).

The mathematical limits follow from the explicit influence-function expansion, Lyapunov theorem, and binomial-to-Poisson convergence. Finite simulations alone do not certify convergence, optimality, literature priority, or independent review. The checker uses eight count levels plus a tail bucket and enforces an expected omitted-count bound of \(10^{-8}\) in its simulation scenarios.
