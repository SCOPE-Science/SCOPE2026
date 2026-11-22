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

# Verification and reproducibility

The standalone `checker.py` is included. With Python 3, run:

```bash
python3 checker.py
```

The checker uses only the standard library, verifies strict branch selections and equality-direction perturbations on eleven parameter values, performs 110,000 randomized positive input-pair / active-branch comparisons, and computes the two one-sided constants at the critical exponent. Its reproducible seed is fixed within the code. The expected last line reports PASS.

The universal validity of the theorem is proved analytically in `RESULT.md`: all 18 nominal selection tuples are covered by a finite case exclusion/upper-bound analysis, strict feasible witnesses yield equality, and the elementary concavity inequalities hold for the whole exponent interval. Numerical tests do not certify this infinite continuum. The evaluation of displayed constants uses floating-point arithmetic; the mathematical claims use exact radical expressions and the unique root of the stated monotone equation. No independent mathematical audit is claimed.
