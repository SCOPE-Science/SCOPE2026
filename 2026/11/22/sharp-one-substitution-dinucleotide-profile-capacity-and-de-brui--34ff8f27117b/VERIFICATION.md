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

# Reproducibility and verification

The accompanying `verify_local.py`, `verify_enumeration.py`, and `verify_tree_count.py` are standalone Python programs requiring no external modules. Their recorded outputs are in the matching `.out` files and end, respectively, `LOCAL_CHECK_PASS`, `ENUMERATION_CHECK_PASS`, and `TREE_COUNT_PASS`.

The first program directly constructs all interior substitution-change vectors for alphabet sizes two through eight, checks their exact collision classes and boundary disjointness, and constructs literal mutant-profile outputs for de Bruijn witnesses. The second directly enumerates all source words and every one-symbol mutant at short lengths, and separately constructs Eulerian witnesses for sizes two through six. The third computes rooted de Bruijn graph arborescence counts using exact integer determinants for alphabet sizes two through five.

Reproduce by executing `python3 verify_local.py`, `python3 verify_enumeration.py`, and `python3 verify_tree_count.py` from the directory holding the package. Check that their standard outputs exactly match the three saved `.out` files. The finite checks corroborate the analytic all-parameter collision classification and the Matrix-Tree/BEST count, but finite enumeration alone cannot establish those identities at all alphabet sizes or word lengths.

The shortest saturation threshold requires \(q\ge3\): the unique-change-vector argument uses a third alphabet symbol. At arbitrary lengths above the threshold, append symbols to any order-three de Bruijn linearization. No claim is made about minimum cardinalities, every shorter-length maximum, code sizes, or multiple substitutions.
