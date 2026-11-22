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

# Reproducible checks

Run `python3 verify.py` using the Python standard library. A successful run prints `VERIFY_OK` and a count of finite checks.

The checker reconstructs the simultaneous update with no sequential replacements, checks exact polynomial and derivative identities for degrees 2–40, verifies the complete Fourier-mode Jacobian spectrum against a direct coordinate-wise differentiation for degrees 2–12, and checks the predicted threshold sides. It supplies finite consistency tests only; the unrestricted theorem is justified by the analytic proof in `RESULT.md`.

The proof and checks concern exact arithmetic and the holomorphic Jacobian. Numerical finite differences have a specified tolerance and are not certificates of global convergence or novelty. Independent audit is not performed.
