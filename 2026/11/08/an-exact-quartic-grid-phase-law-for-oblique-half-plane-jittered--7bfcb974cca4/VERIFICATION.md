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

The exact-rational verifier `verify.py` has been executed successfully with Python 3 and no third-party dependencies; its output is `PASS: 1742 independent exact-rational assertions`.

Direct per-cell Bernoulli variances were compared with the exact grouped lattice counts for all coprime \(1\le a\le5\), \(a\le b\le6\), multiple positive rational heights and \(n\in\{1,2,4,7,11\}\). The quartic coefficient was tested independently for five rational grid phases over the same slope collection. The one-dimensional lattice-count remainder was checked in finite ranges. These computations are finite diagnostics. The infinite-size, all-slope and irrational-phase results rest on the explicit polynomial-sum identity and coprime lattice-counting argument given in the proof, not on exhaustive enumeration or numerical sampling.

To reproduce the finite checks, run `python verify.py`. This does not constitute an independent scientific audit.
