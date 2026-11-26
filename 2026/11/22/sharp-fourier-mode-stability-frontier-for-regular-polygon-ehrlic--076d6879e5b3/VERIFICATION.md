---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
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

The checker reconstructs the simultaneous update with no sequential replacements, checks exact polynomial and derivative identities for degrees 2–40, compares the Fourier-mode Jacobian spectrum against the coordinate-wise analytic derivative evaluated numerically at sampled positive radii for degrees 2–12, and checks the predicted threshold sides. It supplies finite consistency tests only; the all-degree spectrum, complex collapse exception, and positive-radius conclusions are justified by the analytic proof in `RESULT.md`.

The theorem concerns exact arithmetic and the holomorphic Jacobian. The numerical comparisons use a tolerance; they are not certificates of global convergence or novelty.

The standalone standard-library diagnostic `python3 check_modes_fd.py` supplements the analytic argument with centered directional differences of the actual update at representative real and complex inputs, including the collapsed-image scales. Its checks are finite and tolerance-based.
