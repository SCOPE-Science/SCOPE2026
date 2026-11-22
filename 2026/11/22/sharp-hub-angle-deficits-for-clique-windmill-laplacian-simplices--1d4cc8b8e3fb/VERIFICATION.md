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
The proof is self-contained given standard Gaussian maximum bounds. The standalone `verify.py` reads no external files, uses fixed seeds, and checks all hub/peripheral score identities for 480 Gaussian vectors across 40 dimension/parameter pairs. It independently checks the conditional-expectation representation against direct Gaussian support-score sampling for three pairs, reports normalized deficit estimates for twelve combinations, and compares them with their asymptotic constants. It passes only if all exact algebra and conditional-sampling assertions pass. Sampling does not certify the asymptotic or historical originality; the extreme-value squeeze and Taylor argument do.

Run: `OPENBLAS_NUM_THREADS=1 python verify.py` with Python, NumPy and SciPy.

Expected terminal marker: `WINDMILL_LAPLACIAN_CONE_EXACT_PASS`.
