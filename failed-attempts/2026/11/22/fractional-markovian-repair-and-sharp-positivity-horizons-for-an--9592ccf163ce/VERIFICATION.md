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

Write L=N(I−P₀)−Σ k_j(1+a_j)P_j where P_j projects onto mean-zero vectors supported on block j. This gives the stated orthogonal spectrum, with a simple zero mode and positive complementary eigenvalues. The spectral heat kernel has within-block distinct entries F_j/k_j, positive cross-block entries for positive time and positive diagonals; row sums are one. In s=N^αt and d=d_j^α, the sign of F=u+qe^(−s)−e^(−ds) is positive for s>0 when d≥q by strict Jensen. When d<q, multiplying by e^(ds) gives a strictly convex function with negative initial slope and limit +∞, hence one positive crossing with the claimed signs. Off-diagonal rate signs give the same Markov threshold; rows yield the ℓ∞ norm by adding twice the negative mass, and symmetry gives the ℓ¹ norm. Differentiating the scalar F gives the unique active-block minimum at the stated peak time. Writing δ=q−d, F/s extends smoothly at zero with expansion −δ+(qu/2)s+O(δs+s²). The nontrivial root is 2δ/(qu)+O(δ²); the derivative root gives minimum −δ²/(2qu)+O(δ³). Substituting δ=q log(N/λ_j)ε+O(ε²) gives both sharp coefficients, and maxima over finitely many critical blocks preserve the errors. For λ_j↓0, F(s) tends to q(e^(−s)−1)<0 at any fixed s>0, so the positive crossing escapes to infinity and the root equation gives λ_j^α τ_j→−log u_j. The last statement is blockwise and does not cover λ_j=0. Frozen numerical support was inspected but not executed.

## originality

FAIL

The exact Markov threshold, recovery, peak/norm, and both onset laws are already determined by the earlier unsigned complete-multipartite formulas via an exact blockwise reparametrization, despite the difference in physical edge signs. Take β_j=α/α_j and compare block j to the only nonsingleton part in the unsigned graph K_{k_j,1,…,1} on N vertices. With s=N^αt, q_j^(β_j)=d_j^α, so its scalar H_j(β_j,s) is identical to F_j(α,t). Its natural unsigned time is t′=N^(α−β_j)t. In fact a row from block j agrees with an unsigned row at t′ up to labeling: the within-block off-diagonal formula is identical, the cross-block entries share (1−e^(−s))/N, and both diagonals are fixed by row sums. Thus the β=1 boundary and all sharp single-part formulas transfer exactly; the full signed statements follow by taking the relevant block maxima. Near α_j, β_j−1=ε/α_j, and −log q_j/α_j=log(N/λ_j); time rescaling gives exactly the stated constants. The one-sided λ_j↓0 expression was not found stated in that comparator, but follows directly from its exact root at large β_j, with no further model-specific calculation. The frozen record is not accepted as a distinct full classification.

## value

FAIL

The signed positivity question is natural, but the quantitative content of this particular model reuses the exact unsigned row curve, with a block-dependent exponent and time substitution and finite maxima. The explicit spectral-degeneracy coefficient is obtained immediately from the same root and does not establish a separate substantive gap here. The record does not show a new recovery mechanism or independently nonroutine invariant beyond the already evaluated row family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
