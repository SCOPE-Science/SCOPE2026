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

A proper named coloring lifts to integer heights on a tree once a root lift is fixed, since every edge color difference has a unique representative in {-1,1}. A legal recoloring at a nonisolated vertex means its neighbors all have the third color, hence the height there can and must move by 2 in absolute value, with the sign preserving unit slopes. The one-vertex case allows either sign. A closed walk restores all edge differences, so all coordinates shift by a common multiple of 3, which is a multiple of 6 by parity. If the shift is 6q, summing the coordinate changes yields L>=3n*|q| and L congruent to 3n*q modulo 2. This forbids odd walks for even n and gives the lower bound for odd n. In a sweep ordered by descending height, each neighbor currently has height one less at the time of the move; lowering every height by 2 in that order is legal. Three sweeps give the necessary 3n-step closed walk, whose minimal odd length implies simplicity for odd n. A leaf can always be moved to the color different from both the old and pending neighbor colors, proving connectedness by induction. Sum of colors modulo 3 is a proper coloring; combined with the parity result and existence of edges this proves the claimed chromatic numbers. The one- and two-vertex graphs are a triangle and a hexagon. For n>=3 there are two nonadjacent leaves yielding independent moves and a square; a triangle would need to vary only a single unconstrained coordinate, impossible with a neighbor. Maximum-independent-set moves exactly coincide with recolorings because a second token in any triangle is illegal. The count follows from independent choices away from a rooted vertex and the probability 2^(1-d) that its neighbors all agree; dividing directed moves by two gives the edge formula (the singleton is direct). Connectedness gives the stated graph cycle rank.

## originality

FAIL

The all-tree diameter theorem by itself does not determine odd girth. But its primary source supplies the stronger walk-realization lemma for every compatible signed labeling, including nonzero constant labels from a coloring to itself, as well as the uniform-shift description and signed toggles. The odd-girth/parity statement is a direct corollary of those actual lemmas and the elementary parity of signed counts, not just an analogy with a prior lifting method. This does not assert that the odd-girth formula is printed in the prior work.

## value

FAIL

The coexistence of squares and large odd girth is a natural feature worth recording, but the exact odd-girth and bipartiteness classification are immediate walk-label corollaries of the already stronger all-tree realization result. The ordinary-girth cases use independent leaf moves and the elementary triangle obstruction; the remaining chromatic and graph counts either follow directly or are known. No distinct nonmechanically implied structural invariant survives in this record as a finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
