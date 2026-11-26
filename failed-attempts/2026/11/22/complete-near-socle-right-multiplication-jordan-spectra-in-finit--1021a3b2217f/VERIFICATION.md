---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With z=α+β+γ in degrees n−2,n−1,n, multiplication vanishes on source degrees ≥3 and its square vanishes since 2(n−2)>n. If α≠0, the perfect top pairing makes the degree-two source surject onto the one-dimensional top degree. Modulo this top image, the scalar source has an independent component α in degree n−2, and the degree-one source contributes the rank of v↦v∧α in degree n−1. This last map is represented under volume duality by the alternating bilinear form (u,v)↦vol(u∧v∧α); complementary basis monomials show an isomorphism with the space of all alternating forms. The argument uses alternation, not division by 2. To count rank 2r, choose the radical of codimension 2r, then a nondegenerate alternating form on the quotient; symplectic bases give |Sp₂ᵣ|=q^{r²}∏_{j=1}^r(q^{2j}−1), and dividing |GL₂ᵣ| by this yields the frozen product. Each nonzero α has q^{n+1} lifts. If α=0 and β≠0, the scalar and degree-one inputs give two independent image directions by the same perfect pairing; otherwise γ≠0 gives rank 1 and zero gives rank 0. The cases partition the entire ideal of dimension binomial(n,2)+n+1. Square-zero means the Jordan partition is determined by rank. For n=5,q=2 the vector is (1,1,62,9920,55552), matching the recorded exhaustive result. The recorded q=3 exhaustive check is of homogeneous cubic contraction ranks 0,2,4, not of all inhomogeneous operator ranks; its smaller scope is consistent with the statement of verification.

## originality

PASS

Qualified to the literal extension to arbitrary n≥5 and finite fields, including all inhomogeneous lifts. The exact n=5 characteristic-two distribution and lift invariance are already covered, and the alternating-form numbers are classical. The strongest available multiplication source proves the same graded rank mechanism for n=5, not an all-n/all-field theorem that specializes to the frozen scope. There is very little conceptual new content in extending that proof (see value); that is not a claim that the full quantified theorem was found verbatim or follows by specializing a broader independent multiplication theorem.

## value

FAIL

Rank fibers of a radical layer are natural, and the result is correct. The remaining extension does not supply a distinct nonroutine rank mechanism: the overlapping five-generator proof has exactly the three graded inputs and the same independence of higher lifts. Replace grades (3,4,5) by (n−2,n−1,n); the top pairing, one extra scalar direction, and alternating middle rank are unchanged, including in odd characteristic. The covering count of alternating forms is standard and the number of higher coefficient lifts becomes q^{n+1} by free choice. Thus both the claimed rigidity and the precise new weights follow by routine dimension reindexing and the known linear-algebra count, not by overcoming a new exterior-algebra obstruction. The broadened scope is a convenience, but does not establish independent mathematical value under the standard for narrow exact invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
