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

The eight-offset neighbor count yields the stated local map on four column symbols. A 16-state (ordered two-column) transfer graph with 23 edges and a 256-state (ordered four-column) two-step graph with 223 edges encode all periodic strings at any n>=3. Exact independent directed SCC construction found the one-step cyclic components 00, 03/30, 11/12/21/22 and the six two-step cyclic components: the same three fixed components plus rotations of 0033, 0132, 0231. Their length-four cycles contribute exactly twelve distinct configurations iff 4|n. The four-node fixed transfer block has characteristic polynomial (z²-z-1)(z²-z+1), proving the Lucas/trigonometric trace formula. Independent direct eight-offset state enumeration for n=3..8 reproduces counts (fixed: 3,9,13,23,31,49; fixed-after-two: 3,21,13,23,31,61). The displayed X_j traveler updates to a four-cell shape then translates by -2 after two steps; odd returns are excluded by cell count and the translation of the three-cell shape is free.

## originality

PASS

A general transfer-matrix approach to cylindrical cellular automata, standard B3/S23 dynamics and known strip-dependent formulas are prior. The particular eight-offset periodic two-row rule, all-circumference Lucas trace, exhaustive six-orbit two-return rigidity and explicit contrasting unbounded traveler are not implied by the inspected prior comparisons.

## value

PASS

Immediate-period rigidity contrasted with arbitrarily long exact traveling clocks is a natural dynamical boundary problem for Conway Life on the narrowest nontrivial periodic-height lattice. An exhaustive local finite transfer certificate produces valid all-circumference counts, not a collection of incidental small experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
