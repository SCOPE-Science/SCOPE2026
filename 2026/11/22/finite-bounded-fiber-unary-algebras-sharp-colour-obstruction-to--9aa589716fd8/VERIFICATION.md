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

For a finite total unary function, substructures are forward-closed and fiber bounds then pass to substructures; disjoint union gives joint embedding. In the uncolored amalgam, group new vertices by their forward path to A, leaving components never reaching A disjoint. Starting at each old target, recursively identify a maximal pairing of its two sides' new immediate predecessors, then repeat only at paired targets. Tree levels increase away from the common target so this terminates; no vertex pairs twice, function images are consistent, and no same-side vertices are identified. At each old target the fiber is its old fiber plus the larger of the new counts; at paired targets it is the maximum of the original fibers, and remaining targets are unchanged. The cap therefore persists. At k=1 finiteness and totality give a permutation and closed subsets are unions of whole cycles, permitting strong amalgamation with arbitrary colors. At k≥2, two fully saturated extensions of a fixed point each adding k−1 leaves force 1+2(k−1)>k without identifications; for q≥2 even AP fails by reserving exactly one open slot and requiring two differently colored new leaves. These counts include the fixed point itself. With no cap the union over the common domain works strongly. In the AP limits every finite subset lies in a finite closed substructure. New disjoint cycles witness infinitely many components of each admissible cycle type, and adding predecessors in a finite extension forces saturation in the uncolored case. Each cycle vertex therefore has k−1 off-cycle predecessors and each noncycle vertex has k, giving the stated regular trees and the extension property. With cap one the analogous limit is just the stated infinitely repeated colored cycles. The independent small checker reproduced 156, 5218 and 7795 inclusion spans for k=1,2,3, respectively, checking well-defined quotient, embeddings and caps.

## originality

PASS

The standard functional digraph decomposition, hereditary/joint embedding observations and Fraïssé machinery are not original. The supported contribution is the exact combined ordinary and strong amalgamation thresholds under named colors together with the concrete bounded-fiber limits in the positive regimes. No encompassing prior result was established in the inspected comparisons.

## value

PASS

The classification explains when finite capacity can be managed by identification but not by strong amalgamation, and exactly when naming colors obstructs even ordinary amalgamation. The associated generic structures follow an explicit cycle-and-branch description instead of abstract existence alone. These distinctions are useful for choosing bounded-valence classes for homogeneous constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
