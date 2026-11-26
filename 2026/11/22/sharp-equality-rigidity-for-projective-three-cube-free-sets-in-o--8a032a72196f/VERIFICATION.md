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

Write B=G\A and S=A∩2⁻¹A. Because doubling is bijective, |S|≥2|A|−N, and 0∉A by the all-zero cube. If S is empty the bound is already strict. Otherwise for any x∈S the cube (x,x,y) forces B, B−x and B−2x to cover G, hence 3|B|≥N. At equality the cover is disjoint for every x∈S, so subtraction of the indicator partition at y and y+x makes 3x a period. Now |S|≥N/3 and 0∉S, whereas a proper subgroup of an odd-order group has at most N/3 elements including 0. Thus S generates G, and 3G is a period subgroup. Projection preserves a forbidden cube and any quotient cube lifts into a full inverse image, proving the exact correspondence. Rank one forbids 0 and leaves only the two nonzero elements. In rank two the three-point complement contains 0. If its two nonzero points were independent, send them to e₁,e₂: the generators (0,2),(1,2),(1,2) then produce (0,2),(1,2),(1,1),(2,1),(2,0), all outside that complement. The remaining possibility is a line. Complements of all index-three subgroups are free because any triple of nonzero ternary residues contains either an opposite pair or three equal residues, producing a zero subset sum. Linear forms modulo nonzero scalars give the claimed count, and the primary decomposition identifies r=1 with a cyclic three-primary component.

## originality

PASS

Pass is for the structural equality result, not for the translated-complement density argument or cyclic sharpness, which Meng already supplies. The global period subgroup, quotient bijection and exact low-rank classifications were not covered by the compared statements.

## value

PASS

This is an equality-structure theorem for a known sharp density problem. The forced period reduces all finite odd ambient groups in scope to elementary ternary groups, giving complete classifications at ranks one and two and an exact uniqueness criterion across arbitrary ambient orders. It makes the remaining work a higher-rank quotient problem rather than claiming a complete census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
