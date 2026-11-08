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

The standalone `verify.py` script (Python 3 standard library) reproduces 923 checks. Its tests include independent backwards-equation numerical identities and renewal means over a grid of positive parameters, two distinct absorption probabilities and bound-state means, sign checks on both sides of uniquely computed switching thresholds, and independently simulated first-wall-contact events stopped by a bulk-reset clock.

Run with `python3 verify.py`. Expected output begins with `PASS: 923 deterministic and simulation checks`. The event simulation uses a fixed seed and compares 60,000 paths from the home state and 60,000 paths launched from the wall against analytic hit-before-reset transforms.

These finite checks are not a proof of infinite-parameter statements or of publication novelty. The analytical argument in `RESULT.md` proves the global classification. The verification does not evaluate physical systems with translational thermal noise, correlated wall states, or non-Poisson bulk resetting.
