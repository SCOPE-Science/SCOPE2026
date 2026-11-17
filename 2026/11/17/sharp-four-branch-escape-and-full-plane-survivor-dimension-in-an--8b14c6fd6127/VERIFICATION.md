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

The included `verify.py` uses only standard-library `fractions.Fraction` and checks 35 exact-rational parameter--phase combinations with 1, 4, 16, 64 and 256 inverse cylinders through level four. All four inverse identities, monotonic branch memberships, exact finite-cylinder lengths, and outer escape identities are checked. An exact rational point below the sharp parameter cutoff verifies that strict four-branch coverage cannot be retained for all phases.

Reproduction: `python3 verify.py`. Successful output consists of `EXACT_FOUR_BRANCH_OK`, `SHARP_THRESHOLD_WITNESS_OK`, and `ESCAPE_IDENTITIES_OK` lines.

The arithmetic tests alone do not prove the claim for all real parameters or all symbolic lengths. The universal statements follow from the exact inverse formulas, the strict algebraic parameter inequalities, the geometric cylinder construction, the uniform separation argument, the mass-distribution lower bound, and the piecewise-affine finite-iterate inverse decomposition in `RESULT.md`. Independent validation has not been performed.
