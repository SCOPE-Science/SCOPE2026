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

The analytical proof is in `RESULT.md`. To reproduce independent checks from the accompanying source, run `python3 check.py` with Python 3 and no third-party packages. The code recursively enumerates each triangulation for \(5\le n\le11\), compares every ear marginal and pair frequency with Catalan probabilities using exact fractions, and matches the exact count variance with the constant Fourier eigenvalue. It checks all sixteen finite rational inequalities needed to separate the crossover at \(n=20/21\), and stress-tests spectral ordering through \(n=1000\). The recorded execution returned `PASS 6100 assertions`.

The proof for all \(n\ge21\) is symbolic: the polynomial \(147t^3+5389t^2+49281t+359\) has strictly positive coefficients for \(t\ge0\). The sharp all-size conditioning bound comes from exact rational monotonicity and case separation, not sampled data. Numerical spectral loops in the script are corroborative only. No independent mathematical audit or external formal certification has been performed. Historical novelty remains subject to independent priority checks.
