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

The self-contained standard-library script `verify.py` constructs adjacency from row/column/symbol equality independently of the clique formulas. Execute `python3 verify.py` from the extracted folder, and compare its stdout byte-for-byte with `expected_output.txt`. No downloads or external dependencies are used.

Tested: cyclic Latin squares of orders five and six, the order-six nonabelian group \(S_3\) multiplication table, and the elementary abelian order-eight table. For each case it enumerates every maximal clique, every nonempty clique face, all line simplex collapse pairs and all intercalate tetrahedron collapse pairs; checks the exact free-face condition at each deletion; checks intercalate nonoverlap and facet counts; and verifies every square-nullhomotopy disk. Exact mod-two ranks of the unreduced and reduced triangle boundary matrices are compared for all order-five and order-six examples, proving those finite test cases have the predicted first and second Betti ranks. The order-eight example checks the combinatorial decomposition and all collapses but does not perform a boundary-matrix rank reduction.

Finite verification cannot prove a universal statement. The proof for all orders and all Latin squares is in `RESULT.md`, including the strict free-face argument, rectangle-disk formula, and Hurewicz/Whitehead conclusion. No external mathematical audit or independently generated proof certificate is claimed.
