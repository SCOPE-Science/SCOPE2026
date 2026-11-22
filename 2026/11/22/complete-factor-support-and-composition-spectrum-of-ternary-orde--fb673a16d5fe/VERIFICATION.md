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

# Checks and limitations

`verify_supports.cpp` exhaustively enumerates all assignments of antipodal factor pairs in two balanced halves, uses exact integer imbalance signatures, and checks connectedness of every balanced assignment. `verify_supports.py` implements independent Cartesian-doubling half enumeration, sorted exact-integer signature matching, and a separately coded connectedness test. The two programs return exactly 274624 balanced selections, 218564 realizable connected selections, and the same complete composition histogram. The Python program also checks the six literal cycles in `witnesses.txt`; their additive negatives yield the remaining supported compositions.

The enumeration is finite and exhaustive only for alphabet size three and factor length four. The mathematical reduction from negative-avoiding cyclic words to Eulerian selected-factor graphs is proved in `RESULT.md`. No assertion about different orders or number of Euler tours is made. Independent external review has not been performed.
