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

Running `python verify.py` in an environment with SymPy, NumPy, and SciPy checks the exact coexistence Jacobian, degree-two expansion, characteristic polynomial, impulse-kernel identities, resonance-specific closed form, and rational-interval numerical separation. It integrates the smooth coexistence-region equations for two illustrative positive amplitudes under three frozen values and three frequencies. The checker reports `VERIFY_OK exact_jacobian=1 exact_kernel=2 exact_node_response=1 frozen_bound=1 low_high_bounds=2 frozen_scenarios=6 forcing_scenarios=6`.

The analytical proof, not finite integrations, establishes uniform-in-time control for all sufficiently small forcing amplitudes, the all-frozen comparison, slow/fast no-tipping regimes, and the Filippov extinction continuation. No bound on the optimal admissible amplitude, uniform validity for arbitrary model coefficients, independent audit, or certification is claimed.
