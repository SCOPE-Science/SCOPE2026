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

For the asserted model, the universal proof is the derivative-sign calculation and strict log-concavity given in `RESULT.md`. It applies for all positive source strengths, crop separations and attenuation coefficients, including equality thresholds.

Run `python3 check.py` with the standard Python library. Its deterministic output is `PASS: 482428 supplementary assertions; general claim rests on analytic proof`. This verifies (i) the special exact log-power example to floating-point precision, (ii) 800 seeded parameter choices compared against 301 candidate grid points and tested for joint service, and (iii) five fixed-strength separation threshold orders. These tests do not prove the continuous global claim; the self-contained analytic argument is decisive.

The Poisson effective-encounter and spatial decay assumptions are theoretical and have not been empirically calibrated or validated. Review has not been performed by an independent party. The 2004 paper's Poisson one-hit law is prior art, not a new lemma.
