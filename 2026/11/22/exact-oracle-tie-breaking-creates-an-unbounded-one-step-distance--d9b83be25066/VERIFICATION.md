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

The all-real claims are established by the exact analytic derivation in `RESULT.md`: the local-oracle KKT system, the clipped first-step formula, the two-branch finite-interval extremization, and the explicit asymptotic sharpness constructions. These statements are mathematical proofs, not extrapolations from the checker.

The accompanying standard-library `check.py` checks the tied-oracle envelope and objective decrease with rational arithmetic on representative inputs, nontied KKT signs and geometric identities on a parameter grid, and sharp limiting families. Run `python3 check.py` from the extracted package. It returned: `PASS: 31024 finite exact-rational and floating-point assertions`.

Finite examples do not certify the infinite parameter domain, and floating-point tolerance checks cannot prove exact oracle optimality for all real values; those require the explicit KKT and algebraic proofs. The theorem claims nothing beyond the first step, and no independent mathematical audit has been performed.
