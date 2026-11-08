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
Run `python CHECK.py` with Python 3 standard library only. The script compares the analytically evaluated STFT with direct quadrature of its original integral for eight values of \(\sigma^2\omega^2\), checks every listed root and the predicted signs of the real Jacobian at noncritical values, and prints `ALL_FIRST_HERMITE_CHECKS_PASSED` if successful. Exact uniqueness and threshold statements are established by the proof's monotonicity arguments rather than finite numerical checks. The critical singular-zero index is proved analytically by the local cubic model. All source dates refer to the earliest listed public posting of the motivating work.
