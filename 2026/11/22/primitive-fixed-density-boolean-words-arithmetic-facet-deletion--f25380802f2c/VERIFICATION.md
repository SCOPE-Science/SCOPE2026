---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The nontrivial-stabilizer coset sum vanishes at a primitive nth root, whereas a single swap changes the sum by a nonzero difference of distinct roots. Thus the forbidden sets are Johnson-independent. Any trace fiber with nonextreme free weight contains an edge, so it has a primitive extension. At |S|=r the only singleton fibers are the relevant extreme trace(s), and their sets are S or its complement, whose stabilizers agree; this includes the balanced case. Larger supports exceed a weight constraint. Primitive cyclic blocks guarantee attainment. The fixed-density Möbius sum counts labeled words, not rotation classes. The Johnson separation gives purity and fills every missing simplex boundary by the other facets through an outside vertex, all present in the complex. Hence restoring missing cells wedges on top-dimensional spheres. The full skeleton is a wedge of binom(n−1,r) such spheres (collapse the contractible star of one vertex), so the original complex is a retract up to homotopy, is (r−2)-connected, and has the claimed top Betti number. The connected graph case and the discrete r=1 case agree separately. This is an integral homotopy argument; the finite mod-two rank tests are only corroboration.

## originality

PASS

The fixed-density necklace enumerator is classical, and the topology is an application of known sparse-paving/independence-complex structure once the Johnson separation and trace classification are identified. What is distinct on the checked evidence is the determination of all indexed shattered supports for this cyclic primitive class, including the arithmetic description of the missing facets. Neither the topology theorem in isolation nor the necklace count is credited as new. This is a bounded comparison, not proof of priority.

## value

PASS

The motivation is to determine how passing from the uniform Boolean layer to primitive words changes indexed membership-query expressivity. The answer identifies every obstruction, shows the VC dimension is unchanged while top supports are removed in an arithmetic pattern, and gives the exact resulting homotopy invariant. The full trace criterion is stronger than the single VC number and is not furnished by enumerating necklaces or by the generic matroid topology theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
