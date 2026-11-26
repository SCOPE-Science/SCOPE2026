---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The spatial and temporal residuals of F(P)−Q,F(Q)−P give the displayed four equations. On this orbit locus, c,d≠0 implies w≠0 by Aw=2μcd; c,w≠0 implies d≠0 by Cd=2μwc (the frozen prose's reference to the third equation is an adjacent-equation slip). Thus the two descriptions of the class agree. The three squared identities force A,B,C to have a strict common sign, shared by M=(A+B)/2. For an independent determinant derivation put v=(2μw,2μc,2μd) and differentiate the four residuals in u,w,c,d coordinates. The resulting symmetric block matrix has upper-left entry M+γ−1, off-diagonal block −v, and lower 3×3 block T with diagonal A,B,C and off-diagonals −v₃,−v₂,−v₁ respectively. The same invertible orbital transform on input and output makes its determinant equal to det(I−DF(Q)DF(P)) by the 2×2 block Schur formula. Writing D=diag(v), the orbit identities give DTD=ABC(2I−11ᵀ). Since (2I−11ᵀ)⁻¹=(I−11ᵀ)/2, one obtains det T=−4ABC and vᵀT⁻¹v=−(A+B+C). The remaining Schur factor is M+γ−1+A+B+C=4M, giving −16MABC<0. The real monic return characteristic polynomial then has one root larger than 1, so there is a genuine expanding Floquet direction. The supplied symbolic script was inspected, not run.

## originality

PASS

The supported distinct result is the exact determinant sign and positive expanding multiplier for the specified primitive branch over the whole real parameter family with μ>0. The older economic-map stability study is the strongest priority risk: its accessible abstract confirms scope in periodic-cycle stability but supplies no classification matching this branch. A later same-family chaos theorem is not an implication about every such cycle. These comparisons do not establish exhaustive priority.

## value

PASS

This is a parameter-uniform obstruction to attraction in a natural symmetric map, identifying which side of +1 a real multiplier lies on without a case-by-case existence or bifurcation classification. The class is nonvacuous even inside the population square: for μ=7/2 and γ=0 the cycle (6/7,5/7)↔(3/7,5/7) has c=d=3/28 and w=−1/28, with multipliers −5/4 and 9/4. This also demonstrates why an expanding direction does not always mean a saddle. The identity applies without restricting to that uncoupled example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
