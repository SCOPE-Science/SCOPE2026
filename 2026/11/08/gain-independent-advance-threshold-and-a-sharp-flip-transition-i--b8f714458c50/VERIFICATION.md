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

# Reproducibility and verification

The included `verify.py` uses only Python standard-library `math`. It computes sample values by a guaranteed monotone bisection solver, tests the exact mesh derivative identity, oddness, below-threshold contraction, cycle existence and local stability, unconditional advance-phase contraction, and the inverse-square critical asymptotic at 35,000 iterates. The recorded completed run printed:

`VERIFY_OK parameter_checks=339 critical_algebraic_cases=3`

The analytic proof in `RESULT.md` verifies the universal quantifiers, including the endpoint conventions. The finite checks are corroborative, not a proof of exhaustive coverage or an independent assessment. In particular, critical finite-hitting initial states are explicitly exempted from the nonzero-orbit asymptotic, and no full global supercritical basin census is claimed.
