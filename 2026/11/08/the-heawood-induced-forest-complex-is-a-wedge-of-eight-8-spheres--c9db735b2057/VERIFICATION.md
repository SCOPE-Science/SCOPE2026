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

The standalone program `verify_heawood_forest.py` uses only Python standard-library features. Run `python3 verify_heawood_forest.py` in the directory containing the attached file, and compare its stdout to `verification_output.txt`.

The program builds the graph from seven modular Fano lines and verifies the pair-incidence axioms; exhaustively compares two logically independent forest-membership algorithms; enumerates every face and maximal face; constructs the deterministic 14-stage matching on the full nonempty face poset; and topologically sorts the complete directed Hasse diagram. All claims of acyclicity and critical-cell counts are proved by explicit finite loops over the entire domain, with assertions. A separate mod-two simplicial boundary reduction checks homology but is not used to infer the integral homotopy result.

Verified counts: 12,792 faces including the empty face, 6,391 matched pairs, one critical vertex, eight critical 8-faces, 81,634 Hasse covering relations, and 12,791 vertices removed by topological sorting. The face complex is 9-dimensional; its 238 facets are split between dimensions 8 and 9. The total Euler characteristic is 9.

No analytic infinite-family assertion, equivariant result, or independent mathematical certification is claimed.
