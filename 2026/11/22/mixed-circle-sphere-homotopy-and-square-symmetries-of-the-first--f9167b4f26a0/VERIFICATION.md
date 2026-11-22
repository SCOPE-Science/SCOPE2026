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

Execute `python3 verify_gp3x3.py` with standard Python 3; the standalone program uses no external packages or network access. It independently enumerates all subsets of the nine metric vertices and asserts face counts (9,36,16,1), the unique tetrahedron, all twelve grid edges being absent from triangle boundaries, and connectivity of the twenty-four-edge non-grid subcomplex.

For the homotopy reduction it checks one tetrahedron/triangle elementary collapse, a specified eight-edge spanning tree, and fourteen reproducible triangular CW one-/two-cell cancellations. The reduced presentation has two free generators and one empty attaching word, plus twelve separately attached graph edges. It also checks a signed primitive integral two-cycle, its transformed cycles modulo the tetrahedral boundary, all eight Lefschetz traces, and the rational quotient invariant dimensions.

Finite complete enumeration proves statements about this exactly specified nine-vertex complex, not any arbitrary grid. CW cancellation is justified because each eliminated relator has one occurrence of the eliminated generator with exponent +1 or -1. The quotient computation is over the rationals only. An independent audit has not been performed.
