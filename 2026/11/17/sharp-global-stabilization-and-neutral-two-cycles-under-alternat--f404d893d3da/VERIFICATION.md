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

# Verification scope

The self-contained analytic proof in `RESULT.md` establishes the full-plane estimates and all boundary claims for every real parameter within the stated domain. The executable `checker.py` uses only standard-library rational arithmetic, with the concrete parameters \(a=7/5\), \(b=3/10\), \(t=1/2\).

Run `python3 checker.py`. Expected output:

`PERIODIC_LOZI_COORDINATE_SHARP_OK exact_matrix_cases=3 comparison_trajectories=108 critical_two_cycles=3`

The checker confirms the exact two-step Jacobian and positive comparison matrices, determinant and trace identities and threshold for \(r=1/4\), \(r=140/413\), \(r=1/2\). It checks the global comparison on 108 finite initial trajectories and three critical two-season cycles with positive coordinates in both phases. These finite checks do not assert exhaustive initial-state coverage or prove convergence as iteration count grows. The universal assertions follow from the explicit matrix inequality and its eigenvalue analysis.

No independent mathematical validation has been conducted. The originality assessment is based on inspected and accessible published scientific statements and is not proof of bibliographic uniqueness.
