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

The included `check_local_time.py` was executed with Python's standard library. It compares the analytic series against a separate Gaussian-density double integral after the change of variables \(s=u^2\), checks analytic derivatives with centered finite differences, and tests a finite set of noise parameters against the proved high-noise expansion. The derivative bisection is a numerical check, not a theorem asserting uniqueness at intermediate noise. The global and asymptotic assertions are proved symbolically in `RESULT.md`, including endpoint derivative signs and a high-noise \(C^2\) perturbation argument. All numerical tests passed.

Limitations: no machine formalization of the analytic proof, no exhaustive numerical certification of all noise values, and no independent mathematical review.
