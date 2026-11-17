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

The proof uses the exact Hamiltonian and Abel identities and is independent of finite experiments. A Python 3 standard-library checker (`check_signed_residence.py`) was executed on the complete new package input. It verified three exact-rational Hamiltonian parameter examples at three rational points each; it computed nonsingular turning-point integrals and checked the expected signed limit for three increasing finite energies. It also verified the analytic inverse identity at two admissible pairs, plus the symmetric half-time equality at \(a=0\). The checker printed `SIGNED_CUBIC_CENTER_RESIDENCE_INVERSE_OK`.

The asymptotic proof requires the cancellation in the derivative of the two mass primitives and the integrable tail \(O(E^{-5/4})\); these are established in the Proof section, rather than inferred from the finite checker. The exact area identity follows from differentiation under an integrable square-root endpoint and the explicit vanishing endpoint. Exact sign ordering is proved by a mass-coordinate inverse hyperbolic formula and strictly positive polynomial bracket, not by numerical experiments. Errors are not asserted to be uniform as \(k\downarrow a^2\); no independent audit has been performed.
