---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The 36-square queen nonattack complex K is the flag complex of simultaneous rook/bishop nonattacks on the ordinary, nonperiodic 6×6 board. A geometric H-fixed point has barycentric weights constant on each H-orbit of squares, so it is PL-homeomorphic to the complex on individually allowable orbits whose unions remain nonattacking; not the fixed-vertex-only subcomplex. The ten D4 subgroups are exhausted by generator closures. For axis reflections every square orbit attacks itself, giving empty fixed space; diagonal reflections each give 6 isolated squares, quarterturn gives 6 internally nonattacking square orbits with no pair compatible, Klein4 and D4 are empty. For halfturn r², independently enumerating 12 allowable square-pair orbits yields 22 compatible edges and four triangles indexed (0,6,11),(1,7,9),(2,4,10),(3,5,8). Each triangle has an exhibited free edge; four elementary collapses leave a connected 12-vertex,18-edge graph with 11-edge spanning tree, hence rank 18-12+1=7 and wedge7 S1. The identity row M(Z/2,2)∨19S3 is explicitly credited to prior work; no new proof claimed for it. Frozen verifier checked all 2635 original faces with f-vector (1,36,340,1024,982,248,4), alternate orbit construction, ten subgroups and rational Lefschetz traces. Independent fresh halfturn oracle constructed from original square coordinates reproduced exactly (12,22,4) and four listed triangles. No inference from rational character to homotopy was used.

## originality

PASS

Best-of-knowledge PASS for actual all-ten-subgroup geometric fixed homotopy classification of the six-by-six queen complex. Prior result gives nonequivariant Moore plus 19S3 and rational D4 character; that yields Euler/Lefschetz data, not the 7-circle central fixed locus or exact disconnected/empty subgroup spaces. The q-queens literature counts placements on boards without this fixed-space topology.

## value

PASS

The six-by-six queen complex is a natural first torsion-rich chessboard independence complex. Its ten D4 subgroup geometric fixed spaces give an exact equivariant refinement, showing a halfturn with free H1 rank seven despite ambient Moore two-torsion; this is a mathematically motivated topological distinction. A full finite subgroup classification is useful without a theorem for all chessboard sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
