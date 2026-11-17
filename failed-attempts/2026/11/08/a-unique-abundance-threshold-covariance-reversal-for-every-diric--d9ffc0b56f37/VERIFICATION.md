---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. The exact beta-tail identity follows by Dirichlet aggregation and the monomial identity E[P_j^q 1(P_i>t)]. Conditioning on P_1=x gives f_q(x)=x^q+c_q(1-x)^q; strict convexity and the endpoint inequalities f_q(0),f_q(1)>E H_q imply two regression zeros and exactly one integrated covariance crossing. The q=2 beta integration gives t=(a+1)/(ma+2); q→∞ beta-tail concentration gives limit 1-m Pr(Beta(a,(m-1)a)>t). Checked q>1 real, m≥2, a>0, t∈(0,1); no heterogeneity claim. Inspected verify.py exact rational beta-tail and noninteger quadrature paths; computations corroborate analytic proof only.

## originality

FAIL

FAIL. An October 25 published full theorem covers precisely the same symmetric Dirichlet all-real-q negative-to-positive sign transition and the exact quadratic threshold, within a strictly stronger tagged-coordinate theorem covering asymmetric Dirichlet vectors. The Nov 2 published convex-score theorem independently dominates the power-sum special case and gives the same q=2 formula. The large-q exceedance-one root follows from the same elementary shifted-beta tail expression and does not rescue the covered principal claim. No assertion of novelty arises from different variable letters or from an unsearched alias.

## value

FAIL

FAIL for this unchanged principal claim: the complete universal crossing and exact Simpson threshold are direct corollaries of stronger published results. The large-power limit is a routine shifted-beta concentration corollary in this context, not a distinct motivated residual advance. Correctness and reproducible checks do not establish value independent of prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
