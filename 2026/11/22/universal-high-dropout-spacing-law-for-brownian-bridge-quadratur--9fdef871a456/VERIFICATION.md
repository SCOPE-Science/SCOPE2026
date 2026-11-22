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

The independent audit has not been performed. The scientific claim concerns expected posterior mean-square error under independent Bernoulli sensor dropout, a Gaussian Brownian-bridge process, and exact observations when available.

Execute `python verify_dropout.py` after installing dependencies from `requirements.txt`. The verifier computes rational covariance checks, confirms the exact two-sensor first-order stationarity equation, and compares small-network numerical optimizers to the derived high-dropout limits. It does not prove the limiting theorem through finite enumeration; the full analytic argument is in `RESULT.md`.

For each survivor subset the exact conditional risk is the sum of cubes of its consecutive observation gaps divided by twelve. Strict convexity follows from the all-active event, and the asymptotic proof uses uniform order-three expansion after proving the optimal locations are within order \(1-q\) of the midpoint. Repeated positions are allowed at the optimization stage and no extra information is attributed to redundant coincident exact readings.

The mathematical and literature comparisons have received self-review only. Historical-priority and independent mathematical verification remain open.
