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
The necessary inequality \(R>p+1+p^{-1}\) and converse formulas are proved symbolically in `RESULT.md`. Run `python cycle_checker.py` with a standard Python interpreter for the exact rational witness and 500 deterministic parameter trials (skipping trials that do not meet the stipulated strict inequality). The checker was executed successfully before packaging. It is an independent reproducibility aid to check algebraic substitutions, not a substitute for the universal proof or a third-party mathematical audit.

The only original model paper used is the publicly accessible May 15, 2025 version at https://arxiv.org/abs/2505.09968. The closest published exact \(R=2\) nonexistence record is credited in `RESULT.md`. Its complete text was unavailable to the literature comparison. No certification of historical uniqueness is claimed.
