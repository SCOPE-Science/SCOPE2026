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

Deleting the first, middle or last adjacent pair from abcd gives cd, ad or ab, so at least ⌈q²/3⌉ words are needed. I checked the seven local templates by this exact rule: the 2×3, 3×2, 3×3, 3×4 and 4×3 templates hit every cell once; 2×2 doubles exactly local cells (0,0) and (1,0), and 4×4 doubles exactly (1,3) and (3,3). All templates have three distinct outputs per word. For q≡0 mod 3 the Cartesian blocks are all 3×3; for q≡1 or 2 there is one exceptional square of side 4 or 2, respectively, including q=4 or 2 with no other blocks. Source words from different rectangles cannot coincide, since their row and column coordinates identify the rectangle. Thus the block partition lifts the finite certificate to all q≥2 and proves both optimality and the multiplicities of the exhibited family. No claim about the multiplicities of every optimal cover is needed. The uploaded script was not executed; the required finite certificate was checked by direct enumeration.

## originality

FAIL

An earlier published Resultary theorem for alternating alphabets X×Y×X×Y already proves the stronger rectangular optimum ⌈mn/3⌉ and explicitly specializes it to the same q-symbol formula. Its three-edge-path construction also already gives the asserted two distinct doubled outputs in the balanced nondivisible case: its 2×2 base doubles 00 and 10, its 4×4 base doubles 13 and 20, and the strip extensions leave those multiplicities unchanged. The different 4×4 word list and block presentation do not establish a distinct scientific claim.

## value

FAIL

The exact burst-covering parameter is natural and useful, but this record recomputes a known narrow invariant. Even the asserted balanced overlap behavior follows directly from the earlier construction. The replacement local word lists do not offer a new bound, guarantee, or motivated optimization, so there is no independently valuable distinct remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
