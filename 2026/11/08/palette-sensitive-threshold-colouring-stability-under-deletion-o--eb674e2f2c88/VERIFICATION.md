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

The executable `artifacts/verify.py` checks the count by independently enumerating all named vertex assignments and detecting forbidden induced threshold obstructions. It compares against a separate factorial-weight coefficient computation. The tested ranges are \(2\le m,n\le4\), \(0\le d\le n\) and \(1\le q\le3\), with instances above 20,000 assignments omitted. The last independent-of-proof computational replay printed `VERIFY_OK`. Every unbounded result is justified by the exact case classification and exponential generating-function derivation in `RESULT.md`. No external independent audit has occurred.
