---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In the barycentric subdivision face cardinalities distinguish every vertex of a chain; all stabilizers act pointwise on their chain simplex. No two points in one simplex are identified by the quotient: the cardinalities and barycentric coefficients of their supports must agree. Thus triangle sides and edge endpoints are embedded and distinct within each cell, even when distinct cells have identical vertex sets. Free incidences therefore yield actual elementary collapses of the ordinary quotient. An independent bounded enumeration verified the original and orbit counts (231,840,630) and (26,72,48), the fixed-chain counts (19,24,6) for reflections, and all 27 ordered pairs, with 18 triangle–edge and 9 edge–vertex collapses. It verified the core counts (17,45,30), connectivity, exactly two triangles per edge and connected 2-regular multigraph links (including parallel edges, with length counts 2:3, 4:6, 6:5, 10:3). The core is a closed connected surface of Euler characteristic 2; classification gives S². Hence the homotopy and integral homology assertions hold. Replay from the review root: python3 reproductions/3/independent_m7_dihedral.py; output: reproductions/3/independent_check.txt. The original checker was inspected, not run. No claim of formal verification or homeomorphism of the original orbit space is made.

## originality

PASS

Statement-level comparison found exact computations for the cyclic matching quotient (including a separate same-day result) and full dihedral quotients of other heptagon complexes. None supplies the reflection action and attaching data for this matching quotient. The distinct contribution is the full-dihedral ordinary orbit homotopy type and its surface collapse.

## value

PASS

The seven-label complex is a natural early torsion example, and full polygonal symmetry is a canonical action. The exact quotient shows what adjoining fixed-point-bearing reflections does to the torsion-bearing rotation quotient, retaining one sphere. A surface collapse is stronger evidence than homology ranks alone and gives a replayable description of this natural orbit space.

The dated certificate retains the supplied scientific assessment, sources and limitations.
