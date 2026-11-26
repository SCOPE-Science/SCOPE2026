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

On the span of Φ+ and Ψ+, the Hamiltonian is the 2×2 matrix with diagonal (−J,J) and off-diagonal Ω. Exponentiating and tracing gives (I−y_m σ_x)/2 with y_m=[2JΩ/(J²+Ω²)]sin²(mφ) and φ=T√(J²+Ω²). With q=1−p the geometric age sum gives μ=c[1−p(1−q cos(2φ))/(1−2q cos(2φ)+q²)]/2. The fraction is strictly increasing in cos(2φ) for 0<p<1, so μ≤q/(1+q)<1/2, with equality only at c=1 and cos(2φ)=−1. For the entropy f(y)=h₂((1+y)/2), strict concavity gives f(y)≥1−y with equality only at 0 and 1. The resulting upper envelope g(μ)=f(μ)−1+μ is strictly increasing on [0,1/2], since g′≥1−(log₂3)/2>0. Thus saturation requires exactly J=Ω and φ=π/2 modulo π, which gives 0 or 1 polarization depending on parity and saturates the chord. The states commute at all parameters, so σ_x measurement gives precisely the Holevo gap. The maximal mean strictly decreases with p; its limit at p↓0 is 1/2, yielding the nonattained 0.311278124459… bit supremum. This is an analytic replay for the ideal single-spin ensemble, fixed positive T and J,Ω>0, not a claim about other reset states or noise. The finite truncation diagnostics in verify.py were inspected, not executed.

## originality

PASS

The same reset dynamics, reduced-state formula and Holevo identification were already published. Exact optimization of that particular single-spin Holevo gap over the allowed couplings and phase, its full equality conditions, and the resulting absolute supremum are the supported distinction.

## value

PASS

This replaces a one-bit dimension bound by a sharp attainable fixed-reset-rate envelope, gives every exact tuning, and identifies the optimal parity-to-local-measurement channel. It explains quantitatively why the best possible single-spin readout in this model still yields at most about 0.3113 bits of age information. The simple entropy method resolves a real optimization question raised by a published physical model; no extrapolation to noisy devices, two-spin information or larger systems is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
