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

The antisymmetric subspace gives (1−t)u and the two-dimensional block has diagonal ((1+t)u,1) and off-diagonal √2 s√u. Positive definiteness follows from 1−t>0 and the block determinant u(1+t−2s²)>0. The existence of a scaling with condition number at most K is equivalent to feasibility of W≼C≼KW for positive diagonal W, using W=λ_min(DCD)D⁻² in the forward direction. Averaging a feasible W with the first-two-coordinate interchange preserves this bound, so the block-constant minimization gives the unrestricted optimum. The largest eigenvalue is λ+ from the block. The ratio λ+/((1−t)u) strictly decreases by entrywise comparison of the positive block divided by u, while λ+/λ− decreases then increases about u₀=1/(1+t) by the trace divided by square root of determinant. Their order is determined by det(B−(1−t)u I)=2u[t−s²−t(1−t)u] since λ+>(1−t)u. There is a crossing to the right of u₀ exactly when s²<2t²/(1+t); this gives the stated unique symmetric minimizer or otherwise u₀. At the crossing the top eigenvalue is 1+2tu, giving the first formula for K; the balanced block directly gives the second. Equality at the transition and the Jacobi iff s=t follow by substitution. At t=9/10,s=4/5, u=26/9 and K=279/13, whereas the antisymmetric unscaled eigenvalue is 1/10 and the largest is (29+√593)/20. On the near-singular path, q−s²=ε(1−ε)(2−ε−2ε²)/(2−ε²)>0 throughout 0<ε<1/4, and substitution gives the displayed exact K. The unscaled block has determinant ε(2−ε) and trace 3−ε², so its smaller eigenvalue is asymptotic to 2ε/3 and the unscaled least eigenvalue is ε² for small ε. This proves the limit 3/2, not a family-wide upper bound. The frozen uniqueness claim is only within the symmetric representative class.

## originality

FAIL

Kolotilina's primary 2004 Russian paper (English translation DOI 10.1007/s10958-005-0488-1) explicitly supplies positive diagonal optima, the repeated-versus-simple spectral regimes and optimal condition numbers for irreducible quasireal Hermitian SPD 3×3 matrices. The entire frozen family is real, strictly positive and irreducible, so its pointwise classification and Jacobi criterion are direct specializations, verified below. The near-singular witness does not rescue the claimed classification: the exact path and limit also appear in Resultary 4996ec89d4c9 together with a strictly stronger bound, without inferring priority from that record's later catalogue date alone.

## value

FAIL

The positive three-variable family is a natural illustration of Jacobi's limitations. As a proposed research classification, however, its pointwise content merely specializes an existing explicit order-three solution. The exact limit along one path is useful as an example, but the identical path and its stronger sharp gap classification are already in the indexed isosceles record. There is no established distinct surviving scientific conclusion here beyond the covered classification and an illustrative substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
