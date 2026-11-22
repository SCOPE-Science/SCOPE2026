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

# Verification and limitations

The accompanying `verify.py` independently enumerates insertion words for orders \(2\) through \(14\), constructs each actual inversion graph, and tests perfect matchability by subset dynamic programming. It checks the proposed alternating-pair event, the leaf identity and exact count formulas. Run `python verify.py` with the standard Python 3 library. The executed verifier completed with \(8191\) enumerated words and \(41{,}003\) loop assertions.

The infinite claims are established by the four-state induction and elementary probability in `RESULT.md`, not by enumeration. No claim of exhaustive literature coverage or independent scientific certification is made.
