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

# Finite verification and analytic scope

The standalone `verify.py` is self-contained Python 3 using `fractions.Fraction`. It independently recomputes the first exact Rayleigh correction and later RD corrections from the residual differences; compares these against the spectral RD formula, the warm-start identity, and the scaled logarithmic ratio recurrence. It tests several rational eigenvalue ratios and initial directions, including the balanced scaled-ratio start.

Finite replay is a consistency check. The all-iteration statement rests on the full analytic recurrence, characteristic roots, four-phase sign property, and componentwise multiplier bounds in RESULT.md. No numerical test certifies an infinite limit or establishes literature priority.
