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
# Verification record

The proof in `RESULT.md` covers every integer \(N\ge2\). Its critical steps are: lift increment normalization, the half-circle image bound for zero winding, finite-set isometry rigidity, parity of reflected intervals, and explicit realization of all periodic spectra. The zeta identities use exact formal power-series expansions.

Run `python3 artifacts/verify.py` with Python 3 standard library only. The checker directly enumerates and tests all order-preserving maps on crowns of \(4\), \(6\), and \(8\) vertices, verifies the resulting primitive orbit lengths and realizations, and prints `CROWN_DYNAMICS_VERIFY_OK` on success. This is an exhaustive finite diagnostic only, not an infinite-proof certificate. There is no independent mathematical audit or external certification.
