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

Execute `python check.py` with the version-independent SymPy requirements in `requirements.txt`. The test checks the two witnesses by a direct subset-and-path algorithm independently of the series/parallel formulas; exact symbolic computation verifies all integer cardinality counts and the positive polynomial certificate. The series-parallel closure enumerates all distinct two-terminal reliability polynomials through eight edges and uses exact square-free factorization and Sturm-type rational root counts to validate minimality. It prints counts for each edge budget and the explicit witness paths.

Observed checks: 1, 2, 4, 10, 24, 64, 174, 496 distinct reliability polynomials for sizes one through eight; 50 mixed-sign comparisons at size seven, each with an interior odd-order root; nine qualifying nonswitching comparisons at size eight; two 256-state direct enumerations. Mathematical limits: no claim beyond the declared class or source model and no independent audit.
