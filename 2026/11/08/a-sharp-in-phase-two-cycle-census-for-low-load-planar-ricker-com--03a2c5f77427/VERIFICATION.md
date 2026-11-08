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

# Verification and limits

The mathematical argument reduces every positive prime two-cycle to a unique equilibrium midpoint, two logarithmic amplitude equations, a strict phase-sign condition, and an increasing one-variable product equation. The endpoint limits of that product determine exact existence and uniqueness. Directly differentiating the map confirms that the cycle threshold coincides with the sign boundary of \(\det(I+DT(E))\).

The embedded file `verify_ricker.py` uses Python and `mpmath` with 95 decimal digits. Running `python verify_ricker.py` on the packaged file prints `VERIFY_OK finite_parameter_cases=7 analytic_proof_required=1`. It tests four parameter choices predicting positive two-cycles, two choices predicting absence, and one exact threshold case. In the existence cases it reconstructs both forward arrows with residuals less than \(10^{-65}\). The code's threshold comparisons are finite-precision arithmetic, not logical proofs of nonexistence.

Only positive period-two orbits in the specified parameter regime are classified. At the algebraic \(-1\) boundary, this result does not assert any normal-form nondegeneracy or stability of a bifurcating cycle; no global-basin assertion is proved. Independent validation is unperformed.
