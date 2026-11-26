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

For every n≥1, the support product of two nonidentity classes is exactly the row support of the first times the column support of the second. The quantified lifting condition is precisely saturation of every such rectangle; products with the singleton external identity are automatic. Same-colored cells must agree in both palettes, since membership in any product rectangle is tested by its two palettes, and that condition is also sufficient. Disjoint row palettes force identical column partitions in the two rows; one shared color forces identical row palettes globally. In that case linked columns have identical one- or two-color palettes, yielding unique groups and either a monochrome group or a crossed unordered proper bipartition. A group of size s has 2^(s−1) choices, giving the stated Stirling sum and the exponential generating function by the exponential formula. Automorphisms permute the intrinsic row and column coordinates independently; any orbit crossing rows requires a row flip preserving each orbit, hence balanced splits. The subgroup of within-part column permutations together with one simultaneous row flip and swaps of balanced halves gives exactly those orbits. Left and right multiplication extract the coordinate equivalences of a congruence, giving exactly 2B_n with singleton identity. For n≤2 no unbalanced split exists, whereas the displayed n=3 example is one. A separate exhaustive run over cell partitions for n=1–5 reproduced D=2,5,16,64,309; the O and congruence columns were checked by the proved formulas. The uploaded verifier was inspected, not run; its main check does enumerate through n=5 despite a stale four-column docstring.

## originality

PASS

The exact separated and balanced orbit-realizable subfamily is already covered by two indexed Schur classifications, as the frozen result expressly credits. The distinct part is the full classification and count for the weaker setwise dimensionality condition, including unbalanced splits and the resulting exact non-orbit boundary. Neither checked Schur classification supplies those additional partitions and multiplicities; Jenča's general framework does not classify this family.

## value

PASS

The natural family compares support-based equivalence, automorphism orbits, congruences and the stronger Schur closure on the same labeled objects. The full classification identifies exactly which arrangements separate the support and orbit notions, gives the first and smallest counterexample within the family and counts the separation for arbitrary n. This is a structural boundary, not merely another enumeration of the known balanced subfamily.

The dated certificate retains the supplied scientific assessment, sources and limitations.
