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

# Verification details

The analytic proof establishes the exact asymptotic survival equivalent and joint conditional limit, with all parameters and normalization specified in `RESULT.md`. The step requiring the most care, exchange of the infinite reset-renewal sum with the limit, is justified by an explicit integrable envelope for its renewal density. The proof also checks the borderline moment divergences; numerical convergence by itself is not used as a proof.

The standalone `VERIFY.py` performs 53 numerical assertions on incomplete-gamma success probabilities, renewal-kernel masses, several large-time survival tail ratios using a discretized renewal equation, and Brownian absorbing-heat-kernel convergence to the Rayleigh endpoint law. It was run successfully from the delivered scientific source. Its time-grid tests are nonexhaustive, and floating-point results carry discretization and rounding uncertainty.

Earlier general renewal formulas and unconditional geometric reset counts are attributed to their published sources. The sharp asymptotic and conditional path-mark claims are assessed with explicit literature comparisons; an independent scientific audit and independent publication-priority assessment have not been performed.
