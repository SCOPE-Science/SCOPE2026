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

Run `python verify.py` with Python and SciPy to check the three-coordinate system against the original mean-field equation, the mass and equilibrium identities, the centered normal-form equations, and a set of exact-rational parameter and probability-vector inputs. The verifier also checks the critical rate ordering at five parameter values and four numerical trajectories for positivity, convergence, and entropy dissipation.

An observed successful run returned `VERIFY_OK exact_rational_states=3816 analytical_boundaries=5 numeric_trajectories=4`. The universal global-attraction and sharp asymptotic statements are established by the inequalities and convolution estimates in `RESULT.md`, not by finite testing. In particular, no finite trajectory run proves the limit is nonzero or excludes unobserved behavior.

The source-equation identity was independently reconstructed in the stated normalization. The low-, critical-, and high-parameter remainders were separately estimated to avoid treating a slowly decaying quadratic forcing as a weighted-integrable function. No independent external verification has been performed.
