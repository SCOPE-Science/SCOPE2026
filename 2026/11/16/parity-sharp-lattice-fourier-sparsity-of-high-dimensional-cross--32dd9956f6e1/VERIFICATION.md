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

The analytic argument in RESULT.md is the proof. The exact Laplace transform, repeated-node Hermite inversion, isolated collision residues, and intersection-count remainder have been inspected individually.

With Python 3 and `mpmath`, run `python check.py`. Actual observed output: six `STRATUM_PASS` records for dimensions 3 through 8, six `VANISHING_PASS` records, and `COUNTS_BOUNDS_PASS dimensions=3..8`. The test uses 65-digit arithmetic; it is neither exhaustive in frequency nor an all-d proof. A direct full numerical integration over arbitrary high-dimensional cross-polytopes has not been performed.

The first publicly available motivating source was arXiv:2104.06407v1, dated 2021-04-12. Earlier general Fourier literature is cited and is not claimed novel. The d=3 and d=4 specialized formulas are not part of the new priority claim.
