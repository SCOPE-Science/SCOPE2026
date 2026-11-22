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

# Verification evidence and limits

Run `python verify.py` in this directory. The program uses two separate routes: direct powerset enumeration of all Dung semantic definitions, and prediction via the proved recurrence. Every chord subset is tested for each order from four through twelve (1022 distinct frameworks). Closed-form enumerators are checked for orders four through twenty-four. The observed output was:

`VERIFY_OK 1022 complete/preferred/stable cases; enumerator census through n=24`

This is a finite regression check only. The proof of the universally quantified theorem appears in `RESULT.md`. The scientific interpretation and literature-risk limitations are recorded in `REVIEW.md`; no independent review has been conducted.
