---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Independent all-n check: filter the oriented-incidence complex by the number of left arrows. With none, the join of the n two-choice right-arrow complexes is an (n−1)-sphere. Adding one left arrow attaches a cone along a cone: at its target just the opposite right arrow is available. Hence the subcomplex Y with at most one left arrow has the same equivariant homology as the join. The relative chains of (X,Y) split over ordered pairs A_i,B_j and are the augmented right-link chains shifted by two. For i=j the right link omits target i; for i≠j the target choices Y_i and X_j form one 0-sphere (both together make the forbidden four-cycle), joined with the n−2 remaining choices. Thus relative homology is n² lines, all in degree n. The boundary of a diagonal relative generator [A_i,B_i]*z (z the join cycle on remaining right vertices) maps, by using the two one-arrow cones, to (X_i−Y_i)*z up to sign, a generator of H_(n−1)(Y). This gives concentration and rank n²−1, including n=2. Without the left swap, f² relative lines are fixed, each with sign sgn(σ). With the swap, a fixed point of σ gives one diagonal line with sign (−1)^n sgn(σ), while a two-cycle fixes two off-diagonal lines with the opposite sign: the two left vertices and the paired target choices each reverse, the remaining n−2 right factors reverse, and the sign of the permutation of those factors is −sgn(σ). Subtract the single join line, of character (−1)^{ne} sgn(σ), to recover both formulas. The signed exterior-square, standard and unordered-pair traces give the stated rational module.

## originality

FAIL

A distinct earlier published record gives the identical full character for n≥3, with the equivalent rational homology module upon the known concentration. The only additional parameter is n=2 for the specified subgroup, not the full larger automorphism group. This is established prior coverage of the substantive all-parameter character, not a rejection based on an unavailable article. A distinct same-day integral record separately overlaps, without establishing intraday priority.

## value

FAIL

The general equivariant invariant is mathematically natural, but the full interesting family and its rational module already have a complete character in the earlier record. The remaining rank-three n=2 restriction is a direct tiny instance without a substantive motivation here, notably excluding the extra bipartition-swapping symmetry that distinguishes this graph. Repackaging the known rational module or adding finite checks does not supply a valuable surviving finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
