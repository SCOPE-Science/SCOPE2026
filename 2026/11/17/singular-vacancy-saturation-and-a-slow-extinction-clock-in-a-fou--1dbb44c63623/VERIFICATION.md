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

Read full ODE RESULT proof and checked nonnegative invariant simplex E<=V and T+E+I+B=N. At b=0, Z=V-E solves Zdot=-kZT and Tdot=-(a+kZ)T, giving conserved J=T-Z-(a/k)log Z; T<=T0e^-at, Z converges to a strictly positive unique root when Z0>0. Monotone Lambert inversion, first and second derivatives in T0, and W asymptotics at positive/infinite/small argument give all three k regimes with boundary exact formula. For 0<b<a, weighted convolution e^{bt}E_b(t) has finite amplitude A_b; domination by exp(-(a-b)t) and parameter continuity give A_b->E_* and uniform tau>=delta profile. T and I vanish with exponential and bV/gamma bounds. Checked k=2,20,150 numerical ODE endpoints vs independent Lambert formula to at most 1.1e-11. No joint b,k limit claimed. Edge T0+E0=0 appropriately excepted from positive amplitude.

## originality

PASS

Singla–Kumar introduced the exact compartment ODE and local stability/numerical trajectories, not a zero-conflict terminal selection formula or sharp singular two-time asymptotics. Earlier Misra–Singh unemployment flow has exogenous terms, not this closed model. Known Lambert W and singular-limit techniques credited.

## value

PASS

For a natural vacancy-limited finite-population flow, the selected endpoint and noncommuting extinction/zero-conflict limits are concrete dynamical information not given by equilibrium stability. Sharp below/at/above capacity trichotomy and uniform slow clock reveal a mathematically motivated singular surface; idealized social model is not empirical evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
