---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For p>=1, q>=2, edge gradients are independent coordinates of the polar cube. A returning two-edge arm has squared uncentered contribution 1 rather than 5; choosing the better straight-arm sign increases centered squared norm by at least 4-8/N>0 since N=1+p+2q>=6. Thus only fully straight long arms maximize. Direct imbalance of 3 sum(long signs)+sum(short signs) gives d=0,1 or exceptional 2. Opposite polar facet normals force global radius from the origin. The contact-binomial sum and the groupwise sign zero-sum representation yield the stated rank and p=3 parity dimension. Own exact exhaustive signed-gradient checks for arm vectors (1,2,2), (1,2,2,2), (1,1,1,2,2) and exact rank checks for p=3,q=2..5 match all stated norms/contacts/dimensions; these are finite corroboration, not an all-p,q proof.

## originality

FAIL

REJECTED: the earlier November 8 scalar/Hilbert spider variance theorem already gives the same uniform-vertex scalar variance and equality gradients for arbitrary arm lengths. For p short length-one arms and q length-two arms, its scalar weights become 1/N and 3/N and the maximal polar squared norm is N times its maximal variance, exactly p+5q-d²/N. Its maximizer condition yields identical contact signs, while the centered contact rank follows by elementary linear algebra. Additionally the present batch arbitrary-arm theorem contains this as a literal specialization. The p=3 parity table is a simple binomial/sign-rank evaluation, not an independently unentailed claim.

## value

FAIL

The exact mixed-arm formula is mathematically valid, but it is already a special-case computation of the stronger published weighted-spider scalar sharp-variance theorem. Tangent multiplicities, sign-space rank and the p=3 parity profiles are routine consequences of that full equality classification, rather than a new independently needed invariant. A correct calculation and verification script do not rescue a previously covered principal result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
