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

# Reproducibility and scope

Run `python checker.py` with Python, NumPy and SciPy installed. The checker implements the Gaussian Markov integrated-variance formula and independently integrates a covariance-matrix Schur complement over a grid. It also compares random feasible sensor gaps, selected unconstrained numerical optimizations, and short- and long-range asymptotics. Its fresh execution passed 1,192 assertions. This is a finite numerical diagnostic, not an infinite proof, formal certificate, independently audited result, or exhaustive historical-priority verification.

The complete analytical proof is in `RESULT.md`: strict convexity gives unique global optimality; an explicit positive derivative gap proves strictly shorter terminal margins; Taylor and exponential asymptotics give both limits. The physical model assumes known deterministic mean, known stationary exponential covariance and noiseless observations; its geometry is one-dimensional. Source comparison included a full accessible arXiv paper that fixes the endpoints, while the 2010 exact-design full text was not available. Review remains same-model only.
