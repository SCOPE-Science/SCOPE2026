---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The symbol cycle fixes no nonempty simplex setwise, since one full symbol orbit occupies the same board cell. In the geometric quotient each oriented simplex orbit contributes a separate integral cell, with deletion signs in board-cell order. Independent replay `python3 /workspace/record4_replay.py` used board subsets and anchored the first occupied cell's symbol to zero; it found cell counts [9,90,426,1026,1278,804,252,36,4] and checked integral boundary composition. Integral unit cancellation replaces the pivot row by the pivot boundary and removes that row and its pivot column as a contractible pair; the Schur complement changes the surviving current columns, and the adjacent maps just lose the canceled coordinates. A different pivot ordering canceled 1954 pairs and gave ranks [1,1,1,1,13,0,0,0,0], degree-two boundary of absolute value 3, zero in degrees one and three, and degree-four row of gcd 3. Signs and entries may vary with basis, but these invariants give exactly the printed integral homology. Triangle relations with an independently chosen breadth-first spanning tree killed the 244 non-tree edges in rounds of 154, 60 and 30; the cover is simply connected and its deck group is C3. The frozen checkers were inspected, not executed. This PASS covers the mathematical Finding, not its erroneous assertion about what prior results imply.

## originality

FAIL

The earlier indexed wedge theorem and the elementary free-action check determine the entire claimed integral homology and fundamental group by standard covering theory and cyclic group cohomology. The source's assertion that these facts do not determine the third-homology torsion is false; even the lower-degree Cartan–Leray edge suffices for H3. No earlier verbatim table is needed for this coverage decision.

## value

FAIL

The ordinary symbol orbit space and integral torsion are natural, but these exact invariants are determined by the known wedge theorem and standard cyclic-cover periodicity. The basis-dependent residual entries supply an alternate certificate, not a new invariant or substantive surviving claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
