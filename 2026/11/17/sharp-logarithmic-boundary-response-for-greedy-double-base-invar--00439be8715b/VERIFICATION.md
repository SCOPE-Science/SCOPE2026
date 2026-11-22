---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The map G_epsilon uses q_epsilon=B/(B-1)-epsilon on [0,1/B) and Bx-1 on [1/B,M], M=1/(B-1). The positive invariant step density is the source Theorem 1.3 series with weights along the orbit r=q/B. Before first left-branch visit, x_n=M-epsilon B^{n-1}, w_n=B^{-n}; each of L+1 prefix steps removes exactly epsilon/B mass from a layer adjacent to M. L=log(1/epsilon)/log B+O_B(1), while the remaining series tails have O_B(epsilon) L1 norm. Normalization of Z0=B/(B-1)^2 yields weak signed endpoint concentration C_B(mu0-delta_M), C_B=(B-1)^2/(B^2 log B). The total variation sharp constant 2C_B follows from weak lower semicontinuity plus norm upper bound, and the coordinate mean from the weak limit. Independent 80-digit prefix-identity tests at B=1.5,2,3 and epsilon=1e-18 matched every prefix missing-mass identity and coefficient trends. These tests corroborate, not replace, the uniform geometric-tail proof.

## originality

PASS

Huang–Komornik–Zou explicitly establish the exact invariant step density and endpoint uniform law, which the claim credits; that source does not state the epsilon log epsilon signed response. Keller–Howard–Klages concerns general transport coefficient continuity and different lifted interval-map families. Their moduli do not imply the specific weak signed measure, sharp L1 constant, or coordinate mean. Best-of-knowledge original in parameter response.

## value

PASS

Precise response at an expanding-map full-branch boundary is mathematically meaningful because naive differentiability fails. The logarithmically divergent sensitivity, endpoint atom in weak scale, and exact total-variation constant quantify a non-Lipschitz boundary mechanism not captured by existence of invariant density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
