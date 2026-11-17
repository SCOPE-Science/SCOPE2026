---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For any m>=2 positive weighted star, grounding a center leader leaves diagonal follower block with cost sum_{unselected leaves}1/w_i; optimum selects k-1 weakest spokes. With center follower, Schur complement is W=sum leader conductances and trace is sum_{unselected}1/w_i+(m-k+1)/W. For any leaf-only set selecting b>a while smaller a is unselected, either center substitution strictly lowers cost if sum selected <(m-k+1)b or swapping b to a strictly lowers cost otherwise; this proves one of two candidates is globally optimal. Comparing costs yields A_k-B_k=1/w_k-(m-k+1)/P_k and the advertised sharp threshold for 1<=k<=m, with k=m+1 cost zero. For w=(1 five times,100 three times), exact Fraction exhaustive checks give k=5 cost83/100, k=6 cost3/100, k=7 cost81/4100 and every optimizer of these budgets excludes/includes/excludes center respectively (k=7 has three tied optimal sets, not a unique set). Finite enumeration supplements the all-weights dominance proof.

## originality

PASS

PASS best-of-knowledge: standard grounded-Laplacian leader selection and resistance-based evaluation are prior. A related general weighted tripod dynamic-programming theorem has only three arms and no closed two-candidate all-budget star formula for arbitrarily many spokes, nor the reentrant hub threshold. No inspected earlier general theorem proves this sharp star rule; wider tree algorithms may implicitly specialize and remain a priority risk.

## value

PASS

PASS: leader placement on a star is a natural basic stochastic-consensus design problem, and the sharp all-budget optimizer over arbitrarily many heterogeneous positive weights is structurally stronger than evaluating one fixed set. The nonmonotone center-inclusion example invalidates a plausible nestedness heuristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
