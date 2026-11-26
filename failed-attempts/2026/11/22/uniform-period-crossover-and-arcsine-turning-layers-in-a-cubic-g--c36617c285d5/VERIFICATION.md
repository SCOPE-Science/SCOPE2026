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

The conserved energy has an even confining potential strictly increasing for x>0. Each positive level is a single regular oval with nonvanishing flow, and four quarter-transits give the least return time. The increasing change q=integral_0^x exp(beta*u^2/2) du does not change time; the transformed force has derivative 1+(beta+3*alpha)x^2+alpha*beta*x^4, so h(q)/q strictly increases on q>0. Rescaling the conservative quarter-period shows strict decrease; local dominated convergence gives continuity and the 2*pi small-amplitude limit. Independently, at s=beta(A^2-x^2), speed squared is exp(s)*J(s)/beta, where J(s)=integral_0^s (1+alpha*A^2-alpha*u/beta)exp(-u) du. Thus T=2*I/(A*sqrt(beta*(1+alpha*A^2))) and the time-sampled s-density is the kernel divided by I. With B=beta*A^2 and alpha/[beta*(1+alpha*A^2)]<=1/B, the kernel on s<=B/2 is dominated by twice exp(-s/2)/sqrt(1-exp(-s)); the remaining mass is O(B*exp(-B/4)) uniformly in alpha. Compact convergence plus these bounds yields uniform L1 convergence to the limiting kernel of integral pi. This proves both the claimed period normalization and TV convergence, including alpha=0 and arbitrary amplitude-dependent alpha. The bijective exponential change gives the arcsine law, and reflection gives equal mass at the two signs.

## originality

FAIL

A distinct published Resultary record states the same least-period map and the same physical-time distribution and uniform crossover, with stronger quantitative bounds. The coefficient and layer-variable changes are exact and require no time reparametrization. No independent remainder of the assigned theorem survives this comparison. This establishes coverage, not priority or provenance.

## value

FAIL

A uniform physical-time law at the turning scale would be intrinsically useful, but the frozen result recovers an already indexed stronger result for the same field, including its full coefficient range. The change of the gap coordinate is routine and supplies no independently useful new invariant or estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
