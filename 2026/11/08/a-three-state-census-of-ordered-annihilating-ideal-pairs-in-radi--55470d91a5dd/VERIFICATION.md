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

# Computational verification
Run `python check_ideal_census.py` with Python 3 and standard library only. The file builds the defining multiplication table of each truncated path algebra, generates all finite-field subspaces in reduced-row-echelon form, checks two-sided ideal closure, and tests all ordered ideal products by original multiplication. The output is recorded verbatim in `verification_output.txt`.

The direct full ideal-pair tests include \(q=2,3\) as listed by each case in the output, with loops, parallel arrows, a bidirectional edge, a directed chain and a source fork. The separate transfer-matrix calculation agrees with the independently computed normal-form count on five cases. All computations completed without timeouts or skipped branches in those specific finite cases. A finite experiment is not a proof of the all-field and all-quiver theorem. No independent review or audit is claimed.
