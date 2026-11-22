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

The analytic proof is in `RESULT.md`. The portable checker `verify.py` (Python with SymPy and mpmath) reconstructs six exact symbolic identities including the sharp root-ratio maximizer, checks the full-interval orthonormal Gram normalization, and evaluates the original concentration matrices directly through antiderivatives at seven shrinking observation fractions. It also tests randomly selected disjoint two-interval masks against the rigorous finite-area bound. Re-run with `python verify.py`; the expected final assertion summary is `TWO_BAND_RADIAL_CHECKS_PASS 195`.

The observed ratios to the asymptotic constant for area fractions 0.1, 0.05, 0.02, 0.01, 0.005, 0.001 and 0.0001 are respectively approximately 0.721960, 0.854894, 0.940714, 0.970172, 0.985042, 0.997002 and 0.999700. This finite calculation does not prove the limit; the Schur-complement and variational arguments do. No independent audit or formal proof certification was performed.
