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

# Reproducible verification and boundaries

The new theorem is proved symbolically in `RESULT.md`. Two standalone programs reconstruct graph edges from a cycle-length vector and a tree-edge list and enumerate **all** black sets of sizes \(0,\ldots,k\). Each tests skew forcing by propagation until a fixed point. Both compare the complete family of successful size-\(k\) sets to the alternating odd-vertex classification on matched trees and to the empty family on unmatched trees. They also enumerate all replacement edges and assert that every token slide is absent. The set-based implementation separately constructs the exchange network and computes all pairwise shortest-path distances, asserting equality with the coordinate Hamming metric.

Execute `python3 check_bitmask.py > check_bitmask.out.json` and `python3 check_sets.py > check_sets.out.json` in a directory containing the extracted files. The included recorded output files are expected to agree byte-for-byte. The six graph instances are two cycles of lengths 4 and 4; two cycles of 4 and 6; two cycles of 6 and 6; four four-cycles joined by a four-vertex path; three four-cycles joined by a three-vertex path; and four four-cycles joined by a four-vertex star. The last two trees do not admit perfect matchings; all others do.

These computations are exhaustive only for the specified finite graphs; they are not a proof for every tree or arbitrary cycle lengths. The proof instead establishes the general disjoint-fort lower bound and the residual-tree matching equivalence. No independent scholarly audit has been performed.
