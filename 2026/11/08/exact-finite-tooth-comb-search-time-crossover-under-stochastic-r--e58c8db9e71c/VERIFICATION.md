---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The tooth Laplace problem b_0=1 has characteristic resolvent 2cosh θ=2+s and reflecting ghost b_{H+1}=b_H, so b_1 is exactly the half-integer cosh ratio even when H=1. Back-substitution at a backbone vertex gives 2cosh γ=s+3−b_1; on the left half-line only the decaying root is compatible with the bounded hitting transform and f_L=1. No trajectory from the start can pass that backbone coordinate without hitting its target vertex. An attempt has success probability exp(−Lγ) and mean duration (1−exp(−Lγ))/r, giving the renewal MFPT. For s=u/L⁴ the cosh difference gives L²(1−b_1)→√u tanh(κ√u); the direct backbone term L²s vanishes and arcosh then gives the claimed exponent. For u=v/κ the argument of tanh tends to zero and the exponent tends to √v; the large-κ exponent follows by saturation. At fixed κ>0 the profile diverges at both u endpoints, hence has a positive finite interior minimum. Neither convergence of finite-model optimizers nor uniqueness is implied. Inspected the frozen verification code and the recorded 21 tests, not rerun; finite truncation is approximate, and the limit rests on the analytic expansion.

## originality

PASS

Credit the standard restart identity, effective waiting-time reduction, and previously studied normal/anomalous endpoints. The distinct result supported here is the normalized single-target crossover for the discrete one-sided, unit-edge-rate, reflecting comb in the simultaneous H/L² limit, with its exact finite-L,H input. The closest finite-tooth transport formulas use a different junction and holding-time model, and the closest explicit reset-search formula uses a different confining impedance. No inspected stronger statement gives the complete frozen law by specialization. This is a bounded assessment, not a priority finding.

## value

PASS

The nontrivial finite-κ profile resolves the regime in which the reflecting cap is neither negligible nor fully sampled during a reset attempt. It gives a quantitative search-time benchmark at precisely H comparable to L², where choosing either the usual normal or anomalous endpoint alone gives the wrong prediction. The exact lattice boundary response and the controlled simultaneous limit are the useful contribution, not the textbook resetting identity or an unsupported claim about optimizer convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
