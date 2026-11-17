---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The information matrix M=E[qq^T/(q^T S q)] has tr(SM)=1, proving lambda_min(M)<=1/tr S with equality iff M=I/tr S. Eigenvector law with mass lambda_i/tr S and sphere law w(q)=n q^T S q/tr S both realize equality. Metric-guided has M=S^{-1}/n; Haar has strictly larger min eigenvalue than metric guided but cannot be isotropic for nonscalar S (coordinate-swap identity). Planar circle integration gives m_i= lambda_i^{-(1+gamma)/2}/(a^{(1-gamma)/2}+b^{(1-gamma)/2}), isotropic uniquely gamma=-1 when a!=b. Independent numerical quadrature at S=diag(1,4),(1,9) confirmed the three strict levels; analytic trace proof covers all real SPD dimensions.

## originality

PASS

The optimization reduces to an E-optimal information design and the trace bound is elementary prior geometry; that known framing is not claimed independently new. The specific minimax solution for the Chen–Xie alignment denominator, sharp comparison with their inverse-metric guided law and unique opposite-power planar no-rejection realization are not present in accessible source treatment; related standard experimental-design and coordinate-sampling results use different objectives. Historical equivalence in classical design literature is an explicit risk.

## value

PASS

Choosing sampling directions to maximize adversarial-gradient mean line alignment is a naturally motivated exact design problem. The explicit full-support biased sampler, exact accept probability, Haar strictness and planar parameter choice offer practically interpretable optimal designs not implied by merely validating a normalization identity; claims are limited to this static statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
