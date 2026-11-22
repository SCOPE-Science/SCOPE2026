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

# Verification details

Run `python3 verify.py` in the directory containing the supplied files. The executed checker returned `FARHI_LOCAL_BIAS_FINITE_CHECK_OK 8 12000 6`: exact least periods for eight windows, a 12000-window defect analysis, and six fixed-modulus bias comparisons. No external Python packages are required. The checker tests finite arithmetic but cannot establish the asymptotic or prior-work originality.

The proof uses the published Farhi--Kane exact-period theorem, bounded-periodic-weight summation, inclusion--exclusion, and a standard effective prime-number theorem. Quantifiers and the fixed-modulus constraint are stated in RESULT.md. The analytic main term and error are proved there, not inferred from finite data. This document does not assert an independent audit.
