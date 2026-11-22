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

# Verification of the two-step residual amplification formula

Run `python verification/check_two_step.py` using Python 3.9 or later. The checker is entirely standard-library based and reports `VERIFY_OK 4430` after 4,424 exact-rational checks of the source rules, two derived gain formulas, both rescaled identities and a family of inequalities. It additionally uses six floating-point checks of two explicit near-maximizers for increasing spectral ratios.

All-parameter proof is in RESULT.md: it uses two exact rational identities, uniform domination after the two scale changes, and unique maximizers of two elementary limit functions. The checker is supplementary; 4,424 exact finite assertions and six asymptotic spot checks are not an infinite-domain certificate.

The source algorithm was read in the public preprint in the equations and numerical setup noted in RESULT.md. The method is not evaluated under floating-point rounding or for more than two iterations. No external independent validation was performed.
