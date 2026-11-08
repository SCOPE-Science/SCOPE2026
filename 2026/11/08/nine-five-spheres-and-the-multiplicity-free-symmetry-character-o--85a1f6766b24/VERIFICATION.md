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

# Reproducibility and boundaries

Run `python3 franklin_dom_verify.py` under Python \(3.10\) or later, requiring only its standard library. The program reconstructs the twelve-vertex graph from exact integer edges, independently checks the two definitions of the complex for every mask, builds the matching from an exact deterministic rule, and tests each nonempty face-poset covering incidence in an exhaustively constructed orientation graph. Topological sorting of every vertex, rather than a log of matching pairs, certifies discrete-Morse acyclicity. Exact mod-two boundary calculations separately corroborate Betti numbers.

The adjacency-compatible permutation backtracker enumerates and validates all \(48\) automorphisms, compares signed fixed-simplex and cycle-union Lefschetz sums for each permutation, checks all multiplication constraints for its \(S_4\times C_2\) splitting, and computes exact irreducible inner products. Expected results are recorded verbatim in `verification_output.txt`. The matching supplies the integral homotopy proof; finite-field homology alone would be insufficient. This is an exhaustive proof certificate for one finite graph, not an infinite-family classification, independent audit, or publication-priority certification.
