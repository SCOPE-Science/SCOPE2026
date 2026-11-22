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

# Reproduction and verification

The statement and proof are in RESULT.md. Run `python3 checker.py` with NumPy to repeat 622 numerical assertions, including singular-value clipping, boundary derivative limiting ratios, rank-one row-sum formulas and finite two-input stability inequalities. The analytic result does not rely on numerical enumeration or a finite sample. The checker neither proves the global quantifier nor resolves the exact unrestricted constant in general matrix dimensions.

The first public motivating source is the May 26, 2018 UTC arXiv submission arxiv:1805.10408. The earlier arxiv:1209.3318 supplies the established singular-value projection formula as supporting literature; its date is not assigned to the derived statement. Historical priority is not independently certified.
