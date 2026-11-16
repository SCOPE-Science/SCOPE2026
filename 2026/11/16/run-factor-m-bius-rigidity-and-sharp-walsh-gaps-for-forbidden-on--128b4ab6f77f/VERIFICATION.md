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

# Reproducibility and limits

Run `python3 verify_walsh.py` and `python3 verify_mobius.py` using Python 3 standard library. The first command should print `WALSH_FULL_ENUMERATION_PASS 90` with sampled spectra. The second should print `MOBIUS_RUN_CLASSIFICATION_PASS 72 6138`. Both programs raise an exception on any inconsistent certificate.

The computation covers finite ranges and does not replace the proof of the infinite statement. In particular the 90 Walsh spectra use every parameter pair `2 <= k <= 7`, `1 <= n <= 15`; the 72 Möbius checks use `2 <= k <= 7`, `0 <= n <= 11`. Exact integer arithmetic avoids numerical rounding. The proofs of the run factorization, rational generating function, maximal degree and Walsh diagonalization are written in `RESULT.md`.

Historical comparisons rely on accessible literature and remain short of exhaustive priority certification. No independent mathematical audit has been performed.
