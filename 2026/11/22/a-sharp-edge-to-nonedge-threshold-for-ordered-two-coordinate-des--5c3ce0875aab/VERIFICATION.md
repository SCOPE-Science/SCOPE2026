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

# Reproduction and boundaries

From a fresh extraction of these embedded files, install `verification/requirements.txt` and run `python verification/check.py`. The script uses symbolic exact arithmetic to derive the one-step maps, two-step energy matrices, interior positive-semidefinite matrix factorization, the strong-regime generalized-eigenvalue polynomial, and the Rayleigh stationary equation. It separately evaluates 90 ordered pairs across ten rational coupling strengths with numerical generalized eigenvalue checks. The actual embedded script was executed successfully before packaging.

The proof of the universal result is the analytic matrix certificate and explicit worst-direction test; the finite sampling cannot establish the continuum theorem alone. No independent mathematical validation, software formal verification, runtime improvement test, or exhaustive publication-priority certification is represented by these checks.
