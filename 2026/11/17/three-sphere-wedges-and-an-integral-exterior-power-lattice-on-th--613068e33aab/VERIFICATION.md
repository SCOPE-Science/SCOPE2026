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

# Reproducible finite checks and exact proof boundary

The accompanying `verify_rank_interval.py` requires Python 3.9 or later and no third-party package. From the extracted package directory run `python3 verify_rank_interval.py`. This enumerates every face at orders \(4\le n\le8\), implements the **actual two-stage matching** of the proof, checks the full directed Hasse graph is acyclic by a topological sort, and compares the unmatched faces exactly to one critical vertex and the four-triple tetrahedra indexed by four-sets. It also verifies the complete eight-vertex antipodal graph and maximality of every critical tetrahedron.

Run `python3 verify_rank_interval_mod2.py` for a separate finite test. It uses Bron–Kerbosch maximal-clique generation followed by full simplex expansion and binary boundary-matrix elimination to calculate reduced \(\mathbb F_2\)-Betti numbers at \(n=4,5,6,7\). The results match the predicted sole nonzero third Betti numbers \(1,5,15,35\).

The attached `morse_output.txt` and `mod2_output.txt` are actual output from these programs; they are not independent certification and they are not a substitute for a proof in arbitrary dimension.

**The infinite argument** is the fiberwise canonical-singleton matching, exact classification of Johnson cliques with empty intersection, elimination of triangle-to-cone pairs, a monotone rank-two count proving global acyclicity, Forman's CW reduction, and the primitive diagonal pairing between induced octahedral cycles and maximal three-faces. No computation establishes the universal result by extrapolation. The claim does not extend to rank four or to other Rips scales.
