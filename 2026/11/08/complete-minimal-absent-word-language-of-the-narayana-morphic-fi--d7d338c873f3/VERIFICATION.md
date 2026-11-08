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

# Mathematical and computational verification

The mathematical proof in `RESULT.md` establishes the infinite theorem. The source `verify_narayana_maw.py` is a standalone standard-library Python checker: run `python3 verify_narayana_maw.py` in a directory containing this file. It constructs the specified Narayana substitution iterates and explicitly compares predicted and observed minimal absent word *sets* for all lengths 2 through 40, not just their counts.

The checker replayed successfully on the packaged source. Its checks establish agreement between the factor languages of the finite iterates 25 and 26 for lengths up to 40, exact seven-trigram closure, and equality of all direct and recursive MAW sets in that finite range. It also directly compares the 13 successive two-sided extension graphs whose core lengths run through 240. It found 20 MAWs through length 40: four of length 2 and two at each of lengths 3, 4, 6, 8, 12, 17, 25, 36. No finite experiment is used to infer the infinite assertion. Independent external validation has not been performed.
