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
# Verification

Execute \(\texttt{python3 verify\_cones.py}\) using Python 3.10+. It uses no third-party packages and reconstructs all geometric lines by exact arithmetic over \(\mathbb F_4\), all Frobenius orbits and their Gram matrix. The determinant checker exhausts every five-subset of the 21 candidate arithmetic effective rays, identifies every nef-supporting facet, and computes the primitive Cartier intersection profiles.

**Proof dependencies and limits.** The independent geometric facts used are: the standard 27-line theorem for smooth cubic surfaces, the description of their Mori cones by these lines, the unimodular geometric Picard lattice, finite-field Picard descent, and the convex-geometric fact that a facet of a pointed full-dimensional 6-dimensional polyhedral cone is spanned by at least five independent rays. The program verifies all concrete finite calculations under those facts, not an unbounded external theorem. Publication priority remains subject to comparison with potentially unindexed tables. Independent audit has not been performed.
