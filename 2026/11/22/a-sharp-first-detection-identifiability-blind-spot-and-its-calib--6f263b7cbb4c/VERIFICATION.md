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

# Verification

The exact proof in `RESULT.md` establishes all quantified statements over positive rates and initial availability in the closed unit interval. A reproducible supplementary checker is provided as `checker.py`; it forms independent matrix resolvents, checks exact rational observational aliases, checks exponential pole cancellation at a known nonzero initial state, tests randomized inverses, and forms the killed matrix exponential.

Run `python checker.py` with NumPy and SciPy. A clean local run produced: `PASS: 22027 Laplace, moment, cancellation, jet-inverse and matrix-survival checks`.

The checker does not verify a continuum or prove that a search result is absent: the proof supplies universality, and originality is assessed only against the inspected sources listed in `REVIEW.md` and `RESULT.md`. External independent validation has not been performed. The theorem is an exact-population structural result; it is not a finite-sample confidence or error statement.
