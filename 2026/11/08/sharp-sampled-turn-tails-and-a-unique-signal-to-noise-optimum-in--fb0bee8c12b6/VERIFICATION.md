---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The stationary 2D OU covariance solves MΣ+ΣM+2D=0 and detΣ=(4TxTy+u²(Tx−Ty)²)/[4(1−u²)]. Small-lag high-angle events localize at |Z|=O(√h), where chord-angle circular-segment area yields symmetric signed tail coefficient [S/(2π√detΣ)]H(α) with H(α)=(π−α+sinα cosα)/(2sin²α). H~π/(2α²) gives p<2 Gaussian-linearized h^(p/2) moments, critical variance S h log(1/h)/(2√detΣ), and p>2 integral moments. Stationary current gives signed mean h uΔ/(2√detΣ); optimizing its squared mean over leading variance reduces to a quadratic in y=u² with one root y∈(1/2,2/3). Checked positivity Tx,Ty>0, |u|<1, fixed α∈(0,π), fixed p, and Δ=0 exception. Source checker geometry, symbolic, Gaussian diagnostics inspected; simulations do not prove rare-event limits.

## originality

PASS

A precise, physically motivated finite observable resolves divergent angular-speed moments and gives a sharp anisotropic coupling optimum.

## value

PASS

Finite-time principal turns are what experiments observe; identifying their rare large-angle law, sharp moment transition and unique coupling optimizing a well-defined angular SNR is substantive despite earlier angular-speed tail and mean results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
