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

Run `python3 verify.py` in an extracted directory. The script uses only Python standard library and exact fractions. It computes generating-series coefficients through order eight; checks all one-out mappings and all subset valuations through order six against both Dung extension definitions and the independent cycle-pruning classifier. It does not certify the infinite-size limit, global originality or any independent review. The general result is established in `RESULT.md` by a recursive species argument and analytic transfer, not by the finite tests.
