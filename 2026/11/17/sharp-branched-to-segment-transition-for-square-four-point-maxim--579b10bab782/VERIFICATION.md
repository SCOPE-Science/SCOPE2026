---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Any compact connected finite-length competitor meeting all four equal disks may be replaced by a Steiner minimum tree on selected contact points, no greater in length. For four terminals, three paired two-junction trees plus allowed degenerations exhaust Steiner topologies. Eliminating disk contacts gives convex costs ||u-v||+sum_i (||u-c_i||-r)_+. Symmetry averaging for adjacent pairings yields u=(-t,0),v=(t,0); differentiating 2t+4(max(sqrt((a-t)^2+a^2)-r,0)) gives t*=a(1-1/sqrt3), critical r=2a/sqrt3, then clipped segment t_r=a-sqrt(r²-a²). Opposite-corner pairing has optimal u=v=0 and value 4(max(sqrt2*a-r,0)); strict derivative comparison shows it never wins before collapse. Explicit trees and singleton attain all boundary regimes. Independently checked analytic branches against 3-topology scipy optimization for multiple radii; finite numerical comparison corroborates rather than replaces exhaustive topological/convex argument.

## originality

PASS

The original square Steiner length at r=0 and inverse maximal-distance minimizer structure are classical, but the all-radius four-corner disk-contact profile with a branch-to-segment threshold is not supplied by the inspected primary research or the cited exact open-problem collection. Similar words about four-point Steiner trees address the inverse (nonrealizability) question, not this distance-budget value function.

## value

PASS

The full all-radius optimal connected-network length for four square vertices is a natural exact invariant of maximal-distance minimizers. Its nontrivial branched-to-segment transition, matching slopes, and rigorously excluded alternative pairings form a reusable geometric boundary law, beyond r=0 textbook square Steiner length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
