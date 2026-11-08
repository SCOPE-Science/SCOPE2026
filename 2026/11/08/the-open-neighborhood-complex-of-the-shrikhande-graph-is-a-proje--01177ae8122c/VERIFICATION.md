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

# Verification procedures and scope

Run `python3 verify_shrikhande.py` without third-party packages or external files. It reconstructs both graph adjacency and every face from first principles and reproduces deterministic free-face collapse sequences with increasing-mask and decreasing-mask tie-breakers. Every deletion is an elementary simplicial collapse, rather than an unverified Morse count.

The reduced two-dimensional complexes each have sixteen vertices, 120 edges and 160 triangles. Contract the specified fifteen-edge spanning tree. Each triangular attaching map is converted to a freely and cyclically reduced integer edge-word. The verifier then completes 104 generator/two-cell cancellations and checks every surviving attaching word against exactly one generator with degree either zero or absolute degree two. The two reductions independently yield the same homotopy type. Basic mod-two, mod-three and mod-five ranks are supplementary checks.

The finite exhaustive verification establishes the stated result only for the explicitly defined sixteen-vertex graph. No infinite-family inference, equivariant equivalence or external certification follows. No independent audit has been performed. Exact stdout is embedded as `verification_output.txt`.
