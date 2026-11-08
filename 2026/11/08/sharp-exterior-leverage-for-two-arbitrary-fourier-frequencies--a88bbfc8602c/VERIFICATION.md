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

# Reproducible verification

Run `python CHECK.py` using Python 3 standard library. The expected output is `TWO_FREQUENCY_EXTERIOR_CHECKS_PASSED 13160`.

`CHECK.py` verifies the rational identity for the derivative certificate by exact rational coefficient arithmetic, compares complex Fourier-pair Gram norms to independent Simpson quadrature, tests exact fixed-gap Cauchy–Schwarz bounds and exterior strictness across deterministic/random parameters, checks the asymptotic coefficient and an explicit confluent sequence. Each computation uses its actual embedded file. Numerical checks are finite and cannot establish the statement for every real frequency and exterior point; the analytic proof in `RESULT.md` supplies that quantification.

The theorem assumes distinct real frequencies and \(|x|\ge1\). Equality is approached, not attained, as the frequency gap vanishes. Independent auditing of this work has not been performed.
