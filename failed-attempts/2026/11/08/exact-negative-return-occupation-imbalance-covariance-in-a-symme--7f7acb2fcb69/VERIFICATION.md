---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Bridge excursion GF B(z,u)=1/[1-u(1-sqrt(1-4z))]; conditionally independent excursion signs imply E[D^2|lengths]=sum ell_i^2. Marking by (z d/dz)^2 and differentiating in u yields Cov(K,D^2)=-n(n-1)4^n/(12 binom(2n,n)). The Chung-Feller uniform occupation law gives Var(D^2)=4n(n+2)(n(n+2)-3)/45 and the marked GF gives Var(K)=4n+2-b_n-b_n^2, hence the negative correlation limit. Independently enumerated every balanced bridge for n=1,..,8 and recovered covariances 0,-4/9,-8/5,-128/35,-1280/189,-2560/231,-7168/429,-458752/19305.

## originality

FAIL

Decisive PRIOR publication on November 2, 2026: Excursion-conditional transfer between bridge energy and signed occupation, Equation (3), states the identical EXACT all-n covariance of return count K with signed occupation X^2 under the IDENTICAL normalization. X=sum_{i=1}^n sgn(S_{2i-1}) equals A_n-n because each positive step pair has two positive midpoints; conditional on excursion lengths both coincide with sum epsilon_i ell_i. A second earlier published theorem states the identical limiting correlation for returns versus energy; together with the conditional transfer and elementary Chung-Feller moments, the submitted correlation limit is also covered. Full original claim has no surviving novelty.

## value

PASS

The negative dependence between excursion count and squared signed occupation imbalance, with a nonzero asymptotic correlation, is a natural instructive bridge invariant. Mathematical value is real, but originality fails due to earlier direct theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
