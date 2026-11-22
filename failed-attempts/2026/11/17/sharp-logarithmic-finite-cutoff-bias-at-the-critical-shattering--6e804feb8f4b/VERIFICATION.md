---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The stated positive recurrence a_k=k n_k, a_1=4/5, a_k=k/[2(k+4)] sum_{j<k}a_j a_{k-j} yields the exact ODE z(1-A)A'=4(z-A). The mass-one limiting solution and M2=2 are justified using endpoint finite-second-moment bounds from the critical stationary regime, not a truncated simulation. With w=1-z and h=2-(1-A(1-w))/w, direct substitution gives w h'=h^2/[(1-w)(2-h)]-w(2-h)/(1-w). The reciprocal u=1/h obeys u'->1/2 in logarithmic time after the elementary linear upper bound u(L)<=L+C controls e^-L u^2, so 2-A'(1-w)~2/log(1/w). The positive coefficient sandwich at w-=1/[N(log N)^2] and w+=(log N)^2/N bounds the omitted mu_k=k^2 n_k mass and proves (log N)R_N->2. Moment divergence for p>2 and epsilon log N_epsilon->2 follow. Independently recomputed 15 exact recurrence coefficients and tested finite interior ODE residual; that is only a finite algebra check, not the infinite proof.

## originality

FAIL

A separate already published result with a different title proves exactly the same mass-one product-kernel, lambda=4 stationary theorem: lim(log N) sum_{k>N}k^2n_k=2 with the identical recurrence and critical normalizations. Its full RESULT.md gives a construction and Tauberian proof. The submitted p>2 moment divergence and exponential cutoff inversion follow immediately from that exact tail, so neither is an original mathematical final claim. An alternative elementary Tauberian sandwich is a proof presentation rather than a separately motivated mathematical theorem.

## value

FAIL

Sharp critical finite-cutoff error is a genuinely motivated quantity, but the exact fact and constant are already delivered by the full earlier published theorem. The added easy moment/cutoff corollaries and an alternate asymptotic argument do not constitute a new independently valuable claim. Scientific rejection is for comprehensive coverage, not because the topic itself is trivial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
