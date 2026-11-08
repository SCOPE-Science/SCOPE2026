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

Both standalone Python programs were executed with standard-library Python. `verify_direct.py` constructs every vertex and graph edge from the graph definition, enumerates every candidate of the relevant cardinalities for \(2\le n\le9\), and compares actual edge-distance vectors. The captured output is `direct_output.txt`. `verify_structural.py` independently constructs all basis configurations predicted by the theorem for \(7\le n\le10\), checks their exact counts, builds legal token-jump and token-slide adjacency, checks symmetry, and performs an exhaustive connectedness traversal. The captured output is `structural_output.txt`.

The first algorithm is a finite exhaustive check over the tested parameter values. The second is independent of the first's distance-signature calculation but assumes the proposed structural basis description. The proof of the infinite-family result is a direct symbolic comparison of all edge-type pairs, plus a constructive slide path; these computations do not claim automated proof for unbounded \(n\). No outside audit has been performed.
