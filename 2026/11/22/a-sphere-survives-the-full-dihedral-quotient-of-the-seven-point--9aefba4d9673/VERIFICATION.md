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

# Verification of the finite quotient-collapse argument

Execute `python3 verify_m7_dihedral.py` using Python 3. The program uses only its standard library and builds the entire original matching complex, barycentric chains, and full fourteen-element dihedral action from first principles. It derives canonical orbit cells, their attaching faces, and every proposed collapse pair without reading a saved answer table.

The run checks \(231,840,630\) original subdivision cells, \(26,72,48\) orbit cells, and the exact 18 two-dimensional and nine one-dimensional elementary collapses. The remaining complex has \(17,45,30\) cells. It also checks that the core is connected, all edges have exactly two incident triangles, all 17 vertex links are connected cycles as multigraphs, and Euler characteristic is two. The exact success marker is `M7_D7_QUOTIENT_COLLAPSES_TO_SPHERE_OK`.

These are exhaustive, finite checks for this exact object. No extension to other graph sizes is asserted. A homology-only calculation could not establish simple connectivity; the collapse to a classified closed surface does establish it. This is a reproducible mathematical certificate reviewed under the stated same-model status, not an independent audit.
