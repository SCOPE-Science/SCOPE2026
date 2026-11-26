---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

I independently recomputed the distances by breadth-first search from every vertex of the explicit Cartesian-product graph, not by the supplied formula. A triple is excluded exactly when twice the maximum of its three distances equals their sum: concatenating geodesics for the two shorter distances then gives a shortest path containing the third vertex. Enumerating increasing faces by adding one vertex and testing all newly introduced triples is exhaustive by heredity. No face of size ≥5 survives. From the signed chain matrices I recomputed Smith forms over ℤ using SymPy 1.14.0; all nonzero factors have absolute value one. Thus im ∂_(i+1) is saturated in C_i, and H_i embeds into a free cokernel, so it is free. The complete 1-skeleton is connected. For n=3..8, the boundary ranks (r1,r2,r3) are (5,7,0),(7,6,2),(9,31,10),(11,31,18),(13,71,56),(15,73,72). The dimensions then give reduced Betti triples (3,1,0),(15,0,0),(5,9,0),(24,3,0),(7,27,0),(32,15,4), with no unlisted reduced homology. In particular H̃3 first occurs at n=8 with rank 76−72=4. Replay: python3 /workspace/review_evidence/ladder_homology.py; results in ladder_homology.log in that directory. I inspected the supplied proof and unit-pivot implementation without running the supplied code. Verification is for n=3..8 only.

## originality

PASS

Best-knowledge pass for the exact integral homology of these geodesic general-position complexes and the first H̃3 threshold, not for the underlying forbidden-triple construction, the general-position number, or the topology of other complexes on these graphs.

## value

PASS

For this canonical family of known general-position dimension, the first top-dimensional cycle is not where tetrahedra first exist. The sharp onset and torsion-free full profiles distinguish that phenomenon from the already-known extremal size, and give exact tests for any proposed cyclic-ladder homotopy or chain model. The finite end point is dictated by the first occurrence, not an arbitrary truncation. No homotopy-type classification or result beyond the cutoff is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
