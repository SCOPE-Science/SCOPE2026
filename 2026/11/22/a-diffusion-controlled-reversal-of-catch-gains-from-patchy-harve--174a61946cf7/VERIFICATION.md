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

The Neumann linearization has spectrum -c-Dλ_j and is an isomorphism between the stated Hölder spaces; the analytic local branch stays positive and its reaction coefficient stays below -c/2 for small amplitude at each fixed D. The maximum of B1/B2>1 contradicts the second derivative sign (also at a Neumann endpoint) since per-capita recruitment strictly decreases. Integrating B''/B gives the positive log-gradient term; Jensen yields the exact inverse-stock bound and strictness when effort varies. Independently, writing g(B)=aB/(b+B)-mB, integration gives Y=mean g(B). With w_j=-ηqv_j/A_j and c z̄=-(bh³/a²)mean(w²)-η mean(vw), one obtains the stated stock coefficient. Expanding mean g directly gives Y2=(hr-m) z̄-(bh³/a²)mean(w²), exactly (2). At D→0 the catch bracket is -m(1-r)/c, with dominated convergence on square-summable v_j; at large D and K>0 all brackets turn positive by λ_j≥λ_1. The one-mode zero solves Dλ_j=m(1-r)c/(hr-m); if hr≤m there is no sign reversal. For the example the factor mean cos²=1/2 gives B2=(2D+1)/(4(1+D)²) and Y2=(2D-1)/(8(1+D)²), including the zero at D=1/2. The uploaded script is an inspected finite numerical diagnostic, not a PDE certificate; the comparisons above are analytic. The headline is read subject to the explicit positive-stationary and small-amplitude hypotheses, not as a universal finite-amplitude switch.

## originality

PASS

Best-of-knowledge PASS for the quantitative fixed-mean stationary comparison: the general quadratic spectral multiplier with its exact one-mode cutoff and the accompanying explicit nonlinear stock bound. The governing PDE, homogeneous stability, and the qualitative movement-dependent biomass/catch distinction are prior. In particular Hilborn et al. already simulate increase in stock at every tested fixed-effort case and, in the heavily fished case, catch reversal between low and higher adult movement. Do not present the broad qualitative reversal as new.

## value

PASS

The scientific comparison holds total linear fishing effort fixed, separating redistribution from reducing effort. A mode-length-dependent threshold quantifies when a strictly increased stationary stock does or does not translate into increased catch, and the explicit gradient bound provides a distinct nonperturbative comparison. No empirical or finite-amplitude yield claims are needed to make these benchmarks useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
