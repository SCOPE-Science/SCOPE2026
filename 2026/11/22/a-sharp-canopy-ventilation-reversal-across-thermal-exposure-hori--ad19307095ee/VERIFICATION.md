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

The zero-initial-state ODE gives H times the exponential convolution, with the factor T^(k+1) and the stated kernel for terminal heat and each integral order. Independently, u=yv makes g_k(y) the mean of u under density proportional to exp(-u)(1-u/y)^k on (0,y). For y2>y1 the density ratio on the old support is increasing for k>0 (its log derivative is k[1/(y1-u)-1/(y2-u)]), and there is additional mass beyond y1. This gives strict stochastic increase, also for k=0 when the ratio is constant on the old support. The limits of the mean are 0 by support and 1 by dominated convergence. Thus ∂x log E_k=-α+βg_k(λ₀Te^(−βx)) strictly decreases in x, proving strict log-concavity and excluding interior minimizers. The log derivative of the endpoint risk ratio in log T is g_k(y)−g_k(e^(−βL)y)>0; its limits are e^(−αL) and e^((β−α)L). This covers α=β (only a tie at infinite horizon) as well as both strict cases. The interior maximum applies in the explicitly defined α<β regime; at either outer threshold the derivative vanishes only at an endpoint, so the endpoint tie is strictly between them. Independent roots for k=0 and 1 give switch horizons 2.43751145374402 and 4.24857018426497, agreeing with the text. Replay: RESULT.md proof §§1–4 and the density-ratio check above. The frozen verify.py was inspected, not executed, and is finite regression only.

## originality

PASS

The contribution is the complete fixed-intensity, all-horizon classification for this specific heat balance, not marginal log-concavity or the qualitative observation that shade and ventilation compete. No inspected statement gives the same classification or a governing theorem that already establishes it for this model.

## value

PASS

This is a useful exact benchmark for a concrete conflict between source suppression and slower removal. It distinguishes the best boundary choices from the moving worst interior choice, identifies when the best boundary reverses, and shows how the cutoff differs for terminal versus cumulative exposure. Its value is conditional on zero initial excess, constant source, fixed intensity and exponential attenuation; it neither fits urban observations nor recommends actual canopy policy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
