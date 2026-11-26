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

Over F_q the equation in the affine chart is w−λw^((q+1)/2)=0 with w=y²−2x, so w=0 for the permitted λ; the point at infinity is unique. Over F_{q²}, N(y)−Tr(x) lies in F_q. As λ≠0, w^((q+1)/2) lies in F_q, equivalent for w≠0 to the square criterion w^((q²−1)/2)=1. With w=t², y=c+dθ, t=a+bθ and θ²=D a nonsquare in F_q, the equation is (1−λ)a²+D(1+λ)b²−2Dd²=0. It is a nonsingular conic after projectivizing the ternary form, hence gives q² affine triples and q³ quadruples after the free variable c. The zero root occurs in exactly q quadruples; the others pair under t↦−t. Thus the count is (q³+q+2)/2, and subtraction and division by two gives the degree-two closed-point count. The λ=0 comparison follows by taking q trace preimages for each of q² values of y, then adding infinity. The action is over F_q, so the non-base rational points form a union of geometric orbits. Their number is exactly the size of one tame short orbit, less than a long orbit, using the generic range of Theorem 4.25 and Proposition 4.26. An independent enumeration for the six allowed parameters of F_9 returned 10 and 370 over F_9 and F_81 respectively. It is a nonprime-base check, not an all-q proof.

## originality

PASS

Credit the pencil, its base-field conic, smoothness, the Hermitian count and the classification of geometric orbits to existing geometry. The supported distinct content is the uniform generic F_{q²} count, and hence the arithmetic selection of one tame orbit. No existing coverage of that distinction was established.

## value

PASS

The exact first nontrivial extension count separates the Hermitian member from every permitted non-Hermitian parameter and determines which types of geometric points can occur over the quadratic extension: exactly one of the two same-length tame orbits occurs. This imposes a concrete arithmetic constraint on further zeta-function and group-action study independently of the known geometric classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
