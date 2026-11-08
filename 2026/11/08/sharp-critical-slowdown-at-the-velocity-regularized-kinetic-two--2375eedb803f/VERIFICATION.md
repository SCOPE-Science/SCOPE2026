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

# Verification performed

The complete standalone `VERIFY.py` was executed directly with Python 3. It returned:

`VERIFY_OK exact_fraction_cases=4 critical_two_step_trajectories=4 each_120000_iterations`

The four rational momentum values tested were \(0\), \(1/5\), \(1/2\), and \(9/10\). Exact rational checks covered the orbit and center-manifold Taylor coefficient identities; floating-point checks evaluated actual nonlinear two-step trajectories and their rescaled errors. The program uses the Python standard library and no network access.

# What the checks do not establish

Numerical trajectories do not certify the infinite-time limit and a finite list of momenta does not verify all real momentum values. Those conclusions depend on the written center-manifold calculation, the strict sign of the cubic coefficient, local invariant-manifold theory and the reciprocal-square summation argument. The exceptional stable manifold is proved to exist locally but is not explicitly parameterized globally.
