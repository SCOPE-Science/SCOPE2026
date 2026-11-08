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

The proof in `RESULT.md` treats every integer \(n\ge4\) and every matching size \(0\le t\le n\). Its critical comparisons are the exact unique-outside-midpoint condition for all selected same-shore pairs, the excluded three-edge path when a second deleted matching pair survives, the explicit surviving path in the proper-deletion regime, and the two mirror omission shapes at full deletion. Counting configurations is injective on labelled vertex subsets.

The standalone Python 3 standard-library file `verify.py` constructs each graph from adjacency, not from the profile classification; checks induced connectivity by graph exploration; computes graph distances by breadth-first search; and compares each selected pair's full-graph distance to the distance in the induced allowed subgraph after excluding other selected vertices. It exhaustively enumerates every nonempty subset for every \(4\le n\le7\), \(0\le t\le n\), and compares the exact set of optimum configurations with the stated structural families. At \(n=8\), every subset of cardinality at least the claimed optimum is checked. The actual run concluded `VERIFY_OK` with no mismatches.

This bounded computation is corroboration only, not a proof for arbitrary \(n\) and not independent mathematical certification. The unrestricted proof is contained in `RESULT.md`; no external code packages, downloads or prior-run files are required. The theorem excludes \(n=3\), unequal shore sizes, and nonmatching edge deletions. Independent mathematical audit is not performed.
