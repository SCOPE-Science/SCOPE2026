---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Condition on the pre-draw state including the table: the two table terms cancel under uniform sampling. The affine conditional gradient then closes the expectation recurrence exactly, giving local map Hx+(I−H)c−Ky with H_ii=(1−αa_i)^τ and K=(I−H)T/τ. Invariants are zero-sum duals and the unique consensus fixed point u_* with dual τ α diag(a)(c−u_*1); the proof's symbol ν_* at line 67 is the u_* defined in line 29. The centered block map on R^N⊕1^⊥ is the stated Mτ. Compare with the upper-triangular map obtained by H=0, K=T/τ. Its fast block is zero, its slow block is I−LT/τ restricted to 1^⊥, and the off-diagonal block is O(1/τ). The two blocks can be decoupled by a uniformly bounded shear for large τ, and LT on 1^⊥ is diagonalizable with precisely the positive spectrum of T^(1/2)LT^(1/2). The discarded blocks are exponentially small, hence o(1/τ), including relative to the separations between distinct slow groups; the spectral-radius expansion follows, also for repeated smallest positive eigenvalues. The exact witness has H=0 and K=I/τ; Wc=λc gives E[x_{t+1}]=λr_τ^t c. At τ=2 the four local endpoints for agent i are c_i[1±(1+δ)/2], c_i[1±(1−δ)/2], equiprobable; they give the reported positive variance. Indeed repeated first-component versus repeated second-component paths differ for every τ≥2, while τ=1 itself is deterministic. The exact relative-round formula gives Θ(τ²) sampled steps for a fixed reduction; gradient-table setup/refresh can add component evaluations but does not change this order for two components. No second-moment assertion follows. I inspected check.py, not executed it: its spectral sampler at lines 28–45 does not enforce positive definiteness (positive entries and diagonal normalization are insufficient), so the claimed SPD diagnostic characterization is not established by that code. The analytic proof does not depend on those diagnostics.

## originality

PASS

The established distinct claim is the sharp fixed-α first-moment slow coefficient for possibly unequal agent curvatures and the exact stochastic-quadratic budget witness, not the primal–dual iteration, table unbiasedness, zero dual sum, or an assertion that local steps can generally hurt. Liu's shrinking-stepsize second-moment theorem and LED's graph-only comparison blocks are not exact weighted-Hessian slow-spectrum results in this regime. The same arithmetic mean map is obtainable from exact-gradient LED on the quadratic class, but the checked LED result is not a stronger theorem already determining its spectrum.

## value

PASS

For this established decentralized iteration, the weighted Laplacian coefficient identifies precisely how curvature heterogeneity and graph bottlenecks control the budget-induced slow mode, rather than just giving an order bound. The nonzero-mean disagreement of the stochastic two-agent witness makes the deterioration observable from the usual zero initialization: more local steps strictly worsen communication contraction and force quadratic total sampled work for the comparison. This isolates a concrete first-moment failure mode at fixed stepsize, not a rejection of local steps in the original shrinking-stepsize regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
