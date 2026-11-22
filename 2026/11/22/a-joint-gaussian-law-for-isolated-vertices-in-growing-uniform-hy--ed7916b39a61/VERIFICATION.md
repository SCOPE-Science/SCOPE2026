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
# Reproducible checks

The accompanying `checker.py` uses the standard library only. Running it produced `PASS: 1412 exact arithmetic assertions` and the exact limiting coefficient `41/224` for \(k=3,p=1/2\). It checks exact finite-time Markov kernels and symbolic-equivalent covariance identities for rational inputs; its finite-time assertions do not establish an asymptotic theorem.

With NumPy installed, `simulation.py` implements conditional uniform sampling among unused hyperedges by rejecting old non-isolate-only subsets. In a seeded run (16,000 independent replicates of 1,200 steps), the three covariance matrices had maximum relative errors of 0.015855, 0.002605 and 0.015727 against the derived limiting coefficients. Such a check cannot prove limit laws.

Analytic verification is provided in `RESULT.md`: an exact transition kernel, a stabilized isolation contrast, summable duplicate-selection corrections, bounded fourth moments, a weighted martingale CLT, and an invertible covariance transformation. The infinite claims rest on those arguments. Independent external validation has not been performed.
