---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Under exactly regular Morley geometry, Tran’s affine formula l_j(M_i)=t_i q_ij and q_ii=1 yields a=n_i-n_j with a·v=(q-1)(t_i+t_j), |a|^2=(q-1)^2(q+2), |v|=L. Thus ||P_{v^perp}a||^2=(q-1)^2 epsilon. The other n−1 Morley vertices relative to the edge midpoint lie in v^perp, with Gram G=(L^2/4)(2I+J), invertible with G^-1=(2/L^2)(I-J/(n+1)). Their a-pairings are the candidate r_k, so the boxed Q equality follows in every n>=3. The source two-projection inequality gives |t_i-t_j|<=L sqrt((2-q)/(q+2))*sqrt(epsilon). Cauchy–Schwarz with ||w_k||=sqrt(3)L/2 gives the weighted-row bound. The quadratic form eigenvalues 1 and 2/(n+1) give exactly the stated aggregate bounds. At epsilon=0 all rows and scales agree. The equivalent derivation directly from published Theorem 2.3 is verified symbolically and is the basis of the originality rejection, not a correctness error.

## originality

FAIL

The audited equality is a direct algebraic corollary of Tran’s all-dimensional published Theorem 2.3, Eq. (4): H=4K(D^2-dd^T/(n+1))K with D=diag(t_i/(sqrt(2)L)). Taking the (e_i-e_j) contrast gives the complete weighted row-square energy; translating its entries by their special-pair mean immediately yields exactly the candidate centered Q=(L^2/2)(q-1)^2 epsilon. No new hypothesis or nonstandard lemma is required. Tran’s Proposition 3.2 additionally gives the quantitative projection inequality that rearranges to the claimed t_i-t_j bound. The pointwise bound follows by Cauchy–Schwarz and the elementary regular-simplex perpendicular-bisector length. Thus the candidate is materially covered as a corollary of stronger prior source statements, not just a differently titled potentially new result.

## value

FAIL

The weighted Morley row difference is a natural symmetry diagnostic, and the reformulation can be useful pedagogically. Nevertheless the displayed exact energy is only a centered (i,j) contrast of the published complete normal-Gram equation, the t-gap bound is a rearrangement of Tran’s printed projection inequality, the pointwise estimate is Cauchy–Schwarz, and the aggregate inequality is the textbook spectrum of I-J/(n+1). The result does not establish an independently unknown exact natural invariant, new extremal case, new realizable optimal stability exponent, or independent structural theorem beyond these mechanical deductions. The mathematics is correct but intrinsically too derivative to be accepted as a distinct valuable research finding; no paper-sized generalization was demanded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
