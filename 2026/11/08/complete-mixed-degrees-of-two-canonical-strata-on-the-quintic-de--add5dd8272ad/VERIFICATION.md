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

The standard-library checker `verify.py` was executed against its actual packaged source and returned `VERIFY_OK`. It evaluates both degeneracy-cycle classes in formal Chern roots, uses the coefficient-residue rule for \(\operatorname{Gr}(2,7)\), checks the quintic-del-Pezzo Chern numbers from \(\operatorname{Gr}(2,5)\), and reproduces the same two degree tables using successive projective-bundle pushforwards. This is an exact symbolic finite calculation of fixed intersection numbers. The mathematical justification for the class identities, proper codimensions and pushforward formulas is in `RESULT.md`. The source geometry is from Fu's arXiv:2610.39336v1, Sections 1 and 7; the computed tables are not a classification of other moduli strata. Independent mathematical audit was not performed.
