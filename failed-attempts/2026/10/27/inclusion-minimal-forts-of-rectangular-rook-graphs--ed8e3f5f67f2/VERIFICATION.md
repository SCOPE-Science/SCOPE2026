---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For an unselected cell the number of fort neighbors is the sum of its incidence degrees. Exactly the zero/one pair is forbidden, making the two side-coverage conditions necessary and sufficient. If both sides are covered, minimality requires a minimal edge cover, hence stars. A leaf in each class prevents a one-side-covering proper subfort, and a subfort omitting vertices on both sides would require a cycle. If there are no leaves on one side, its stars must all have two edges: degree ≥3 allows a deletion, and degree exactly two forces any proper subset either to leave a degree-one covered vertex opposite an isolate, or to omit an entire row or column opposite degree-one vertices. If just one side is covered, its vertices must all have degree two by deletion; a contained cycle is a fort, otherwise every proper subset that could be a fort would omit vertices on both sides and require a cycle. If both sides have isolates a cycle is necessary. A proper subset of a nonspanning simple cycle can neither keep an entire required side covered in degree two nor contain a cycle; a cycle spanning both sides contains a perfect matching and is not minimal. Counting star components by labeled sets gives S−B−C and the two degree-two exceptions, counted by pairing labeled leaves at each prescribed center. Suppression of the covered side in a subdivision forest gives distinct labeled edges of a simple forest, with an isolate still present. Cayley and subtraction of the no-isolate EGF give U. Alternating undirected cycles on fixed labels have k!(k−1)!/2 orders. For p≤q there are spanning forests of size q (one row star and p−1 single edges) and of size p+q−2 (complementary row- and column-centered stars); subdivision forests have 2p edges and require q≥p+2; cycles top out at 2p off the square diagonal and 2p−2 on it when present. This checks both extrema, including 2×2 and 2×3. My independent subset-DAG check matched the polynomial on all ten frozen boards and two transposes (1,189,956 subsets), and the set classification both ways on boards with at most 16 cells. Replay: python3 /workspace/branches/reproduce_frozen.py rook; log /workspace/branches/reproduction-rook.txt. These checks are finite, not a replacement for the coverage and counting arguments.

## originality

FAIL

A distinct indexed record gives the same all-size taxonomy and the same exact labeled polynomial in an equivalent generating-function format. This is demonstrated scientific coverage, not a priority attribution from its later path date. Primary literature checked here establishes some components and general context but is not the cause of the full-claim failure.

## value

FAIL

A full minimal-fort classification of this natural product graph would have clear intrinsic value. This package, however, does not add a distinct usable result beyond the equivalent recorded taxonomy and polynomial: the extrema are recoverable from those families, and the finite-board computations corroborate rather than extend the known coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
