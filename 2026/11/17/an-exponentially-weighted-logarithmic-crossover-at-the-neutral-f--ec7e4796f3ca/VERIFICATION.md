---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

On |x|<=0.1 for a near 8, F reverses sign, absolute magnitude w_{k+1}=T_a(w_k)=(a/4-1)w-(a³/48)w³+(a⁵/480)w⁵+O(w^7), strictly maps positive neighborhood into itself. v=w^-2 satisfies exact uniform asymptotic recurrence v_next=q_N v+A_N+B_N/v+O(v^-2), q_N=(a/4-1)^-2=1-theta/(2N)+O(N^-2), A_8=64/3, B_8=1024/5. Positive bounded additive drift and discrete comparison show v_{k,N} asymptotic to k+1 for 0<=k<=N. Summing gives v_k=(64/3)k+O(1+log(k+1)+k²/N) and reciprocal harmonic sum sum1/v_k=(3/64)log N+O(1). Weighted factors q_N^{N-1-k}=exp(-theta/2)+O((k+1)/N) lead to exponentially reweighted log term B/A=(48/5), and remaining O(v^-2) sum bounded. Leading geometric sum yields Phi(theta). Uniform bounds hold on compact theta, x0 away from zero; fixed a within each run, not time-varying a_k.

## originality

PASS

On the stated bounded primary literature and Resultary comparisons, the exact final claim is neither stated nor directly implied by the identified relevant antecedents; known special cases and methodology were credited. This is best-of-knowledge, not proof of global novelty. See four explicit implication checks, actual source inspections, and residual risks.

## value

PASS

The natural finite-horizon critical detuning a-8=theta/N probes a neutral flip at its observable time scale. A sharp parameter-dependent logarithmic correction distinguishes model-specific second-order behavior beyond generic leading parabolic scaling and previously known fixed-critical logarithm, a meaningful quantitative asymptotic for this sigmoid map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
