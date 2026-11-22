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

# Verification of the finite checks

Run `python3 checker.py` with the Python 3 standard library, without downloads or external dependencies. It directly enumerates disjoint lax-split witnesses, exploiting the fact that any split with overlap may be represented by assigning the overlap to either side (the row-functional side is downward closed; the other side stays unchanged). Direct semantics is compared to the exact row-intersection condition on 848 teams from the 2-by-2, 2-by-3, 2-by-4 and 3-by-3 rectangles. The code independently enumerates all subteams of 2-by-2, 2-by-3, 2-by-4, 3-by-3, 3-by-4, 4-by-3 and 4-by-4 rectangles (74,576 total), checks each inclusion-minimal false team, classifies it, and compares the two exact coefficient formulas. The expected final line is `ALL_OK`.

The tests confirm the theorem on enumerated finite domains only. The accompanying proof derives its general necessity, sufficiency, false-pattern extraction and counts for arbitrary finite positive alphabet sizes. A complete 3-by-3 rectangle satisfies independence but contains a six-edge falsifying subteam: the theorem explicitly makes no two-sided coherence claim. Independent mathematical auditing has not occurred.
