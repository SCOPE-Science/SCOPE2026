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

The standard-library script `CHECKER.py` is a standalone reproducibility check. Execute `python3 CHECKER.py` in the same directory as this file. The program constructs all \(945\) seven-leaf binary phylogenetic trees in two different ways, verifies all \(105\) quartet indicators by two distinct criteria, and enumerates every shattered query support containing the first quartet query. The completeness of the symmetry reduction, recursion, and double-count is proved in `RESULT.md`.

Expected output begins `QUARTET7_PASS trees=945 queries=105 searched=206992`; the shattering coefficient vector is `[1, 105, 5355, 171045, 3305610, 1586970, 8820, 0]`, the size-six orbit vector is `[1260, 2520, 5040]`, and every one of the \(64\) binary trace patterns on the exhibited six-query support is checked against an explicit witness in the generated hierarchy data. `WITNESSES.json` contains an additional readable witness certificate with all \(64\) cases.

Scope: exact finite enumeration only, not a general theorem for arbitrary taxon counts. The substantive finite proof needs the completeness arguments in `RESULT.md`, not merely successful execution or a stored log. Independent audit remains unperformed.
