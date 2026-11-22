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

The analytical derivation in `RESULT.md` covers every allowed parameter, every Neumann mode, and the boundary at which the first zero eigenvalue occurs. The diagnostic `checker.py` verifies exact rational determinants, the full-mode real-instability sign on a finite independent numerical mesh, special finite-length thresholds, quantization predictions, and sign-definite negative-energy test paths. Execute `python checker.py` using Python 3 and NumPy. The finite checks do not imply exhaustive coverage; the exact proof does.

No independent audit or independent scientific validation has been performed. Publication priority remains conditional on the residual literature-coverage risks disclosed in `REVIEW.md` and `AUDIT.json`.
