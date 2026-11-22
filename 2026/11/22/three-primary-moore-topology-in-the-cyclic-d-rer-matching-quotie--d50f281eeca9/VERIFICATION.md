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

Run `python3 verify_cyclic_quotient.py certificate.json` with Python 3 standard library. The verifier rebuilds the graph, its six rotations, 1,037 matching faces, 166,087 flags and 27,703 quotient cells from definitions. It verifies every listed free coface before 12,488 geometric pairs are removed, then rechecks all 1,360 exact integer unit pivots. It reconstructs cellular boundaries and checks their squared composition is zero before algebraic reductions. The remaining integer differential has a single coefficient three, with four independent closed three-cells. Separately, it checks the 93-edge spanning tree and all 580 one-occurrence Tietze substitutions, ending in the trivial fundamental group.

Successful output: `DURER_CYCLIC_MATCHING_QUOTIENT_MOORE_THREE_TORSION_OK`.

The finite checker and certificate prove exact assertions for this finite object; they do not verify any infinite extension. The Moore wedge is a homotopy classification via standard algebraic topology, not a claimed explicit simplicial collapse. Independent mathematical audit is not performed.
