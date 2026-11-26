---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Complete matchings are in bijection with fixed-point-free involutions via their one-line permutations, and each lower cell is an ordered subsequence, not an unordered support. The deletion faces give the cellular differential, including augmentation to the empty word; characteristic two makes each two-position deletion occur twice and cancel. A separate exact Python replay, not the supplied program, generated 1, 3, 15 and 105 full words and reproduced both conventions for computing the boundary ranks. For n=8 the cell counts were (8,56,336,1680,3612,2677,840,105) and ranks were (1,7,49,287,1385,1933,735,105), beginning at degree zero. Rank-nullity on the augmented complex gave the complete Betti vectors (0,0), (0,1,1,0), (0,0,3,19,0,0), and (0,0,0,8,294,9,0,0). These are all even sizes up to and including 8, so the first occurrence follows without extrapolation.

## originality

PASS

Earlier general techniques and low-degree vanishing for the same class do not give its positive mod-two ranks or the first three-degree occurrence. Related exact computations use different generator sets. The searched exact record is the same assigned item; the comparison is not a historical-priority certification.

## value

PASS

The double-transposition-type generalization to all perfect matchings is a natural uniform conjugacy-class family of permutation complexes. The calculation is bounded by a meaningful first-occurrence criterion rather than by a claim of convenience at n=8. The precise three-degree onset establishes a concrete obstruction to models predicting homology supported only in one or two degrees for this family, and the full vectors distinguish the smaller sizes and give tests for future structural formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
