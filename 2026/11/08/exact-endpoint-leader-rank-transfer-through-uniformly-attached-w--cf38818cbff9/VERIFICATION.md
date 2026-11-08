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

# Reproduction and limits

Execute `python3 verify.py` from this directory. The script uses exact rational integer matrix powers and Gaussian elimination, checks 925 finite instances/conditions, and prints `VERIFY_OK 925` on success. The exact six-state interior-input failure is checked by direct controllability ranks. The general theorem is proved algebraically using strict Jacobi interlacing, fiber eigenvector endpoint nonvanishing, and the spectral formula for symmetric Kalman rank, not by finite examples. The script supplies no independent audit and does not evaluate floating-point condition numbers or control energy.
