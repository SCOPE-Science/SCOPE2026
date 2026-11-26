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

Cut the timetable at a certain departure and rotate labels to p_1=1. This yields the exact cycle partition even if availability is resampled in subsequent periods: no forward wait crosses the next certain departure. For normalized gaps, uniform-time integration of the residual wait over each realized active interval gives W/T=gᵀHg/2, with H_ij the probability the two gaps belong to the same interval. For i<j this is H_ij=∏_{k=i+1}^j q_k, q_k=1−p_k, since precisely the intervening services must cancel. The all-operate event gives H≥(∏p_k)I in quadratic form. Independently, with D unit lower bidiagonal and D_(i,i−1)=−q_i, the product formula gives DHDᵀ=diag(1,1−q_2²,…,1−q_n²). Its inverse factorization gives s_i=(H^−1 1)_i=1/(1+q_i)−q_(i+1)/(1+q_(i+1))=(v_i+v_(i+1))/2, where q_1=q_(n+1)=0. Thus 1ᵀs=S, s/S is interior, and H(s/S)=1/S. Positive definiteness proves uniqueness and the minimum. Subtracting the optimum cancels the linear term on the fixed-sum hyperplane; expanding zᵀHz by realized blocks proves the exact regret and all-operate certificate. The displayed coefficient is a valid bound (and equality is possible for instances in the class), not necessarily the best coefficient for each fixed reliability vector. The symmetric S proves order invariance. For the example, masks with no optional cancellations, one cancellation, and two adjacent cancellations have total probabilities 1/10, 1/2, 2/5 and equal-spacing conditional costs T/8, 3T/16, 5T/16. This reproduces 37T/160 and, from S=22/9, 9T/44 and the relative reduction 47/407. The finite checker and verification notes were inspected without running the supplied script. The proof uses the specified p_i>0, independence and at least one certain service; no extension to a fully unreliable cycle or correlated cancellations is inferred.

## originality

FAIL

Demonstrable coverage by stronger existing optimal-weight and variance formulas, not an unresolved possibility of overlap. After cutting at the certain departure, the exact passenger waiting quadratic is half the variance of a constant-trend linear estimator with irregular exponential covariance, up to T. Dette–Pepelyshev–Zhigljavsky (2016), arXiv:1501.01774, Eq. (1.6), Lemma 2.1 and Corollary 2.1 (Eqs. (2.5)–(2.7)), give the optimal weights and variance for the larger class of triangular covariance kernels. The specialization below covers the claimed gaps, value, and permutation invariance; the regret is the accompanying quadratic identity, and the explicit bound is the immediate all-operate summand. No claim is made that the prior authors wrote a transit interpretation.

## value

FAIL

The objective and cancellation model are motivated, and the formulas can be useful as a transit interpretation. But after the guaranteed cut makes the objective an irregular exponential covariance quadratic, the exact minimizing weights, minimum and order invariance are mechanical consequences of existing stronger formulas. The exact excess follows from expansion about the prior optimizer, and its stated lower constant simply retains the all-operate event. No independently substantive new invariant or supported extension remains in this frozen theorem under the scientific-value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
