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

# Verification scope

Run the included standalone program with `python verify.py`; its final line must be `ALL_VERIFY_OK`. The recorded finite run is in `verify_output.txt`. The program has no third-party dependencies.

The code exhaustively enumerates injective vertex orders and their earlier-neighbor strong gradients for 16 positive part-size tuples; it checks actual maximal gradients against explicit facets, face counts, labels of disjoint components, generators of multipartite graph automorphisms, and mod-two simplicial homology. It includes tripartite and four-part examples, and the bipartite boundary cases as controls. The largest tested inputs use nine graph vertices and exactly 362,880 vertex orders each.

The exact formula for arbitrary numbers and sizes of parts follows from the combinatorial first-three-parts argument and the explicit piecewise-linear equivariant deformation retraction in `RESULT.md`. No finite enumeration is asserted to prove the infinite statement. Integral homology and the group action are proved through the retraction, not inferred from mod-two computations. All claims are confined to unfilled graphs with a unique largest part.
