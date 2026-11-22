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

The analytic certificate consists of the two exact determinant identities and the two strict concavity estimates in RESULT.md. These imply unrestricted global optimality over all three distinct observation times within one period; no finite numerical search is used as an infinite proof.

The companion `verify_design.py` checks the two determinant identities with SymPy. It then compares the theorem's optimum with full two-variable numerical optimizations at eight correlation-rate ratios and checks many unequal-gap pairs and perturbations. Run `python verify_design.py` with standard installations of NumPy, SciPy and SymPy. The procedure prints the exact checks and numeric phase values. No machine or observational measurements are necessary.

The theorem does not cover instrumental white noise, quasi-periodic correlated noise, unknown frequency/covariance parameters, or the marginal mass precision objective. The singular perfect-correlation limit is interpreted only through finite positive correlation times. No independent audit or empirical validation is claimed.
