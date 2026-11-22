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

Run `python3 check.py` using only the standard library. The checker exhausts 32768 labelled simple graphs at six vertices, retains their 2932 forests, and compares all nonempty marked subsets against the previously established numerical bound. It constructs and deduplicates all 3 trace families at three marked points and all 810 at six marked points, checks the tree realization and exact distinct trace count for each, and verifies representative nine-marked-point constructions.

Checks executed locally against this `check.py`: `ALL_CHECKS_OK`. The proof for arbitrary \(q\) is in RESULT.md; finite testing is not a proof of an infinite family. The input is the supplied mathematical constructions, not a published certificate. Historical priority and independent audit remain open.
