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

With zero or one mark, an extension type specifies only a color, since no distinct ordered triple is yet present. With at least two marks, it specifies an oriented gap and a color (already at two marks, C distinguishes the two gaps). For rank at least s+1, each challenged gap must offer a pivot of each color with two child gaps of linear rank at least s; other gaps keep their ranks. Induction thus gives the minimum-of-gaps formula, then the two small-mark formulas. Challenging a fixed color recursively in a linear gap of rank s forces 2^s−1 occurrences; challenging the same color for each of the first two circular points forces 2^(t−1) including those points. In a cycle of 2^(t−1) permutations, the second point chosen in the period starting q·2^(t−2) positions beyond the first leaves at least q(2^(t−2)−1) positions in each open arc; induction by a central period gives each arc the requisite rank. Adding points preserves the induced witnesses, including when nq⁻¹ is not an exact power of two. Rank two reduces to each color appearing twice. An independent game keyed by actual ternary-relation values confirmed that of all 70 balanced eight-position words exactly the eight rotations of 00001111 fail rank three; the other orbit sizes are 2,4,8,8,8,8,8,8,8. A same-color second challenge on the excluded word always leaves an arc without both colors. The finite census confirms the explicit certificate; the universal law uses the proof, not numerical extrapolation.

## originality

PASS

The defining rank and the linear-gap recursion are existing ingredients. The supported distinct claim is the colored ternary circular rank computation with its low-mark exceptions, sharp cyclic size law, and binary extremal classification. Neither the earlier-comparison linear result nor the related circular results cover this combination.

## value

PASS

This is an exact answer for a natural extension-game age with no named cut: separating the early cyclic choices leads to a different sharp per-color scale from the linear problem. The optimal eight-point case shows concretely where color balance is insufficient, rather than just reproducing the exponential order of magnitude from an uncolored two-host comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
