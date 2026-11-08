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

The proof is self-contained in RESULT.md. Run the included file `verify_price.py` using `python3 verify_price.py`. It uses Python's standard library only, produces a PASS line on success, and checks exact rational finite-\(k\) welfare identities, an independent beta-integral expression for uniform top-\(k\) expected quality, positivity and exact two-/three-candidate covariance values, direct finite-grid optimization, and fixed-seed numerical Monte Carlo checks. The exact deficit variance for two candidates per group is \(1/72\), and the corresponding limiting quality-ratio variance is \(52/2187\).

The checked finite grid uses quantized qualities to test only the optimization identity; it does not imply that these discrete profiles satisfy the continuous-distribution asymptotic hypotheses. The numerical experiments are reproducibility tests and do not prove probability limits. Strong-law and central-limit conclusions are justified by the top-\(k\) variational identity, local quantile concentration and the iid-bloc CLT in the proof. For full numerical reproducibility, use Python 3.9 or later; no external data, private files or network access is required.

Originality comparisons are limited by incomplete access to a recent closely related manuscript. The self-review does not constitute independent verification.
