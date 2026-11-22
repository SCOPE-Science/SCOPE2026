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
# Verification

Run `python3 check.py` in this directory. The script uses only Python's standard library. Its final line should read `ALL CHECKS PASS`; a complete sample output is in `check_output.txt`.

The script independently reconstructs the graph from each clique-size vector, exhaustively enumerates every vertex subset to identify *all* maximum independent sets, enumerates every possible query support and every membership trace, and checks exact agreement with the support characterization and generating polynomial. It separately evaluates adaptive mistake-tree depth by a memoized recurrence on version spaces. For test graphs of at most ten vertices it builds all simplicial boundary matrices over the field of two elements and verifies the reduced Betti ranks. The tested vectors are (2,2,2), (3,2,2), (3,3,2), (3,3,3), (3,3,2,2), (4,3,3), (4,4,3), and (2,2,2,2). Cases with first block size two are prior-boundary regression checks only.

The universal assertions for every integer a>=3 and n>2a require the full symbolic argument in RESULT.md; finite tests do not establish infinite quantifiers or integral torsion absence. The integral homotopy types are proved by join and homotopy-pushout arguments, not inferred from mod-two computations. No external independent audit has been performed.
