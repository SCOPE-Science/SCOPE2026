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

For the precise 20-vertex 35-edge Cartesian cylinder P4 square C5, matchings are exactly edge subsets with disjoint endpoints. The include/exclude recursion exhausts all 253880 augmented matchings; independently derived matching polynomial coefficients (1,35,505,3910,17725,48193,77405,69510,31060,5360,176) and reduced Euler characteristic 136. Inspected source enumerate.cpp creates the claimed toggle matching; check_acyclic.cpp examines the entire directed Hasse graph with 1574120 cover incidences and reports a topological order (a genuine acyclicity certificate when executed). build_morse.py computes signed integer gradient-path differentials. The two checked matching orders have critical ranks (1,149,12) and (9,172,27) in dimensions (5,6,7), with adjacent Smith ranks (1,7) and (9,22), all nonzero factors 1. After pairing the augmented empty cell, there is one basepoint and no cells below 5, so primitive incidence matrices can be canceled integrally: first cancel the 5-cell against a 6-cell and then seven 7-to-6 pairs. Attaching maps to wedges of 6-spheres are classified by degree in pi6, yielding wedge 141 S6 plus 5 S7, not just those Betti ranks. Independent face-count reproduction corroborates; the full expensive Morse/Smith pipeline was source-inspected rather than independently re-run in this execution.

## originality

PASS

PASS best-of-knowledge: this exact finite ordinary matching complex of the 4-row pentagonal Cartesian cylinder has no identified previously computed integral homotopy type. Nearby rectangular, shorter cylinder, and three-row cases do not imply it by inclusion or dimensional coincidence.

## value

PASS

The minimal odd-circumference four-row cylindrical lattice is a natural boundary-condition test for matching complex topology. Its simultaneous 6- and 7-sphere wedge changes the topological profile relative to the 4-by-5 rectangular strip and supplies a precise complete integral finite invariant; 253880-face exhaustive Morse certificate is motivated by that structural comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
