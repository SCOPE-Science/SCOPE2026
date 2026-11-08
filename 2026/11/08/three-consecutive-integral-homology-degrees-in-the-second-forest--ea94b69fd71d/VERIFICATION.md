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

# Computational verification

Run `python3 artifacts/verify.py` in the package root. It requires Python 3.9+ and the standard library only, enumerates the graph and all 262144 subsets directly, and emits a deterministic JSON record that must agree byte-for-byte with `artifacts/verify.out`.

Verified assertions: 18 vertices, 36 edges, 49743 faces including empty, 108/1202/252 facets in dimensions 7/8/9, reduced Euler characteristic 13; two independent face predicates agree exhaustively. Ascending and descending element matchings each have 24826 pairs and 91 augmented critical faces, of counts 16/33/36/6 in dimensions 6/7/8/9. For each matching, topological sorting the full directed Hasse diagram visits all 49743 faces and 322092 incidences. Exact signed integer algebraic-Morse differentials are a 16-by-33 matrix with 19 nonzeros and a 16-column unimodular minor, followed by zero 33-by-36 and 36-by-6 matrices. This proves the complete torsion-free reduced integral homology groups of ranks 17/36/6 in dimensions 7/8/9 and none elsewhere. Independent mod-two reduction of original simplicial boundary matrices gives ranks 5216/7570/6326/2360/246 for degrees 5/6/7/8/9, as expected.

The empty simplex is paired with a vertex only in the augmented calculation. The corresponding ordinary Morse CW model has one critical vertex and no cells in degrees 1 through 5, yielding 5-connectivity; surjectivity in degree seven and the Hurewicz theorem improve this to 6-connectivity.

The finite code and its record certify the specified enumeration and integer matrices but do not prove novelty against unindexed literature or determine unstable attaching maps; no complete sphere-wedge decomposition is claimed. This is a reproducible self-review, not an independent external audit.
