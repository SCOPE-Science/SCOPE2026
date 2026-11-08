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
# Reproducible finite checks

The file `verify_matching_bicliques.py` is a standalone Python 3 program, using only the standard library. Run it with `python verify_matching_bicliques.py` from the directory holding that file. It builds the graph explicitly; its definition of semipaired domination is independent of the counting formula.

For each test instance it builds adjacency for \(K_{a,b}\) with a fixed matching of size \(t\) deleted; determines shortest distances via breadth-first search; determines whether a subset is semipaired by recursively seeking a perfect matching of admissible distance-at-most-two pairs; tests domination vertex-by-vertex; tests inclusion-minimality against **all** proper nonempty subsets. It then independently forms the claimed coefficients and compares three complete dictionaries.

Observed output:

`VERIFY_OK instances=61 subsets=58819 all_domination_semipaired_minimal_polynomials=PASS`

The tested instances include \(3\le a,b\le5\) for all matching sizes, larger unequal and balanced examples, and full matching deletions. These finitely many checks are not an exhaustive validation of all integer parameters. The general proof, including the algebraic crossover at \(n=10\), appears in `RESULT.md`. No external or independent mathematical validation has been performed.
