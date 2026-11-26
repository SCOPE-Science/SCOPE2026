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

The independent replay `python3 /workspace/reviews/2-check.py` builds the three metrics by Floyd–Warshall and tests each unordered triple by comparing twice its largest pairwise distance with the sum of its three distances. It checked connectivity and reproduced forbidden triple counts 30, 50, 33 and nonempty face vectors (10,45,90,80,30,5), (10,45,70,38,6), (9,36,51,24,3). All nonempty faces participate in the oriented Hasse acyclicity check, with 860, 482, 336 incidences. The disjoint toggles give 129, 82, 60 pairs and critical cell counts (1,0,0,1), (1,1,3,0), (1,0,2,0) from dimension zero upwards. Relabeling the five ground labels sends any two-set to any two-set and any disjoint pair to any disjoint pair, so testing the representative faults is exhaustive. By discrete Morse theory the first and last complexes reduce up to homotopy to CW complexes with only the indicated 0/3- or 0/2-cells; these are the stated sphere or wedge. For the edge fault an independent exact calculation avoids reliance on the bundled signed gradient implementation: the complete simplicial one-skeleton has a star spanning tree, and projection onto the 36 non-tree edges identifies the rational cycle space with Q^36. The projected oriented triangle boundaries span rank 35, so b1=1. In the Morse CW model the sole 1-cell is a circle and its three 2-cell attaching maps have integral degrees. A single nonzero degree would make rational b1=0, so all three degrees are zero and all three attachments are nullhomotopic. Thus the wedge is an integral homotopy statement, not just a mod-two check. The frozen signed recursion is consistent with cancellation of unit face incidences in acyclic order; the independent route establishes the required vanishing without executing that script. No extrapolation to simultaneous or larger faults.

## originality

PASS

Best of knowledge, the previously computed intact Petersen general-position polynomial and facet list do not cover the two fault-metric homotopy types. The intact type is only a baseline; originality does not rest on having new intact faces or a new method of discrete Morse theory.

## value

PASS

The Petersen graph is a natural symmetric test case for shortest-path betweenness under faults. All single deletions fall in just the two canonical orbits, so the result is a complete first-fault calculation rather than a hand-picked edge. A single lost edge creates a loop, while a lost vertex leaves the complex simply connected; the integral homotopy classification gives usable information not supplied by forbidden counts or Betti numbers alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
