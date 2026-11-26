---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The signs reuse beta_k across time, so the conditional pair expectation is the Bernoulli character on the symmetric difference of two Pascal supports, not a product over independent rows. For s<t the highest differing digit produces at least 2^(popcount(t)-1) support elements absent at s. The no-increase event has probability 2^-(n-m). Fourier inversion for the fair count modulo 2^ell, ell=floor(log_2(n)/4), gives exponentially small distance to uniform in sqrt(n); Hoeffding controls fewer than ell/4 ones by exp(-ell/8). This yields the claimed power delta=1/(32 log 2) for the absolute pair bound and then the normalized bracket second moment (with the j=0 term treated separately). Along ceil(j^32) the squared estimates are summable because 32 delta>1; bounded increments interpolate, and Fubini gives the almost-sure quenched limit. The bounded martingale differences and local uniform bracket convergence then give the quenched FCLT. The finite checks in verify_pascal.py were inspected, not run, and are not a substitute for these steps.

## originality

FAIL

Both the static heterogeneous quenched theorem and the quantitative annealed bound are covered at the statement level. The later same-model rate record gives sufficiently strong pair-envelope estimates to imply the advertised annealed second moment, not just a stronger almost-sure statement. No scientific remainder survives; this finding of coverage does not determine priority.

## value

PASS

A quantitative pathwise upgrade in the static environment answers an explicit annealed-to-quenched gap. It addresses the persistent dependence created by coefficient reuse and arbitrary biases; the modular proof explains a uniform quantitative mechanism. Value of the question and method does not overcome duplicated statement coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
