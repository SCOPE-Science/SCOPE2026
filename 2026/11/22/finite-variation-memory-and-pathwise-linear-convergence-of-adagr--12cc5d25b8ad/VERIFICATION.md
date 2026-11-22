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

# Verification notes

The source-order update used in the proof and checker is: sample the gradient at the current iterate; add its squared change relative to the immediately preceding sampled gradient; compute the positive weight; then apply the gradient update. Initial sampled gradient is zero at index \(-1\). No averaging or same-sample gradient-difference substitution is made.

Run the standard-library checker with `python3 verify.py`. Its checks comprise exact rational tests of the stabilized descent inequality and the difference-square inequality, elementary real-valued comparisons for the square-root telescoping step, and reproducible Bernoulli/controlled-curvature trajectories with a variety of step, floor, curvature and activation parameters. The executable tests are finite diagnostics and should not be read as an exhaustive proof or an independent validation. The deterministic argument in RESULT.md supplies the infinite-series conclusion; the strong law of large numbers supplies the almost-sure assertions.

The quantitative terminal convergence rate depends on the random limiting adaptive weight, and the checker does not establish a finite-time uniform numerical contraction constant. Equality at the terminal stability boundary is excluded only for trajectories that never hit zero. This result has not undergone independent mathematical audit.
