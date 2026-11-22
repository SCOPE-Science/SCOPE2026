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

The accompanying exact-arithmetic Python/SymPy verifier independently reconstructs the twelve projective line equations over the Eisenstein integers and all 66 pairwise intersections; finds exactly 9 quadruple points and 12 nodes; forms the 21-vertex, 48-edge graph; computes the exact Laplacian characteristic polynomial, the integer determinant of a reduced Laplacian, its complete Smith factors, and the full ranks modulo 3 and 7. It independently builds the affine-plane combinatorial model and compares Smith factors.

Run `python verify_hesse_boundary.py`. Expected terminal line: `HESSE_RESOLVED_NERON_COMPONENT_GROUP_OK; 21 vertices, 48 nodes, genus 28, SNF 3^2 21^8`.

The unrestricted mathematical argument is a direct block-incidence proof in `RESULT.md`, not an inference from tests. The graph-to-Néron identification is conditional on regular split unit-thickness semistable smoothing. Historical priority is not an independently verified assertion.
