---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: Both 16-vertex graphs have adjacency spectrum 6^1 2^6 (-2)^9 from A^2=4I+2J. For 3 color classes with sizes n_c, monochromatic edge count B>=sum n_c^2/4-16>=5.5, so integer B>=6. A Shrikhande coloring attains six; the rook row/column eight edge-disjoint K4 cliques force B>=8 and a witness attains eight. Independent C++ subset-partition enumeration visited exactly 3^16=43046721 labeled states for EACH graph, with all 17 favored-color occupancy minima and degeneracies reproduced exactly, including the zero-field totals 288 versus 90936. Convex hull of (k,m_{G,k}) gives field transitions rook (-2,0,4,6), Shrikhande (-5/2,0,1,7/2,9/2,6); collinear sectors included in critical degeneracies. This finite census is exhaustive, not sampling.

## originality

PASS

Best-of-knowledge: exact published same-object claims and primary literature compared by statement/implication, with strong prior ingredients acknowledged and residual risks retained. The complete accepted contribution is not shown covered by the inspected sources.

## value

PASS

PASS: A full finite exact magnetic staircase for the two canonical cospectral strongly regular 16-vertex graphs exhibits failure of spectral data to determine three-state frustration, magnetization and degeneracy. The 34 occupancy-sector table is a meaningful complete classification of a natural pair, not an arbitrary small graph slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
