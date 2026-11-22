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

# Reproducibility
Run `python3 checker.py` with Python 3 standard library. Expected output: `GEOMETRIC_SPECTRAL_EXTRAPOLATION_EXACT_OK 9327`. The tests enumerate finite rational patterns and verify stated weight/projection identities at selected rational ratios. The infinite-dimensional exact theorem relies on the proof in `RESULT.md`, not the finite checker. Public source details and residual bibliographic risks appear in `RESULT.md` and `REVIEW.md`. No external independent mathematical assessment is asserted.
