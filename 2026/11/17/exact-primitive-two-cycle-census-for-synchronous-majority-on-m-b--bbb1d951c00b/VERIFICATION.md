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

The provided `verify_transfer.py` is Python 3 standard-library only. It constructs all 256 pair states and 400 permitted edges from the majority rule, uses Tarjan's algorithm to enumerate every strongly connected component, checks the exact row-swap action, constructs the ten- and six-dimensional symmetry blocks, and checks their characteristic polynomials by exact integer Newton identities. It evaluates the twisted trace through length twelve, against the closed recurrences. The all-size argument is the transfer identity plus these exhaustively checked finite structural identities; the trace tests themselves are only finite checks.

`verify_vertex.cpp` separately builds the graph update directly on labelled bits and fully enumerates all binary states for each rim half-length from three through twelve. The programs require no external data or network access. Captured outputs are in `transfer_output.txt` and `vertex_output.txt`. They were executed before packaging from the exact included source bytes.

The closed fixed-point enumerator is classical. The full historical priority status is not independently certified; the chordal-ring majority reference could not be read in full.
