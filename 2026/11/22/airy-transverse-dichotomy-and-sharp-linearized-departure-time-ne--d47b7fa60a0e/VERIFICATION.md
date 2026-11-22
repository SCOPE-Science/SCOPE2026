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

The Airy change of dependent and independent variables was substituted into the exact variational equation; the Airy Wronskian establishes invertibility of the initial-value parametrization. The asymptotic norm equivalents yield both transverse growth branches and the stated first-passage expansion. `verify_airy.py` checks multiple independent parameter choices, residual equations, Wronskian, angular slopes and two first-passage examples, using mpmath 1.3.0. It passed at the stated dependency version.

The proof does not establish nonlinear nearby-orbit first-exit behavior, a stable manifold theorem or properties of compact invariant measures. The independent-audit field reports no independent audit, and numerical examples are not substituted for infinite-time asymptotics.
