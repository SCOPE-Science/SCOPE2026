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

# Verification procedure

Run `python3 verify_grid_vertex_punctures.py` (Python standard library only) in a directory containing the embedded script. Its exact current output is embedded as `CERTIFICATE_OUTPUT.txt`; it concludes with `PASS cases=16 faces=87378 covers=419433 pairs=43636`.

The checker re-generates all possible nonempty matchings for all row/column-reversal representative vertex deletions in the \(3\times4\), \(3\times5\), and \(3\times6\) grids. For every complex, it checks disjoint Morse pairings, coverage and counts of critical cells, acyclicity of the complete directed Hasse graph by Kahn topological sorting, independently calculated mod-two reduced Betti numbers by full simplicial boundary ranks, and direct alternating face-count Euler characteristics. Each of the original grid vertices is accounted for exactly once by the listed representative symmetry orbits.

The perfect discrete-Morse matching establishes the integral homotopy types without needing the mod-two computations: the CW models have one critical vertex and critical cells in only one dimension at least two. The calculations make no statement for widths outside the specified finite range. The 2026 primary paper's full text and external independent audit were not available; priority is not certified.
