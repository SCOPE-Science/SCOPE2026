---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The retained standard-library `verify.py` checks labeled cographs through order six and constructs witnesses for all spectrum values for marked-set size at most eleven. For replay, place it beside this file and run `python3 verify.py`. The proof in `RESULT.md` establishes the all-size minimum order, extension by unmarked false twins, and the transfer to closed neighborhoods. The finite checker does not exhaust graph orders or serve as formal verification of the order-bounded theorem.
