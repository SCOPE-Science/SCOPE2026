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

# Finite certificate verification

Run `python3 checker.py` with any standard Python 3 interpreter. The code constructs all 17 pointed semantic types and the 11 witness terms, then evaluates the latter in two ways: directly at each reduced type, and independently over all 25 pairs of upward-closed valuations on the actual three-world frame. The asserted 17-bit masks are printed in `RESULT.md`.

The code next verifies all 251 directed pairs outside the 38-pair type order are separated by a witness term, constructs the 17 principal upsets using conjunctions, and enumerates all 9,934 distinct upsets using a leaf-subset/root-subset decomposition. It returns `MEDVEDEV_M2_TWO_VARIABLE_9934_OK 17 types 38 comparabilities 9934 inequivalent formulas` on successful completion.

This computation proves only the explicitly finite table and matrix facts; the reduction from arbitrary formulas to the 17-type semantics is a structural induction in `RESULT.md`. It does not assess larger Medvedev frames, higher ranks, or bibliographic priority. No independent audit has been performed.
