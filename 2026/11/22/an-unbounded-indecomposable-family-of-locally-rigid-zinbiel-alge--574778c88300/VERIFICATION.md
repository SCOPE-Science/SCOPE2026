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

The self-contained `zinbiel_glue_checker.py` uses only Python's standard library. Running `python zinbiel_glue_checker.py` verifies every multiplication-table triple for the Zinbiel law, the square and annihilator, and the modular rank of every derivation constraint for \(k\in\{1,2,3\}\) over the prime fields of characteristics \(3,5,101\). Output ends with `ZINBIEL_CENTRAL_AMALGAM_CHECKS_OK` and the respective derivation dimensions \(4,12,24\).

The general correctness argument is symbolic and appears in RESULT.md; finite modular calculations cannot establish the unbounded or characteristic-zero theorem. The proof of indecomposability is independent of finite enumeration. The full text of arXiv:2611.07863v1 was inspected for the base derivation lemma and the stated open question. The priority comparison is provisionally limited by inaccessible or unindexed historical literature.
