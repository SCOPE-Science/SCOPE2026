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

Johnson distance is k-|W∩X|, so a nonresolving family lies in a bisector and a largest one must be a full bisector. Splitting the ground set into the two r-element differences and their complement gives b_r=sum_j C(r,j)^2 C(n-2r,k-2j). I independently expanded the four short-separation polynomials and checked the long-separation quotient by exact symbolic algebra, including the positive denominator-minus-numerator polynomial and the three r=6 seeds. The r=2 base polynomial is 2z+2z^4: degree 3 ties at n=6, and at n=7 the interior coefficients are all positive, which propagates. For r=3,4,5 the bases at 2r+1 are strictly positive in interior degrees; the permitted n=2r cases are evaluated directly. For long separations the base at n=2r vanishes on the bisector side at odd degrees; at even degrees use the checked monotone ratio with fixed j and complement symmetry. The central three Vandermonde terms give the stated strict seed for j>=4; convolution with (1+z) preserves the needed strictness. For r=1 the exchanged pair is the unique pair of indicators always equal: any other pair can be split by choosing a k-set omitting both exchanged elements. For J(6,3) the distance-two families are transversals of three pairs, recovered as the non-co-occurring pairs; none has an always-equal coordinate pair. For J(8,4) the pair incidence counts 6 versus 9 recover the bipartition. Fresh exhaustive witness-pair enumeration reproduced the exceptional bisector-size vectors (8,8,0) and (30,26,18,36), and the distinct optimum counts 30 and 35.

## originality

FAIL

A distinct indexed theorem already gives the exact resolving threshold on a strictly larger Johnson-graph domain. It does not explicitly claim the full optimizer census, so that part was separately tested against the proof. Retaining a positive summand in its existing coefficientwise argument gives the strict comparisons, apart from the one directly visible distance-two tie and the already covered antipodal exception. Its existing bisector membership criterion then yields the families and counts by direct pair or block recovery. The stated remainder is thus a routine extraction from that proof, not an independently established new extremal phenomenon.

## value

FAIL

An optimizer classification for a natural graph invariant would ordinarily be useful, and knowing the special tie prevents treating every adjacent bisector as the only possible witness type. Here the exact threshold is already known, and the remaining classifications are obtained by the immediate strictness and coordinate-recovery checks on the existing proof and membership rule. This adds an explicit account but no distinct nonmechanical exact invariant or extension of scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
