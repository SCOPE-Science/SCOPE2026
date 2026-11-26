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

For right multiplication by g^b the basis action on C_m is the affine bijection R_b(x)=tx+(1-t)b. An invariant subspace is invariant under its inverse by finite dimensionality, so it is invariant under R_b R_c^(-1), which translates by (1-t)(b-c). This covers every cyclic displacement. For left multiplications the corresponding difference translates by t(a-c), again covering the regular cyclic action. In either direction closure is therefore equivalent to an ordinary group-ring ideal: the converse holds because every ordinary ideal is a power of (g-1) and is preserved by the two multiplier automorphisms. Over any field of characteristic p, g^(p^s)-1=(g-1)^(p^s), and the ideals of K[z]/(z^m) are exactly (z^a): a nonzero element of least z-adic order a is z^a times a unit. The basis transport multiplies the two automorphic images in this ordinary ring; it gives the stated span even for zero powers and saturated exponents. Induction on the product tree gives J^k for any parenthesization, nonzero for k=m-1 and zero for k=m.

## originality

FAIL

No checked source was found to print precisely this modular left-and-right classification verbatim. Nevertheless it is a direct consequence of the prior Alexander transport and the standard ordinary cyclic regular-module chain. From the published transport one has I*1=alpha(I) for any right ideal and 1*I=beta(I) for any left ideal. Invertibility gives equality, and surjectivity of the other multiplier then gives closure under ordinary multiplication by every element. Conversely all ordinary ideals of the truncated polynomial ring are multiplier-invariant. This mechanically yields the asserted exhaustion in both directions. It is also immediate from the published permutation-module description for the right side, since a quotient of two affine translations gives every cyclic shift, with the same calculation for the left side. The powers and independence of parenthesization are already covered by the prior general augmentation theorem; the pairwise product formula is ordinary multiplication of preserved powers. The failure is deductive prior coverage, not evidence of a verbatim duplicate or reliance on inaccessible literature.

## value

FAIL

Describing all one-sided ideals is natural, but in this precise cyclic case the proposed increment is a routine recognition of the standard regular-module chain, not a new modular obstruction or structural calculation. The ideal count, quotients, exact products and nilpotency add no separate invariant beyond that chain and the previously established transport.

The dated certificate retains the supplied scientific assessment, sources and limitations.
