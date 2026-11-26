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

In the affine chart Z=1 a singularity must have Y=0 and X≠0; eliminating from the equation and the X derivative gives r=-2X² and X⁴=1, equivalent to r²=4. The only point at infinity is smooth by the Z derivative. The smooth plane quintic has genus six. In the superelliptic model all finite branch points have dx of order three and the infinity valuations (-4,-5,-5) for (x,y,dx) show regularity of the six claimed differentials, which are independent by automorphism character in y and powers of x. Raising the denominator to a seventeenth power gives the F_t^(4i) coefficient rule; its parity and degree give the invariant-block structure, with seventeenth roots not affecting invertibility. Independently checked the whole exceptional-locus calculation in the original plane model, replay python3 /workspace/check_quintic.py, returning PLANE_FROBENIUS_OK. The exact sequence for the plane hypersurface identifies H¹(O_C) with H²(O(-5)); in the Čech basis of monomials with negative exponents -u where u>0 and sum(u)=5, Frobenius takes seventeenth powers then multiplies by F^16 (since F^17/F=F^16). The (v,u) entry is the coefficient of exponent 17u-v of F^16, computed exactly by multinomial expansion in F17[r]. There is one invariant 2x2 block of determinant 5(r²-4)^4; the remaining scalar entries are 2(r²-5)(r²-13) twice, 6(r²-5), and 15(r²-4)^4(r²-5). Each block is zero or invertible on the smooth locus, so the semilinear first and stable ranks coincide. The stable Frobenius rank on H¹(O_C) is the p-rank and the dual Cartier kernel has dimension six minus the first rank, giving (2,4), (4,2), (6,0) as claimed, without relying on finite parameter sampling. Ohashi's §3.3 confirms that the squared parameter classifies these models and that the full automorphism group is cyclic of order eight when r≠0 (the r=0 member has order sixteen). Alternatively ±r are isomorphic by scaling X by a square root of -1 and scaling Y, and the two exceptional squared values give different ranks, so they cannot be isomorphic. Both exceptional parameters are nonzero and smooth. No superspecial case can have the positive stable rank obtained here. The uploaded checker was inspected but not executed.

## originality

FAIL

Resultary dffe580fe6e3 covers the same family in every prime characteristic p>13 congruent to 1 modulo 8. It explicitly gives the characteristic-17 p-rank strata and supplies an all-parameter invariant Cartier decomposition that mechanically gives both a-numbers, although its scope paragraph does not itself claim a-numbers. The two class and automorphism statements follow from Ohashi's model classification. Recomputing in the reciprocal parameter and giving the a-numbers explicitly do not leave a distinct mathematical remainder.

## value

FAIL

The stratifying invariants of this moduli family are worthwhile, but the exact p-ranks were explicitly given, and the a-numbers are immediate kernel counts of the same previously described summands. A second coefficient calculation, a different parameter, or attachment of the already known automorphism classes does not yield a useful independent unknown fact. No validated remainder or repair is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
