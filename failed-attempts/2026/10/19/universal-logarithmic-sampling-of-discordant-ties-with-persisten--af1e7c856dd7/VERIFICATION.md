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

With fixed classifications, any receptive initial weight furnishes a deterministic positive lower bound on the normalizer; m bounds it above. After n selections of a negative edge, its conditional hazard until the next lies between a_e δ_e^n and b_e δ_e^n, with both constants positive and finite. Taking τ_n just after draw n of this edge makes it a stopping time without an indexing ambiguity. Each wait is finite; a union bound at δ_e^{−(1−ε)n} and iterated survival at δ_e^{−(1+ε)n} give summable bounds even without independent waits. Borel–Cantelli at countably many ε then gives log wait/n→|log δ_e|, which passes to log τ_n/n by the last-summand lower bound and geometric-rate upper bound. Inversion and the exact weight identity give the two negative-edge limits. Each positive edge has uniformly positive conditional selection probability, hence positive lower frequency by the bounded martingale strong law. Its exact deficit (1−z_f(0))(1−γ_f)^{N_f(t)} tends exponentially to zero; together with the negative result this makes each positive selection probability tend to 1/k, giving the stated frequency and log-deficit rate by Cesàro and the same strong law. For eventual stabilization use a frozen coupling started at each deterministic integer T and partition, driven by the same future uniforms; the probability-one fixed-class result holds given the observed weights at T and the two trajectories agree on the event of permanent matching classes after T. A countable union avoids conditioning on a possibly anticipative last-change time. This proves the assertion only on the event stated, not stabilization itself.

## originality

FAIL

A distinct indexed result states the same log-count law, log-weight exponent, positive-edge frequencies and eventually fixed-class extension for common factors. Inspection of its proof shows the claimed heterogeneous variant is obtained by inserting δ_e in an already single-edge hazard estimate and γ_f in an already single-edge deficit identity. The explicit deficit rate follows by taking logs of that identity and substituting the known frequency. There is no distinct valuable remainder to repair on these claims. The catalogue match is dated after the frozen record; the demonstrated coverage does not establish priority or dependence.

## value

PASS

The mixed-regime rates quantify a genuine distinction between disappearing weight and a finite selection count: inactive contacts recur infinitely often but only on a logarithmic calendar-time scale. The count coefficient distinguishes discount factors that cannot be distinguished by the universal weight exponent alone. This is value of the mathematical law, not an incremental contribution over the matching result; the per-edge generalization has no separate scientific advance in the frozen formulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
