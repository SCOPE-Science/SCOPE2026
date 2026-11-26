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

For the specified finite field, n>=2, a nonzero and a^2!=1, the identity with first input z gives B(h,v)P(z)=0 for every v, where h is the V-component of P(z). Nondegeneracy gives h=0, and idempotence leaves P(z)=0 or z. In the first branch the image of the induced idempotent Q on V is totally isotropic. The two orders of B imply orthogonality of its coordinate images X,Y by the invertible 2-by-2 system with determinant 1-a^2. With dim X=s, dim Y=t, a subdirect r-space is specified by two d-dimensional quotients (d=s+t-r) and an isomorphism between them, giving the displayed Goursat sum. Independent choices of a complementary kernel and a functional on the image contribute q^{r(2n-r)+r}. In the fixing branch the averaging equations reduce to Q^T M=M Q by Q^2=Q. In blocks [A C; D E], they give D=a D^T, C^T=a C and E=A^T; hence C=D=0, including in characteristic two. An image and complement specify each rank-j idempotent A, and fQ=0 gives q^{2(n-j)} lifts, so the rank is 2j+1 with exactly the stated count. If this branch also preserves products, nondegeneracy gives Q=I and f=0. Every r<=n occurs in the killing branch by choosing a subspace of the first summand. Independent hand check at q=5,n=2: the isotropic line count is 6+6+6*4=36, and the isotropic plane count is 2+6=8; the fixing branch gives 625 rank-one maps, 750 rank-three maps and the identity. This gives exactly the asserted example and rank support. Read RESULT.md lines 40–69, VERIFICATION.md, verify_counts.py and exhaust.cpp; the supplied finite checks did not need to be executed and do not prove the all-field theorem.

## originality

PASS

The retraction census for this exact algebra is already known and explicitly credited; it gives the entire socle-killing summand and the identity. The pass concerns the additional non-endomorphic socle-fixing projections and the resulting complete labeled averaging census. The inspected same-rank-support Heisenberg analogue has a different pairing and a different count, and the general averaging criterion does not state or count these projections.

## value

PASS

This is a complete count of a natural relaxation of retractions on the same noncommutative algebra, not just a reformulation. It identifies exactly which additional maps and ranks occur and why many odd ranks above n become possible but no new even rank above n occurs. The formula for labeled maps is useful beyond the illustrated example; the previously known retraction count alone would not resolve the averaging classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
