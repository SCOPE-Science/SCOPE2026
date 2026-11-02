---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The final theorem uses the real two-dimensional norm N_8(s,t)=max{|s|,|t|,(|s|+|t|)/√2}, unit Birkhoff pairs x⊥_B y characterized by a norming functional that annihilates y, and oriented (not symmetric) ||x+y||. Its polygonal reduction is exhaustive: D8 symmetry takes any x to the relative interior of E=[(1,√2−1),(√2−1,1)] or its endpoint. On E, the unique support f=(s+t)/√2 forces y=±(1/√2,−1/√2); direct max-facet calculations give affine lengths U−(2−√2)t and L+(2−√2)t with L=3√2/2−1 and U=1+1/√2. At the vertex a=(1,√2−1) the support segment from (1,0) to (1/√2,1/√2) annihilates precisely the two-arc partner sector y=(s,−1),0≤s≤√2−1, and y=(s,s−√2),√2−1≤s≤1/√2, plus their negatives. Independent symbolic SymPy arithmetic over Q(√2) checked eight support halfspaces at both endpoints for all six affine norm pieces (two smooth-edge and four vertex arcs), and checked partner unit arcs and supporting-functional signs; endpoint interpolation proves each formula for a continuum. Both L and U have explicit Birkhoff witnesses and the smooth edge fills the whole interval. Applying Du–Li's definitions yields exactly the reported moduli and ρ_B=3δ_B. A separate symbolic check independently reproduced the 2024 published standard-octagon witness under an explicit linear isometry. This C PASS concerns mathematical truth only and does not imply O or V.

## originality

FAIL

Martín and Papini (2024), Section 5 Example 5, already determines the minimum and maximum Birkhoff-orthogonal unit-sum lengths for the regular octagonal plane and provides a common extremizing pair with exact expressions. Its regular octagon is linearly isometric to the assigned normed plane, not merely numerically similar. Du and Li (2023) already define δ_B and ρ_B as simple transforms of those endpoints. Martín–Papini Proposition 3 cites the Jordan-curve structure of the oriented sum set; the remaining full-interval wording follows by continuity (also immediately from the smooth edge). Therefore all substantive claims are prior-covered despite different symbols and an octagon rotation. No scientific repair is permitted that simply rephrases the known theorem or adds a checker.

## value

FAIL

The quantities are mathematically natural and the regular octagon is a canonical test case; however the precise extrema for this very example were already published in Martín–Papini (2024), Example 5. The remaining δ_B and ρ_B values and their 3:1 ratio are routine affine conversions from those known extrema, and interval filling follows by continuity of the known planar Birkhoff-sum locus. Thus, as an asserted new finding, the package amounts to a known-example recomputation plus routine notational substitutions, without an independently motivated new invariant, boundary, or classification. Its exact checker and presentation do not restore contribution-level scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
