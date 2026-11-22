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

# Reproducibility and limits

The exact finite checker is `verify_fair_pca.py`. Run `python verify_fair_pca.py` without third-party packages. Its successful output is:

```
PASS: 2082 exact checks; n=1..10; six rational parameter pairs; four-block law checked.
```

The code directly enumerates independent fair input spins and evaluates the source's probabilistic rule using `fractions.Fraction`; it does not use a floating-point threshold or fit. It checks selected rational parameter pairs, each site's one-spin marginal, adjacent and distance-two moments, all distinct site subsets through order three at \(r=1/2\), and the four-spin parity moment and all sixteen four-word probabilities at selected ring sizes. The proof of the infinite and arbitrary-ring identities instead uses the exact polynomial conditional response and a finite parity-incidence argument for the fourth moment; no exhaustive enumeration over unbounded ring sizes is claimed.

The review of the written proof is same-model only. No external independent audit was performed. The result does not determine the arbitrary-parameter stationary measure, long-time convergence, or correlations from nonproduct initial states.
