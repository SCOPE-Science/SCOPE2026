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

# Verification and scope

Run `python verify.py` from the same directory after installing NumPy, SymPy, and SciPy. The script reconstructs the stable linearization's exact algebraic identities, checks the two distinct individual-frequency optimizations and all three possible joint-optimum regimes, and integrates nonlinear forced positive trajectories to compare first harmonic amplitudes. Its successful marker is:

`VERIFY_OK exact_identities=3 minimax_regimes=6 nonlinear_amplitude_checks=24`

The script's finite checks do not certify the all-parameter theorem. The full proof is in `RESULT.md`; the crucial all-frequency error estimate follows from the bounded causal convolution of the Hurwitz Jacobian, and the strict uniqueness follows from the exact derivative signs. The conclusions exclude actual threshold-switched trajectories, transient tipping, and fixed nonshrinking threshold distances. Only self-review has been performed; there is no independent scientific audit or external certification.
