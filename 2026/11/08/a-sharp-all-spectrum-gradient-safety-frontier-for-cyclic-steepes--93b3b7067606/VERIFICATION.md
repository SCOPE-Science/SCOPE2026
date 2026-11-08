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

Run `python3 verify.py` with Python 3's standard library. The script performs 303 exact-rational or supplementary numerical assertions and prints sample threshold estimates. In particular, it verifies the rational identity for the complete-cycle gradient ratio on multiple values of \(m\), \(\kappa\), and endpoint mass \(t\), and uses exact fractions to check the chord inequality for selected finite spectra. It checks the exact strict-growth witness \(19521/10000\) at \(m=2\), \(\kappa=4\), \(t=1/16\).

The proof's universal endpoint domination is the pointwise convex chord inequality; the existence and strict monotonicity of the threshold are proved analytically, not by a sampled search. The asymptotic bound is based on the two-sided inequality for \(h_m\) in RESULT.md; the illustrative threshold approximations depend on floating-point optimization and are not certified interval bounds.

Self-review: passed. Independent audit: not yet performed.
