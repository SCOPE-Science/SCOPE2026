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

The analytic proof applies a characteristic-function decomposition for independent centered Bernoulli variables with ranked \(\ell^2\)-normalized weights, followed by a variance-controlled local inverse of the strict threshold. It treats all fixed \(\theta\in(0,1)\) and the full Zipf range \(0\le\rho\le1\).

The independent finite-state enumerators in `CHECK.py` agree on the exact probability mass for each finite weighted sum, including the distinct equality versus strict-exceedance convention. Exact rational moment and cumulant identities match the proof. `python CHECK.py` returned `PASS 1019 exact rational checks`. This is not a numerical proof of any infinite limit.

The general non-Gaussian limit law is proved in the paper's restricted model; the calculation says nothing about original publication priority, independent audit, rates of weak convergence or stopping-time moment convergence. The primary motivating paper's later sections could not be read during this comparison; the historical-priority conclusion therefore carries the explicit residual risk recorded in `REVIEW.md`.
