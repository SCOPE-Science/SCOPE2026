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

Run `python3 bring2_neron_verify.py` in Python 3 with SymPy. The exact program printed `BRING2_NERON_LOCAL_AND_GRAPH_VERIFIED_OK` on replay. It verifies local coordinate expansions, the regularity-enabling cotangent initial forms, the mod-two node tangent form, the reduced intersection Smith factor five, and Frobenius negation on the degree-zero lattice.

The general theorem that a regular semistable Jacobian's component group is the intersection-matrix cokernel and the connected fibre is the dual-graph torus is used as a mathematical lemma, not empirically certified. The five-node, two-component geometric special fibre is previously established literature. The result does not amount to independent mathematical audit.
