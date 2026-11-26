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

On a connected cubic graph, a surjective FAT coloring with at least two colors has a positive integral off-diagonal neighbor count, so at most four colors are feasible. The two constant layers always give a FAT two-coloring. With three colors, each vertex sees all three colors once. Over F_3, if u_i is an ordered column and J swaps layers, the rule u_(i+1)=-u_(i-1)-Ju_i gives u_(i+3)=Ju_i. The 36 seeds are exactly the two-column assignments (a,b),(c,d) with a!=d and b!=c: the missing colors complete the next column, and these inequalities propagate. When 6 divides n all seeds close; when n is three modulo six, every column must be invariant under the swap, leaving six colorings. If 3 does not divide n, equal color-class sizes are impossible, also by double counting opposite-color edges. With four colors each vertex and its three neighbors use every label. Consecutive columns use complementary pairs, and after two columns each pair comes back in the opposite order, forcing period four and giving 4*3*2=24 seeds exactly when 4 divides n. Requiring each named color to occur makes the palette action free, so the unnamed counts divide by 3! or 4!, with no graph-automorphism quotient. A new local transfer check matched all 36 census cases for n=3..20; it corroborates rather than proves the infinite classification.

## originality

FAIL

The submitted all-order classification is mathematically covered by the inspected statements, not just similar colorings of the same graph. The earlier indexed strong-odd transfer table gives exactly the FAT-four subfamily and count after the local rainbow filter. The separate neighborhood-3-balanced indexed result gives the identical full FAT-three census and rigidity, and extends it to a second closure type. Published earlier work already gives the three-color existence test. The chromatic and unnamed spectra then follow from elementary degree bounds, a layer coloring, and freely permuting labels. This is a decision about distinct scientific content in the existing record, not a finding that the later-dated exact three-color census has historical priority over the frozen result. It does not rely on inaccessible literature.

## value

FAIL

Exact counts and rigidity on a natural all-order ladder family are worthwhile in principle. In this submitted scope, however, the useful classification and both exact censuses are already available through the inspected equivalent local formulations. Expressing them as a maximum over palettes and dividing by the palette factorials provides no additional exact invariant or structural consequence beyond those mechanically recovered results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
