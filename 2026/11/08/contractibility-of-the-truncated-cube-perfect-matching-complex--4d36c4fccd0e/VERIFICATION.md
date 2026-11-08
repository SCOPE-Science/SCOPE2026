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

# Reproducible finite verification

The included `verify.py` uses only Python 3's standard library. All graph vertices, adjacency and graph-edge indices are constructed from binary three-cube darts. The primary perfect-matching enumeration is independent graph-vertex backtracking; the second enumerates all 4,096 cube-edge parity patterns, of which 32 satisfy odd degree at every cube vertex. Both agree on all 32 matching facets.

The face enumeration contains 118,096 distinct faces including the empty face, with dimensions zero to eleven and vector \((36,510,3492,11865,22920,28700,25176,15828,7040,2112,384,32)\).

In the ascending graph-edge ordering, the exact element matching yields 59,036 pairs, 11 critical three-cells, 11 critical four-cells and one critical vertex. In reverse ordering, it yields 59,024 pairs, 23 critical three-cells, 23 critical four-cells and one critical vertex. For both, an independent topological sort of the reversed-matched Hasse diagram processes all 118,095 nonempty faces and 737,700 covering incidences. No directed cycles remain. Both oriented integral degree-four-to-three Morse matrices have determinant \(+1\); their full coefficients are reconstructed from signed gradient paths by the script. No floating-point arithmetic or homology-rank inference alone is used.

An independent deletion recurrence for graph matchings gives alternating matching sum 332 and ordinary matching-complex Euler characteristic \(-331\). These checks certify only the specified finite graph and complexes. They are not independent external validation, and no assertion is made about arbitrary graph truncations or a general perfect-matching-complex classification.

Execution instructions: `python3 verify.py`. The exact expected terminal output is in `verify_output.txt`.
