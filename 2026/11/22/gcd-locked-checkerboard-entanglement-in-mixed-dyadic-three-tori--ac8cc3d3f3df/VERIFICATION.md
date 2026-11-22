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

# Reproducibility

Run `python3 verify_graph.py` and `python3 verify_spectral.py` in the same folder as the corresponding scripts. Both require only the Python 3 standard library, have no network operations, and use no precomputed rank tables.

The graph script constructs each integer-coordinate vertex, derives the actual six neighboring vertices, forms the checkerboard biadjacency bit rows, and performs exact XOR elimination; it passed 17 comparisons, including a controlled equal-volume pair of 720-vertex graphs with different gcd values. The spectral script separately creates the full adjacency matrix from the vertex list, performs repeated multiplication on every standard-basis column, and computes ranks over \(\mathbb F_2\). It passed 10 complete profiles: for each tested size, all powers up to one past the predicted terminal zero-primary Jordan length were checked against the proved formula. Full outputs are included in `verify_graph_output.txt` and `verify_spectral_output.txt`.

Only the algebraic proof in `RESULT.md` establishes the theorem for all allowed sizes. These computations are finite corroboration; they are not independent external validation or claims about untested geometries.
