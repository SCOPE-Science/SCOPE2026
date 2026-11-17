---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The exact constant-source IF-SSPRK2 step is endpoint exponential trapezoid. Its signed error equals (1/2)∫_0^h s(h-s)e^{sA}L_A(Q)e^{sA^T}ds with L_A(Q)=A²Q+2AQA^T+Q(A^T)², and Δ_h=(h³/12)L_A(Q)+O(h⁴). Rank-one Q=vv^T positivity requires A²v in span(v,Av); the maximal-cyclic-vector lemma then forces A minimal polynomial degree at most two. For nonscalar quadratic case A²=aI+bA, universal PSD is equivalent to [[2a,b],[b,2]]⪰0, i.e. 4a≥b², and square completion suffices. Non-scalar Hurwitz A cannot meet this condition, and explicit diag(-1,-2), Q=11^T gives L_A=[[4,9],[9,16]], determinant -17. Independently recomputed witness and safe square-completion identities.

## originality

PASS

Earlier 2026 work establishes positivity preservation for IF-SSPRK2 and a sharp stationary-error correlation threshold in diagonal two-mode Hurwitz dynamics. Neither proves the present global universal all-input, all-step, all-real-matrix minimal-polynomial characterization or rank-one arbitrarily-small-step obstruction. The latter answers a new natural characterization question.

## value

PASS

This sharp all-dimensional necessary-and-sufficient criterion distinguishes merely PSD-preserving time integration from actually overestimating continuous covariance in Loewner order. The minimal-polynomial obstruction and rank-one small-step witness show every heterogeneous stable drift lacks a universal conservative covariance guarantee, directly meaningful for numerical reliability and comparison methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
