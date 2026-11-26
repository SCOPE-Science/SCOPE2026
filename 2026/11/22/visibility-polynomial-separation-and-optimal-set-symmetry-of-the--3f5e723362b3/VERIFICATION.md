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

Every pair has exactly two common neighbors in both specified graphs. Adjacent pairs need no interior vertex, so a nonadjacent pair in X fails visibility precisely when both its common neighbors also belong to X. All resulting quartets are minimal obstructions and duplicate witnesses must be identified. Structurally the rook graph has 36 Cartesian squares. Shrikhande neighborhoods are induced 6-cycles, so each of its 48 adjacent pairs produces a distinct diamond with a unique nonedge diagonal; the other 24 nonedges generate 12 induced squares counted twice, yielding 60 distinct quartets. Independent replay python3 /workspace/review_checks/3.py tests actual available length-two routes on every labelled subset rather than testing a precomputed obstruction family. It confirms both complete coefficient vectors, the 96 size-nine rook optima and 32 size-ten Shrikhande optima, then tests every pair of optima for symmetric difference two (none). The orbit of one optimum under separately adjacency-checked generators equals the entire optimum family in each graph; no assertion about the full automorphism group is needed. Here exchange means on maximum ordinary visibility sets as explicitly defined, not on metric bases (the phrase ‘minimum-basis’ in the Finding is a terminological slip; the extremal sets and single replacements tested are unambiguous). For the common spectrum, the verified strongly regular parameters give A²=4I+2J, hence eigenvalues 6,2,−2 with common multiplicities 1,6,9. The coefficients at degrees below four agree and those at degree four are 1820−36 and 1820−60.

## originality

PASS

Pass the exact paired ordinary visibility comparison with the Shrikhande census, optimum orbit and exchange isolation, not the visibility polynomial definition or the rook extremal reduction. Prior work explicitly gives the rook square-free characterization and Zarankiewicz maximum, and the little rook extremizer classification follows elementarily from it. Neither the two inspected polynomial papers nor the exact neighbouring catalogue records establish the full paired classification. Same graphs or same numerical entries in a different invariant do not count as equivalence.

## value

PASS

The Shrikhande–rook pair is a canonical equal-parameter, cospectral test of whether a graph invariant sees more than adjacency eigenvalues. Ordinary visibility distinguishes the pair at the first degree where any obstruction is possible, with a structural explanation via diamonds and duplicated square witnesses. The full labelled tables expose further differences and the contrast in optimum sizes, while both distinct optimum families turn out to be transitive yet exchange-isolated. This comparative information is useful beyond the known extremal rook number or a bare claim that cospectral visibility can differ.

The dated certificate retains the supplied scientific assessment, sources and limitations.
