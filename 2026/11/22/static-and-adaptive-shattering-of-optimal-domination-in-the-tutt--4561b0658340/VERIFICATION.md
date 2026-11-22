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

# Verification procedures

The full universe consists of 15 points, 15 lines, 45 flags and 90 distinct size-nine optimum dominating sets. Compile and execute `crosscheck_gq2.cpp`, and run `python3 verify_gq2.py TREE_DEPTH5.json`. The two programs independently generate the geometry and hypotheses from the finite alternating form, without using a precomputed concept table. Python checks each of 174437 possible query supports through cardinality five against the exact structural predicate, records 420 four-faces and 1980 maximal three-faces, and checks all 32 terminal witnesses in the explicit depth-five tree. C++ exhaustively enumerates shattered supports with a separate search and confirms all coefficients. The printed success markers and outputs are in `VERIFY_OUTPUT.txt`. Larger supports are excluded mathematically by hereditary shattering and the absence of shattered five-supports. The published full classification of minimum dominating sets (RESULT.md reference [1]) is the separately cited exhaustiveness premise. Independent external audit: not performed.
