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
# Verification

To reproduce the finite checks, run `python3 verify_resistance_theta.py` from the package root. It has no third-party dependencies. The code independently forms a three-node subdivided electrical network, inverts a two-by-two grounded Kirchhoff system over exact fractions, and compares its effective resistances to the analytic edge formula.

The run completed with:

`VERIFY_OK exact_nodal_cases=120 random_global_bounds=8000 inverse_theta_cases=1000 four_arm_counterexample=1`

Critical proved steps in `RESULT.md`: (1) series/parallel reduction; (2) localization on the longest arcs, with a derivative sign and boundary cases; (3) quadratic inversion of \(m\); (4) Vieta inversion of the two remaining lengths, including equal roots; (5) explicit four-path ambiguity extended to all larger counts; (6) sharp fixed-length bounds via majorization and an exact positive factorization. The finite tests do not establish infinite quantifiers or historical originality.
