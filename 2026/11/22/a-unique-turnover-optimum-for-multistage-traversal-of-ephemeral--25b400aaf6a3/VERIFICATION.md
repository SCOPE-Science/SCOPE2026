---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Fresh attempts start from the same closed state; the stage-sum Laplace transform gives success probability q=P_n⁻¹. An open attempt consumes mean (1−q)/(βλ) before success or closure and is preceded by mean 1/(αλ) closed delay. Dividing expected trial duration by q gives M_n=(P_n−p)/(pβλ), p=α/(α+β). The positive coefficients of P_n give strict convexity from the reciprocal term plus nonnegative second derivatives of the powers. The derivative is negative near zero; for n≥2 the positive quadratic coefficient in P_n makes it positive at sufficiently high turnover, whereas for n=1 only the decreasing reciprocal term varies. Appending rate ν increases the mean by (α+β)P_n/(αν); the positive derivative of this increment shifts the unique minimum left whenever the old finite minimum exists. With equal stage rates, P_n−λP_n′=p gives the stated strictly decreasing root equation on 0<βλ/μ<1/(n−1). The rescaled roots are bounded by n/(n−1), and every subsequential limit solves (1−y)e^y=p, whose sole root on [0,1] is on the principal Lambert branch. The unit-rate samples and c(1/2)=0.768039047013465… agree. This is an analytic result; the frozen rational diagnostics were inspected, not executed.

## originality

PASS

The mean formula is directly covered by general interrupted-service/refractory renewal theory, and an intermediate fluctuation-rate optimum is not itself a new phenomenon. Originality is supported for the fixed-availability optimizer classification in this serial-stage model, in particular the strict arbitrary-rate stage-extension ordering and equal-stage optimizer convergence. The strongest inspected overlapping general formulas do not state those optimizing results; the distinct temporary-habitat record optimizes a deterministic window offset for one journey. No priority is inferred from dates shared by indexed records.

## value

PASS

The modeled turnover decision fixes the usable fraction of time, so the competing mechanisms are waiting for a fresh opportunity and losing accumulated progress. The sharp one-stage versus multistage boundary and ordering under an arbitrary additional bottleneck isolate which feature generates a finite optimum and predict its shift without assuming stage homogeneity. The Erlang sequence further answers how the optimal clock changes for many comparable stages. These are substantive decisions about a motivated model beyond the routine mean transform or a single resonant example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
