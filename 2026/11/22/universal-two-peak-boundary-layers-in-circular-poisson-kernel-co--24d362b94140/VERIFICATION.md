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

# Reproduction and limitations

The analytic verification is the proof in RESULT.md, especially its compactness argument eliminating unexamined global maximizers and the implicit-function argument guaranteeing exactly two branches near the boundary.

The standalone `check.py` requires Python 3 and `mpmath` (tested version 1.3.0). From a directory containing the files, run `python check.py`. Its deterministic checks independently integrate Poisson products, reconstruct the exact squared-error identity, solve finite low- and high-radius stationary equations and compare the leading constants and angular fourth-order drift. The sample tests do not certify global optimality or asymptotic quantifiers; those require the proof.

The prior-literature assessment is based on inspected published material and exact comparisons with related recorded claims. No independent mathematical audit has been performed. The threshold values delimiting 'sufficiently small' and 'sufficiently close to one' are not claimed to be explicit.
