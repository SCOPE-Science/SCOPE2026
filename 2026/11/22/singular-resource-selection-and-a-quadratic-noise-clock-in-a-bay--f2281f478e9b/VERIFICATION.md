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

# Verification and reproducibility

The proof in `RESULT.md` is the mathematical certificate. The accompanying `checker.py` implements finite consistency checks using only the Python standard library and can be run as follows:

```bash
python3 checker.py
```

It checks exact phenotype-payoff reconstruction for three full-support frequency samples and four perception probabilities; exact rational identities behind the Gaussian large-noise expansion; existence and approach to the interior resource root for several \(c\) and \(\sigma\); the logistic infinite-noise memory formula for nine initial-marginal combinations; and a direct full finite-noise integration against the scaled cubic prediction in a fully specified example. All scripted checks were executed successfully against the packaged version.

The numerical comparisons of finite noise with infinite noise are illustrative and do not establish the uniform-in-time theorems. The proof's strict dominance, covariance monotonicity, integrable fast transient, uniform Taylor remainder and scalar comparison establish the claimed quantified limits.

The time-rescaling statement is deliberately restricted to positive stretched times: a fast initial boundary layer makes convergence at \(\tau=0\) different from convergence uniformly on \([0,T]\). No external independent audit or replication is asserted.
