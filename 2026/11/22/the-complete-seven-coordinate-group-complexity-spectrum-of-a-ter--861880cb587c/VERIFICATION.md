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

Because mu has no image beginning in 1 and any 1 is the last symbol of 01, 11 never occurs in its fixed point; 00,01,10 all occur in 01001. In the psi(mu^4) tiling the block lengths are 11 and 7, so a length-seven factor meets at most two blocks. Independently generated pair windows give exactly the nine listed factors: two isolated Parikh classes and the seven rotations of 0012012. Every intransitive group is contained in the full stabilizer of one of the 63 proper coordinate bipartitions, with complexity no smaller than that block group's; sorted restricted-color strings reproduce the published bipartition table and realize every value 5 through 9. For the transitive groups, ASU degree-seven data supply the exhaustive conjugacy types. An independent computation constructs four affine groups and the binary linear group by ordered bases, uses canonical orbit representatives for all factor permutations, and normalizes counts over the 5040 coordinate bijections by the independently calculated normalizer size of each representative. It reproduces all five histograms and none contains 4. For A7, adjust any odd matching permutation by an odd stabilizer interchanging equal letters; thus A7 and S7 give 3. This exhausts subgroups under their full ambient actions, not merely generator moves within the factor set.

## originality

PASS

Credit prior work for the type-III construction, the ordinary/abelian endpoints at the stated standard length, attainability of 5 through 9, and the intransitive exclusion of 4. The distinct remaining assertion is that no transitive subgroup attains 4 at this exact word and length, together with the explicit conjugacy-type histograms. Thus the displayed spectrum is new here only in the sense of completing a partially known spectrum.

## value

PASS

Length seven is an early odd standard-image length (psi(01001) has length seven) in the range of the prior transitivity obstruction. The exact all-subgroup negative answer supplies a checkable instance for Open Problem 3 where the generic argument genuinely leaves cases, and the full histograms distinguish five candidate transitive actions at exactly that unresolved boundary. The motivation is the exclusion of 4, not the already guaranteed positive attainments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
