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

Run `python3 verify.py` using Python 3 with the standard library. The expected final output is `BINARY_QUASINECKLACE_ASYMPTOTIC_VERIFY_OK`.

The script exhaustively enumerates all binary words at lengths 1 through 16 and checks quasinecklace membership against two independently implemented exact counts: bounded-composition recurrences and trailing-zero finite-state dynamic programming. The exact count at lengths 32, 64, 128, 256, 512, and 1024 is checked against the phase approximation within a specified finite numerical tolerance; direct exact counts at lengths 2048 and 4096 were also evaluated separately. Numerical agreement is not proof of the limit.

The all-parameter result is proved by the symbolic run-boundary decomposition, Poisson inclusion–exclusion for length-\(\ell+1\) zero patterns, uniform upper and lower window tails, Burnside normalization, and Fourier integral in RESULT.md. No independent mathematical audit or externally verified certificate is asserted.
