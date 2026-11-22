---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Read RESULT.md and check_stationary.py. The triangular recurrence fixes a1=4/5 and all coefficients positive; the Catalan convolution majorant gives positive power-series radius. Strict barriers z^2<q(z)<z together with Pringsheim force radius at least one and q(1-)=1, proving mass 1. The generating ODE z(1-q)q'=4(z-q), with bounded q', yields M=q'(1)=2 from M^2=4(M-1). In the singular variables x=1-z, u=(1-q)/x and v=2-u, the exact transformed ODE yields 1/v~(1/2)log(1/x), and hence 2-q'(1-x)~2/log(1/x). Nonnegative b_k=k²n_k and their monotone tail allow the Laplace Tauberian/monotone density step, obtaining the boxed asymptotic. Independently checked 14 exact rational recurrence coefficients and the truncated generating ODE; finite values do not prove the tail. The mass-one stationary infinite model, not finite truncation or time dynamics, is the domain.

## originality

FAIL

FAIL: a distinct published mathematical RESULT.md dated November 17, 2026 states exactly the same model, recurrence, stationary second moment and boxed lim (log N)R_N=2, with a different complete proof and stronger epsilon-cutoff and higher-moment consequences. The identical sharp limit is explicitly stated; it is not just an analogous title or parameter match. Historical same-day ordering is not established, but as a separate already published theorem it covers the entire submitted final claim. The earlier Matveev source itself supplies recurrence and M2=2 but not the sharp logarithmic law.

## value

PASS

The sharp logarithmic missing second moment is meaningful because convergence is unusually slow at a critical marginal stationary distribution, quantifies computational cutoffs exponentially in tolerance, and is not a routine numerical lookup. Scientific value survives independently of the decisive originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
