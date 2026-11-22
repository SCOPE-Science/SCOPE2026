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

The one-coordinate stationary Gaussian proof explicitly includes the correlation between the earliest active-work Itô noise and the later work drift; this term is indispensable to the thermal-noise threshold. The Lyapunov covariance, semigroup, pair-contraction identity, and resulting two-exponential kernel are all stated in `RESULT.md`.

`check.py` uses only the Python standard library. It tests the fourth-moment covariance by explicit Gaussian contractions with exact-rational numbers for independent exponential monomials, the exact resonant propagator, the finite-time Green–Kubo variance-rate limit, and the positive/negative-lag phase regimes. A clean execution from the embedded file reports 1,039 passing assertions.

The extrapolation from finite tests to every \(\kappa>0\), \(A>0\), \(D\ge0\), and \(t>0\) comes solely from the analytic semigroup and sign proof. The two published primary sources study related integrated-work fluctuations; one full preprint was materially inspected, while the earlier preprint was available only through its public abstract. An implicit prior occurrence of this finite-lag law has not been conclusively excluded.
