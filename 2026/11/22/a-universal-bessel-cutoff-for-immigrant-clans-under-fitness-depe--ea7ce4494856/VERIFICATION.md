---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The stationary single-site generator for linear birth and death plus independent total clearing was checked by exact rational identities. The rare-input coefficient of the stationary factorial moments was checked against its analytic product expression. The independent branch-transition formula was evaluated at three distinct near-critical parameter choices and compared with numerical quadrature of the Bessel integral. The standalone script `CHECK.py` passed 319 checks from its packaged source.

Only the proof in `RESULT.md` establishes the infinite-site, double-scaling and Bessel claims; numerical quadrature is finite and does not certify an infinite limit. The calculation uses positive clearing rates at interior fitness, a finite mean-field input, \(0<\nu<1\), and a strictly positive finite scaling variable. No independent scientific validation has been performed.
