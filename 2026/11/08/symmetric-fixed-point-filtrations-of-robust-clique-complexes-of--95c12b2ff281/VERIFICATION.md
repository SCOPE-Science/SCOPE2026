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
# Verification and reproduction

The executable `verify_prism_fixed.py` is a standalone Python 3 program requiring only the standard library. Run `python3 verify_prism_fixed.py` from the directory containing the program. The exact recorded output is embedded as `verification_output.txt`.

It performs **independent finite checks** using two different combinatorial formulations: a full adjacency-level exhaustive independent-set calculation in the product graph, and an induced-subgraph recursive proper-coloring search in the base graph. Every subset of each base vertex set is checked. For graphs on one through four vertices it exhausts all 75 labeled simple graphs for each of the two complete-fiber sizes 2 and 3, for a total of 150 graph-and-fiber tests. It adds twelve targeted five-vertex graph-and-fiber tests, including odd cycles, complete and near-complete graphs and paths. For small products it separately enumerates the group-invariant vertex subsets in the original product complex, resulting in 416 invariant-face-level tests. Finally it checks standard simplex-skeleton Euler characteristic identities for up to eight vertices.

The terminal output must be `PRISM_FIXED_COMPLEX_AND_COLORABILITY_TESTS_OK`. The finite checks exercise the noncolorable sharp boundary as well as the colorable skeleton cases. No finite check alone can prove the statement for arbitrary graph size or arbitrary transitive group; those cases are covered by the exact orbit-barycenter and coloring-bijection proof in `RESULT.md`. A PL model of the fixed point space is justified by its support and barycentric-coordinate argument, not by numerical homology alone.

**Scientific limits:** The verification does not check intermediate-level homotopy types for noncolorable bases beyond the explicit simplicial description, and does not provide external certification. Independent audit remains unperformed.
