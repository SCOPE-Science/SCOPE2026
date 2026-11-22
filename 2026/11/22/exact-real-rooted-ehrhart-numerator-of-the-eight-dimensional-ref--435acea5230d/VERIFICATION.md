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

# Reproducibility

Run `python3 verify.py` in the same directory as this file. The program is self-contained and uses only Python 3 standard-library integer arithmetic. It generates and verifies the primitive facet inequalities from all triples of the 21 given points, checks independent determinant-volume and extremality conditions, computes the exhaustive integer gauge shells within \(8Q\), reconstructs all nine Ehrhart counts and numerator coefficients, and certifies eight distinct negative roots using four exact rational intervals. It verifies, rather than assumes, the required computed intermediate data. No claims about polytopes outside the displayed construction are checked. Independent audit is not yet performed.
