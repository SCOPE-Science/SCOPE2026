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
# Reproducibility checks

The standalone Python 3 script \(\texttt{verification/check_cyclic_whisker.py}\) enumerates all faces of the Alexander dual using exact graph-matching recursion. For each integer \(5\le n\le11\), it enumerates all subsets of the \(2n\)-vertex graph with at most four deleted vertices and tests whether the complementary graph has a matching of size \(n-2\). It then removes every center vertex by descending-dimensional elementary collapse pairs, checks each pair is free when removed, and compares the resulting *entire* face set on pendant vertices with the subfaces of two-disjoint-cycle-edge quadruples.

To reproduce, run \(\texttt{python3 verification/check_cyclic_whisker.py}\) from the package root. The supplied \(\texttt{verification/check_output.txt}\) records the actual stdout of this program. It concludes with \(\texttt{CYCLIC_WHISKER_DUAL_CHECKS_PASS}\).

The finite program establishes no universal mathematical statement by itself; the full proof for all \(n\ge5\) appears in RESULT.md. The universal proof's key ingredients are the dominated-center collapse, the leaf-set matching criterion, Gale's evenness identification, Alexander duality and the homological Whitehead theorem. These are ordinary mathematical arguments; no independent audit has been performed.
