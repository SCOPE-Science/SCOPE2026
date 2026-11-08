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

Run `python verification/check.py` from the extracted package root. It uses Python's standard library only and exercises exact rational arithmetic using `fractions.Fraction`.

Observed execution: `PASS: 11 exact example identities; 9053 rational grid candidates (4164 stable); 288 independent exact rational covariance identities; 99 floating-point root consistency checks`.

The exact arithmetic covers the three-component optimizer's stationary value, the uniform benchmark, the fivefold ratio, both one-step multipliers and the Cauchy equality certificate. The grid checks compare stable probability vectors at eight denominators; they are finite corroboration, **not** a proof that the global minimum has been located. The proof's universal quantifiers, positive-root uniqueness, and stability equivalence follow analytically from independent affine recursions, monotonicity and Cauchy–Schwarz as stated in `RESULT.md`. The numerical root checks use floating point and are only diagnostics.

Independent mathematical validation and full publication-precedence review have not been performed.
