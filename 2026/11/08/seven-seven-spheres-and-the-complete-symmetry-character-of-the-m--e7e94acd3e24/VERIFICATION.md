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

# Reproduction and limits

Running `python verify.py` using the Python 3 standard library generates every face of the specified sixteen-vertex graph's dominance complex, first by the forbidden-closed-neighborhood test and independently by testing its complementary dominating set. Both predicates agree on all 65,536 subsets.

The code repeats the exact sixteen-stage coordinate-toggle matching and checks disjointness, completeness, residual critical masks and a directed acyclic graph containing all 32,390 nonempty faces and 218,672 cover arrows. All directed vertices are exhausted by a topological sort. The unmatched nonempty faces are precisely one critical vertex and seven critical dimension-seven simplices. This acyclic matching is an integral homotopy certificate by Forman's theorem, not an approximate numerical measurement.

A separately coded reduction of every mod-two augmented simplicial boundary matrix gives reduced Betti number seven only in degree seven, corroborating rather than establishing the integral homotopy result. The verifier next enumerates all 96 graph automorphisms by adjacency-preserving backtracking, verifies group closure/inverses and all adjacencies, partitions conjugacy classes, and computes all 96 signed Lefschetz traces. It checks both character inner product and fixed-subspace dimension exactly.

`verification-output.txt` records a complete successful execution, including class representatives. Only those two local files are needed to reproduce all claimed checks; neither external graph databases nor network access are required.

The finite exhaustive certificate establishes this graph only. It does not prove novelty against unseen literature, nor provide an equivariant homotopy decomposition or an integral irreducible lattice classification. Independent mathematical review has not been performed.
