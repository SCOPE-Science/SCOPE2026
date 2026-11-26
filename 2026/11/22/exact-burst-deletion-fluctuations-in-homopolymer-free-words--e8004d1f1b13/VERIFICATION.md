---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Comparing two outputs with starts i<j, the middle coordinates are W[t] versus W[t+b] for i<=t<j and all others match automatically. Thus equality classes of start sites are intervals and S=1+L-sum(E_i), with L=n-b and E_i the lag-b return. Uniform proper words are exactly a uniform initial symbol with independent uniform nonzero additive increments modulo q, including composite q. For 0<d<b the joint return probability is the sum over a conditioned intermediate symbol a of P^d(x,a)^2 P^(b-d)(a,x), by symmetry of P. With m=q-1, x=r^d and y=r^(b-d), substituting the two eigenmodes into this sum and subtracting p^2 simplifies to m*x^2*(1+(m-1)y-m*y^2)/q^2. Its factors (1-y)(1+m*y) give zero for b-d=1 and positivity for b-d>=2. Disjoint increment windows give independence for d>=b. Counting available pairs gives the stated finite variance, including L=1 and positivity of adjacent covariance whenever such pairs exist for b>=3. At b=2, conditional on all increments up through U_i, exactly one of the q-1 values of U_(i+1) yields a return, making the full sequence of return indicators IID by induction, not merely uncorrelated. The fixed-parameter CLT follows by independent length-floor(L^(1/3)) blocks separated by b indices. The omitted indices including the final remainder have centered variance O_b(L^(2/3)); Cauchy–Schwarz compares retained and full variances, and every centered block is o(sqrt(L)), so Lindeberg applies with the positive displayed variance. Since L/n tends to 1, the normalization is as stated. The uploaded small-strata checker was inspected as text, not executed, and is not used as the proof.

## originality

PASS

The deterministic burst-size identity and the finite-dependence CLT method are known ingredients. The surviving novelty is the simplified exact covariance and variance for the uniform proper nonbinary source, including the b=2 full law and the exact fixed-b limiting variance. No inspected earlier statement supplies these constrained-source results or covers them as a direct specialization of a stronger evaluated law.

## value

PASS

Exact uncertainty of the number of distinct outputs is meaningful even when the deterministic collision identity and expected size are known. The covariance calculation shows exactly when the independent-trials variance fails and by how much for every finite length, while the b=2 exception is a genuine full-law simplification. The fixed-b Gaussian variance quantifies the same effect at scale. This is a motivated constrained-input benchmark, not a deletion-code capacity or large-burst claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
