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

With Python 3, NumPy, SciPy and SymPy installed, run `python verify.py` in this directory. The program reads no external data or other findings. A successful run prints the same summary as `verification_output.txt`: 712 assertions passed. The checks cover rational-symbolic two-by-two identities, deterministic circle quadrature for 45 noncommuting SPD pairs, eigenalignment extrema, angular-uncertainty threshold and interior anisotropy inequalities, exact rational examples, and the joint high-anisotropy law. The proof of the circle expectation for all matrices is in `RESULT.md` and does not depend on numerical quadrature.

The program uses strict numerical tolerances on a fixed deterministic test collection, not randomized success as a proof. No machine-formal proof or independent validation is claimed. The stated sharp assertions require the analytic argument in `RESULT.md`.
